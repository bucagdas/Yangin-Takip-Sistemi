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
### Son Güncelleme: 2024-10-05 08:41:23 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.42661, 27.2148](https://www.google.com/maps?q=38.42661,27.2148) | 2024-10-05 00:35 | 304.73 | 1.0 | Orta | Gece |
| [38.45293, 30.87511](https://www.google.com/maps?q=38.45293,30.87511) | 2024-10-05 00:35 | 298.2 | 0.44 | Orta | Gece |
| [38.67692, 27.77021](https://www.google.com/maps?q=38.67692,27.77021) | 2024-10-05 00:35 | 301.27 | 0.38 | Orta | Gece |
| [38.7383, 26.92883](https://www.google.com/maps?q=38.7383,26.92883) | 2024-10-05 00:35 | 327.17 | 2.45 | Orta | Gece |
| [38.73897, 26.94588](https://www.google.com/maps?q=38.73897,26.94588) | 2024-10-05 00:35 | 309.81 | 1.47 | Orta | Gece |
| [38.74319, 26.94744](https://www.google.com/maps?q=38.74319,26.94744) | 2024-10-05 00:35 | 305.23 | 1.47 | Orta | Gece |
| [38.7474, 26.94908](https://www.google.com/maps?q=38.7474,26.94908) | 2024-10-05 00:35 | 314.23 | 1.64 | Orta | Gece |
| [39.16782, 27.63423](https://www.google.com/maps?q=39.16782,27.63423) | 2024-10-05 00:35 | 299.01 | 1.32 | Orta | Gece |
| [39.48248, 30.04024](https://www.google.com/maps?q=39.48248,30.04024) | 2024-10-05 00:35 | 297.57 | 1.03 | Orta | Gece |
| [39.86533, 26.24531](https://www.google.com/maps?q=39.86533,26.24531) | 2024-10-05 00:35 | 303.13 | 0.79 | Orta | Gece |
| [40.76319, 32.21628](https://www.google.com/maps?q=40.76319,32.21628) | 2024-10-05 00:37 | 295.19 | 0.42 | Orta | Gece |
| [40.76571, 29.52685](https://www.google.com/maps?q=40.76571,29.52685) | 2024-10-05 00:37 | 302.16 | 2.05 | Orta | Gece |
| [40.94568, 31.3974](https://www.google.com/maps?q=40.94568,31.3974) | 2024-10-05 00:37 | 296.74 | 0.32 | Orta | Gece |
| [41.01969, 28.55278](https://www.google.com/maps?q=41.01969,28.55278) | 2024-10-05 00:37 | 301.22 | 1.0 | Orta | Gece |
| [41.172, 32.63063](https://www.google.com/maps?q=41.172,32.63063) | 2024-10-05 00:37 | 302.07 | 0.41 | Orta | Gece |
| [41.17459, 32.63561](https://www.google.com/maps?q=41.17459,32.63561) | 2024-10-05 00:37 | 300.34 | 0.66 | Orta | Gece |
| [41.17587, 32.63099](https://www.google.com/maps?q=41.17587,32.63099) | 2024-10-05 00:37 | 297.95 | 0.66 | Orta | Gece |
| [41.17709, 32.63345](https://www.google.com/maps?q=41.17709,32.63345) | 2024-10-05 00:37 | 301.39 | 1.17 | Orta | Gece |
| [41.25529, 31.41732](https://www.google.com/maps?q=41.25529,31.41732) | 2024-10-05 00:37 | 306.04 | 1.5 | Orta | Gece |
| [41.2563, 31.41349](https://www.google.com/maps?q=41.2563,31.41349) | 2024-10-05 00:37 | 346.55 | 3.95 | Orta | Gece |
| [41.26505, 31.42194](https://www.google.com/maps?q=41.26505,31.42194) | 2024-10-05 00:37 | 304.03 | 1.35 | Orta | Gece |
| [41.79708, 26.70099](https://www.google.com/maps?q=41.79708,26.70099) | 2024-10-05 00:37 | 302.76 | 0.7 | Orta | Gece |
| [36.68972, 36.20674](https://www.google.com/maps?q=36.68972,36.20674) | 2024-10-05 00:11 | 305.3 | 1.71 | Orta | Gece |
| [36.69487, 36.20861](https://www.google.com/maps?q=36.69487,36.20861) | 2024-10-05 00:11 | 309.26 | 1.71 | Orta | Gece |
| [36.71936, 36.20126](https://www.google.com/maps?q=36.71936,36.20126) | 2024-10-05 00:11 | 317.7 | 1.96 | Orta | Gece |
| [36.7285, 36.20946](https://www.google.com/maps?q=36.7285,36.20946) | 2024-10-05 00:11 | 308.8 | 1.34 | Orta | Gece |
| [36.74685, 36.20387](https://www.google.com/maps?q=36.74685,36.20387) | 2024-10-05 00:11 | 311.77 | 2.13 | Orta | Gece |
| [37.02347, 36.10947](https://www.google.com/maps?q=37.02347,36.10947) | 2024-10-05 00:11 | 313.09 | 2.21 | Orta | Gece |
| [37.29333, 37.15678](https://www.google.com/maps?q=37.29333,37.15678) | 2024-10-05 00:11 | 307.15 | 1.32 | Orta | Gece |
| [37.35101, 37.16427](https://www.google.com/maps?q=37.35101,37.16427) | 2024-10-05 00:11 | 298.59 | 1.93 | Orta | Gece |
| [37.41648, 39.63523](https://www.google.com/maps?q=37.41648,39.63523) | 2024-10-05 00:11 | 303.84 | 1.23 | Orta | Gece |
| [37.41716, 39.63375](https://www.google.com/maps?q=37.41716,39.63375) | 2024-10-05 00:11 | 300.17 | 1.39 | Orta | Gece |
| [37.56923, 40.23864](https://www.google.com/maps?q=37.56923,40.23864) | 2024-10-05 00:11 | 307.08 | 1.49 | Orta | Gece |
| [37.57145, 40.24095](https://www.google.com/maps?q=37.57145,40.24095) | 2024-10-05 00:11 | 299.62 | 2.23 | Orta | Gece |
| [37.63817, 38.11598](https://www.google.com/maps?q=37.63817,38.11598) | 2024-10-05 00:11 | 301.28 | 1.05 | Orta | Gece |
| [37.64015, 38.11929](https://www.google.com/maps?q=37.64015,38.11929) | 2024-10-05 00:11 | 297.11 | 1.04 | Orta | Gece |
| [37.72039, 38.76791](https://www.google.com/maps?q=37.72039,38.76791) | 2024-10-05 00:11 | 296.99 | 1.13 | Orta | Gece |
| [37.87694, 40.82783](https://www.google.com/maps?q=37.87694,40.82783) | 2024-10-05 00:11 | 297.35 | 1.27 | Orta | Gece |
| [37.96504, 40.01218](https://www.google.com/maps?q=37.96504,40.01218) | 2024-10-05 00:11 | 298.39 | 0.57 | Orta | Gece |
| [37.96509, 40.01129](https://www.google.com/maps?q=37.96509,40.01129) | 2024-10-05 00:11 | 298.16 | 0.77 | Orta | Gece |
| [37.9762, 40.13099](https://www.google.com/maps?q=37.9762,40.13099) | 2024-10-05 00:11 | 300.77 | 1.13 | Orta | Gece |
| [38.03308, 40.63841](https://www.google.com/maps?q=38.03308,40.63841) | 2024-10-05 00:11 | 297.86 | 1.91 | Orta | Gece |
| [38.03489, 40.63239](https://www.google.com/maps?q=38.03489,40.63239) | 2024-10-05 00:11 | 297.61 | 1.48 | Orta | Gece |
| [38.03582, 40.64079](https://www.google.com/maps?q=38.03582,40.64079) | 2024-10-05 00:11 | 323.91 | 2.87 | Orta | Gece |
| [38.03768, 40.63472](https://www.google.com/maps?q=38.03768,40.63472) | 2024-10-05 00:11 | 302.83 | 2.87 | Orta | Gece |
| [38.03912, 40.64124](https://www.google.com/maps?q=38.03912,40.64124) | 2024-10-05 00:11 | 321.23 | 3.33 | Orta | Gece |
| [38.03981, 40.65033](https://www.google.com/maps?q=38.03981,40.65033) | 2024-10-05 00:11 | 298.1 | 1.61 | Orta | Gece |
| [38.04182, 40.64373](https://www.google.com/maps?q=38.04182,40.64373) | 2024-10-05 00:11 | 308.4 | 3.02 | Orta | Gece |
| [38.04308, 40.65102](https://www.google.com/maps?q=38.04308,40.65102) | 2024-10-05 00:11 | 301.26 | 3.33 | Orta | Gece |
| [38.09703, 40.34964](https://www.google.com/maps?q=38.09703,40.34964) | 2024-10-05 00:11 | 326.82 | 6.15 | Orta | Gece |
| [38.09719, 40.35456](https://www.google.com/maps?q=38.09719,40.35456) | 2024-10-05 00:11 | 303.87 | 3.2 | Orta | Gece |
| [38.09881, 40.3491](https://www.google.com/maps?q=38.09881,40.3491) | 2024-10-05 00:11 | 324.22 | 3.2 | Orta | Gece |
| [38.1566, 40.9207](https://www.google.com/maps?q=38.1566,40.9207) | 2024-10-05 00:11 | 321.4 | 2.94 | Orta | Gece |
| [38.15984, 40.92511](https://www.google.com/maps?q=38.15984,40.92511) | 2024-10-05 00:11 | 295.89 | 1.93 | Orta | Gece |
| [38.16175, 40.91876](https://www.google.com/maps?q=38.16175,40.91876) | 2024-10-05 00:11 | 299.35 | 1.93 | Orta | Gece |
| [38.19835, 40.59232](https://www.google.com/maps?q=38.19835,40.59232) | 2024-10-05 00:11 | 304.92 | 1.59 | Orta | Gece |
| [38.21914, 40.72829](https://www.google.com/maps?q=38.21914,40.72829) | 2024-10-05 00:11 | 312.94 | 1.98 | Orta | Gece |
| [38.22116, 40.73338](https://www.google.com/maps?q=38.22116,40.73338) | 2024-10-05 00:11 | 295.0 | 1.81 | Orta | Gece |
| [38.22303, 40.72728](https://www.google.com/maps?q=38.22303,40.72728) | 2024-10-05 00:11 | 316.31 | 2.94 | Orta | Gece |
| [38.22526, 40.73082](https://www.google.com/maps?q=38.22526,40.73082) | 2024-10-05 00:11 | 301.55 | 1.17 | Orta | Gece |
| [38.24324, 40.39833](https://www.google.com/maps?q=38.24324,40.39833) | 2024-10-05 00:11 | 305.19 | 1.82 | Orta | Gece |
| [38.24836, 40.60798](https://www.google.com/maps?q=38.24836,40.60798) | 2024-10-05 00:11 | 298.36 | 0.97 | Orta | Gece |
| [38.42582, 27.21461](https://www.google.com/maps?q=38.42582,27.21461) | 2024-10-05 00:11 | 317.88 | 1.31 | Orta | Gece |
| [38.45207, 30.87437](https://www.google.com/maps?q=38.45207,30.87437) | 2024-10-05 00:11 | 315.52 | 2.5 | Orta | Gece |
| [38.45431, 38.72414](https://www.google.com/maps?q=38.45431,38.72414) | 2024-10-05 00:11 | 297.21 | 1.41 | Orta | Gece |
| [38.45606, 27.26141](https://www.google.com/maps?q=38.45606,27.26141) | 2024-10-05 00:11 | 302.13 | 0.39 | Orta | Gece |
| [38.45621, 38.72366](https://www.google.com/maps?q=38.45621,38.72366) | 2024-10-05 00:11 | 300.71 | 2.45 | Orta | Gece |
| [38.65834, 30.62071](https://www.google.com/maps?q=38.65834,30.62071) | 2024-10-05 00:11 | 305.04 | 2.07 | Orta | Gece |
| [38.66207, 39.23415](https://www.google.com/maps?q=38.66207,39.23415) | 2024-10-05 00:11 | 295.58 | 0.85 | Orta | Gece |
| [38.66209, 39.23326](https://www.google.com/maps?q=38.66209,39.23326) | 2024-10-05 00:11 | 296.24 | 1.02 | Orta | Gece |
| [38.72984, 26.9307](https://www.google.com/maps?q=38.72984,26.9307) | 2024-10-05 00:11 | 307.53 | 0.82 | Orta | Gece |
| [38.73744, 26.94698](https://www.google.com/maps?q=38.73744,26.94698) | 2024-10-05 00:11 | 325.69 | 3.51 | Orta | Gece |
| [38.73997, 26.95241](https://www.google.com/maps?q=38.73997,26.95241) | 2024-10-05 00:11 | 314.03 | 1.78 | Orta | Gece |
| [38.74405, 26.94883](https://www.google.com/maps?q=38.74405,26.94883) | 2024-10-05 00:11 | 316.81 | 1.53 | Orta | Gece |
| [38.74735, 26.94977](https://www.google.com/maps?q=38.74735,26.94977) | 2024-10-05 00:11 | 308.78 | 1.53 | Orta | Gece |
| [39.09002, 27.50995](https://www.google.com/maps?q=39.09002,27.50995) | 2024-10-05 00:11 | 300.73 | 0.31 | Orta | Gece |
| [39.11045, 27.59313](https://www.google.com/maps?q=39.11045,27.59313) | 2024-10-05 00:11 | 302.33 | 0.71 | Orta | Gece |
| [39.16812, 27.63213](https://www.google.com/maps?q=39.16812,27.63213) | 2024-10-05 00:11 | 314.75 | 1.81 | Orta | Gece |
| [39.48389, 30.03928](https://www.google.com/maps?q=39.48389,30.03928) | 2024-10-05 00:11 | 313.27 | 1.81 | Orta | Gece |
| [39.60707, 27.87874](https://www.google.com/maps?q=39.60707,27.87874) | 2024-10-05 00:11 | 299.73 | 0.64 | Orta | Gece |
| [39.74286, 30.19845](https://www.google.com/maps?q=39.74286,30.19845) | 2024-10-05 00:11 | 299.4 | 0.87 | Orta | Gece |
| [39.86674, 26.24353](https://www.google.com/maps?q=39.86674,26.24353) | 2024-10-05 00:11 | 311.68 | 1.34 | Orta | Gece |
| [39.94388, 33.19198](https://www.google.com/maps?q=39.94388,33.19198) | 2024-10-05 00:11 | 295.7 | 0.83 | Orta | Gece |
| [40.44243, 27.13737](https://www.google.com/maps?q=40.44243,27.13737) | 2024-10-05 00:11 | 305.94 | 1.22 | Orta | Gece |
| [40.74804, 29.76405](https://www.google.com/maps?q=40.74804,29.76405) | 2024-10-05 00:11 | 302.93 | 1.34 | Orta | Gece |
| [40.76365, 29.5283](https://www.google.com/maps?q=40.76365,29.5283) | 2024-10-05 00:11 | 319.8 | 3.05 | Orta | Gece |
| [40.76488, 32.21468](https://www.google.com/maps?q=40.76488,32.21468) | 2024-10-05 00:11 | 308.42 | 1.43 | Orta | Gece |
| [40.76499, 32.21456](https://www.google.com/maps?q=40.76499,32.21456) | 2024-10-05 00:11 | 308.57 | 1.81 | Orta | Gece |
| [40.94633, 31.39719](https://www.google.com/maps?q=40.94633,31.39719) | 2024-10-05 00:11 | 300.9 | 0.99 | Orta | Gece |
| [41.01918, 28.55265](https://www.google.com/maps?q=41.01918,28.55265) | 2024-10-05 00:11 | 301.84 | 0.47 | Orta | Gece |
| [41.02167, 28.55856](https://www.google.com/maps?q=41.02167,28.55856) | 2024-10-05 00:11 | 305.7 | 0.69 | Orta | Gece |
| [41.17478, 32.63235](https://www.google.com/maps?q=41.17478,32.63235) | 2024-10-05 00:11 | 312.25 | 1.78 | Orta | Gece |
| [41.17863, 32.63389](https://www.google.com/maps?q=41.17863,32.63389) | 2024-10-05 00:11 | 301.43 | 1.26 | Orta | Gece |
| [41.193, 32.62531](https://www.google.com/maps?q=41.193,32.62531) | 2024-10-05 00:11 | 300.73 | 0.96 | Orta | Gece |
| [41.24063, 36.46526](https://www.google.com/maps?q=41.24063,36.46526) | 2024-10-05 00:11 | 302.25 | 1.74 | Orta | Gece |
| [41.25354, 31.41195](https://www.google.com/maps?q=41.25354,31.41195) | 2024-10-05 00:11 | 317.07 | 2.87 | Orta | Gece |
| [41.255, 31.4184](https://www.google.com/maps?q=41.255,31.4184) | 2024-10-05 00:11 | 301.19 | 1.74 | Orta | Gece |
| [41.25597, 31.41916](https://www.google.com/maps?q=41.25597,31.41916) | 2024-10-05 00:11 | 303.96 | 0.64 | Orta | Gece |
| [41.25618, 31.41258](https://www.google.com/maps?q=41.25618,31.41258) | 2024-10-05 00:11 | 314.34 | 1.74 | Orta | Gece |
| [41.26112, 31.42702](https://www.google.com/maps?q=41.26112,31.42702) | 2024-10-05 00:11 | 303.86 | 1.18 | Orta | Gece |
| [41.26696, 31.42315](https://www.google.com/maps?q=41.26696,31.42315) | 2024-10-05 00:11 | 309.28 | 1.77 | Orta | Gece |
| [41.63427, 27.50454](https://www.google.com/maps?q=41.63427,27.50454) | 2024-10-05 00:11 | 306.47 | 0.73 | Orta | Gece |
| [41.79756, 26.7011](https://www.google.com/maps?q=41.79756,26.7011) | 2024-10-05 00:11 | 303.13 | 0.95 | Orta | Gece |
| [36.26367, 33.7277](https://www.google.com/maps?q=36.26367,33.7277) | 2024-10-05 00:13 | 306.3 | 0.69 | Orta | Gece |
| [38.42926, 27.21578](https://www.google.com/maps?q=38.42926,27.21578) | 2024-10-05 01:00 | 301.79 | 0.53 | Orta | Gece |
| [38.73889, 26.94046](https://www.google.com/maps?q=38.73889,26.94046) | 2024-10-05 01:00 | 301.59 | 1.37 | Orta | Gece |
| [38.74033, 26.94447](https://www.google.com/maps?q=38.74033,26.94447) | 2024-10-05 01:00 | 304.17 | 1.3 | Orta | Gece |
| [38.74458, 26.94305](https://www.google.com/maps?q=38.74458,26.94305) | 2024-10-05 01:00 | 306.85 | 1.37 | Orta | Gece |
| [38.74598, 26.94718](https://www.google.com/maps?q=38.74598,26.94718) | 2024-10-05 01:00 | 310.87 | 1.3 | Orta | Gece |
| [39.4846, 30.04038](https://www.google.com/maps?q=39.4846,30.04038) | 2024-10-05 01:00 | 298.08 | 1.82 | Orta | Gece |
| [39.48808, 30.04113](https://www.google.com/maps?q=39.48808,30.04113) | 2024-10-05 01:00 | 295.29 | 0.88 | Orta | Gece |
| [40.76815, 29.52792](https://www.google.com/maps?q=40.76815,29.52792) | 2024-10-05 01:00 | 307.91 | 1.49 | Orta | Gece |
| [41.02119, 28.55222](https://www.google.com/maps?q=41.02119,28.55222) | 2024-10-05 01:00 | 304.93 | 0.85 | Orta | Gece |
| [41.18387, 32.63234](https://www.google.com/maps?q=41.18387,32.63234) | 2024-10-05 01:00 | 296.2 | 1.75 | Orta | Gece |
| [41.25747, 31.41336](https://www.google.com/maps?q=41.25747,31.41336) | 2024-10-05 01:00 | 312.92 | 2.24 | Orta | Gece |
| [41.79738, 26.70055](https://www.google.com/maps?q=41.79738,26.70055) | 2024-10-05 01:00 | 297.25 | 0.49 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
