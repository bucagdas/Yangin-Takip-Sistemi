# Yangın Takip Sistemi

Bu repo, **Türkiye'deki yangın verilerini** NASA FIRMS (Fire Information for Resource Management System) API'si üzerinden düzenli olarak çekmekte ve kaydetmektedir. Farklı uydulardan (VIIRS_NOAA20_NRT, VIIRS_NOAA21_NRT, VIIRS_SNPP_NRT) gelen veriler, Türkiye'deki son yangınların konumlarını, sıcaklıklarını, parlaklıklarını ve güven seviyelerini içermektedir.

### Özellikler:
- **Üç uydu** ile yangın verilerini toplar.
- Veriler, **sıcaklık**, **parlaklık** ve **güven seviyesi** bilgilerini içerir.
- **Gece ve gündüz** yangın tespitlerini ayırır.
- **JSON, CSV ve SQLite** formatlarında saklanır.
- **Ülke kodları** ve **kullanılabilir uydular** bilgileri de otomatik olarak çekilir.
- **main.py** içerisinde **uydu bilgilerini** dinamik olarak ayarlayabilirsiniz:

```python
satellite_sources = ['VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT', 'VIIRS_SNPP_NRT']
```
- **main.py** içerisinde ülke kodu ve gün aralığı parametreleri dinamik olarak ayarlanabilir:

```python
country_code = 'TUR'  # Ülke kodu burada ayarlanabilir
days = 1  # Son 24 saatlik veriler için gün aralığı
```

### `update_readme.py` Ne Yapar?
Bu script verilerin nasıl kullanılabileceğine dair bir örnektir. Script çekilen son verileri işleyerek, **README.md** dosyasına bir tablo halinde kaydeder. Tabloda yangınların enlem, boylam, sıcaklık, güven seviyesi ve gündüz/gece bilgileri yer alır. Güncellemeler her çalıştırıldığında otomatik olarak yapılır ve dosyanın üzerine yazılır, böylece en güncel veriler her zaman README.md dosyasında bulunur.

