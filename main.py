import pandas as pd 
import requests
import json
import sqlite3
import os
import io
import logging 
from datetime import datetime
import random

# Log dosyasını ayarla
logging.basicConfig(filename='main.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='a')

# GitHub Secrets'dan gelen MAP_KEY'leri al
map_keys = [
    os.environ.get('MAP_KEY_1'),
    os.environ.get('MAP_KEY_2'),
    os.environ.get('MAP_KEY_3'),
    os.environ.get('MAP_KEY_4'),
    os.environ.get('MAP_KEY_5'),
    os.environ.get('MAP_KEY_6')
]

# Rastgele bir MAP_KEY seç
selected_map_key = random.choice(map_keys)

# FIRMS API için ülke ve zaman değişkenleri
country_code = 'TUR'
days = 1

# Alınacak uydu verileri
satellite_sources = ['VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT', 'VIIRS_SNPP_NRT']

# Zaman damgası oluştur (dosya isimlerine eklemek için)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Klasörler
json_dir = 'json_data/'
csv_dir = 'csv_data/'
sqlite_dir = 'sqlite_data/'

# Klasörleri oluştur (eğer yoksa)
os.makedirs(json_dir, exist_ok=True)
os.makedirs(csv_dir, exist_ok=True)
os.makedirs(sqlite_dir, exist_ok=True)

# API'den verileri çekmek ve dosyalara kaydetmek için döngü
for satellite in satellite_sources:
    # API URL'si
    url = f'https://firms.modaps.eosdis.nasa.gov/api/country/csv/{selected_map_key}/{satellite}/{country_code}/{days}'
    
    # API isteği yap
    response = requests.get(url)

    if response.status_code == 200:
        # Veriyi pandas DataFrame'e yükle
        data = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(data))

        # CSV olarak kaydet
        csv_filename = f'{csv_dir}TUR_{satellite}_{timestamp}.csv'
        df.to_csv(csv_filename, index=False)
        logging.info(f"Veriler CSV formatında '{csv_filename}' olarak kaydedildi.")

        # JSON olarak kaydet
        json_filename = f'{json_dir}TUR_{satellite}_{timestamp}.json'
        df.to_json(json_filename, orient='records')
        logging.info(f"Veriler JSON formatında '{json_filename}' olarak kaydedildi.")

        # SQLite veritabanına kaydet
        sqlite_filename = f'{sqlite_dir}TUR_{satellite}_{timestamp}.db'
        conn = sqlite3.connect(sqlite_filename)
        df.to_sql('fire_data', conn, if_exists='replace', index=False)
        conn.close()
        logging.info(f"Veriler SQLite veritabanına '{sqlite_filename}' olarak kaydedildi.")
    
    else:
        logging.error(f"API isteği başarısız oldu: {response.status_code} - Uydu: {satellite}")

# Kullanılabilir uyduları ve ülkeleri kaydetme fonksiyonu
def save_satellite_and_country_info(selected_map_key):
    # Uydu ve ülke bilgileri dosya yollarını oluştur
    current_dir = os.getcwd()
    satellite_file_path = os.path.join(current_dir, 'available_satellites.txt')
    country_file_path = os.path.join(current_dir, 'country_codes.txt')
    
    # Kullanılabilir uyduları çekme
    satellite_url = f'https://firms.modaps.eosdis.nasa.gov/api/data_availability/csv/{selected_map_key}/ALL'
    satellite_response = requests.get(satellite_url)

    # Ülke kodlarını çekme
    country_url = 'https://firms.modaps.eosdis.nasa.gov/api/countries'
    country_response = requests.get(country_url)

    # API yanıtlarını kontrol et ve dosyalara yaz
    if satellite_response.status_code == 200 and country_response.status_code == 200:
        # Uydu verilerini kaydetme
        with open(satellite_file_path, 'w', encoding='utf-8') as satellite_file:
            satellite_file.write(satellite_response.text)
        logging.info(f"Uydu bilgileri '{satellite_file_path}' dosyasına kaydedildi.")

        # Ülke kodlarını kaydetme
        with open(country_file_path, 'w', encoding='utf-8') as country_file:
            country_file.write(country_response.text)
        logging.info(f"Ülke kodları bilgileri '{country_file_path}' dosyasına kaydedildi.")
    else:
        logging.error(f"Uydu veya ülke kodlarını çekmede hata oluştu. Uydu: {satellite_response.status_code}, Ülke: {country_response.status_code}")
        logging.info(f"Uydu yanıtı: {satellite_response.text}")
        logging.info(f"Ülke yanıtı: {country_response.text}")

# Uydu ve ülke bilgilerini kaydet
save_satellite_and_country_info(selected_map_key)
