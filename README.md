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
### Son Güncelleme: 2024-10-04 13:35:07 (UTC)

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
| [36.65555, 37.46731](https://www.google.com/maps?q=36.65555,37.46731) | 2024-10-04 10:11 | 334.19 | 3.11 | Orta | Gündüz |
| [36.6562, 35.2806](https://www.google.com/maps?q=36.6562,35.2806) | 2024-10-04 10:11 | 340.35 | 7.2 | Orta | Gündüz |
| [36.7254, 35.24391](https://www.google.com/maps?q=36.7254,35.24391) | 2024-10-04 10:11 | 334.33 | 5.34 | Orta | Gündüz |
| [36.72635, 35.24837](https://www.google.com/maps?q=36.72635,35.24837) | 2024-10-04 10:11 | 353.71 | 8.11 | Orta | Gündüz |
| [36.73035, 35.24707](https://www.google.com/maps?q=36.73035,35.24707) | 2024-10-04 10:11 | 341.1 | 8.11 | Orta | Gündüz |
| [36.76587, 37.62452](https://www.google.com/maps?q=36.76587,37.62452) | 2024-10-04 10:11 | 345.54 | 10.36 | Orta | Gündüz |
| [36.84926, 34.8465](https://www.google.com/maps?q=36.84926,34.8465) | 2024-10-04 10:11 | 332.22 | 3.0 | Orta | Gündüz |
| [36.94416, 35.7597](https://www.google.com/maps?q=36.94416,35.7597) | 2024-10-04 10:11 | 341.13 | 9.8 | Orta | Gündüz |
| [36.97548, 38.69616](https://www.google.com/maps?q=36.97548,38.69616) | 2024-10-04 10:11 | 348.89 | 3.95 | Orta | Gündüz |
| [36.97559, 37.42879](https://www.google.com/maps?q=36.97559,37.42879) | 2024-10-04 10:11 | 336.21 | 1.57 | Düşük | Gündüz |
| [36.97633, 38.70089](https://www.google.com/maps?q=36.97633,38.70089) | 2024-10-04 10:11 | 337.33 | 1.37 | Düşük | Gündüz |
| [36.99433, 38.3357](https://www.google.com/maps?q=36.99433,38.3357) | 2024-10-04 10:11 | 342.88 | 7.99 | Orta | Gündüz |
| [37.14341, 36.8838](https://www.google.com/maps?q=37.14341,36.8838) | 2024-10-04 10:11 | 345.41 | 9.18 | Orta | Gündüz |
| [37.20651, 39.44168](https://www.google.com/maps?q=37.20651,39.44168) | 2024-10-04 10:11 | 338.15 | 2.51 | Orta | Gündüz |
| [37.2073, 39.44622](https://www.google.com/maps?q=37.2073,39.44622) | 2024-10-04 10:11 | 344.0 | 2.51 | Orta | Gündüz |
| [37.26862, 40.19196](https://www.google.com/maps?q=37.26862,40.19196) | 2024-10-04 10:11 | 339.01 | 6.37 | Orta | Gündüz |
| [37.26936, 40.19637](https://www.google.com/maps?q=37.26936,40.19637) | 2024-10-04 10:11 | 352.34 | 6.37 | Orta | Gündüz |
| [37.27193, 40.1911](https://www.google.com/maps?q=37.27193,40.1911) | 2024-10-04 10:11 | 367.0 | 6.37 | Yüksek | Gündüz |
| [37.27267, 40.19551](https://www.google.com/maps?q=37.27267,40.19551) | 2024-10-04 10:11 | 337.52 | 6.37 | Orta | Gündüz |
| [37.27524, 40.19024](https://www.google.com/maps?q=37.27524,40.19024) | 2024-10-04 10:11 | 347.97 | 7.61 | Orta | Gündüz |
| [37.48573, 38.03415](https://www.google.com/maps?q=37.48573,38.03415) | 2024-10-04 10:11 | 338.14 | 11.41 | Orta | Gündüz |
| [37.57344, 38.80988](https://www.google.com/maps?q=37.57344,38.80988) | 2024-10-04 10:11 | 344.72 | 5.47 | Orta | Gündüz |
| [37.58115, 37.43017](https://www.google.com/maps?q=37.58115,37.43017) | 2024-10-04 10:11 | 347.57 | 11.63 | Orta | Gündüz |
| [37.58585, 37.39555](https://www.google.com/maps?q=37.58585,37.39555) | 2024-10-04 10:11 | 339.9 | 26.23 | Düşük | Gündüz |
| [37.58992, 39.14098](https://www.google.com/maps?q=37.58992,39.14098) | 2024-10-04 10:11 | 339.06 | 3.61 | Düşük | Gündüz |
| [37.60183, 37.38028](https://www.google.com/maps?q=37.60183,37.38028) | 2024-10-04 10:11 | 340.4 | 4.04 | Orta | Gündüz |
| [37.62605, 37.42827](https://www.google.com/maps?q=37.62605,37.42827) | 2024-10-04 10:11 | 344.4 | 17.46 | Düşük | Gündüz |
| [37.62664, 37.42639](https://www.google.com/maps?q=37.62664,37.42639) | 2024-10-04 10:11 | 349.72 | 24.54 | Orta | Gündüz |
| [37.66554, 38.2137](https://www.google.com/maps?q=37.66554,38.2137) | 2024-10-04 10:11 | 343.4 | 6.65 | Orta | Gündüz |
| [37.70988, 38.77805](https://www.google.com/maps?q=37.70988,38.77805) | 2024-10-04 10:11 | 345.59 | 4.14 | Orta | Gündüz |
| [37.71073, 38.78277](https://www.google.com/maps?q=37.71073,38.78277) | 2024-10-04 10:11 | 335.65 | 4.14 | Düşük | Gündüz |
| [37.71762, 39.44489](https://www.google.com/maps?q=37.71762,39.44489) | 2024-10-04 10:11 | 345.25 | 6.17 | Orta | Gündüz |
| [37.72097, 39.44398](https://www.google.com/maps?q=37.72097,39.44398) | 2024-10-04 10:11 | 347.9 | 6.17 | Orta | Gündüz |
| [37.79568, 40.20622](https://www.google.com/maps?q=37.79568,40.20622) | 2024-10-04 10:11 | 339.85 | 2.32 | Orta | Gündüz |
| [37.91706, 40.93086](https://www.google.com/maps?q=37.91706,40.93086) | 2024-10-04 10:11 | 346.79 | 7.07 | Orta | Gündüz |
| [37.94922, 40.85501](https://www.google.com/maps?q=37.94922,40.85501) | 2024-10-04 10:11 | 346.72 | 4.19 | Orta | Gündüz |
| [37.9613, 40.88797](https://www.google.com/maps?q=37.9613,40.88797) | 2024-10-04 10:11 | 337.95 | 4.32 | Düşük | Gündüz |
| [37.99988, 41.04498](https://www.google.com/maps?q=37.99988,41.04498) | 2024-10-04 10:11 | 338.99 | 8.22 | Düşük | Gündüz |
| [38.01741, 40.49401](https://www.google.com/maps?q=38.01741,40.49401) | 2024-10-04 10:11 | 340.87 | 3.71 | Düşük | Gündüz |
| [38.11377, 40.85929](https://www.google.com/maps?q=38.11377,40.85929) | 2024-10-04 10:11 | 343.97 | 7.14 | Düşük | Gündüz |
| [38.11705, 40.85845](https://www.google.com/maps?q=38.11705,40.85845) | 2024-10-04 10:11 | 349.82 | 7.28 | Orta | Gündüz |
| [38.12033, 40.66388](https://www.google.com/maps?q=38.12033,40.66388) | 2024-10-04 10:11 | 337.9 | 3.25 | Orta | Gündüz |
| [38.12361, 40.66304](https://www.google.com/maps?q=38.12361,40.66304) | 2024-10-04 10:11 | 337.0 | 3.25 | Orta | Gündüz |
| [38.12978, 40.98166](https://www.google.com/maps?q=38.12978,40.98166) | 2024-10-04 10:11 | 345.38 | 6.27 | Orta | Gündüz |
| [38.13047, 40.98599](https://www.google.com/maps?q=38.13047,40.98599) | 2024-10-04 10:11 | 351.84 | 10.12 | Orta | Gündüz |
| [38.13531, 36.92759](https://www.google.com/maps?q=38.13531,36.92759) | 2024-10-04 10:11 | 332.73 | 19.85 | Düşük | Gündüz |
| [38.14097, 40.98786](https://www.google.com/maps?q=38.14097,40.98786) | 2024-10-04 10:11 | 339.12 | 4.18 | Orta | Gündüz |
| [38.17338, 40.78172](https://www.google.com/maps?q=38.17338,40.78172) | 2024-10-04 10:11 | 349.06 | 4.47 | Orta | Gündüz |
| [38.1737, 40.6774](https://www.google.com/maps?q=38.1737,40.6774) | 2024-10-04 10:11 | 345.09 | 7.46 | Düşük | Gündüz |
| [38.17627, 40.6722](https://www.google.com/maps?q=38.17627,40.6722) | 2024-10-04 10:11 | 353.92 | 8.68 | Orta | Gündüz |
| [38.17653, 29.69821](https://www.google.com/maps?q=38.17653,29.69821) | 2024-10-04 10:11 | 337.02 | 2.88 | Orta | Gündüz |
| [38.17955, 40.67135](https://www.google.com/maps?q=38.17955,40.67135) | 2024-10-04 10:11 | 346.57 | 8.68 | Orta | Gündüz |
| [38.188, 37.0419](https://www.google.com/maps?q=38.188,37.0419) | 2024-10-04 10:11 | 335.1 | 6.4 | Orta | Gündüz |
| [38.18984, 40.86353](https://www.google.com/maps?q=38.18984,40.86353) | 2024-10-04 10:11 | 348.56 | 5.18 | Orta | Gündüz |
| [38.23396, 41.0779](https://www.google.com/maps?q=38.23396,41.0779) | 2024-10-04 10:11 | 337.5 | 1.82 | Düşük | Gündüz |
| [38.25779, 37.08679](https://www.google.com/maps?q=38.25779,37.08679) | 2024-10-04 10:11 | 337.98 | 4.16 | Orta | Gündüz |
| [38.28061, 37.60704](https://www.google.com/maps?q=38.28061,37.60704) | 2024-10-04 10:11 | 336.78 | 5.62 | Orta | Gündüz |
| [38.4229, 29.58679](https://www.google.com/maps?q=38.4229,29.58679) | 2024-10-04 10:11 | 344.07 | 5.33 | Orta | Gündüz |
| [38.51192, 29.49912](https://www.google.com/maps?q=38.51192,29.49912) | 2024-10-04 10:11 | 367.0 | 8.68 | Yüksek | Gündüz |
| [38.52466, 39.09147](https://www.google.com/maps?q=38.52466,39.09147) | 2024-10-04 10:11 | 342.24 | 3.72 | Orta | Gündüz |
| [38.52547, 39.0961](https://www.google.com/maps?q=38.52547,39.0961) | 2024-10-04 10:11 | 335.42 | 3.72 | Düşük | Gündüz |
| [38.69724, 39.75579](https://www.google.com/maps?q=38.69724,39.75579) | 2024-10-04 10:11 | 340.04 | 5.52 | Orta | Gündüz |
| [38.77504, 39.93707](https://www.google.com/maps?q=38.77504,39.93707) | 2024-10-04 10:11 | 343.66 | 3.55 | Orta | Gündüz |
| [38.79063, 37.44472](https://www.google.com/maps?q=38.79063,37.44472) | 2024-10-04 10:11 | 331.93 | 2.64 | Orta | Gündüz |
| [38.80914, 39.95605](https://www.google.com/maps?q=38.80914,39.95605) | 2024-10-04 10:11 | 342.58 | 6.2 | Orta | Gündüz |
| [38.83919, 30.45971](https://www.google.com/maps?q=38.83919,30.45971) | 2024-10-04 10:11 | 340.39 | 2.32 | Orta | Gündüz |
| [38.8423, 38.61982](https://www.google.com/maps?q=38.8423,38.61982) | 2024-10-04 10:11 | 338.06 | 3.43 | Orta | Gündüz |
| [38.84246, 32.82681](https://www.google.com/maps?q=38.84246,32.82681) | 2024-10-04 10:11 | 340.01 | 2.8 | Orta | Gündüz |
| [38.91967, 41.49247](https://www.google.com/maps?q=38.91967,41.49247) | 2024-10-04 10:11 | 342.03 | 2.81 | Orta | Gündüz |
| [39.05837, 42.72452](https://www.google.com/maps?q=39.05837,42.72452) | 2024-10-04 10:11 | 338.01 | 3.71 | Orta | Gündüz |
| [39.06664, 42.4443](https://www.google.com/maps?q=39.06664,42.4443) | 2024-10-04 10:11 | 339.97 | 4.67 | Orta | Gündüz |
| [39.09549, 42.17239](https://www.google.com/maps?q=39.09549,42.17239) | 2024-10-04 10:11 | 340.94 | 3.73 | Orta | Gündüz |
| [39.13364, 37.88807](https://www.google.com/maps?q=39.13364,37.88807) | 2024-10-04 10:11 | 336.51 | 7.55 | Orta | Gündüz |
| [39.13456, 37.89311](https://www.google.com/maps?q=39.13456,37.89311) | 2024-10-04 10:11 | 337.25 | 5.13 | Orta | Gündüz |
| [39.13802, 37.89227](https://www.google.com/maps?q=39.13802,37.89227) | 2024-10-04 10:11 | 343.61 | 5.13 | Orta | Gündüz |
| [39.13962, 37.88117](https://www.google.com/maps?q=39.13962,37.88117) | 2024-10-04 10:11 | 347.08 | 10.47 | Orta | Gündüz |
| [39.14148, 37.89143](https://www.google.com/maps?q=39.14148,37.89143) | 2024-10-04 10:11 | 347.76 | 7.24 | Orta | Gündüz |
| [39.14505, 37.82322](https://www.google.com/maps?q=39.14505,37.82322) | 2024-10-04 10:11 | 337.37 | 6.38 | Orta | Gündüz |
| [39.17113, 34.79887](https://www.google.com/maps?q=39.17113,34.79887) | 2024-10-04 10:11 | 336.37 | 3.54 | Orta | Gündüz |
| [39.18656, 34.79306](https://www.google.com/maps?q=39.18656,34.79306) | 2024-10-04 10:11 | 335.05 | 6.93 | Orta | Gündüz |
| [39.1875, 34.79753](https://www.google.com/maps?q=39.1875,34.79753) | 2024-10-04 10:11 | 340.29 | 7.97 | Orta | Gündüz |
| [39.18951, 34.78732](https://www.google.com/maps?q=39.18951,34.78732) | 2024-10-04 10:11 | 330.07 | 2.23 | Orta | Gündüz |
| [39.19254, 37.52836](https://www.google.com/maps?q=39.19254,37.52836) | 2024-10-04 10:11 | 337.1 | 3.7 | Orta | Gündüz |
| [39.19317, 37.53062](https://www.google.com/maps?q=39.19317,37.53062) | 2024-10-04 10:11 | 332.22 | 4.52 | Düşük | Gündüz |
| [39.196, 37.52723](https://www.google.com/maps?q=39.196,37.52723) | 2024-10-04 10:11 | 334.8 | 3.7 | Düşük | Gündüz |
| [39.19663, 37.52949](https://www.google.com/maps?q=39.19663,37.52949) | 2024-10-04 10:11 | 346.2 | 4.52 | Orta | Gündüz |
| [39.19693, 37.53225](https://www.google.com/maps?q=39.19693,37.53225) | 2024-10-04 10:11 | 336.88 | 3.7 | Orta | Gündüz |
| [39.3143, 42.31945](https://www.google.com/maps?q=39.3143,42.31945) | 2024-10-04 10:11 | 331.23 | 1.36 | Düşük | Gündüz |
| [39.64376, 43.06647](https://www.google.com/maps?q=39.64376,43.06647) | 2024-10-04 10:11 | 334.13 | 8.45 | Düşük | Gündüz |
| [39.88763, 37.03667](https://www.google.com/maps?q=39.88763,37.03667) | 2024-10-04 10:11 | 334.72 | 4.86 | Orta | Gündüz |
| [40.15191, 36.08332](https://www.google.com/maps?q=40.15191,36.08332) | 2024-10-04 10:11 | 336.39 | 7.46 | Orta | Gündüz |
| [36.67249, 39.26664](https://www.google.com/maps?q=36.67249,39.26664) | 2024-10-04 10:13 | 346.77 | 6.54 | Orta | Gündüz |
| [36.70318, 38.80676](https://www.google.com/maps?q=36.70318,38.80676) | 2024-10-04 10:13 | 346.18 | 7.67 | Orta | Gündüz |
| [36.96256, 40.10181](https://www.google.com/maps?q=36.96256,40.10181) | 2024-10-04 10:13 | 367.0 | 72.25 | Yüksek | Gündüz |
| [37.14068, 41.68848](https://www.google.com/maps?q=37.14068,41.68848) | 2024-10-04 10:13 | 347.24 | 10.39 | Orta | Gündüz |
| [37.14329, 41.68342](https://www.google.com/maps?q=37.14329,41.68342) | 2024-10-04 10:13 | 351.2 | 10.39 | Orta | Gündüz |
| [37.14395, 41.68769](https://www.google.com/maps?q=37.14395,41.68769) | 2024-10-04 10:13 | 343.76 | 10.39 | Düşük | Gündüz |
| [37.17559, 41.73412](https://www.google.com/maps?q=37.17559,41.73412) | 2024-10-04 10:13 | 343.2 | 5.72 | Düşük | Gündüz |
| [37.20917, 44.65594](https://www.google.com/maps?q=37.20917,44.65594) | 2024-10-04 10:13 | 332.75 | 2.74 | Orta | Gündüz |
| [37.44564, 43.19483](https://www.google.com/maps?q=37.44564,43.19483) | 2024-10-04 10:13 | 346.32 | 49.96 | Orta | Gündüz |
| [38.25296, 26.34233](https://www.google.com/maps?q=38.25296,26.34233) | 2024-10-04 10:13 | 344.26 | 8.5 | Orta | Gündüz |
| [38.74537, 26.94877](https://www.google.com/maps?q=38.74537,26.94877) | 2024-10-04 10:13 | 329.89 | 3.75 | Orta | Gündüz |
| [39.14791, 30.11801](https://www.google.com/maps?q=39.14791,30.11801) | 2024-10-04 10:13 | 342.27 | 3.12 | Orta | Gündüz |
| [39.48248, 30.0428](https://www.google.com/maps?q=39.48248,30.0428) | 2024-10-04 10:13 | 330.39 | 2.2 | Orta | Gündüz |
| [39.72955, 30.37315](https://www.google.com/maps?q=39.72955,30.37315) | 2024-10-04 10:13 | 337.96 | 6.23 | Orta | Gündüz |
| [39.73171, 30.37231](https://www.google.com/maps?q=39.73171,30.37231) | 2024-10-04 10:13 | 343.32 | 11.06 | Orta | Gündüz |
| [40.08614, 27.99088](https://www.google.com/maps?q=40.08614,27.99088) | 2024-10-04 10:13 | 335.18 | 3.5 | Orta | Gündüz |
| [40.14997, 28.15926](https://www.google.com/maps?q=40.14997,28.15926) | 2024-10-04 10:13 | 332.76 | 1.9 | Orta | Gündüz |
| [40.26631, 27.71596](https://www.google.com/maps?q=40.26631,27.71596) | 2024-10-04 10:13 | 329.43 | 2.87 | Düşük | Gündüz |
| [40.27729, 27.71184](https://www.google.com/maps?q=40.27729,27.71184) | 2024-10-04 10:13 | 329.02 | 3.37 | Orta | Gündüz |
| [40.27815, 27.71581](https://www.google.com/maps?q=40.27815,27.71581) | 2024-10-04 10:13 | 342.06 | 5.19 | Orta | Gündüz |
| [40.27851, 27.71617](https://www.google.com/maps?q=40.27851,27.71617) | 2024-10-04 10:13 | 336.11 | 3.37 | Orta | Gündüz |
| [40.72956, 26.32307](https://www.google.com/maps?q=40.72956,26.32307) | 2024-10-04 10:13 | 335.59 | 3.77 | Orta | Gündüz |
| [40.74361, 26.32794](https://www.google.com/maps?q=40.74361,26.32794) | 2024-10-04 10:13 | 343.6 | 4.8 | Orta | Gündüz |
| [40.76616, 29.52779](https://www.google.com/maps?q=40.76616,29.52779) | 2024-10-04 10:13 | 326.9 | 2.56 | Düşük | Gündüz |
| [40.76934, 26.13572](https://www.google.com/maps?q=40.76934,26.13572) | 2024-10-04 10:13 | 335.03 | 5.63 | Orta | Gündüz |
| [40.78327, 26.18283](https://www.google.com/maps?q=40.78327,26.18283) | 2024-10-04 10:13 | 347.02 | 7.72 | Orta | Gündüz |
| [40.83593, 26.27576](https://www.google.com/maps?q=40.83593,26.27576) | 2024-10-04 10:13 | 333.01 | 3.86 | Orta | Gündüz |
| [41.22161, 27.62792](https://www.google.com/maps?q=41.22161,27.62792) | 2024-10-04 10:13 | 336.29 | 3.71 | Orta | Gündüz |
| [41.23561, 26.60069](https://www.google.com/maps?q=41.23561,26.60069) | 2024-10-04 10:13 | 338.23 | 3.2 | Orta | Gündüz |
| [41.24262, 36.46774](https://www.google.com/maps?q=41.24262,36.46774) | 2024-10-04 10:13 | 332.27 | 3.57 | Orta | Gündüz |
| [41.25745, 27.20048](https://www.google.com/maps?q=41.25745,27.20048) | 2024-10-04 10:13 | 335.14 | 4.74 | Orta | Gündüz |
| [41.25798, 27.20062](https://www.google.com/maps?q=41.25798,27.20062) | 2024-10-04 10:13 | 336.73 | 4.67 | Orta | Gündüz |
| [41.25871, 27.20495](https://www.google.com/maps?q=41.25871,27.20495) | 2024-10-04 10:13 | 329.44 | 10.98 | Orta | Gündüz |
| [41.25925, 27.20506](https://www.google.com/maps?q=41.25925,27.20506) | 2024-10-04 10:13 | 331.04 | 6.4 | Orta | Gündüz |
| [41.28791, 26.65431](https://www.google.com/maps?q=41.28791,26.65431) | 2024-10-04 10:13 | 337.84 | 3.93 | Orta | Gündüz |
| [41.31172, 27.58481](https://www.google.com/maps?q=41.31172,27.58481) | 2024-10-04 10:13 | 335.0 | 5.02 | Orta | Gündüz |
| [41.31787, 26.7587](https://www.google.com/maps?q=41.31787,26.7587) | 2024-10-04 10:13 | 329.13 | 1.09 | Orta | Gündüz |
| [41.32984, 26.71547](https://www.google.com/maps?q=41.32984,26.71547) | 2024-10-04 10:13 | 330.42 | 4.79 | Orta | Gündüz |
| [41.33661, 26.71783](https://www.google.com/maps?q=41.33661,26.71783) | 2024-10-04 10:13 | 346.89 | 6.7 | Orta | Gündüz |
| [41.33931, 26.72732](https://www.google.com/maps?q=41.33931,26.72732) | 2024-10-04 10:13 | 330.91 | 6.74 | Orta | Gündüz |
| [41.36645, 26.63741](https://www.google.com/maps?q=41.36645,26.63741) | 2024-10-04 10:13 | 367.0 | 15.84 | Yüksek | Gündüz |
| [41.39573, 27.39504](https://www.google.com/maps?q=41.39573,27.39504) | 2024-10-04 10:13 | 344.11 | 4.94 | Orta | Gündüz |
| [41.5129, 27.10686](https://www.google.com/maps?q=41.5129,27.10686) | 2024-10-04 10:13 | 335.84 | 4.23 | Orta | Gündüz |
| [41.2982, 27.97364](https://www.google.com/maps?q=41.2982,27.97364) | 2024-10-04 01:17 | 298.15 | 0.91 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
