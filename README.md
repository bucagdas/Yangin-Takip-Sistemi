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
### Son Güncelleme: 2024-10-04 11:38:21 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.65732, 30.61868](https://www.google.com/maps?q=38.65732,30.61868) | 2024-10-04 00:54 | 299.85 | 1.52 | Orta | Gece |
| [38.65868, 30.62128](https://www.google.com/maps?q=38.65868,30.62128) | 2024-10-04 00:54 | 297.44 | 1.15 | Orta | Gece |
| [39.48164, 30.0402](https://www.google.com/maps?q=39.48164,30.0402) | 2024-10-04 00:54 | 298.94 | 1.82 | Orta | Gece |
| [39.86686, 26.24587](https://www.google.com/maps?q=39.86686,26.24587) | 2024-10-04 00:54 | 297.68 | 0.35 | Orta | Gece |
| [40.18222, 28.90865](https://www.google.com/maps?q=40.18222,28.90865) | 2024-10-04 00:54 | 298.32 | 0.48 | Orta | Gece |
| [40.18321, 28.9081](https://www.google.com/maps?q=40.18321,28.9081) | 2024-10-04 00:54 | 295.91 | 0.52 | Orta | Gece |
| [41.02139, 28.55472](https://www.google.com/maps?q=41.02139,28.55472) | 2024-10-04 00:54 | 306.57 | 0.92 | Orta | Gece |
| [41.25256, 31.4131](https://www.google.com/maps?q=41.25256,31.4131) | 2024-10-04 00:54 | 305.94 | 1.21 | Orta | Gece |
| [41.25505, 31.41415](https://www.google.com/maps?q=41.25505,31.41415) | 2024-10-04 00:54 | 307.42 | 0.89 | Orta | Gece |
| [41.26231, 31.42662](https://www.google.com/maps?q=41.26231,31.42662) | 2024-10-04 00:54 | 297.87 | 1.05 | Orta | Gece |
| [41.29116, 27.98003](https://www.google.com/maps?q=41.29116,27.98003) | 2024-10-04 00:54 | 297.9 | 1.17 | Orta | Gece |
| [41.29242, 27.97553](https://www.google.com/maps?q=41.29242,27.97553) | 2024-10-04 00:54 | 313.84 | 1.17 | Orta | Gece |
| [41.79741, 26.70156](https://www.google.com/maps?q=41.79741,26.70156) | 2024-10-04 00:54 | 298.87 | 0.4 | Orta | Gece |
| [38.42524, 27.2156](https://www.google.com/maps?q=38.42524,27.2156) | 2024-10-04 00:56 | 305.38 | 0.71 | Orta | Gece |
| [38.42798, 27.21608](https://www.google.com/maps?q=38.42798,27.21608) | 2024-10-04 00:56 | 302.46 | 0.79 | Orta | Gece |
| [38.73245, 26.96438](https://www.google.com/maps?q=38.73245,26.96438) | 2024-10-04 00:56 | 297.0 | 0.4 | Orta | Gece |
| [38.73729, 26.94695](https://www.google.com/maps?q=38.73729,26.94695) | 2024-10-04 00:56 | 306.17 | 0.75 | Orta | Gece |
| [38.73813, 26.94547](https://www.google.com/maps?q=38.73813,26.94547) | 2024-10-04 00:56 | 315.24 | 1.86 | Orta | Gece |
| [38.73856, 26.94239](https://www.google.com/maps?q=38.73856,26.94239) | 2024-10-04 00:56 | 304.41 | 0.75 | Orta | Gece |
| [38.7426, 26.94931](https://www.google.com/maps?q=38.7426,26.94931) | 2024-10-04 00:56 | 302.07 | 0.75 | Orta | Gece |
| [38.74388, 26.9447](https://www.google.com/maps?q=38.74388,26.9447) | 2024-10-04 00:56 | 297.96 | 0.75 | Orta | Gece |
| [39.10979, 27.59354](https://www.google.com/maps?q=39.10979,27.59354) | 2024-10-04 00:56 | 296.73 | 0.46 | Orta | Gece |
| [39.16848, 27.63172](https://www.google.com/maps?q=39.16848,27.63172) | 2024-10-04 00:56 | 299.04 | 0.68 | Orta | Gece |
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
| [41.2982, 27.97364](https://www.google.com/maps?q=41.2982,27.97364) | 2024-10-04 01:17 | 298.15 | 0.91 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
