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
### Son Güncelleme: 2024-10-10 07:37:12 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [41.24394, 36.46225](https://www.google.com/maps?q=41.24394,36.46225) | 2024-10-10 00:39 | 300.65 | 1.56 | Orta | Gece |
| [41.24413, 36.46517](https://www.google.com/maps?q=41.24413,36.46517) | 2024-10-10 00:39 | 301.74 | 2.19 | Orta | Gece |
| [37.89367, 34.877](https://www.google.com/maps?q=37.89367,34.877) | 2024-10-10 00:41 | 315.3 | 6.02 | Orta | Gece |
| [37.89894, 34.8844](https://www.google.com/maps?q=37.89894,34.8844) | 2024-10-10 00:41 | 316.28 | 5.07 | Orta | Gece |
| [38.4276, 27.21898](https://www.google.com/maps?q=38.4276,27.21898) | 2024-10-10 00:41 | 299.01 | 0.75 | Orta | Gece |
| [38.65657, 30.61735](https://www.google.com/maps?q=38.65657,30.61735) | 2024-10-10 00:41 | 302.83 | 1.67 | Orta | Gece |
| [38.73736, 26.94437](https://www.google.com/maps?q=38.73736,26.94437) | 2024-10-10 00:41 | 309.18 | 2.34 | Orta | Gece |
| [38.74032, 26.93208](https://www.google.com/maps?q=38.74032,26.93208) | 2024-10-10 00:41 | 310.59 | 2.48 | Orta | Gece |
| [38.74644, 26.94804](https://www.google.com/maps?q=38.74644,26.94804) | 2024-10-10 00:41 | 312.86 | 2.78 | Orta | Gece |
| [38.74813, 26.94917](https://www.google.com/maps?q=38.74813,26.94917) | 2024-10-10 00:41 | 309.05 | 2.55 | Orta | Gece |
| [39.48306, 30.04048](https://www.google.com/maps?q=39.48306,30.04048) | 2024-10-10 00:41 | 308.8 | 1.71 | Orta | Gece |
| [41.17265, 32.62917](https://www.google.com/maps?q=41.17265,32.62917) | 2024-10-10 00:41 | 296.55 | 1.37 | Orta | Gece |
| [41.25742, 31.4139](https://www.google.com/maps?q=41.25742,31.4139) | 2024-10-10 00:41 | 307.32 | 2.43 | Orta | Gece |
| [41.26661, 31.4236](https://www.google.com/maps?q=41.26661,31.4236) | 2024-10-10 00:41 | 310.15 | 2.98 | Orta | Gece |
| [41.79726, 26.70372](https://www.google.com/maps?q=41.79726,26.70372) | 2024-10-10 00:41 | 300.56 | 0.69 | Orta | Gece |
| [37.34969, 37.16185](https://www.google.com/maps?q=37.34969,37.16185) | 2024-10-10 00:18 | 306.39 | 1.39 | Orta | Gece |
| [37.46167, 38.14823](https://www.google.com/maps?q=37.46167,38.14823) | 2024-10-10 00:18 | 300.18 | 0.66 | Orta | Gece |
| [37.74117, 38.5524](https://www.google.com/maps?q=37.74117,38.5524) | 2024-10-10 00:18 | 296.83 | 1.04 | Orta | Gece |
| [37.78777, 38.17142](https://www.google.com/maps?q=37.78777,38.17142) | 2024-10-10 00:18 | 298.84 | 1.78 | Orta | Gece |
| [37.9395, 41.00243](https://www.google.com/maps?q=37.9395,41.00243) | 2024-10-10 00:18 | 296.66 | 0.98 | Orta | Gece |
| [38.00186, 41.55333](https://www.google.com/maps?q=38.00186,41.55333) | 2024-10-10 00:18 | 305.06 | 2.23 | Orta | Gece |
| [38.0036, 41.55495](https://www.google.com/maps?q=38.0036,41.55495) | 2024-10-10 00:18 | 306.42 | 2.49 | Orta | Gece |
| [38.06121, 40.97907](https://www.google.com/maps?q=38.06121,40.97907) | 2024-10-10 00:18 | 342.52 | 12.63 | Orta | Gece |
| [38.06957, 41.00005](https://www.google.com/maps?q=38.06957,41.00005) | 2024-10-10 00:18 | 296.2 | 2.22 | Orta | Gece |
| [38.07114, 40.99693](https://www.google.com/maps?q=38.07114,40.99693) | 2024-10-10 00:18 | 311.29 | 2.93 | Orta | Gece |
| [38.07192, 40.99274](https://www.google.com/maps?q=38.07192,40.99274) | 2024-10-10 00:18 | 308.42 | 3.64 | Orta | Gece |
| [38.07347, 40.98981](https://www.google.com/maps?q=38.07347,40.98981) | 2024-10-10 00:18 | 309.44 | 2.93 | Orta | Gece |
| [38.07613, 41.00316](https://www.google.com/maps?q=38.07613,41.00316) | 2024-10-10 00:18 | 307.45 | 2.22 | Orta | Gece |
| [38.07768, 41.00008](https://www.google.com/maps?q=38.07768,41.00008) | 2024-10-10 00:18 | 297.05 | 1.81 | Orta | Gece |
| [38.07845, 40.99591](https://www.google.com/maps?q=38.07845,40.99591) | 2024-10-10 00:18 | 297.97 | 3.64 | Orta | Gece |
| [38.08004, 40.99289](https://www.google.com/maps?q=38.08004,40.99289) | 2024-10-10 00:18 | 302.28 | 1.81 | Orta | Gece |
| [38.09808, 40.98394](https://www.google.com/maps?q=38.09808,40.98394) | 2024-10-10 00:18 | 296.85 | 1.34 | Orta | Gece |
| [38.11028, 40.89652](https://www.google.com/maps?q=38.11028,40.89652) | 2024-10-10 00:18 | 305.29 | 2.09 | Orta | Gece |
| [38.11242, 40.89362](https://www.google.com/maps?q=38.11242,40.89362) | 2024-10-10 00:18 | 307.12 | 2.34 | Orta | Gece |
| [38.11656, 40.90403](https://www.google.com/maps?q=38.11656,40.90403) | 2024-10-10 00:18 | 296.16 | 3.26 | Orta | Gece |
| [38.11681, 40.89963](https://www.google.com/maps?q=38.11681,40.89963) | 2024-10-10 00:18 | 296.37 | 3.23 | Orta | Gece |
| [38.11889, 40.89686](https://www.google.com/maps?q=38.11889,40.89686) | 2024-10-10 00:18 | 303.02 | 2.34 | Orta | Gece |
| [38.12671, 39.75525](https://www.google.com/maps?q=38.12671,39.75525) | 2024-10-10 00:18 | 297.36 | 1.36 | Orta | Gece |
| [38.12753, 39.75215](https://www.google.com/maps?q=38.12753,39.75215) | 2024-10-10 00:18 | 298.04 | 1.35 | Orta | Gece |
| [38.96642, 36.40409](https://www.google.com/maps?q=38.96642,36.40409) | 2024-10-10 00:18 | 316.1 | 2.75 | Orta | Gece |
| [39.48275, 30.042](https://www.google.com/maps?q=39.48275,30.042) | 2024-10-10 00:18 | 303.84 | 2.19 | Orta | Gece |
| [39.55596, 36.79222](https://www.google.com/maps?q=39.55596,36.79222) | 2024-10-10 00:18 | 295.56 | 0.57 | Orta | Gece |
| [39.80188, 37.57063](https://www.google.com/maps?q=39.80188,37.57063) | 2024-10-10 00:18 | 308.6 | 1.75 | Orta | Gece |
| [39.80307, 37.58777](https://www.google.com/maps?q=39.80307,37.58777) | 2024-10-10 00:18 | 309.11 | 1.48 | Orta | Gece |
| [39.80433, 37.5717](https://www.google.com/maps?q=39.80433,37.5717) | 2024-10-10 00:18 | 298.21 | 1.48 | Orta | Gece |
| [39.83561, 30.30073](https://www.google.com/maps?q=39.83561,30.30073) | 2024-10-10 00:18 | 296.98 | 1.24 | Orta | Gece |
| [40.18412, 29.22659](https://www.google.com/maps?q=40.18412,29.22659) | 2024-10-10 00:18 | 298.41 | 0.36 | Orta | Gece |
| [40.74829, 29.76462](https://www.google.com/maps?q=40.74829,29.76462) | 2024-10-10 00:18 | 299.94 | 1.76 | Orta | Gece |
| [40.75689, 29.7613](https://www.google.com/maps?q=40.75689,29.7613) | 2024-10-10 00:18 | 300.93 | 1.2 | Orta | Gece |
| [40.76355, 29.5305](https://www.google.com/maps?q=40.76355,29.5305) | 2024-10-10 00:18 | 308.58 | 2.06 | Orta | Gece |
| [40.765, 29.53113](https://www.google.com/maps?q=40.765,29.53113) | 2024-10-10 00:18 | 309.03 | 2.29 | Orta | Gece |
| [40.78238, 29.59916](https://www.google.com/maps?q=40.78238,29.59916) | 2024-10-10 00:18 | 300.12 | 1.1 | Orta | Gece |
| [41.02076, 28.55729](https://www.google.com/maps?q=41.02076,28.55729) | 2024-10-10 00:18 | 304.65 | 1.33 | Orta | Gece |
| [41.24052, 36.46527](https://www.google.com/maps?q=41.24052,36.46527) | 2024-10-10 00:18 | 317.29 | 1.96 | Orta | Gece |
| [41.24158, 36.4613](https://www.google.com/maps?q=41.24158,36.4613) | 2024-10-10 00:18 | 302.8 | 2.0 | Orta | Gece |
| [41.25381, 31.41205](https://www.google.com/maps?q=41.25381,31.41205) | 2024-10-10 00:18 | 302.93 | 1.83 | Orta | Gece |
| [41.26352, 31.42579](https://www.google.com/maps?q=41.26352,31.42579) | 2024-10-10 00:18 | 302.73 | 1.09 | Orta | Gece |
| [41.26454, 31.42122](https://www.google.com/maps?q=41.26454,31.42122) | 2024-10-10 00:18 | 309.18 | 1.78 | Orta | Gece |
| [41.26744, 31.4273](https://www.google.com/maps?q=41.26744,31.4273) | 2024-10-10 00:18 | 301.29 | 1.09 | Orta | Gece |
| [41.6361, 27.50471](https://www.google.com/maps?q=41.6361,27.50471) | 2024-10-10 00:18 | 300.01 | 0.59 | Orta | Gece |
| [41.79778, 26.70046](https://www.google.com/maps?q=41.79778,26.70046) | 2024-10-10 00:18 | 303.67 | 0.59 | Orta | Gece |
| [36.26424, 33.72929](https://www.google.com/maps?q=36.26424,33.72929) | 2024-10-10 00:20 | 307.58 | 0.64 | Orta | Gece |
| [36.71782, 36.20272](https://www.google.com/maps?q=36.71782,36.20272) | 2024-10-10 00:20 | 316.31 | 5.14 | Orta | Gece |
| [36.8669, 34.75877](https://www.google.com/maps?q=36.8669,34.75877) | 2024-10-10 00:20 | 302.36 | 0.91 | Orta | Gece |
| [36.87096, 34.76485](https://www.google.com/maps?q=36.87096,34.76485) | 2024-10-10 00:20 | 305.19 | 0.83 | Orta | Gece |
| [36.88306, 34.89146](https://www.google.com/maps?q=36.88306,34.89146) | 2024-10-10 00:20 | 305.75 | 0.5 | Orta | Gece |
| [37.29512, 37.15769](https://www.google.com/maps?q=37.29512,37.15769) | 2024-10-10 00:20 | 303.7 | 1.41 | Orta | Gece |
| [37.89212, 34.87679](https://www.google.com/maps?q=37.89212,34.87679) | 2024-10-10 00:20 | 296.26 | 0.77 | Orta | Gece |
| [37.8956, 34.88478](https://www.google.com/maps?q=37.8956,34.88478) | 2024-10-10 00:20 | 329.31 | 5.67 | Orta | Gece |
| [37.89678, 34.88023](https://www.google.com/maps?q=37.89678,34.88023) | 2024-10-10 00:20 | 340.86 | 5.67 | Orta | Gece |
| [38.4272, 27.21867](https://www.google.com/maps?q=38.4272,27.21867) | 2024-10-10 00:20 | 316.2 | 2.1 | Orta | Gece |
| [38.45591, 27.26095](https://www.google.com/maps?q=38.45591,27.26095) | 2024-10-10 00:20 | 299.68 | 0.81 | Orta | Gece |
| [38.65653, 30.61653](https://www.google.com/maps?q=38.65653,30.61653) | 2024-10-10 00:20 | 300.28 | 1.22 | Orta | Gece |
| [38.66046, 30.61823](https://www.google.com/maps?q=38.66046,30.61823) | 2024-10-10 00:20 | 297.85 | 0.84 | Orta | Gece |
| [38.73197, 26.93042](https://www.google.com/maps?q=38.73197,26.93042) | 2024-10-10 00:20 | 299.1 | 0.77 | Orta | Gece |
| [38.73608, 26.94721](https://www.google.com/maps?q=38.73608,26.94721) | 2024-10-10 00:20 | 305.12 | 1.74 | Orta | Gece |
| [38.737, 26.94229](https://www.google.com/maps?q=38.737,26.94229) | 2024-10-10 00:20 | 314.41 | 1.74 | Orta | Gece |
| [38.73883, 26.93252](https://www.google.com/maps?q=38.73883,26.93252) | 2024-10-10 00:20 | 326.9 | 2.9 | Orta | Gece |
| [38.74295, 26.9493](https://www.google.com/maps?q=38.74295,26.9493) | 2024-10-10 00:20 | 310.94 | 1.57 | Orta | Gece |
| [38.74317, 26.92872](https://www.google.com/maps?q=38.74317,26.92872) | 2024-10-10 00:20 | 304.89 | 2.08 | Orta | Gece |
| [38.74638, 26.95036](https://www.google.com/maps?q=38.74638,26.95036) | 2024-10-10 00:20 | 311.95 | 1.57 | Orta | Gece |
| [39.08977, 27.51068](https://www.google.com/maps?q=39.08977,27.51068) | 2024-10-10 00:20 | 297.27 | 0.32 | Orta | Gece |
| [39.11111, 27.59248](https://www.google.com/maps?q=39.11111,27.59248) | 2024-10-10 00:20 | 302.47 | 0.96 | Orta | Gece |
| [39.1131, 27.52371](https://www.google.com/maps?q=39.1131,27.52371) | 2024-10-10 00:20 | 298.94 | 1.06 | Orta | Gece |
| [39.11499, 27.51375](https://www.google.com/maps?q=39.11499,27.51375) | 2024-10-10 00:20 | 299.21 | 1.0 | Orta | Gece |
| [39.16582, 27.63352](https://www.google.com/maps?q=39.16582,27.63352) | 2024-10-10 00:20 | 301.53 | 1.11 | Orta | Gece |
| [39.16679, 27.62846](https://www.google.com/maps?q=39.16679,27.62846) | 2024-10-10 00:20 | 300.48 | 1.11 | Orta | Gece |
| [39.1805, 27.49911](https://www.google.com/maps?q=39.1805,27.49911) | 2024-10-10 00:20 | 297.26 | 0.84 | Orta | Gece |
| [38.43035, 27.21324](https://www.google.com/maps?q=38.43035,27.21324) | 2024-10-10 01:05 | 297.22 | 0.73 | Orta | Gece |
| [38.74051, 26.94743](https://www.google.com/maps?q=38.74051,26.94743) | 2024-10-10 01:05 | 305.38 | 2.33 | Orta | Gece |
| [38.74855, 26.94401](https://www.google.com/maps?q=38.74855,26.94401) | 2024-10-10 01:05 | 308.36 | 2.18 | Orta | Gece |
| [40.44463, 27.13934](https://www.google.com/maps?q=40.44463,27.13934) | 2024-10-10 01:05 | 303.94 | 1.9 | Orta | Gece |
| [40.44564, 27.13769](https://www.google.com/maps?q=40.44564,27.13769) | 2024-10-10 01:05 | 302.71 | 1.11 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
