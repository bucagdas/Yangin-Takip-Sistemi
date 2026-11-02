import glob
import logging
from datetime import datetime, timedelta, timezone

import pandas as pd

CSV_PATTERN = 'csv_data/*.csv'
README_FILE = 'README.md'
WINDOW = timedelta(days=1)

INTRO = (
    "# Yangın Takip Sistemi\n\n"
    "Bu repo, **Türkiye'deki aktif ısı noktalarını** NASA FIRMS (Fire Information for Resource "
    "Management System) API'si üzerinden düzenli olarak çekmekte ve kaydetmektedir. Veriler "
    "VIIRS sensörlü uydulardan (VIIRS_NOAA20_NRT, VIIRS_NOAA21_NRT, VIIRS_SNPP_NRT) gelir ve "
    "Türkiye sınırına göre süzülür.\n\n"
    "Her nokta bir uydu pikselinin merkezidir; çoğu bitki örtüsü yangınıdır ama sanayi tesisi "
    "gibi sabit ısı kaynakları da görünebilir. Aynı yangın birden çok uydu ve noktada yer alabilir.\n"
)
FOOTER = "\n## Yazar\n\n[bucagdas](https://x.com/bucagdas)\n"
TABLE_HEADER = (
    '| Koordinatlar (Enlem, Boylam) | Tarih ve Saat (UTC) | Parlaklık Sıcaklığı (K) | FRP (MW) '
    '| Güven Seviyesi | Gündüz/Gece |\n'
    '|-----------------------------|----------------|----------|-----|----------------|-------------|\n'
)


def format_time(acq_time):
    try:
        acq_time_str = str(int(acq_time)).zfill(4)
        return f"{acq_time_str[:2]}:{acq_time_str[2:]}"
    except (ValueError, TypeError):
        return "Bilinmiyor"


def translate_daynight(value):
    return {'D': 'Gündüz', 'N': 'Gece'}.get(value, 'Bilinmiyor')


def translate_confidence(value):
    return {'l': 'Düşük', 'n': 'Orta', 'h': 'Yüksek'}.get(value, 'Bilinmiyor')


def create_google_maps_link(lat, lon):
    return f"[{lat}, {lon}](https://www.google.com/maps?q={lat},{lon})"


def load_last_24_hours(now, pattern=CSV_PATTERN):
    """CSV arşivlerinden son 24 saatin tespitlerini en yeniden eskiye döndür."""
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError('Klasörde CSV dosyası bulunamadı.')
    merged = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)
    merged = merged.drop_duplicates()
    merged['acq_datetime'] = pd.to_datetime(
        merged['acq_date'].astype(str) + ' ' + merged['acq_time'].apply(format_time),
        format='%Y-%m-%d %H:%M', errors='coerce'
    )
    recent = merged[merged['acq_datetime'] >= now - WINDOW]
    return recent.sort_values('acq_datetime', ascending=False)


def build_table(rows):
    lines = [TABLE_HEADER]
    for _, row in rows.fillna('Yok').iterrows():
        coords = create_google_maps_link(row['latitude'], row['longitude'])
        date_time = f"{row['acq_date']} {format_time(row['acq_time'])}"
        lines.append(
            f"| {coords} | {date_time} | {row.get('bright_ti4', 'Yok')} | {row.get('frp', 'Yok')} "
            f"| {translate_confidence(row.get('confidence'))} "
            f"| {translate_daynight(row.get('daynight'))} |\n"
        )
    return ''.join(lines)


def build_readme(rows, now):
    body = "Son 24 saatte Türkiye'de aktif ısı noktası tespit edilmedi.\n" if rows.empty else build_table(rows)
    return (
        f"{INTRO}\n## Son 24 Saatin Verileri\n"
        f"### Son Güncelleme: {now.strftime('%Y-%m-%d %H:%M:%S')} (UTC)\n\n"
        f"{body}{FOOTER}"
    )


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    rows = load_last_24_hours(now)
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(build_readme(rows, now))
    logging.info(f"README.md güncellendi ({len(rows)} nokta).")


if __name__ == '__main__':
    main()