## Son Yangın Verileri
### Son Güncelleme: 2024-10-04 02:43:27 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.45564, 38.72377](https://www.google.com/maps?q=38.45564,38.72377) | 2024-10-04 00:30 | 297.3 | 2.41 | Orta | Gece |
| [40.76294, 29.53064](https://www.google.com/maps?q=40.76294,29.53064) | 2024-10-04 00:30 | 330.18 | 5.64 | Orta | Gece |
| [41.0207, 28.55591](https://www.google.com/maps?q=41.0207,28.55591) | 2024-10-04 00:30 | 311.81 | 1.51 | Orta | Gece |
| [41.24054, 36.46345](https://www.google.com/maps?q=41.24054,36.46345) | 2024-10-04 00:30 | 308.7 | 2.04 | Orta | Gece |
| [41.24385, 36.46381](https://www.google.com/maps?q=41.24385,36.46381) | 2024-10-04 00:30 | 304.63 | 2.03 | Orta | Gece |
| [41.25238, 31.40984](https://www.google.com/maps?q=41.25238,31.40984) | 2024-10-04 00:30 | 300.54 | 0.8 | Orta | Gece |
| [41.25688, 31.41197](https://www.google.com/maps?q=41.25688,31.41197) | 2024-10-04 00:30 | 312.39 | 1.78 | Orta | Gece |
| [41.26432, 31.42247](https://www.google.com/maps?q=41.26432,31.42247) | 2024-10-04 00:30 | 303.63 | 2.53 | Orta | Gece |
| [41.26659, 31.42231](https://www.google.com/maps?q=41.26659,31.42231) | 2024-10-04 00:30 | 304.91 | 2.35 | Orta | Gece |
| [41.29445, 27.98087](https://www.google.com/maps?q=41.29445,27.98087) | 2024-10-04 00:30 | 312.62 | 2.62 | Orta | Gece |
| [41.29543, 27.97639](https://www.google.com/maps?q=41.29543,27.97639) | 2024-10-04 00:30 | 327.64 | 3.33 | Orta | Gece |
| [41.7979, 26.70042](https://www.google.com/maps?q=41.7979,26.70042) | 2024-10-04 00:30 | 300.77 | 0.95 | Orta | Gece |
| [36.7314, 36.2121](https://www.google.com/maps?q=36.7314,36.2121) | 2024-10-04 00:33 | 304.26 | 2.07 | Orta | Gece |
| [37.01278, 36.10263](https://www.google.com/maps?q=37.01278,36.10263) | 2024-10-04 00:33 | 300.5 | 1.46 | Orta | Gece |
| [37.01902, 36.10556](https://www.google.com/maps?q=37.01902,36.10556) | 2024-10-04 00:33 | 302.64 | 1.46 | Orta | Gece |
| [37.29126, 37.15622](https://www.google.com/maps?q=37.29126,37.15622) | 2024-10-04 00:33 | 298.65 | 1.8 | Orta | Gece |
| [37.35247, 37.16269](https://www.google.com/maps?q=37.35247,37.16269) | 2024-10-04 00:33 | 299.5 | 2.13 | Orta | Gece |
| [38.42468, 27.21661](https://www.google.com/maps?q=38.42468,27.21661) | 2024-10-04 00:33 | 311.34 | 1.63 | Orta | Gece |
| [38.45298, 27.26376](https://www.google.com/maps?q=38.45298,27.26376) | 2024-10-04 00:33 | 300.06 | 0.91 | Orta | Gece |
| [38.65954, 30.61669](https://www.google.com/maps?q=38.65954,30.61669) | 2024-10-04 00:33 | 303.57 | 1.7 | Orta | Gece |
| [38.66032, 30.61652](https://www.google.com/maps?q=38.66032,30.61652) | 2024-10-04 00:33 | 296.68 | 2.44 | Orta | Gece |
| [38.73115, 26.93241](https://www.google.com/maps?q=38.73115,26.93241) | 2024-10-04 00:33 | 297.76 | 0.36 | Orta | Gece |
| [38.73704, 26.94392](https://www.google.com/maps?q=38.73704,26.94392) | 2024-10-04 00:33 | 321.16 | 3.08 | Orta | Gece |
| [38.73986, 26.9309](https://www.google.com/maps?q=38.73986,26.9309) | 2024-10-04 00:33 | 323.3 | 3.1 | Orta | Gece |
| [38.73999, 26.94967](https://www.google.com/maps?q=38.73999,26.94967) | 2024-10-04 00:33 | 301.06 | 0.95 | Orta | Gece |
| [38.74388, 26.95108](https://www.google.com/maps?q=38.74388,26.95108) | 2024-10-04 00:33 | 299.48 | 0.95 | Orta | Gece |
| [38.74483, 26.94666](https://www.google.com/maps?q=38.74483,26.94666) | 2024-10-04 00:33 | 308.65 | 0.95 | Orta | Gece |
| [39.09304, 27.50981](https://www.google.com/maps?q=39.09304,27.50981) | 2024-10-04 00:33 | 306.06 | 1.4 | Orta | Gece |
| [39.10904, 27.59363](https://www.google.com/maps?q=39.10904,27.59363) | 2024-10-04 00:33 | 297.63 | 0.62 | Orta | Gece |
| [39.11368, 27.51335](https://www.google.com/maps?q=39.11368,27.51335) | 2024-10-04 00:33 | 298.73 | 0.88 | Orta | Gece |
| [39.16846, 27.63413](https://www.google.com/maps?q=39.16846,27.63413) | 2024-10-04 00:33 | 301.24 | 0.85 | Orta | Gece |
| [39.48553, 30.0433](https://www.google.com/maps?q=39.48553,30.0433) | 2024-10-04 00:33 | 304.64 | 1.55 | Orta | Gece |
| [39.83742, 30.30316](https://www.google.com/maps?q=39.83742,30.30316) | 2024-10-04 00:33 | 296.51 | 0.94 | Orta | Gece |
| [39.86623, 26.24479](https://www.google.com/maps?q=39.86623,26.24479) | 2024-10-04 00:33 | 301.04 | 0.89 | Orta | Gece |
| [39.86628, 26.24531](https://www.google.com/maps?q=39.86628,26.24531) | 2024-10-04 00:33 | 301.49 | 1.33 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
