import pandas as pd
import requests
import sqlite3
import os
import io
import logging
import random
from requests.exceptions import RequestException

MAX_LOG_LINES = 1000

def trim_log(path, max_lines):
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            if len(lines) > max_lines:
                with open(path, 'w', encoding='utf-8') as f:
                    f.writelines(lines[-max_lines:])
    except Exception:
        pass

trim_log('main.log', MAX_LOG_LINES)
logging.basicConfig(filename='main.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='a')

map_keys = [k for k in [
    os.environ.get('MAP_KEY_1'),
    os.environ.get('MAP_KEY_2'),
    os.environ.get('MAP_KEY_3'),
    os.environ.get('MAP_KEY_4'),
    os.environ.get('MAP_KEY_5'),
    os.environ.get('MAP_KEY_6'),
    os.environ.get('MAP_KEY_7')
] if k is not None]

if not map_keys:
    logging.error("Hiçbir MAP_KEY tanımlı değil, çıkılıyor.")
    raise SystemExit(1)

selected_map_key = random.choice(map_keys)

TUR_BBOX = '25.6,35.8,44.8,42.1'  # west,south,east,north
days = 1
satellite_sources = ['VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT', 'VIIRS_SNPP_NRT']

json_dir = 'json_data/'
csv_dir = 'csv_data/'
sqlite_dir = 'sqlite_data/'

os.makedirs(json_dir, exist_ok=True)
os.makedirs(csv_dir, exist_ok=True)
os.makedirs(sqlite_dir, exist_ok=True)

all_dfs = []

for satellite in satellite_sources:
    url = f'https://firms.modaps.eosdis.nasa.gov/api/area/csv/{selected_map_key}/{satellite}/{TUR_BBOX}/{days}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"API yanıtı: {response.status_code}, {response.text[:100]}")

        df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))

        csv_filename = f'{csv_dir}TUR_{satellite}.csv'
        if os.path.exists(csv_filename):
            df_to_save = pd.concat([pd.read_csv(csv_filename), df], ignore_index=True).drop_duplicates()
        else:
            df_to_save = df
        df_to_save.to_csv(csv_filename, mode='w', header=True, index=False)
        logging.info(f"CSV güncellendi: '{csv_filename}'")

        json_filename = f'{json_dir}TUR_{satellite}.json'
        df.to_json(json_filename, orient='records')
        logging.info(f"JSON güncellendi: '{json_filename}'")

        all_dfs.append(df)

    except RequestException as e:
        logging.error(f"API isteği sırasında hata oluştu: {e}")
    except Exception as e:
        logging.error(f"Veri işleme veya dosya kaydetme işlemi sırasında hata oluştu: {e}")

if all_dfs:
    sqlite_filename = f'{sqlite_dir}TUR_fire_data.db'
    conn = sqlite3.connect(sqlite_filename)
    pd.concat(all_dfs, ignore_index=True).to_sql('fire_data', conn, if_exists='replace', index=False)
    conn.close()
    logging.info(f"SQLite güncellendi: '{sqlite_filename}'")


def save_to_text_file(file_path, data):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                if file.read() == data:
                    logging.info(f"'{file_path}' zaten güncel.")
                    return
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        logging.info(f"'{file_path}' kaydedildi.")
    except Exception as e:
        logging.error(f"'{file_path}' kaydedilemedi: {e}")


def save_satellite_and_country_info(selected_map_key):
    try:
        satellite_response = requests.get(
            f'https://firms.modaps.eosdis.nasa.gov/api/data_availability/csv/{selected_map_key}/ALL'
        )
        satellite_response.raise_for_status()
        save_to_text_file('./available_satellites.txt', satellite_response.text)


    except RequestException as e:
        logging.error(f"API isteği sırasında hata oluştu: {e}")
    except Exception as e:
        logging.error(f"Veri kaydetme işlemi sırasında hata oluştu: {e}")


save_satellite_and_country_info(selected_map_key)
