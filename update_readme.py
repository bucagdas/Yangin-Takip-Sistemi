import os
import pandas as pd
import logging
from datetime import datetime, timedelta

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

trim_log('update_readme.log', MAX_LOG_LINES)
logging.basicConfig(filename='update_readme.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='a')


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


def format_time(acq_time):
    try:
        acq_time_str = str(int(acq_time)).zfill(4)
        return f"{acq_time_str[:2]}:{acq_time_str[2:]}"
    except (ValueError, TypeError):
        return "Bilinmiyor"


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


def create_google_maps_link(lat, lon):
    return f"[{lat}, {lon}](https://www.google.com/maps?q={lat},{lon})"


def update_readme_with_fire_data():
    csv_files = get_latest_csv_files()

    if csv_files:
        try:
            dfs = []
            for file in csv_files:
                df = pd.read_csv(file)
                satellite_name = os.path.basename(file).replace('.csv', '').split('_', 1)[1]
                df['Satellite'] = satellite_name
                dfs.append(df)

            merged_df = pd.concat(dfs, ignore_index=True, sort=False).fillna('Yok')

            now = datetime.utcnow()
            merged_df['acq_datetime'] = pd.to_datetime(merged_df['acq_date'] + ' ' + merged_df['acq_time'].apply(format_time))
            filtered_df = merged_df[merged_df['acq_datetime'] >= now - timedelta(days=1)]

            if filtered_df.empty:
                logging.info("Son 24 saatte veri bulunamadı.")
                return

            table_md = f"### Son Güncelleme: {now.strftime('%Y-%m-%d %H:%M:%S')} (UTC)\n\n"
            table_md += '| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |\n'
            table_md += '|-----------------------------|----------------|----------|-----|----------------|-------------|\n'

            for _, row in filtered_df.iterrows():
                coords = create_google_maps_link(row['latitude'], row['longitude'])
                date_time = f"{row['acq_date']} {format_time(row['acq_time'])}"
                confidence_tr = translate_confidence(row.get('confidence', 'Yok'))
                daynight_tr = translate_daynight(row.get('daynight', 'Yok'))
                table_md += f"| {coords} | {date_time} | {row.get('bright_ti4', 'Yok')} | {row.get('frp', 'Yok')} | {confidence_tr} | {daynight_tr} |\n"

            with open('README.md', 'w', encoding='utf-8') as f:
                f.write("# Yangın Takip Sistemi\n")
                f.write("\nBu repo, **Türkiye'deki yangın verilerini** NASA FIRMS (Fire Information for Resource Management System) API'si üzerinden düzenli olarak çekmekte ve kaydetmektedir. Farklı uydulardan (VIIRS_NOAA20_NRT, VIIRS_NOAA21_NRT, VIIRS_SNPP_NRT) gelen veriler, Türkiye'deki son yangınların konumlarını, sıcaklıklarını, parlaklıklarını ve güven seviyelerini içermektedir.\n")
                f.write("\n## Son Yangın Verileri\n")
                f.write(table_md)
                f.write("\n## Yazar\n")
                f.write("\n[bucagdas](https://x.com/bucagdas)\n")

            logging.info("README.md güncellendi.")
        except Exception as e:
            logging.error(f"README.md güncellenirken hata oluştu: {e}")
    else:
        logging.error("Son CSV dosyaları bulunamadı.")


if __name__ == "__main__":
    update_readme_with_fire_data()
