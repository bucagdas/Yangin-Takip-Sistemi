import io
import json
import logging
import os
import random
import re
import sqlite3
from datetime import datetime, timedelta, timezone

import pandas as pd
import requests
import shapely
from requests.exceptions import RequestException
from shapely.geometry import shape

API_URL = 'https://firms.modaps.eosdis.nasa.gov/api'
TUR_BBOX = '25.6,35.8,44.8,42.1'  # west,south,east,north
# DAY_RANGE=1 yalnızca bugünü (UTC) döndürür; gün dönümünde veri kaçmasın diye dün de istenir.
DAY_RANGE = 2
WINDOW_HOURS = 24
SATELLITE_SOURCES = ['VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT', 'VIIRS_SNPP_NRT']
REQUEST_TIMEOUT = 30  # saniye
REQUIRED_COLUMNS = {'latitude', 'longitude', 'acq_date', 'acq_time'}
MAP_KEY_COUNT = 7

CSV_DIR = 'csv_data/'
JSON_DIR = 'json_data/'
SQLITE_DIR = 'sqlite_data/'
AVAILABILITY_FILE = './available_satellites.txt'

# Natural Earth 1:10m sınırı; ~1 km tampon kıyıdaki piksel merkezlerinin düşmesini önler.
BORDER_FILE = 'turkey_border.geojson'
BORDER_BUFFER_DEG = 0.01
# Bu tarihten önceki satırlar FIRMS ülke filtresinden geldi, sonrası bbox ile alındı.
BBOX_ERA_START = '2026-02-19'

SECRET_PATTERN = re.compile(r'\b[0-9a-fA-F]{32}\b')  # FIRMS MAP_KEY biçimi

_border = None


def scrub_secrets(text):
    """Metindeki MAP_KEY değerlerini maskele."""
    return SECRET_PATTERN.sub('[REDACTED]', text)


class SecretFilter(logging.Filter):
    """requests hata metinleri anahtarlı URL içerir; hiçbir kayıt anahtar taşımasın."""

    def filter(self, record):
        record.msg = scrub_secrets(record.getMessage())
        record.args = ()
        return True


def configure_logging():
    """Loglar yalnızca Actions konsoluna yazılır; repoda log dosyası tutulmaz."""
    handler = logging.StreamHandler()
    handler.addFilter(SecretFilter())
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
    logging.basicConfig(level=logging.INFO, handlers=[handler], force=True)


def select_map_key():
    keys = [os.environ.get(f'MAP_KEY_{index}') for index in range(1, MAP_KEY_COUNT + 1)]
    keys = [key for key in keys if key]  # Tanımsız secret boş metin olarak gelir
    if not keys:
        raise SystemExit('Hiçbir MAP_KEY tanımlı değil.')
    return random.choice(keys)


def turkey_border():
    global _border
    if _border is None:
        with open(BORDER_FILE, 'r', encoding='utf-8') as f:
            _border = shape(json.load(f)['geometry']).buffer(BORDER_BUFFER_DEG)
        shapely.prepare(_border)
    return _border


def in_turkey(df):
    """Satırların Türkiye sınırı içinde olup olmadığını döndür."""
    return shapely.contains_xy(turkey_border(), df['longitude'].values, df['latitude'].values)


def filter_to_turkey(df):
    return df[in_turkey(df)].reset_index(drop=True) if not df.empty else df


def last_24_hours(df, now=None):
    """Yalnızca son WINDOW_HOURS saatte alınmış tespitleri bırak."""
    if df.empty:
        return df
    now = now or datetime.now(timezone.utc)
    times = pd.to_numeric(df['acq_time'], errors='coerce').fillna(-1).astype(int)
    acquired = pd.to_datetime(
        df['acq_date'].astype(str) + ' ' + times.astype(str).str.zfill(4),
        format='%Y-%m-%d %H%M', utc=True, errors='coerce'
    )
    return df[acquired >= now - timedelta(hours=WINDOW_HOURS)].reset_index(drop=True)


def fetch_satellite(map_key, satellite):
    url = f'{API_URL}/area/csv/{map_key}/{satellite}/{TUR_BBOX}/{DAY_RANGE}'
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f'{satellite} yanıtında eksik sütunlar: {sorted(missing)}')
    return df


def concat_non_empty(frames):
    """Boş tabloları atlayarak birleştir.

    pandas 3, boş tablonun metin tipli sütunlarını da hesaba katar; boş bir API
    yanıtı koordinat sütunlarını sayıdan metne çevirir. Hepsi boşsa ilki döner.
    """
    non_empty = [frame for frame in frames if not frame.empty]
    return pd.concat(non_empty, ignore_index=True) if non_empty else frames[0]


def update_archive(path, new_rows):
    """CSV arşivine yeni satırları ekle ve bbox döneminden kalan sınır dışı satırları at."""
    if os.path.exists(path):
        combined = concat_non_empty([pd.read_csv(path), new_rows])
    else:
        combined = new_rows
    combined = combined.drop_duplicates()
    if not combined.empty:
        keep = (combined['acq_date'].astype(str) < BBOX_ERA_START) | in_turkey(combined)
        combined = combined[keep]
    combined.to_csv(path, index=False)
    logging.info(f"CSV güncellendi: '{path}' ({len(combined)} satır)")


def update_database(path, latest):
    """Son 24 saatin verisini yaz; replace boş sayfa bıraktığı için dosyayı küçült."""
    conn = sqlite3.connect(path)
    try:
        latest.to_sql('fire_data', conn, if_exists='replace', index=False)
        conn.commit()
        conn.execute('VACUUM')
    finally:
        conn.close()
    logging.info(f"SQLite güncellendi: '{path}' ({len(latest)} satır)")


def save_text_if_changed(path, data):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            if f.read() == data:
                return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
    logging.info(f"'{path}' kaydedildi.")


def save_data_availability(map_key):
    url = f'{API_URL}/data_availability/csv/{map_key}/ALL'
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    save_text_if_changed(AVAILABILITY_FILE, response.text)


def main():
    configure_logging()
    map_key = select_map_key()
    for folder in (CSV_DIR, JSON_DIR, SQLITE_DIR):
        os.makedirs(folder, exist_ok=True)

    latest = []
    for satellite in SATELLITE_SOURCES:
        try:
            rows = filter_to_turkey(fetch_satellite(map_key, satellite))
            update_archive(f'{CSV_DIR}TUR_{satellite}.csv', rows)
            recent = last_24_hours(rows)
            recent.to_json(f'{JSON_DIR}TUR_{satellite}.json', orient='records')
            latest.append(recent)
        except RequestException as e:
            logging.error(f'{satellite} API isteği başarısız: {e}')
        except Exception as e:
            logging.error(f'{satellite} işlenemedi: {e}')

    if not latest:
        raise SystemExit('Hiçbir uydu kaynağından veri alınamadı.')
    update_database(f'{SQLITE_DIR}TUR_fire_data.db', concat_non_empty(latest))

    try:
        save_data_availability(map_key)
    except Exception as e:
        logging.error(f'Veri erişilebilirlik bilgisi alınamadı: {e}')


if __name__ == '__main__':
    main()
