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
### Son Güncelleme: 2024-10-05 11:58:44 (UTC)

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
| [36.70474, 37.47869](https://www.google.com/maps?q=36.70474,37.47869) | 2024-10-05 09:52 | 338.41 | 5.62 | Orta | Gündüz |
| [36.96082, 39.71017](https://www.google.com/maps?q=36.96082,39.71017) | 2024-10-05 09:52 | 351.72 | 34.82 | Orta | Gündüz |
| [37.11377, 41.58395](https://www.google.com/maps?q=37.11377,41.58395) | 2024-10-05 09:52 | 347.06 | 5.97 | Düşük | Gündüz |
| [37.18477, 41.73706](https://www.google.com/maps?q=37.18477,41.73706) | 2024-10-05 09:52 | 345.31 | 7.65 | Orta | Gündüz |
| [37.18844, 41.73599](https://www.google.com/maps?q=37.18844,41.73599) | 2024-10-05 09:52 | 346.62 | 7.65 | Orta | Gündüz |
| [37.18962, 41.73252](https://www.google.com/maps?q=37.18962,41.73252) | 2024-10-05 09:52 | 341.44 | 5.23 | Düşük | Gündüz |
| [37.21944, 39.92175](https://www.google.com/maps?q=37.21944,39.92175) | 2024-10-05 09:52 | 352.3 | 7.84 | Orta | Gündüz |
| [37.23423, 42.37869](https://www.google.com/maps?q=37.23423,42.37869) | 2024-10-05 09:52 | 344.65 | 4.36 | Orta | Gündüz |
| [37.24331, 39.91404](https://www.google.com/maps?q=37.24331,39.91404) | 2024-10-05 09:52 | 343.75 | 5.83 | Orta | Gündüz |
| [37.30463, 41.87515](https://www.google.com/maps?q=37.30463,41.87515) | 2024-10-05 09:52 | 344.42 | 8.27 | Düşük | Gündüz |
| [37.31188, 41.87289](https://www.google.com/maps?q=37.31188,41.87289) | 2024-10-05 09:52 | 340.7 | 6.33 | Düşük | Gündüz |
| [37.58362, 41.22587](https://www.google.com/maps?q=37.58362,41.22587) | 2024-10-05 09:52 | 339.96 | 5.48 | Orta | Gündüz |
| [36.72978, 36.21175](https://www.google.com/maps?q=36.72978,36.21175) | 2024-10-05 09:54 | 332.79 | 3.14 | Orta | Gündüz |
| [36.74829, 36.20098](https://www.google.com/maps?q=36.74829,36.20098) | 2024-10-05 09:54 | 331.82 | 2.39 | Düşük | Gündüz |
| [36.82083, 34.91681](https://www.google.com/maps?q=36.82083,34.91681) | 2024-10-05 09:54 | 336.64 | 2.75 | Orta | Gündüz |
| [37.01188, 35.78756](https://www.google.com/maps?q=37.01188,35.78756) | 2024-10-05 09:54 | 335.16 | 2.93 | Orta | Gündüz |
| [37.02962, 35.94198](https://www.google.com/maps?q=37.02962,35.94198) | 2024-10-05 09:54 | 346.61 | 4.04 | Orta | Gündüz |
| [37.03054, 35.94559](https://www.google.com/maps?q=37.03054,35.94559) | 2024-10-05 09:54 | 333.52 | 4.04 | Orta | Gündüz |
| [37.05938, 35.03645](https://www.google.com/maps?q=37.05938,35.03645) | 2024-10-05 09:54 | 335.89 | 3.4 | Düşük | Gündüz |
| [37.31107, 36.86959](https://www.google.com/maps?q=37.31107,36.86959) | 2024-10-05 09:54 | 339.27 | 8.66 | Orta | Gündüz |
| [37.32644, 38.92167](https://www.google.com/maps?q=37.32644,38.92167) | 2024-10-05 09:54 | 341.96 | 6.29 | Orta | Gündüz |
| [37.33385, 35.46311](https://www.google.com/maps?q=37.33385,35.46311) | 2024-10-05 09:54 | 338.27 | 3.57 | Orta | Gündüz |
| [37.36152, 39.16012](https://www.google.com/maps?q=37.36152,39.16012) | 2024-10-05 09:54 | 342.65 | 6.95 | Orta | Gündüz |
| [37.39054, 40.14654](https://www.google.com/maps?q=37.39054,40.14654) | 2024-10-05 09:54 | 341.69 | 7.55 | Orta | Gündüz |
| [37.39447, 40.14528](https://www.google.com/maps?q=37.39447,40.14528) | 2024-10-05 09:54 | 339.11 | 7.55 | Orta | Gündüz |
| [37.42917, 39.12348](https://www.google.com/maps?q=37.42917,39.12348) | 2024-10-05 09:54 | 341.9 | 5.52 | Orta | Gündüz |
| [37.488, 38.70925](https://www.google.com/maps?q=37.488,38.70925) | 2024-10-05 09:54 | 340.36 | 5.53 | Orta | Gündüz |
| [37.50536, 39.12824](https://www.google.com/maps?q=37.50536,39.12824) | 2024-10-05 09:54 | 342.53 | 27.99 | Düşük | Gündüz |
| [37.50948, 39.12688](https://www.google.com/maps?q=37.50948,39.12688) | 2024-10-05 09:54 | 347.08 | 27.99 | Orta | Gündüz |
| [37.51257, 39.12082](https://www.google.com/maps?q=37.51257,39.12082) | 2024-10-05 09:54 | 343.36 | 10.91 | Düşük | Gündüz |
| [37.53118, 37.04184](https://www.google.com/maps?q=37.53118,37.04184) | 2024-10-05 09:54 | 341.3 | 10.13 | Orta | Gündüz |
| [37.54487, 38.90339](https://www.google.com/maps?q=37.54487,38.90339) | 2024-10-05 09:54 | 342.51 | 4.77 | Orta | Gündüz |
| [37.55986, 40.21366](https://www.google.com/maps?q=37.55986,40.21366) | 2024-10-05 09:54 | 342.58 | 3.77 | Orta | Gündüz |
| [37.56043, 37.38657](https://www.google.com/maps?q=37.56043,37.38657) | 2024-10-05 09:54 | 339.2 | 9.75 | Düşük | Gündüz |
| [37.5605, 40.23626](https://www.google.com/maps?q=37.5605,40.23626) | 2024-10-05 09:54 | 339.8 | 7.58 | Düşük | Gündüz |
| [37.56139, 40.24045](https://www.google.com/maps?q=37.56139,40.24045) | 2024-10-05 09:54 | 341.88 | 7.0 | Orta | Gündüz |
| [37.56179, 37.3924](https://www.google.com/maps?q=37.56179,37.3924) | 2024-10-05 09:54 | 341.56 | 9.75 | Düşük | Gündüz |
| [37.57693, 38.22164](https://www.google.com/maps?q=37.57693,38.22164) | 2024-10-05 09:54 | 341.04 | 4.6 | Orta | Gündüz |
| [37.58824, 31.76877](https://www.google.com/maps?q=37.58824,31.76877) | 2024-10-05 09:54 | 334.19 | 5.95 | Orta | Gündüz |
| [37.60091, 39.52909](https://www.google.com/maps?q=37.60091,39.52909) | 2024-10-05 09:54 | 339.35 | 10.97 | Düşük | Gündüz |
| [37.60592, 39.53238](https://www.google.com/maps?q=37.60592,39.53238) | 2024-10-05 09:54 | 348.04 | 35.55 | Orta | Gündüz |
| [37.61431, 38.08028](https://www.google.com/maps?q=37.61431,38.08028) | 2024-10-05 09:54 | 344.88 | 4.91 | Orta | Gündüz |
| [37.65438, 38.13506](https://www.google.com/maps?q=37.65438,38.13506) | 2024-10-05 09:54 | 342.41 | 7.18 | Orta | Gündüz |
| [37.65676, 37.90274](https://www.google.com/maps?q=37.65676,37.90274) | 2024-10-05 09:54 | 351.88 | 28.65 | Orta | Gündüz |
| [37.65864, 37.97191](https://www.google.com/maps?q=37.65864,37.97191) | 2024-10-05 09:54 | 342.07 | 5.93 | Orta | Gündüz |
| [37.66417, 40.5738](https://www.google.com/maps?q=37.66417,40.5738) | 2024-10-05 09:54 | 346.34 | 12.12 | Orta | Gündüz |
| [37.66797, 40.57252](https://www.google.com/maps?q=37.66797,40.57252) | 2024-10-05 09:54 | 342.12 | 49.46 | Orta | Gündüz |
| [37.66993, 39.41371](https://www.google.com/maps?q=37.66993,39.41371) | 2024-10-05 09:54 | 344.21 | 7.57 | Orta | Gündüz |
| [37.67049, 40.58471](https://www.google.com/maps?q=37.67049,40.58471) | 2024-10-05 09:54 | 336.52 | 17.29 | Düşük | Gündüz |
| [37.67383, 38.09841](https://www.google.com/maps?q=37.67383,38.09841) | 2024-10-05 09:54 | 337.93 | 3.49 | Düşük | Gündüz |
| [37.68225, 39.28024](https://www.google.com/maps?q=37.68225,39.28024) | 2024-10-05 09:54 | 346.85 | 8.24 | Orta | Gündüz |
| [37.69183, 39.53517](https://www.google.com/maps?q=37.69183,39.53517) | 2024-10-05 09:54 | 343.04 | 6.08 | Orta | Gündüz |
| [37.69755, 37.90165](https://www.google.com/maps?q=37.69755,37.90165) | 2024-10-05 09:54 | 343.4 | 5.59 | Orta | Gündüz |
| [37.71202, 38.18366](https://www.google.com/maps?q=37.71202,38.18366) | 2024-10-05 09:54 | 342.11 | 9.59 | Orta | Gündüz |
| [37.7351, 38.5352](https://www.google.com/maps?q=37.7351,38.5352) | 2024-10-05 09:54 | 342.31 | 4.64 | Orta | Gündüz |
| [37.7547, 38.68462](https://www.google.com/maps?q=37.7547,38.68462) | 2024-10-05 09:54 | 343.78 | 9.7 | Orta | Gündüz |
| [37.76789, 38.68886](https://www.google.com/maps?q=37.76789,38.68886) | 2024-10-05 09:54 | 341.54 | 8.57 | Orta | Gündüz |
| [37.76904, 38.69391](https://www.google.com/maps?q=37.76904,38.69391) | 2024-10-05 09:54 | 341.63 | 8.53 | Orta | Gündüz |
| [37.76948, 38.69043](https://www.google.com/maps?q=37.76948,38.69043) | 2024-10-05 09:54 | 348.4 | 5.46 | Orta | Gündüz |
| [37.7706, 38.69553](https://www.google.com/maps?q=37.7706,38.69553) | 2024-10-05 09:54 | 341.26 | 5.46 | Düşük | Gündüz |
| [37.83654, 40.9717](https://www.google.com/maps?q=37.83654,40.9717) | 2024-10-05 09:54 | 340.92 | 9.28 | Düşük | Gündüz |
| [37.8417, 32.80098](https://www.google.com/maps?q=37.8417,32.80098) | 2024-10-05 09:54 | 350.23 | 10.19 | Orta | Gündüz |
| [37.84285, 32.8016](https://www.google.com/maps?q=37.84285,32.8016) | 2024-10-05 09:54 | 367.0 | 9.85 | Yüksek | Gündüz |
| [37.89123, 40.02938](https://www.google.com/maps?q=37.89123,40.02938) | 2024-10-05 09:54 | 338.94 | 4.49 | Düşük | Gündüz |
| [37.93256, 40.66332](https://www.google.com/maps?q=37.93256,40.66332) | 2024-10-05 09:54 | 344.67 | 14.16 | Orta | Gündüz |
| [37.96108, 41.17851](https://www.google.com/maps?q=37.96108,41.17851) | 2024-10-05 09:54 | 337.46 | 3.69 | Orta | Gündüz |
| [37.96476, 41.17728](https://www.google.com/maps?q=37.96476,41.17728) | 2024-10-05 09:54 | 347.65 | 11.69 | Orta | Gündüz |
| [37.96512, 41.17554](https://www.google.com/maps?q=37.96512,41.17554) | 2024-10-05 09:54 | 338.86 | 7.91 | Düşük | Gündüz |
| [37.98906, 34.85372](https://www.google.com/maps?q=37.98906,34.85372) | 2024-10-05 09:54 | 354.16 | 13.06 | Orta | Gündüz |
| [37.99002, 34.85738](https://www.google.com/maps?q=37.99002,34.85738) | 2024-10-05 09:54 | 331.77 | 13.06 | Düşük | Gündüz |
| [38.02018, 40.9189](https://www.google.com/maps?q=38.02018,40.9189) | 2024-10-05 09:54 | 339.98 | 6.71 | Orta | Gündüz |
| [38.0204, 41.81607](https://www.google.com/maps?q=38.0204,41.81607) | 2024-10-05 09:54 | 344.07 | 8.1 | Orta | Gündüz |
| [38.02424, 41.07797](https://www.google.com/maps?q=38.02424,41.07797) | 2024-10-05 09:54 | 346.48 | 25.88 | Düşük | Gündüz |
| [38.02681, 41.07113](https://www.google.com/maps?q=38.02681,41.07113) | 2024-10-05 09:54 | 310.84 | 25.88 | Düşük | Gündüz |
| [38.04281, 40.91609](https://www.google.com/maps?q=38.04281,40.91609) | 2024-10-05 09:54 | 339.8 | 3.42 | Düşük | Gündüz |
| [38.05159, 40.42101](https://www.google.com/maps?q=38.05159,40.42101) | 2024-10-05 09:54 | 337.84 | 3.53 | Düşük | Gündüz |
| [38.10248, 40.35173](https://www.google.com/maps?q=38.10248,40.35173) | 2024-10-05 09:54 | 346.53 | 11.4 | Orta | Gündüz |
| [38.14079, 39.75426](https://www.google.com/maps?q=38.14079,39.75426) | 2024-10-05 09:54 | 342.41 | 4.72 | Orta | Gündüz |
| [38.15748, 40.91494](https://www.google.com/maps?q=38.15748,40.91494) | 2024-10-05 09:54 | 345.38 | 27.21 | Düşük | Gündüz |
| [38.16169, 37.05583](https://www.google.com/maps?q=38.16169,37.05583) | 2024-10-05 09:54 | 340.69 | 21.33 | Orta | Gündüz |
| [38.16267, 37.05832](https://www.google.com/maps?q=38.16267,37.05832) | 2024-10-05 09:54 | 340.25 | 23.12 | Orta | Gündüz |
| [38.17693, 37.0178](https://www.google.com/maps?q=38.17693,37.0178) | 2024-10-05 09:54 | 342.26 | 8.59 | Orta | Gündüz |
| [38.18328, 40.66857](https://www.google.com/maps?q=38.18328,40.66857) | 2024-10-05 09:54 | 338.18 | 2.66 | Düşük | Gündüz |
| [38.20022, 39.77662](https://www.google.com/maps?q=38.20022,39.77662) | 2024-10-05 09:54 | 355.0 | 8.22 | Orta | Gündüz |
| [38.20413, 39.77524](https://www.google.com/maps?q=38.20413,39.77524) | 2024-10-05 09:54 | 343.5 | 8.22 | Orta | Gündüz |
| [38.20863, 37.10886](https://www.google.com/maps?q=38.20863,37.10886) | 2024-10-05 09:54 | 339.78 | 17.36 | Orta | Gündüz |
| [38.2435, 40.55876](https://www.google.com/maps?q=38.2435,40.55876) | 2024-10-05 09:54 | 341.03 | 6.95 | Düşük | Gündüz |
| [38.28393, 37.07845](https://www.google.com/maps?q=38.28393,37.07845) | 2024-10-05 09:54 | 341.05 | 4.08 | Orta | Gündüz |
| [38.2884, 37.07682](https://www.google.com/maps?q=38.2884,37.07682) | 2024-10-05 09:54 | 340.69 | 8.54 | Orta | Gündüz |
| [38.28903, 37.07907](https://www.google.com/maps?q=38.28903,37.07907) | 2024-10-05 09:54 | 353.4 | 20.43 | Orta | Gündüz |
| [38.28981, 37.08267](https://www.google.com/maps?q=38.28981,37.08267) | 2024-10-05 09:54 | 340.71 | 8.54 | Orta | Gündüz |
| [38.31753, 37.1171](https://www.google.com/maps?q=38.31753,37.1171) | 2024-10-05 09:54 | 340.73 | 9.58 | Orta | Gündüz |
| [38.31898, 37.12316](https://www.google.com/maps?q=38.31898,37.12316) | 2024-10-05 09:54 | 340.59 | 9.58 | Orta | Gündüz |
| [38.32602, 37.25307](https://www.google.com/maps?q=38.32602,37.25307) | 2024-10-05 09:54 | 334.06 | 3.9 | Orta | Gündüz |
| [38.51157, 34.67918](https://www.google.com/maps?q=38.51157,34.67918) | 2024-10-05 09:54 | 336.5 | 2.3 | Orta | Gündüz |
| [38.5221, 34.46477](https://www.google.com/maps?q=38.5221,34.46477) | 2024-10-05 09:54 | 330.07 | 1.45 | Düşük | Gündüz |
| [38.54587, 38.2794](https://www.google.com/maps?q=38.54587,38.2794) | 2024-10-05 09:54 | 333.94 | 2.38 | Orta | Gündüz |
| [38.55399, 39.43067](https://www.google.com/maps?q=38.55399,39.43067) | 2024-10-05 09:54 | 354.47 | 7.14 | Orta | Gündüz |
| [38.55779, 39.42863](https://www.google.com/maps?q=38.55779,39.42863) | 2024-10-05 09:54 | 332.27 | 7.14 | Orta | Gündüz |
| [38.55849, 36.18562](https://www.google.com/maps?q=38.55849,36.18562) | 2024-10-05 09:54 | 338.1 | 4.13 | Orta | Gündüz |
| [38.73662, 36.02008](https://www.google.com/maps?q=38.73662,36.02008) | 2024-10-05 09:54 | 339.11 | 9.46 | Orta | Gündüz |
| [38.74301, 36.02522](https://www.google.com/maps?q=38.74301,36.02522) | 2024-10-05 09:54 | 340.96 | 17.27 | Orta | Gündüz |
| [38.82438, 39.03899](https://www.google.com/maps?q=38.82438,39.03899) | 2024-10-05 09:54 | 341.55 | 3.5 | Orta | Gündüz |
| [38.8255, 37.47005](https://www.google.com/maps?q=38.8255,37.47005) | 2024-10-05 09:54 | 340.38 | 5.91 | Orta | Gündüz |
| [38.82705, 37.47227](https://www.google.com/maps?q=38.82705,37.47227) | 2024-10-05 09:54 | 345.56 | 8.01 | Orta | Gündüz |
| [38.84229, 39.04215](https://www.google.com/maps?q=38.84229,39.04215) | 2024-10-05 09:54 | 342.31 | 6.27 | Orta | Gündüz |
| [39.08033, 42.4755](https://www.google.com/maps?q=39.08033,42.4755) | 2024-10-05 09:54 | 345.97 | 9.05 | Orta | Gündüz |
| [39.18655, 37.55721](https://www.google.com/maps?q=39.18655,37.55721) | 2024-10-05 09:54 | 339.75 | 8.04 | Orta | Gündüz |
| [39.1866, 37.56076](https://www.google.com/maps?q=39.1866,37.56076) | 2024-10-05 09:54 | 341.01 | 12.37 | Orta | Gündüz |
| [39.19065, 38.07686](https://www.google.com/maps?q=39.19065,38.07686) | 2024-10-05 09:54 | 341.62 | 5.15 | Orta | Gündüz |
| [39.1908, 37.55887](https://www.google.com/maps?q=39.1908,37.55887) | 2024-10-05 09:54 | 347.1 | 12.37 | Orta | Gündüz |
| [39.19118, 38.07474](https://www.google.com/maps?q=39.19118,38.07474) | 2024-10-05 09:54 | 345.08 | 11.54 | Orta | Gündüz |
| [39.19201, 37.56071](https://www.google.com/maps?q=39.19201,37.56071) | 2024-10-05 09:54 | 347.08 | 18.94 | Orta | Gündüz |
| [39.1948, 38.07529](https://www.google.com/maps?q=39.1948,38.07529) | 2024-10-05 09:54 | 344.25 | 10.46 | Orta | Gündüz |
| [39.21547, 37.4222](https://www.google.com/maps?q=39.21547,37.4222) | 2024-10-05 09:54 | 332.1 | 3.35 | Orta | Gündüz |
| [39.25991, 42.50992](https://www.google.com/maps?q=39.25991,42.50992) | 2024-10-05 09:54 | 333.52 | 1.29 | Orta | Gündüz |
| [39.81438, 40.28125](https://www.google.com/maps?q=39.81438,40.28125) | 2024-10-05 09:54 | 336.61 | 5.01 | Orta | Gündüz |
| [40.03884, 44.28403](https://www.google.com/maps?q=40.03884,44.28403) | 2024-10-05 09:54 | 331.27 | 2.93 | Orta | Gündüz |
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
| [37.30787, 41.87963](https://www.google.com/maps?q=37.30787,41.87963) | 2024-10-05 09:00 | 333.43 | 3.94 | Orta | Gündüz |
| [37.99258, 41.08692](https://www.google.com/maps?q=37.99258,41.08692) | 2024-10-05 09:02 | 348.24 | 6.74 | Orta | Gündüz |
| [37.99467, 41.0773](https://www.google.com/maps?q=37.99467,41.0773) | 2024-10-05 09:02 | 354.62 | 28.08 | Orta | Gündüz |
| [37.99669, 41.07571](https://www.google.com/maps?q=37.99669,41.07571) | 2024-10-05 09:02 | 355.93 | 17.03 | Orta | Gündüz |
| [37.99733, 41.08538](https://www.google.com/maps?q=37.99733,41.08538) | 2024-10-05 09:02 | 367.0 | 27.73 | Yüksek | Gündüz |
| [37.99931, 41.08381](https://www.google.com/maps?q=37.99931,41.08381) | 2024-10-05 09:02 | 367.0 | 17.03 | Yüksek | Gündüz |
| [38.02672, 41.08047](https://www.google.com/maps?q=38.02672,41.08047) | 2024-10-05 09:02 | 351.95 | 14.03 | Orta | Gündüz |
| [38.02861, 41.07875](https://www.google.com/maps?q=38.02861,41.07875) | 2024-10-05 09:02 | 344.03 | 4.92 | Orta | Gündüz |
| [38.03098, 41.08611](https://www.google.com/maps?q=38.03098,41.08611) | 2024-10-05 09:02 | 332.08 | 4.92 | Düşük | Gündüz |
| [38.04137, 41.05423](https://www.google.com/maps?q=38.04137,41.05423) | 2024-10-05 09:02 | 338.18 | 2.42 | Orta | Gündüz |
| [38.99339, 42.00266](https://www.google.com/maps?q=38.99339,42.00266) | 2024-10-05 09:02 | 335.18 | 4.39 | Orta | Gündüz |
| [38.99539, 42.00226](https://www.google.com/maps?q=38.99539,42.00226) | 2024-10-05 09:02 | 334.39 | 3.8 | Orta | Gündüz |
| [39.20498, 42.54232](https://www.google.com/maps?q=39.20498,42.54232) | 2024-10-05 09:02 | 348.18 | 8.1 | Orta | Gündüz |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
