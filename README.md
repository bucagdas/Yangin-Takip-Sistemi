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
### Son Güncelleme: 2024-10-12 11:18:14 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [36.86851, 34.76537](https://www.google.com/maps?q=36.86851,34.76537) | 2024-10-12 00:03 | 302.32 | 1.54 | Orta | Gece |
| [37.02074, 36.10958](https://www.google.com/maps?q=37.02074,36.10958) | 2024-10-12 00:03 | 304.53 | 1.23 | Orta | Gece |
| [37.29361, 37.15895](https://www.google.com/maps?q=37.29361,37.15895) | 2024-10-12 00:03 | 302.24 | 0.57 | Orta | Gece |
| [37.29439, 37.15594](https://www.google.com/maps?q=37.29439,37.15594) | 2024-10-12 00:03 | 298.35 | 0.57 | Orta | Gece |
| [37.29515, 37.15694](https://www.google.com/maps?q=37.29515,37.15694) | 2024-10-12 00:03 | 302.65 | 1.12 | Orta | Gece |
| [37.35164, 37.16309](https://www.google.com/maps?q=37.35164,37.16309) | 2024-10-12 00:03 | 310.35 | 0.9 | Orta | Gece |
| [37.6592, 40.21764](https://www.google.com/maps?q=37.6592,40.21764) | 2024-10-12 00:03 | 295.61 | 0.36 | Orta | Gece |
| [37.66931, 38.26469](https://www.google.com/maps?q=37.66931,38.26469) | 2024-10-12 00:03 | 296.11 | 0.43 | Orta | Gece |
| [37.71026, 40.89472](https://www.google.com/maps?q=37.71026,40.89472) | 2024-10-12 00:03 | 308.48 | 1.1 | Orta | Gece |
| [37.71175, 40.88952](https://www.google.com/maps?q=37.71175,40.88952) | 2024-10-12 00:03 | 299.65 | 1.1 | Orta | Gece |
| [37.72835, 38.1699](https://www.google.com/maps?q=37.72835,38.1699) | 2024-10-12 00:03 | 296.68 | 0.37 | Orta | Gece |
| [37.76801, 38.34153](https://www.google.com/maps?q=37.76801,38.34153) | 2024-10-12 00:03 | 297.84 | 0.33 | Orta | Gece |
| [37.7719, 27.44005](https://www.google.com/maps?q=37.7719,27.44005) | 2024-10-12 00:03 | 299.68 | 0.8 | Orta | Gece |
| [37.78412, 38.55219](https://www.google.com/maps?q=37.78412,38.55219) | 2024-10-12 00:03 | 302.61 | 0.87 | Orta | Gece |
| [37.85764, 40.33261](https://www.google.com/maps?q=37.85764,40.33261) | 2024-10-12 00:03 | 300.64 | 1.35 | Orta | Gece |
| [37.86033, 40.34536](https://www.google.com/maps?q=37.86033,40.34536) | 2024-10-12 00:03 | 300.04 | 0.78 | Orta | Gece |
| [37.8606, 29.37261](https://www.google.com/maps?q=37.8606,29.37261) | 2024-10-12 00:03 | 298.17 | 0.58 | Orta | Gece |
| [37.86322, 40.33511](https://www.google.com/maps?q=37.86322,40.33511) | 2024-10-12 00:03 | 311.27 | 1.35 | Orta | Gece |
| [37.93891, 32.53222](https://www.google.com/maps?q=37.93891,32.53222) | 2024-10-12 00:03 | 295.72 | 0.75 | Orta | Gece |
| [37.951, 40.0886](https://www.google.com/maps?q=37.951,40.0886) | 2024-10-12 00:03 | 297.74 | 0.86 | Orta | Gece |
| [37.95586, 41.03117](https://www.google.com/maps?q=37.95586,41.03117) | 2024-10-12 00:03 | 297.52 | 0.95 | Orta | Gece |
| [37.95736, 41.02602](https://www.google.com/maps?q=37.95736,41.02602) | 2024-10-12 00:03 | 305.91 | 0.95 | Orta | Gece |
| [38.01483, 41.05224](https://www.google.com/maps?q=38.01483,41.05224) | 2024-10-12 00:03 | 336.37 | 2.22 | Orta | Gece |
| [38.01675, 41.05386](https://www.google.com/maps?q=38.01675,41.05386) | 2024-10-12 00:03 | 334.42 | 5.01 | Orta | Gece |
| [38.02061, 41.05473](https://www.google.com/maps?q=38.02061,41.05473) | 2024-10-12 00:03 | 296.29 | 2.22 | Orta | Gece |
| [38.12301, 40.16565](https://www.google.com/maps?q=38.12301,40.16565) | 2024-10-12 00:03 | 297.33 | 0.6 | Orta | Gece |
| [38.12442, 40.16062](https://www.google.com/maps?q=38.12442,40.16062) | 2024-10-12 00:03 | 302.2 | 0.9 | Orta | Gece |
| [38.12504, 40.92689](https://www.google.com/maps?q=38.12504,40.92689) | 2024-10-12 00:03 | 300.4 | 1.71 | Orta | Gece |
| [38.12668, 40.92123](https://www.google.com/maps?q=38.12668,40.92123) | 2024-10-12 00:03 | 296.86 | 1.03 | Orta | Gece |
| [38.13239, 40.92378](https://www.google.com/maps?q=38.13239,40.92378) | 2024-10-12 00:03 | 296.54 | 1.03 | Orta | Gece |
| [38.15612, 40.66377](https://www.google.com/maps?q=38.15612,40.66377) | 2024-10-12 00:03 | 308.95 | 1.85 | Orta | Gece |
| [38.15627, 40.6685](https://www.google.com/maps?q=38.15627,40.6685) | 2024-10-12 00:03 | 302.7 | 0.98 | Orta | Gece |
| [38.1577, 40.66344](https://www.google.com/maps?q=38.1577,40.66344) | 2024-10-12 00:03 | 301.29 | 0.98 | Orta | Gece |
| [38.39082, 30.76323](https://www.google.com/maps?q=38.39082,30.76323) | 2024-10-12 00:03 | 297.31 | 1.47 | Orta | Gece |
| [38.42748, 27.21807](https://www.google.com/maps?q=38.42748,27.21807) | 2024-10-12 00:03 | 313.07 | 1.38 | Orta | Gece |
| [38.45322, 38.72651](https://www.google.com/maps?q=38.45322,38.72651) | 2024-10-12 00:03 | 301.78 | 1.31 | Orta | Gece |
| [38.45415, 38.72842](https://www.google.com/maps?q=38.45415,38.72842) | 2024-10-12 00:03 | 309.41 | 0.85 | Orta | Gece |
| [38.61913, 27.05889](https://www.google.com/maps?q=38.61913,27.05889) | 2024-10-12 00:03 | 299.56 | 0.48 | Orta | Gece |
| [38.66181, 39.2358](https://www.google.com/maps?q=38.66181,39.2358) | 2024-10-12 00:03 | 295.75 | 0.56 | Orta | Gece |
| [38.73121, 26.93049](https://www.google.com/maps?q=38.73121,26.93049) | 2024-10-12 00:03 | 307.16 | 0.91 | Orta | Gece |
| [38.73573, 26.94534](https://www.google.com/maps?q=38.73573,26.94534) | 2024-10-12 00:03 | 307.33 | 1.86 | Orta | Gece |
| [38.73779, 26.93218](https://www.google.com/maps?q=38.73779,26.93218) | 2024-10-12 00:03 | 329.36 | 1.02 | Orta | Gece |
| [38.73833, 26.95057](https://www.google.com/maps?q=38.73833,26.95057) | 2024-10-12 00:03 | 302.31 | 0.87 | Orta | Gece |
| [38.73901, 26.94619](https://www.google.com/maps?q=38.73901,26.94619) | 2024-10-12 00:03 | 329.49 | 1.86 | Orta | Gece |
| [38.74108, 26.93302](https://www.google.com/maps?q=38.74108,26.93302) | 2024-10-12 00:03 | 302.09 | 1.02 | Orta | Gece |
| [38.74231, 26.94703](https://www.google.com/maps?q=38.74231,26.94703) | 2024-10-12 00:03 | 306.98 | 1.0 | Orta | Gece |
| [38.74559, 26.94787](https://www.google.com/maps?q=38.74559,26.94787) | 2024-10-12 00:03 | 309.93 | 1.0 | Orta | Gece |
| [38.7482, 26.9531](https://www.google.com/maps?q=38.7482,26.9531) | 2024-10-12 00:03 | 309.25 | 0.61 | Orta | Gece |
| [38.7899, 26.92725](https://www.google.com/maps?q=38.7899,26.92725) | 2024-10-12 00:03 | 307.79 | 0.71 | Orta | Gece |
| [38.79319, 26.92809](https://www.google.com/maps?q=38.79319,26.92809) | 2024-10-12 00:03 | 302.05 | 0.78 | Orta | Gece |
| [39.0913, 27.51047](https://www.google.com/maps?q=39.0913,27.51047) | 2024-10-12 00:03 | 304.26 | 0.65 | Orta | Gece |
| [39.11502, 27.51221](https://www.google.com/maps?q=39.11502,27.51221) | 2024-10-12 00:03 | 301.03 | 0.54 | Orta | Gece |
| [39.16625, 27.63406](https://www.google.com/maps?q=39.16625,27.63406) | 2024-10-12 00:03 | 302.48 | 0.74 | Orta | Gece |
| [39.16696, 27.62965](https://www.google.com/maps?q=39.16696,27.62965) | 2024-10-12 00:03 | 306.13 | 0.74 | Orta | Gece |
| [39.18105, 27.49985](https://www.google.com/maps?q=39.18105,27.49985) | 2024-10-12 00:03 | 305.72 | 0.78 | Orta | Gece |
| [39.60687, 27.87857](https://www.google.com/maps?q=39.60687,27.87857) | 2024-10-12 00:03 | 300.32 | 0.63 | Orta | Gece |
| [39.83604, 30.30066](https://www.google.com/maps?q=39.83604,30.30066) | 2024-10-12 00:03 | 296.89 | 0.83 | Orta | Gece |
| [39.86378, 26.24499](https://www.google.com/maps?q=39.86378,26.24499) | 2024-10-12 00:03 | 311.67 | 1.08 | Orta | Gece |
| [39.86709, 26.24581](https://www.google.com/maps?q=39.86709,26.24581) | 2024-10-12 00:03 | 312.25 | 0.93 | Orta | Gece |
| [40.75687, 31.7836](https://www.google.com/maps?q=40.75687,31.7836) | 2024-10-12 00:03 | 299.88 | 0.88 | Orta | Gece |
| [40.78107, 29.60403](https://www.google.com/maps?q=40.78107,29.60403) | 2024-10-12 00:03 | 305.62 | 1.12 | Orta | Gece |
| [41.01891, 28.55633](https://www.google.com/maps?q=41.01891,28.55633) | 2024-10-12 00:03 | 306.44 | 0.93 | Orta | Gece |
| [41.02219, 28.55728](https://www.google.com/maps?q=41.02219,28.55728) | 2024-10-12 00:03 | 306.4 | 0.74 | Orta | Gece |
| [41.24083, 36.44472](https://www.google.com/maps?q=41.24083,36.44472) | 2024-10-12 00:03 | 303.71 | 1.32 | Orta | Gece |
| [41.24118, 36.46318](https://www.google.com/maps?q=41.24118,36.46318) | 2024-10-12 00:03 | 315.81 | 2.36 | Orta | Gece |
| [41.25402, 31.41153](https://www.google.com/maps?q=41.25402,31.41153) | 2024-10-12 00:03 | 323.19 | 0.97 | Orta | Gece |
| [41.2575, 31.41269](https://www.google.com/maps?q=41.2575,31.41269) | 2024-10-12 00:03 | 302.54 | 0.97 | Orta | Gece |
| [41.26247, 31.42536](https://www.google.com/maps?q=41.26247,31.42536) | 2024-10-12 00:03 | 304.81 | 1.53 | Orta | Gece |
| [41.26595, 31.42651](https://www.google.com/maps?q=41.26595,31.42651) | 2024-10-12 00:03 | 307.59 | 1.49 | Orta | Gece |
| [41.26942, 31.42766](https://www.google.com/maps?q=41.26942,31.42766) | 2024-10-12 00:03 | 307.37 | 1.49 | Orta | Gece |
| [36.26342, 33.73008](https://www.google.com/maps?q=36.26342,33.73008) | 2024-10-12 00:05 | 309.25 | 0.96 | Orta | Gece |
| [37.0051, 40.39933](https://www.google.com/maps?q=37.0051,40.39933) | 2024-10-12 09:22 | 345.5 | 10.21 | Orta | Gündüz |
| [37.0084, 40.3987](https://www.google.com/maps?q=37.0084,40.3987) | 2024-10-12 09:22 | 351.45 | 13.26 | Orta | Gündüz |
| [37.15285, 41.77684](https://www.google.com/maps?q=37.15285,41.77684) | 2024-10-12 09:22 | 353.46 | 13.37 | Orta | Gündüz |
| [37.15409, 41.78143](https://www.google.com/maps?q=37.15409,41.78143) | 2024-10-12 09:22 | 367.0 | 13.37 | Yüksek | Gündüz |
| [37.15534, 41.78603](https://www.google.com/maps?q=37.15534,41.78603) | 2024-10-12 09:22 | 367.0 | 10.42 | Yüksek | Gündüz |
| [37.25641, 40.21827](https://www.google.com/maps?q=37.25641,40.21827) | 2024-10-12 09:22 | 333.33 | 4.52 | Orta | Gündüz |
| [37.35152, 37.02679](https://www.google.com/maps?q=37.35152,37.02679) | 2024-10-12 09:22 | 330.34 | 3.56 | Orta | Gündüz |
| [37.67782, 42.71723](https://www.google.com/maps?q=37.67782,42.71723) | 2024-10-12 09:22 | 331.8 | 3.93 | Orta | Gündüz |
| [37.7769, 38.72582](https://www.google.com/maps?q=37.7769,38.72582) | 2024-10-12 09:22 | 343.9 | 7.63 | Orta | Gündüz |
| [37.78057, 38.72691](https://www.google.com/maps?q=37.78057,38.72691) | 2024-10-12 09:22 | 343.81 | 12.34 | Orta | Gündüz |
| [37.92093, 40.00128](https://www.google.com/maps?q=37.92093,40.00128) | 2024-10-12 09:22 | 334.89 | 4.69 | Orta | Gündüz |
| [37.92365, 40.00149](https://www.google.com/maps?q=37.92365,40.00149) | 2024-10-12 09:22 | 330.12 | 5.19 | Orta | Gündüz |
| [37.9339, 40.5913](https://www.google.com/maps?q=37.9339,40.5913) | 2024-10-12 09:22 | 367.0 | 8.47 | Yüksek | Gündüz |
| [37.94266, 40.44446](https://www.google.com/maps?q=37.94266,40.44446) | 2024-10-12 09:22 | 367.0 | 25.3 | Yüksek | Gündüz |
| [37.94274, 40.44577](https://www.google.com/maps?q=37.94274,40.44577) | 2024-10-12 09:22 | 367.0 | 32.44 | Yüksek | Gündüz |
| [37.94415, 40.44977](https://www.google.com/maps?q=37.94415,40.44977) | 2024-10-12 09:22 | 335.11 | 14.02 | Orta | Gündüz |
| [37.96095, 41.02649](https://www.google.com/maps?q=37.96095,41.02649) | 2024-10-12 09:22 | 340.02 | 8.16 | Orta | Gündüz |
| [37.96232, 41.03147](https://www.google.com/maps?q=37.96232,41.03147) | 2024-10-12 09:22 | 349.37 | 8.16 | Orta | Gündüz |
| [37.98258, 41.10482](https://www.google.com/maps?q=37.98258,41.10482) | 2024-10-12 09:22 | 335.23 | 3.34 | Orta | Gündüz |
| [37.99923, 40.44543](https://www.google.com/maps?q=37.99923,40.44543) | 2024-10-12 09:22 | 336.47 | 12.86 | Orta | Gündüz |
| [38.02942, 40.66194](https://www.google.com/maps?q=38.02942,40.66194) | 2024-10-12 09:22 | 333.8 | 4.71 | Orta | Gündüz |
| [38.04664, 40.19258](https://www.google.com/maps?q=38.04664,40.19258) | 2024-10-12 09:22 | 343.55 | 6.28 | Orta | Gündüz |
| [38.05973, 40.65943](https://www.google.com/maps?q=38.05973,40.65943) | 2024-10-12 09:22 | 330.62 | 3.07 | Orta | Gündüz |
| [38.06107, 40.66416](https://www.google.com/maps?q=38.06107,40.66416) | 2024-10-12 09:22 | 336.48 | 3.07 | Orta | Gündüz |
| [38.13976, 40.40947](https://www.google.com/maps?q=38.13976,40.40947) | 2024-10-12 09:22 | 341.92 | 4.73 | Orta | Gündüz |
| [38.16071, 40.93289](https://www.google.com/maps?q=38.16071,40.93289) | 2024-10-12 09:22 | 333.44 | 5.84 | Düşük | Gündüz |
| [38.17826, 40.54644](https://www.google.com/maps?q=38.17826,40.54644) | 2024-10-12 09:22 | 340.38 | 4.29 | Orta | Gündüz |
| [38.2214, 39.7115](https://www.google.com/maps?q=38.2214,39.7115) | 2024-10-12 09:22 | 346.73 | 8.41 | Orta | Gündüz |
| [38.23294, 39.70656](https://www.google.com/maps?q=38.23294,39.70656) | 2024-10-12 09:22 | 331.1 | 4.32 | Orta | Gündüz |
| [38.24585, 40.49619](https://www.google.com/maps?q=38.24585,40.49619) | 2024-10-12 09:22 | 330.68 | 2.8 | Düşük | Gündüz |
| [38.53349, 36.12186](https://www.google.com/maps?q=38.53349,36.12186) | 2024-10-12 09:22 | 331.19 | 7.39 | Orta | Gündüz |
| [38.53353, 36.12318](https://www.google.com/maps?q=38.53353,36.12318) | 2024-10-12 09:22 | 329.75 | 5.42 | Orta | Gündüz |
| [39.09497, 42.18189](https://www.google.com/maps?q=39.09497,42.18189) | 2024-10-12 09:22 | 331.78 | 2.84 | Orta | Gündüz |
| [39.09598, 42.18108](https://www.google.com/maps?q=39.09598,42.18108) | 2024-10-12 09:22 | 331.58 | 2.73 | Orta | Gündüz |
| [39.43388, 36.81457](https://www.google.com/maps?q=39.43388,36.81457) | 2024-10-12 09:22 | 328.49 | 8.85 | Orta | Gündüz |
| [39.4353, 36.81442](https://www.google.com/maps?q=39.4353,36.81442) | 2024-10-12 09:22 | 333.02 | 11.5 | Orta | Gündüz |
| [39.43818, 36.80539](https://www.google.com/maps?q=39.43818,36.80539) | 2024-10-12 09:22 | 334.38 | 8.94 | Orta | Gündüz |
| [39.43956, 36.80499](https://www.google.com/maps?q=39.43956,36.80499) | 2024-10-12 09:22 | 328.29 | 3.05 | Orta | Gündüz |
| [39.70163, 40.27536](https://www.google.com/maps?q=39.70163,40.27536) | 2024-10-12 09:22 | 328.63 | 4.82 | Orta | Gündüz |
| [39.70442, 40.27792](https://www.google.com/maps?q=39.70442,40.27792) | 2024-10-12 09:22 | 327.89 | 2.46 | Düşük | Gündüz |
| [39.92716, 39.9911](https://www.google.com/maps?q=39.92716,39.9911) | 2024-10-12 09:22 | 334.66 | 4.13 | Orta | Gündüz |
| [39.94486, 43.97656](https://www.google.com/maps?q=39.94486,43.97656) | 2024-10-12 09:22 | 329.79 | 3.07 | Orta | Gündüz |
| [39.97011, 44.08033](https://www.google.com/maps?q=39.97011,44.08033) | 2024-10-12 09:22 | 338.88 | 7.77 | Orta | Gündüz |
| [39.98866, 41.80759](https://www.google.com/maps?q=39.98866,41.80759) | 2024-10-12 09:22 | 328.99 | 2.18 | Orta | Gündüz |
| [40.01392, 43.98198](https://www.google.com/maps?q=40.01392,43.98198) | 2024-10-12 09:22 | 330.41 | 4.51 | Orta | Gündüz |
| [40.02473, 44.34667](https://www.google.com/maps?q=40.02473,44.34667) | 2024-10-12 09:22 | 326.99 | 3.08 | Orta | Gündüz |
| [37.2921, 37.15482](https://www.google.com/maps?q=37.2921,37.15482) | 2024-10-12 00:28 | 296.08 | 0.92 | Orta | Gece |
| [37.29408, 37.15311](https://www.google.com/maps?q=37.29408,37.15311) | 2024-10-12 00:28 | 296.82 | 1.47 | Orta | Gece |
| [38.455, 38.72016](https://www.google.com/maps?q=38.455,38.72016) | 2024-10-12 00:28 | 295.44 | 1.02 | Orta | Gece |
| [38.4595, 38.71998](https://www.google.com/maps?q=38.4595,38.71998) | 2024-10-12 00:28 | 296.84 | 1.25 | Orta | Gece |
| [39.60887, 27.87903](https://www.google.com/maps?q=39.60887,27.87903) | 2024-10-12 00:28 | 299.65 | 0.6 | Orta | Gece |
| [39.86546, 26.24596](https://www.google.com/maps?q=39.86546,26.24596) | 2024-10-12 00:28 | 313.2 | 2.29 | Orta | Gece |
| [39.94498, 33.19042](https://www.google.com/maps?q=39.94498,33.19042) | 2024-10-12 00:28 | 295.51 | 0.52 | Orta | Gece |
| [40.05103, 32.64949](https://www.google.com/maps?q=40.05103,32.64949) | 2024-10-12 00:28 | 296.63 | 0.54 | Orta | Gece |
| [40.76585, 32.21411](https://www.google.com/maps?q=40.76585,32.21411) | 2024-10-12 00:28 | 295.47 | 0.56 | Orta | Gece |
| [40.76913, 29.5264](https://www.google.com/maps?q=40.76913,29.5264) | 2024-10-12 00:28 | 301.39 | 1.62 | Orta | Gece |
| [41.01868, 28.55506](https://www.google.com/maps?q=41.01868,28.55506) | 2024-10-12 00:28 | 301.94 | 0.44 | Orta | Gece |
| [41.02268, 28.55667](https://www.google.com/maps?q=41.02268,28.55667) | 2024-10-12 00:28 | 295.9 | 0.51 | Orta | Gece |
| [41.24134, 36.46168](https://www.google.com/maps?q=41.24134,36.46168) | 2024-10-12 00:28 | 326.93 | 3.05 | Orta | Gece |
| [41.24506, 36.46251](https://www.google.com/maps?q=41.24506,36.46251) | 2024-10-12 00:28 | 324.9 | 3.91 | Orta | Gece |
| [41.25289, 31.41387](https://www.google.com/maps?q=41.25289,31.41387) | 2024-10-12 00:28 | 296.32 | 0.61 | Orta | Gece |
| [41.25742, 31.4159](https://www.google.com/maps?q=41.25742,31.4159) | 2024-10-12 00:28 | 296.91 | 0.61 | Orta | Gece |
| [36.26211, 33.72788](https://www.google.com/maps?q=36.26211,33.72788) | 2024-10-12 00:30 | 299.58 | 0.46 | Orta | Gece |
| [36.26537, 33.72614](https://www.google.com/maps?q=36.26537,33.72614) | 2024-10-12 00:30 | 297.29 | 0.78 | Orta | Gece |
| [37.02261, 36.10442](https://www.google.com/maps?q=37.02261,36.10442) | 2024-10-12 00:30 | 303.2 | 1.97 | Orta | Gece |
| [38.42865, 27.21599](https://www.google.com/maps?q=38.42865,27.21599) | 2024-10-12 00:30 | 307.48 | 1.02 | Orta | Gece |
| [38.73775, 26.92893](https://www.google.com/maps?q=38.73775,26.92893) | 2024-10-12 00:30 | 310.19 | 0.91 | Orta | Gece |
| [38.73795, 26.94776](https://www.google.com/maps?q=38.73795,26.94776) | 2024-10-12 00:30 | 305.06 | 0.96 | Orta | Gece |
| [38.73889, 26.94335](https://www.google.com/maps?q=38.73889,26.94335) | 2024-10-12 00:30 | 303.75 | 0.96 | Orta | Gece |
| [38.74186, 26.94912](https://www.google.com/maps?q=38.74186,26.94912) | 2024-10-12 00:30 | 304.18 | 0.96 | Orta | Gece |
| [38.74577, 26.95053](https://www.google.com/maps?q=38.74577,26.95053) | 2024-10-12 00:30 | 306.9 | 0.85 | Orta | Gece |
| [38.74671, 26.9461](https://www.google.com/maps?q=38.74671,26.9461) | 2024-10-12 00:30 | 305.2 | 0.85 | Orta | Gece |
| [38.74767, 26.94906](https://www.google.com/maps?q=38.74767,26.94906) | 2024-10-12 00:30 | 320.17 | 1.77 | Orta | Gece |
| [38.74967, 26.95196](https://www.google.com/maps?q=38.74967,26.95196) | 2024-10-12 00:30 | 307.04 | 0.85 | Orta | Gece |
| [39.1134, 27.52398](https://www.google.com/maps?q=39.1134,27.52398) | 2024-10-12 00:30 | 300.2 | 0.48 | Orta | Gece |
| [39.16668, 27.63083](https://www.google.com/maps?q=39.16668,27.63083) | 2024-10-12 00:30 | 303.94 | 0.86 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
