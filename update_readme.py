import os  
import pandas as pd
import logging
from datetime import datetime

# Log dosyasını ayarla
logging.basicConfig(filename='update_readme.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s', 
                    filemode='a')

# Son çekilen CSV dosyalarını bul
def get_latest_csv_files(csv_dir='csv_data/'):
    try:
        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        if not csv_files:
            raise FileNotFoundError("Klasörde CSV dosyası bulunamadı.")
        latest_files = sorted(csv_files, key=lambda x: os.path.getctime(os.path.join(csv_dir, x)), reverse=True)[:3]
        return [os.path.join(csv_dir, f) for f in latest_files]
    except Exception as e:
        logging.error(f"Son CSV dosyaları bulunurken hata oluştu: {e}")
        return None

# acq_time değerini HH:MM formatına çevir
def format_time(acq_time):
    try:
        acq_time_str = str(int(acq_time)).zfill(4)
        return f"{acq_time_str[:2]}:{acq_time_str[2:]}"
    except:
        return "Bilinmiyor"

# Gün/Gece ve Güven seviyelerini Türkçeye çevir
def translate_daynight(value):
    if value == 'D':
        return 'Gündüz'
    elif value == 'N':
        return 'Gece'
    return 'Bilinmiyor'

def translate_confidence(value):
    if value == 'l':
        return 'Düşük'
    elif value == 'n':
        return 'Orta'
    elif value == 'h':
        return 'Yüksek'
    return 'Bilinmiyor'

# Enlem ve boylamı birleştirip Google Maps bağlantısını oluştur
def create_google_maps_link(lat, lon):
    return f"[{lat}, {lon}](https://www.google.com/maps?q={lat},{lon})"

# Verileri birleştirip README.md dosyasına yazdır
def update_readme_with_fire_data():
    csv_files = get_latest_csv_files()

    if csv_files:
        try:
            dfs = []
            satellites = ['VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT', 'VIIRS_SNPP_NRT']
            for file in csv_files:
                df = pd.read_csv(file)
                satellite_name = file.split('_')[1]
                df['Satellite'] = satellite_name
                dfs.append(df)

            merged_df = pd.concat(dfs, ignore_index=True, sort=False).fillna('Yok')

            last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            table_md = f"### Son Güncelleme: {last_update}\n\n"
            table_md += '| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |\n'
            table_md += '|-----------------------------|----------------|----------|-----|----------------|-------------|\n'

            for _, row in merged_df.iterrows():
                # Enlem ve boylamı Google Maps linki ile birleştir
                coords = create_google_maps_link(row['latitude'], row['longitude'])
                
                # Tarih ve saat sütunlarını birleştir
                date_time = f"{row['acq_date']} {format_time(row['acq_time'])}"

                # Güven seviyesi ve gündüz/gece bilgilerini Türkçeye çevir
                confidence_tr = translate_confidence(row.get('confidence', 'Yok'))
                daynight_tr = translate_daynight(row.get('daynight', 'Yok'))

                table_md += f"| {coords} | {date_time} | {row.get('bright_ti4', 'Yok')} | {row.get('frp', 'Yok')} | {confidence_tr} | {daynight_tr} |\n"

            # README.md dosyasını güncelleme, eski verinin üzerine yaz
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write("# Yangın Verileri Takip Sistemi\n")
                f.write("\nBu repo, **Türkiye'deki yangın verilerini** NASA FIRMS (Fire Information for Resource Management System) API'si üzerinden düzenli olarak çekmekte ve kaydetmektedir. Farklı uydulardan (VIIRS_NOAA20_NRT, VIIRS_NOAA21_NRT, VIIRS_SNPP_NRT) gelen veriler, Türkiye'deki son yangınların konumlarını, sıcaklıklarını, parlaklıklarını ve güven seviyelerini içermektedir.\n")
                f.write("\n### Özellikler:\n")
                f.write("- **Üç uydu** ile yangın verilerini toplar.\n")
                f.write("- Veriler, **sıcaklık**, **parlaklık** ve **güven seviyesi** bilgilerini içerir.\n")
                f.write("- **Gece ve gündüz** yangın tespitlerini ayırır.\n")
                f.write("- **JSON, CSV ve SQLite** formatlarında saklanır.\n")
                f.write("- **Ülke kodları** ve **kullanılabilir uydular** bilgileri de otomatik olarak çekilir.\n")
                f.write("- **main.py** içerisinde **uydu bilgilerini** dinamik olarak ayarlayabilirsiniz:\n")
                f.write("\n```python\nsatellite_sources = ['VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT', 'VIIRS_SNPP_NRT']\n```\n")
                f.write("- **main.py** içerisinde ülke kodu ve gün aralığı parametreleri dinamik olarak ayarlanabilir:\n")
                f.write("\n```python\ncountry_code = 'TUR'  # Ülke kodu burada ayarlanabilir\ndays = 1  # Son 24 saatlik veriler için gün aralığı\n```\n")
                f.write("\n### `update_readme.py` Ne Yapar?\n")
                f.write("Bu script, çekilen son verileri işleyerek, **README.md** dosyasına bir tablo halinde kaydeder. Tabloda yangınların enlem, boylam, sıcaklık, güven seviyesi ve gündüz/gece bilgileri yer alır. Güncellemeler her çalıştırıldığında otomatik olarak yapılır ve dosyanın üzerine yazılır, böylece en güncel veriler her zaman README.md dosyasında bulunur. Verilerin nasıl kullanılabileceğine bir örnektir.\n")
                f.write("\n## Son Yangın Verileri\n")
                f.write(table_md)

            logging.info(f"README.md dosyasına son veriler başarıyla eklendi.")
        except Exception as e:
            logging.error(f"README.md güncellenirken hata oluştu: {e}")
    else:
        logging.error("Son CSV dosyaları bulunamadı.")

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    update_readme_with_fire_data()
