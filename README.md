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
### Son Güncelleme: 2024-10-11 13:56:01 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [40.75659, 31.78308](https://www.google.com/maps?q=40.75659,31.78308) | 2024-10-11 00:22 | 295.91 | 0.62 | Orta | Gece |
| [40.7586, 29.76215](https://www.google.com/maps?q=40.7586,29.76215) | 2024-10-11 00:22 | 302.74 | 1.21 | Orta | Gece |
| [40.76302, 29.52773](https://www.google.com/maps?q=40.76302,29.52773) | 2024-10-11 00:22 | 304.09 | 1.5 | Orta | Gece |
| [40.78067, 29.60237](https://www.google.com/maps?q=40.78067,29.60237) | 2024-10-11 00:22 | 300.73 | 0.9 | Orta | Gece |
| [40.81435, 26.21575](https://www.google.com/maps?q=40.81435,26.21575) | 2024-10-11 00:22 | 298.34 | 0.91 | Orta | Gece |
| [41.01421, 27.96398](https://www.google.com/maps?q=41.01421,27.96398) | 2024-10-11 00:22 | 301.36 | 0.37 | Orta | Gece |
| [41.01899, 28.55728](https://www.google.com/maps?q=41.01899,28.55728) | 2024-10-11 00:22 | 305.95 | 0.64 | Orta | Gece |
| [41.173, 32.6314](https://www.google.com/maps?q=41.173,32.6314) | 2024-10-11 00:22 | 299.49 | 1.33 | Orta | Gece |
| [41.24028, 36.46495](https://www.google.com/maps?q=41.24028,36.46495) | 2024-10-11 00:22 | 300.71 | 0.94 | Orta | Gece |
| [41.25215, 31.41252](https://www.google.com/maps?q=41.25215,31.41252) | 2024-10-11 00:22 | 312.89 | 2.69 | Orta | Gece |
| [41.25632, 31.41448](https://www.google.com/maps?q=41.25632,31.41448) | 2024-10-11 00:22 | 328.47 | 2.69 | Orta | Gece |
| [41.26349, 31.42335](https://www.google.com/maps?q=41.26349,31.42335) | 2024-10-11 00:22 | 299.34 | 1.45 | Orta | Gece |
| [41.26772, 31.42507](https://www.google.com/maps?q=41.26772,31.42507) | 2024-10-11 00:22 | 308.29 | 1.23 | Orta | Gece |
| [41.7962, 26.70357](https://www.google.com/maps?q=41.7962,26.70357) | 2024-10-11 00:22 | 299.5 | 0.59 | Orta | Gece |
| [37.01196, 36.10645](https://www.google.com/maps?q=37.01196,36.10645) | 2024-10-11 00:24 | 302.43 | 1.44 | Orta | Gece |
| [37.29258, 37.15525](https://www.google.com/maps?q=37.29258,37.15525) | 2024-10-11 00:24 | 296.17 | 1.06 | Orta | Gece |
| [37.29417, 37.15796](https://www.google.com/maps?q=37.29417,37.15796) | 2024-10-11 00:24 | 299.88 | 1.0 | Orta | Gece |
| [37.68979, 37.96113](https://www.google.com/maps?q=37.68979,37.96113) | 2024-10-11 00:24 | 300.26 | 1.56 | Orta | Gece |
| [37.89819, 30.49288](https://www.google.com/maps?q=37.89819,30.49288) | 2024-10-11 00:24 | 295.96 | 0.89 | Orta | Gece |
| [38.39021, 30.76332](https://www.google.com/maps?q=38.39021,30.76332) | 2024-10-11 00:24 | 296.91 | 1.24 | Orta | Gece |
| [38.42474, 27.21534](https://www.google.com/maps?q=38.42474,27.21534) | 2024-10-11 00:24 | 301.52 | 0.87 | Orta | Gece |
| [38.4284, 27.21679](https://www.google.com/maps?q=38.4284,27.21679) | 2024-10-11 00:24 | 301.11 | 0.87 | Orta | Gece |
| [38.45431, 27.26279](https://www.google.com/maps?q=38.45431,27.26279) | 2024-10-11 00:24 | 300.34 | 0.67 | Orta | Gece |
| [38.65974, 30.62201](https://www.google.com/maps?q=38.65974,30.62201) | 2024-10-11 00:24 | 295.81 | 0.95 | Orta | Gece |
| [38.73484, 26.9476](https://www.google.com/maps?q=38.73484,26.9476) | 2024-10-11 00:24 | 314.69 | 1.76 | Orta | Gece |
| [38.73594, 26.94211](https://www.google.com/maps?q=38.73594,26.94211) | 2024-10-11 00:24 | 302.98 | 1.22 | Orta | Gece |
| [38.73682, 26.92944](https://www.google.com/maps?q=38.73682,26.92944) | 2024-10-11 00:24 | 303.95 | 1.25 | Orta | Gece |
| [38.73816, 26.9311](https://www.google.com/maps?q=38.73816,26.9311) | 2024-10-11 00:24 | 318.62 | 2.22 | Orta | Gece |
| [38.73846, 26.94893](https://www.google.com/maps?q=38.73846,26.94893) | 2024-10-11 00:24 | 325.38 | 1.5 | Orta | Gece |
| [38.74181, 26.93228](https://www.google.com/maps?q=38.74181,26.93228) | 2024-10-11 00:24 | 302.1 | 0.77 | Orta | Gece |
| [38.7421, 26.95013](https://www.google.com/maps?q=38.7421,26.95013) | 2024-10-11 00:24 | 306.9 | 1.5 | Orta | Gece |
| [39.11397, 27.52314](https://www.google.com/maps?q=39.11397,27.52314) | 2024-10-11 00:24 | 298.62 | 0.83 | Orta | Gece |
| [39.16668, 27.62872](https://www.google.com/maps?q=39.16668,27.62872) | 2024-10-11 00:24 | 300.5 | 1.37 | Orta | Gece |
| [39.48544, 30.04305](https://www.google.com/maps?q=39.48544,30.04305) | 2024-10-11 00:24 | 304.53 | 1.29 | Orta | Gece |
| [39.74266, 30.19937](https://www.google.com/maps?q=39.74266,30.19937) | 2024-10-11 00:24 | 295.97 | 0.87 | Orta | Gece |
| [39.86319, 26.2453](https://www.google.com/maps?q=39.86319,26.2453) | 2024-10-11 00:24 | 310.83 | 1.26 | Orta | Gece |
| [39.86668, 26.24644](https://www.google.com/maps?q=39.86668,26.24644) | 2024-10-11 00:24 | 307.03 | 0.69 | Orta | Gece |
| [40.18462, 29.22705](https://www.google.com/maps?q=40.18462,29.22705) | 2024-10-11 00:24 | 296.73 | 0.61 | Orta | Gece |
| [40.44041, 27.14111](https://www.google.com/maps?q=40.44041,27.14111) | 2024-10-11 00:24 | 304.84 | 0.9 | Orta | Gece |
| [40.44398, 27.14233](https://www.google.com/maps?q=40.44398,27.14233) | 2024-10-11 00:24 | 301.07 | 0.85 | Orta | Gece |
| [36.2616, 33.73088](https://www.google.com/maps?q=36.2616,33.73088) | 2024-10-11 00:01 | 305.5 | 1.9 | Orta | Gece |
| [36.72978, 36.21193](https://www.google.com/maps?q=36.72978,36.21193) | 2024-10-11 00:01 | 308.67 | 2.77 | Orta | Gece |
| [36.86857, 34.76285](https://www.google.com/maps?q=36.86857,34.76285) | 2024-10-11 00:01 | 296.14 | 1.39 | Orta | Gece |
| [36.90743, 39.73189](https://www.google.com/maps?q=36.90743,39.73189) | 2024-10-11 00:01 | 300.37 | 0.87 | Orta | Gece |
| [36.90935, 39.73327](https://www.google.com/maps?q=36.90935,39.73327) | 2024-10-11 00:01 | 298.05 | 0.78 | Orta | Gece |
| [37.25191, 30.44331](https://www.google.com/maps?q=37.25191,30.44331) | 2024-10-11 00:01 | 295.77 | 0.78 | Orta | Gece |
| [37.2949, 37.15556](https://www.google.com/maps?q=37.2949,37.15556) | 2024-10-11 00:01 | 300.24 | 1.87 | Orta | Gece |
| [37.3402, 40.80171](https://www.google.com/maps?q=37.3402,40.80171) | 2024-10-11 00:01 | 297.07 | 0.85 | Orta | Gece |
| [37.35068, 37.16365](https://www.google.com/maps?q=37.35068,37.16365) | 2024-10-11 00:01 | 304.38 | 1.92 | Orta | Gece |
| [37.68496, 37.96218](https://www.google.com/maps?q=37.68496,37.96218) | 2024-10-11 00:01 | 307.09 | 2.5 | Orta | Gece |
| [37.6865, 37.9558](https://www.google.com/maps?q=37.6865,37.9558) | 2024-10-11 00:01 | 316.35 | 3.52 | Orta | Gece |
| [37.68653, 37.95653](https://www.google.com/maps?q=37.68653,37.95653) | 2024-10-11 00:01 | 322.44 | 6.02 | Orta | Gece |
| [37.73944, 38.1772](https://www.google.com/maps?q=37.73944,38.1772) | 2024-10-11 00:01 | 295.7 | 1.23 | Orta | Gece |
| [37.74321, 38.17774](https://www.google.com/maps?q=37.74321,38.17774) | 2024-10-11 00:01 | 296.56 | 0.79 | Orta | Gece |
| [37.84518, 40.38781](https://www.google.com/maps?q=37.84518,40.38781) | 2024-10-11 00:01 | 310.5 | 3.56 | Orta | Gece |
| [37.84636, 40.3835](https://www.google.com/maps?q=37.84636,40.3835) | 2024-10-11 00:01 | 349.64 | 5.14 | Orta | Gece |
| [37.84868, 40.38755](https://www.google.com/maps?q=37.84868,40.38755) | 2024-10-11 00:01 | 367.0 | 6.38 | Yüksek | Gece |
| [37.84983, 40.38321](https://www.google.com/maps?q=37.84983,40.38321) | 2024-10-11 00:01 | 302.75 | 6.38 | Orta | Gece |
| [37.85038, 40.39003](https://www.google.com/maps?q=37.85038,40.39003) | 2024-10-11 00:01 | 297.81 | 3.56 | Orta | Gece |
| [37.85156, 40.3857](https://www.google.com/maps?q=37.85156,40.3857) | 2024-10-11 00:01 | 301.52 | 5.14 | Orta | Gece |
| [37.93929, 32.53392](https://www.google.com/maps?q=37.93929,32.53392) | 2024-10-11 00:01 | 300.55 | 1.02 | Orta | Gece |
| [37.96572, 40.41341](https://www.google.com/maps?q=37.96572,40.41341) | 2024-10-11 00:01 | 295.81 | 0.59 | Orta | Gece |
| [37.96808, 40.415](https://www.google.com/maps?q=37.96808,40.415) | 2024-10-11 00:01 | 296.43 | 0.39 | Orta | Gece |
| [37.99731, 40.37111](https://www.google.com/maps?q=37.99731,40.37111) | 2024-10-11 00:01 | 295.52 | 0.44 | Orta | Gece |
| [37.99948, 41.59018](https://www.google.com/maps?q=37.99948,41.59018) | 2024-10-11 00:01 | 297.98 | 0.8 | Orta | Gece |
| [38.05149, 40.62991](https://www.google.com/maps?q=38.05149,40.62991) | 2024-10-11 00:01 | 308.48 | 1.12 | Orta | Gece |
| [38.05265, 40.62566](https://www.google.com/maps?q=38.05265,40.62566) | 2024-10-11 00:01 | 295.09 | 1.12 | Orta | Gece |
| [38.0531, 40.99332](https://www.google.com/maps?q=38.0531,40.99332) | 2024-10-11 00:01 | 314.76 | 1.77 | Orta | Gece |
| [38.06896, 40.86954](https://www.google.com/maps?q=38.06896,40.86954) | 2024-10-11 00:01 | 313.65 | 1.4 | Orta | Gece |
| [38.06919, 40.87038](https://www.google.com/maps?q=38.06919,40.87038) | 2024-10-11 00:01 | 313.21 | 1.54 | Orta | Gece |
| [38.07036, 40.86616](https://www.google.com/maps?q=38.07036,40.86616) | 2024-10-11 00:01 | 302.54 | 1.54 | Orta | Gece |
| [38.07423, 40.87191](https://www.google.com/maps?q=38.07423,40.87191) | 2024-10-11 00:01 | 296.6 | 1.4 | Orta | Gece |
| [38.13273, 40.85418](https://www.google.com/maps?q=38.13273,40.85418) | 2024-10-11 00:01 | 297.94 | 1.12 | Orta | Gece |
| [38.13569, 40.86499](https://www.google.com/maps?q=38.13569,40.86499) | 2024-10-11 00:01 | 307.47 | 1.89 | Orta | Gece |
| [38.13686, 40.86068](https://www.google.com/maps?q=38.13686,40.86068) | 2024-10-11 00:01 | 312.26 | 1.17 | Orta | Gece |
| [38.13804, 40.85634](https://www.google.com/maps?q=38.13804,40.85634) | 2024-10-11 00:01 | 301.28 | 1.17 | Orta | Gece |
| [38.14096, 40.86732](https://www.google.com/maps?q=38.14096,40.86732) | 2024-10-11 00:01 | 311.29 | 1.89 | Orta | Gece |
| [38.14214, 40.86296](https://www.google.com/maps?q=38.14214,40.86296) | 2024-10-11 00:01 | 295.85 | 1.17 | Orta | Gece |
| [38.14334, 40.85854](https://www.google.com/maps?q=38.14334,40.85854) | 2024-10-11 00:01 | 296.79 | 1.17 | Orta | Gece |
| [38.35492, 28.53714](https://www.google.com/maps?q=38.35492,28.53714) | 2024-10-11 00:01 | 301.48 | 0.6 | Orta | Gece |
| [38.3886, 30.75881](https://www.google.com/maps?q=38.3886,30.75881) | 2024-10-11 00:01 | 301.27 | 0.56 | Orta | Gece |
| [38.42747, 27.21782](https://www.google.com/maps?q=38.42747,27.21782) | 2024-10-11 00:01 | 314.7 | 1.4 | Orta | Gece |
| [38.45357, 38.72502](https://www.google.com/maps?q=38.45357,38.72502) | 2024-10-11 00:01 | 304.54 | 1.71 | Orta | Gece |
| [38.45519, 27.26099](https://www.google.com/maps?q=38.45519,27.26099) | 2024-10-11 00:01 | 305.62 | 1.05 | Orta | Gece |
| [38.65252, 39.76836](https://www.google.com/maps?q=38.65252,39.76836) | 2024-10-11 00:01 | 298.06 | 0.98 | Orta | Gece |
| [38.65808, 30.6186](https://www.google.com/maps?q=38.65808,30.6186) | 2024-10-11 00:01 | 305.7 | 1.39 | Orta | Gece |
| [38.7362, 26.94393](https://www.google.com/maps?q=38.7362,26.94393) | 2024-10-11 00:01 | 307.44 | 1.37 | Orta | Gece |
| [38.73813, 26.93045](https://www.google.com/maps?q=38.73813,26.93045) | 2024-10-11 00:01 | 323.0 | 2.49 | Orta | Gece |
| [38.73951, 26.9447](https://www.google.com/maps?q=38.73951,26.9447) | 2024-10-11 00:01 | 311.32 | 1.58 | Orta | Gece |
| [38.74218, 26.94997](https://www.google.com/maps?q=38.74218,26.94997) | 2024-10-11 00:01 | 313.84 | 1.58 | Orta | Gece |
| [39.1673, 27.6313](https://www.google.com/maps?q=39.1673,27.6313) | 2024-10-11 00:01 | 318.34 | 1.81 | Orta | Gece |
| [39.18392, 27.49689](https://www.google.com/maps?q=39.18392,27.49689) | 2024-10-11 00:01 | 300.57 | 0.92 | Orta | Gece |
| [39.48567, 30.04051](https://www.google.com/maps?q=39.48567,30.04051) | 2024-10-11 00:01 | 309.18 | 1.31 | Orta | Gece |
| [39.6081, 27.8774](https://www.google.com/maps?q=39.6081,27.8774) | 2024-10-11 00:01 | 302.32 | 0.77 | Orta | Gece |
| [39.74395, 30.19896](https://www.google.com/maps?q=39.74395,30.19896) | 2024-10-11 00:01 | 302.22 | 0.61 | Orta | Gece |
| [39.86402, 26.24565](https://www.google.com/maps?q=39.86402,26.24565) | 2024-10-11 00:01 | 321.12 | 2.32 | Orta | Gece |
| [39.86467, 26.24087](https://www.google.com/maps?q=39.86467,26.24087) | 2024-10-11 00:01 | 302.74 | 1.5 | Orta | Gece |
| [39.94341, 33.19236](https://www.google.com/maps?q=39.94341,33.19236) | 2024-10-11 00:01 | 299.51 | 1.03 | Orta | Gece |
| [40.26091, 30.04351](https://www.google.com/maps?q=40.26091,30.04351) | 2024-10-11 00:01 | 304.63 | 0.82 | Orta | Gece |
| [40.4404, 27.13846](https://www.google.com/maps?q=40.4404,27.13846) | 2024-10-11 00:01 | 307.52 | 1.17 | Orta | Gece |
| [40.44374, 27.13925](https://www.google.com/maps?q=40.44374,27.13925) | 2024-10-11 00:01 | 315.22 | 1.17 | Orta | Gece |
| [40.75656, 31.78419](https://www.google.com/maps?q=40.75656,31.78419) | 2024-10-11 00:01 | 297.5 | 0.71 | Orta | Gece |
| [40.76329, 32.21479](https://www.google.com/maps?q=40.76329,32.21479) | 2024-10-11 00:01 | 298.59 | 0.72 | Orta | Gece |
| [40.76372, 29.52896](https://www.google.com/maps?q=40.76372,29.52896) | 2024-10-11 00:01 | 306.0 | 1.62 | Orta | Gece |
| [40.81392, 26.21375](https://www.google.com/maps?q=40.81392,26.21375) | 2024-10-11 00:01 | 302.46 | 0.91 | Orta | Gece |
| [40.94637, 31.39802](https://www.google.com/maps?q=40.94637,31.39802) | 2024-10-11 00:01 | 300.86 | 0.79 | Orta | Gece |
| [41.0146, 27.96051](https://www.google.com/maps?q=41.0146,27.96051) | 2024-10-11 00:01 | 329.36 | 3.7 | Orta | Gece |
| [41.01833, 28.55525](https://www.google.com/maps?q=41.01833,28.55525) | 2024-10-11 00:01 | 306.72 | 1.16 | Orta | Gece |
| [41.02161, 28.55611](https://www.google.com/maps?q=41.02161,28.55611) | 2024-10-11 00:01 | 310.08 | 1.16 | Orta | Gece |
| [41.17422, 32.63593](https://www.google.com/maps?q=41.17422,32.63593) | 2024-10-11 00:01 | 326.92 | 2.38 | Orta | Gece |
| [41.17517, 32.63079](https://www.google.com/maps?q=41.17517,32.63079) | 2024-10-11 00:01 | 308.78 | 2.62 | Orta | Gece |
| [41.17764, 32.63706](https://www.google.com/maps?q=41.17764,32.63706) | 2024-10-11 00:01 | 296.05 | 2.38 | Orta | Gece |
| [41.18298, 32.63596](https://www.google.com/maps?q=41.18298,32.63596) | 2024-10-11 00:01 | 299.53 | 1.0 | Orta | Gece |
| [41.24011, 36.4621](https://www.google.com/maps?q=41.24011,36.4621) | 2024-10-11 00:01 | 308.59 | 0.96 | Orta | Gece |
| [41.26513, 31.42489](https://www.google.com/maps?q=41.26513,31.42489) | 2024-10-11 00:01 | 299.98 | 0.96 | Orta | Gece |
| [37.10568, 41.37507](https://www.google.com/maps?q=37.10568,41.37507) | 2024-10-11 09:41 | 348.54 | 13.16 | Orta | Gündüz |
| [37.29653, 35.8176](https://www.google.com/maps?q=37.29653,35.8176) | 2024-10-11 09:41 | 342.87 | 5.88 | Orta | Gündüz |
| [37.54743, 38.4527](https://www.google.com/maps?q=37.54743,38.4527) | 2024-10-11 09:41 | 332.45 | 5.22 | Düşük | Gündüz |
| [37.55696, 38.14845](https://www.google.com/maps?q=37.55696,38.14845) | 2024-10-11 09:41 | 336.11 | 3.85 | Orta | Gündüz |
| [37.68004, 38.31882](https://www.google.com/maps?q=37.68004,38.31882) | 2024-10-11 09:41 | 333.96 | 9.19 | Orta | Gündüz |
| [37.77137, 38.78113](https://www.google.com/maps?q=37.77137,38.78113) | 2024-10-11 09:41 | 338.88 | 6.8 | Orta | Gündüz |
| [37.77226, 38.78465](https://www.google.com/maps?q=37.77226,38.78465) | 2024-10-11 09:41 | 350.56 | 7.27 | Orta | Gündüz |
| [38.01593, 41.82124](https://www.google.com/maps?q=38.01593,41.82124) | 2024-10-11 09:41 | 342.29 | 7.39 | Orta | Gündüz |
| [38.01708, 41.82634](https://www.google.com/maps?q=38.01708,41.82634) | 2024-10-11 09:41 | 346.28 | 7.39 | Orta | Gündüz |
| [38.01949, 41.14881](https://www.google.com/maps?q=38.01949,41.14881) | 2024-10-11 09:41 | 331.04 | 4.95 | Orta | Gündüz |
| [38.07867, 39.81338](https://www.google.com/maps?q=38.07867,39.81338) | 2024-10-11 09:41 | 330.83 | 6.11 | Orta | Gündüz |
| [38.08018, 39.81963](https://www.google.com/maps?q=38.08018,39.81963) | 2024-10-11 09:41 | 339.8 | 9.05 | Orta | Gündüz |
| [39.55249, 31.87406](https://www.google.com/maps?q=39.55249,31.87406) | 2024-10-11 09:41 | 350.33 | 15.71 | Orta | Gündüz |
| [40.79385, 30.57901](https://www.google.com/maps?q=40.79385,30.57901) | 2024-10-11 09:41 | 326.09 | 4.66 | Orta | Gündüz |
| [41.6809, 35.85193](https://www.google.com/maps?q=41.6809,35.85193) | 2024-10-11 09:41 | 325.45 | 2.21 | Orta | Gündüz |
| [38.28035, 37.07228](https://www.google.com/maps?q=38.28035,37.07228) | 2024-10-11 09:43 | 336.71 | 3.5 | Orta | Gündüz |
| [38.28251, 37.07122](https://www.google.com/maps?q=38.28251,37.07122) | 2024-10-11 09:43 | 334.63 | 4.8 | Orta | Gündüz |
| [38.46609, 35.59981](https://www.google.com/maps?q=38.46609,35.59981) | 2024-10-11 09:43 | 331.8 | 4.84 | Düşük | Gündüz |
| [38.47113, 37.34615](https://www.google.com/maps?q=38.47113,37.34615) | 2024-10-11 09:43 | 335.42 | 4.34 | Orta | Gündüz |
| [38.47536, 37.34361](https://www.google.com/maps?q=38.47536,37.34361) | 2024-10-11 09:43 | 354.27 | 9.02 | Orta | Gündüz |
| [38.47624, 37.34399](https://www.google.com/maps?q=38.47624,37.34399) | 2024-10-11 09:43 | 351.06 | 4.34 | Orta | Gündüz |
| [39.14788, 37.24267](https://www.google.com/maps?q=39.14788,37.24267) | 2024-10-11 09:43 | 367.0 | 8.89 | Yüksek | Gündüz |
| [39.2174, 37.54487](https://www.google.com/maps?q=39.2174,37.54487) | 2024-10-11 09:43 | 351.43 | 6.38 | Orta | Gündüz |
| [39.21841, 37.54868](https://www.google.com/maps?q=39.21841,37.54868) | 2024-10-11 09:43 | 345.03 | 6.38 | Orta | Gündüz |
| [39.36689, 36.32272](https://www.google.com/maps?q=39.36689,36.32272) | 2024-10-11 09:43 | 335.17 | 5.44 | Orta | Gündüz |
| [39.88428, 36.89408](https://www.google.com/maps?q=39.88428,36.89408) | 2024-10-11 09:43 | 367.0 | 10.32 | Yüksek | Gündüz |
| [39.88923, 36.89157](https://www.google.com/maps?q=39.88923,36.89157) | 2024-10-11 09:43 | 354.63 | 10.32 | Orta | Gündüz |
| [37.02695, 35.76462](https://www.google.com/maps?q=37.02695,35.76462) | 2024-10-11 11:21 | 348.09 | 6.63 | Orta | Gündüz |
| [37.36988, 36.94808](https://www.google.com/maps?q=37.36988,36.94808) | 2024-10-11 11:21 | 330.56 | 3.99 | Düşük | Gündüz |
| [37.97263, 32.73938](https://www.google.com/maps?q=37.97263,32.73938) | 2024-10-11 11:21 | 339.51 | 8.64 | Orta | Gündüz |
| [38.10541, 29.66383](https://www.google.com/maps?q=38.10541,29.66383) | 2024-10-11 11:21 | 344.43 | 10.2 | Orta | Gündüz |
| [38.10632, 29.66233](https://www.google.com/maps?q=38.10632,29.66233) | 2024-10-11 11:21 | 336.81 | 10.96 | Orta | Gündüz |
| [38.23479, 37.11519](https://www.google.com/maps?q=38.23479,37.11519) | 2024-10-11 11:21 | 346.08 | 5.36 | Orta | Gündüz |
| [38.23521, 37.11258](https://www.google.com/maps?q=38.23521,37.11258) | 2024-10-11 11:21 | 330.9 | 6.43 | Düşük | Gündüz |
| [38.25967, 37.29821](https://www.google.com/maps?q=38.25967,37.29821) | 2024-10-11 11:21 | 332.65 | 2.81 | Orta | Gündüz |
| [38.27221, 37.17046](https://www.google.com/maps?q=38.27221,37.17046) | 2024-10-11 11:21 | 334.71 | 3.58 | Orta | Gündüz |
| [38.2797, 37.06978](https://www.google.com/maps?q=38.2797,37.06978) | 2024-10-11 11:21 | 334.0 | 5.0 | Orta | Gündüz |
| [38.28037, 37.08549](https://www.google.com/maps?q=38.28037,37.08549) | 2024-10-11 11:21 | 334.31 | 4.34 | Orta | Gündüz |
| [38.28687, 37.10081](https://www.google.com/maps?q=38.28687,37.10081) | 2024-10-11 11:21 | 367.0 | 12.84 | Yüksek | Gündüz |
| [38.2871, 37.10607](https://www.google.com/maps?q=38.2871,37.10607) | 2024-10-11 11:21 | 337.98 | 12.84 | Orta | Gündüz |
| [38.31407, 36.92598](https://www.google.com/maps?q=38.31407,36.92598) | 2024-10-11 11:21 | 330.05 | 2.11 | Orta | Gündüz |
| [38.46195, 35.59855](https://www.google.com/maps?q=38.46195,35.59855) | 2024-10-11 11:21 | 340.63 | 3.99 | Orta | Gündüz |
| [38.75471, 32.01284](https://www.google.com/maps?q=38.75471,32.01284) | 2024-10-11 11:21 | 337.84 | 4.83 | Orta | Gündüz |
| [38.75835, 32.01169](https://www.google.com/maps?q=38.75835,32.01169) | 2024-10-11 11:21 | 333.98 | 5.1 | Düşük | Gündüz |
| [39.0394, 34.74192](https://www.google.com/maps?q=39.0394,34.74192) | 2024-10-11 11:21 | 342.88 | 3.16 | Orta | Gündüz |
| [39.11712, 31.52504](https://www.google.com/maps?q=39.11712,31.52504) | 2024-10-11 11:21 | 351.35 | 71.91 | Orta | Gündüz |
| [39.13763, 37.41236](https://www.google.com/maps?q=39.13763,37.41236) | 2024-10-11 11:21 | 343.12 | 9.27 | Orta | Gündüz |
| [39.27427, 35.42653](https://www.google.com/maps?q=39.27427,35.42653) | 2024-10-11 11:21 | 336.18 | 8.97 | Orta | Gündüz |
| [39.27449, 35.4306](https://www.google.com/maps?q=39.27449,35.4306) | 2024-10-11 11:21 | 349.57 | 8.12 | Orta | Gündüz |
| [39.3675, 36.31738](https://www.google.com/maps?q=39.3675,36.31738) | 2024-10-11 11:21 | 337.6 | 5.41 | Orta | Gündüz |
| [39.36772, 36.32253](https://www.google.com/maps?q=39.36772,36.32253) | 2024-10-11 11:21 | 349.72 | 5.41 | Orta | Gündüz |
| [39.37021, 36.31976](https://www.google.com/maps?q=39.37021,36.31976) | 2024-10-11 11:21 | 353.04 | 10.27 | Orta | Gündüz |
| [39.51405, 31.53026](https://www.google.com/maps?q=39.51405,31.53026) | 2024-10-11 11:21 | 332.74 | 3.58 | Düşük | Gündüz |
| [39.5469, 31.86933](https://www.google.com/maps?q=39.5469,31.86933) | 2024-10-11 11:21 | 336.64 | 5.63 | Orta | Gündüz |
| [39.80646, 31.25501](https://www.google.com/maps?q=39.80646,31.25501) | 2024-10-11 11:21 | 342.15 | 8.17 | Orta | Gündüz |
| [40.01279, 28.22297](https://www.google.com/maps?q=40.01279,28.22297) | 2024-10-11 11:21 | 343.58 | 20.27 | Orta | Gündüz |
| [40.08441, 27.9985](https://www.google.com/maps?q=40.08441,27.9985) | 2024-10-11 11:21 | 345.8 | 10.88 | Orta | Gündüz |
| [40.08536, 27.99938](https://www.google.com/maps?q=40.08536,27.99938) | 2024-10-11 11:21 | 345.2 | 10.04 | Orta | Gündüz |
| [40.08808, 27.99778](https://www.google.com/maps?q=40.08808,27.99778) | 2024-10-11 11:21 | 340.94 | 6.68 | Orta | Gündüz |
| [40.08904, 27.99867](https://www.google.com/maps?q=40.08904,27.99867) | 2024-10-11 11:21 | 334.57 | 10.04 | Orta | Gündüz |
| [40.10452, 27.97726](https://www.google.com/maps?q=40.10452,27.97726) | 2024-10-11 11:21 | 326.06 | 2.56 | Orta | Gündüz |
| [40.10739, 27.9364](https://www.google.com/maps?q=40.10739,27.9364) | 2024-10-11 11:21 | 330.69 | 2.12 | Orta | Gündüz |
| [40.1136, 27.95819](https://www.google.com/maps?q=40.1136,27.95819) | 2024-10-11 11:21 | 328.34 | 5.37 | Orta | Gündüz |
| [40.11726, 27.95748](https://www.google.com/maps?q=40.11726,27.95748) | 2024-10-11 11:21 | 344.91 | 5.37 | Orta | Gündüz |
| [40.11854, 27.96875](https://www.google.com/maps?q=40.11854,27.96875) | 2024-10-11 11:21 | 326.77 | 4.98 | Orta | Gündüz |
| [40.13707, 27.99981](https://www.google.com/maps?q=40.13707,27.99981) | 2024-10-11 11:21 | 334.79 | 5.95 | Orta | Gündüz |
| [40.14074, 27.99909](https://www.google.com/maps?q=40.14074,27.99909) | 2024-10-11 11:21 | 345.41 | 7.57 | Orta | Gündüz |
| [40.14441, 27.99838](https://www.google.com/maps?q=40.14441,27.99838) | 2024-10-11 11:21 | 337.53 | 7.57 | Orta | Gündüz |
| [40.17371, 28.29198](https://www.google.com/maps?q=40.17371,28.29198) | 2024-10-11 11:21 | 332.44 | 4.92 | Orta | Gündüz |
| [40.18448, 28.21874](https://www.google.com/maps?q=40.18448,28.21874) | 2024-10-11 11:21 | 329.26 | 6.37 | Orta | Gündüz |
| [40.31298, 27.2197](https://www.google.com/maps?q=40.31298,27.2197) | 2024-10-11 11:21 | 331.68 | 4.24 | Orta | Gündüz |
| [40.73705, 26.33768](https://www.google.com/maps?q=40.73705,26.33768) | 2024-10-11 11:21 | 331.38 | 2.67 | Orta | Gündüz |
| [40.74338, 30.53653](https://www.google.com/maps?q=40.74338,30.53653) | 2024-10-11 11:21 | 332.86 | 3.22 | Orta | Gündüz |
| [40.77505, 30.45227](https://www.google.com/maps?q=40.77505,30.45227) | 2024-10-11 11:21 | 341.46 | 5.02 | Orta | Gündüz |
| [40.77695, 30.57761](https://www.google.com/maps?q=40.77695,30.57761) | 2024-10-11 11:21 | 348.05 | 25.76 | Orta | Gündüz |
| [40.77733, 30.57507](https://www.google.com/maps?q=40.77733,30.57507) | 2024-10-11 11:21 | 345.29 | 15.94 | Orta | Gündüz |
| [40.77742, 30.58269](https://www.google.com/maps?q=40.77742,30.58269) | 2024-10-11 11:21 | 341.42 | 11.23 | Orta | Gündüz |
| [40.77777, 30.58015](https://www.google.com/maps?q=40.77777,30.58015) | 2024-10-11 11:21 | 352.22 | 15.94 | Orta | Gündüz |
| [40.78115, 30.57696](https://www.google.com/maps?q=40.78115,30.57696) | 2024-10-11 11:21 | 354.54 | 25.76 | Orta | Gündüz |
| [40.78153, 30.57441](https://www.google.com/maps?q=40.78153,30.57441) | 2024-10-11 11:21 | 340.69 | 13.37 | Orta | Gündüz |
| [40.78162, 30.58205](https://www.google.com/maps?q=40.78162,30.58205) | 2024-10-11 11:21 | 338.55 | 11.23 | Orta | Gündüz |
| [40.78197, 30.5795](https://www.google.com/maps?q=40.78197,30.5795) | 2024-10-11 11:21 | 345.72 | 13.37 | Orta | Gündüz |
| [40.78242, 30.58459](https://www.google.com/maps?q=40.78242,30.58459) | 2024-10-11 11:21 | 332.52 | 17.61 | Orta | Gündüz |
| [40.78257, 30.59222](https://www.google.com/maps?q=40.78257,30.59222) | 2024-10-11 11:21 | 339.25 | 5.46 | Orta | Gündüz |
| [40.78286, 30.58969](https://www.google.com/maps?q=40.78286,30.58969) | 2024-10-11 11:21 | 352.99 | 17.61 | Orta | Gündüz |
| [40.78296, 30.44591](https://www.google.com/maps?q=40.78296,30.44591) | 2024-10-11 11:21 | 328.9 | 1.61 | Düşük | Gündüz |
| [40.78331, 30.5948](https://www.google.com/maps?q=40.78331,30.5948) | 2024-10-11 11:21 | 328.11 | 4.36 | Orta | Gündüz |
| [40.78484, 30.56357](https://www.google.com/maps?q=40.78484,30.56357) | 2024-10-11 11:21 | 355.37 | 18.58 | Orta | Gündüz |
| [40.78618, 30.57883](https://www.google.com/maps?q=40.78618,30.57883) | 2024-10-11 11:21 | 341.29 | 13.37 | Orta | Gündüz |
| [40.78662, 30.58393](https://www.google.com/maps?q=40.78662,30.58393) | 2024-10-11 11:21 | 347.81 | 17.61 | Orta | Gündüz |
| [40.78706, 30.58903](https://www.google.com/maps?q=40.78706,30.58903) | 2024-10-11 11:21 | 353.32 | 17.61 | Orta | Gündüz |
| [40.78904, 30.56291](https://www.google.com/maps?q=40.78904,30.56291) | 2024-10-11 11:21 | 353.8 | 11.33 | Orta | Gündüz |
| [40.79038, 30.57817](https://www.google.com/maps?q=40.79038,30.57817) | 2024-10-11 11:21 | 328.49 | 4.2 | Orta | Gündüz |
| [40.79082, 30.58327](https://www.google.com/maps?q=40.79082,30.58327) | 2024-10-11 11:21 | 327.12 | 19.78 | Orta | Gündüz |
| [40.79354, 26.20866](https://www.google.com/maps?q=40.79354,26.20866) | 2024-10-11 11:21 | 330.78 | 6.72 | Orta | Gündüz |
| [40.79458, 30.57751](https://www.google.com/maps?q=40.79458,30.57751) | 2024-10-11 11:21 | 340.43 | 4.2 | Orta | Gündüz |
| [40.79502, 30.58261](https://www.google.com/maps?q=40.79502,30.58261) | 2024-10-11 11:21 | 346.07 | 19.78 | Orta | Gündüz |
| [40.79548, 30.58772](https://www.google.com/maps?q=40.79548,30.58772) | 2024-10-11 11:21 | 340.64 | 19.78 | Orta | Gündüz |
| [40.79624, 30.50002](https://www.google.com/maps?q=40.79624,30.50002) | 2024-10-11 11:21 | 339.49 | 6.58 | Orta | Gündüz |
| [40.79788, 26.18707](https://www.google.com/maps?q=40.79788,26.18707) | 2024-10-11 11:21 | 336.49 | 4.16 | Orta | Gündüz |
| [40.80761, 26.31949](https://www.google.com/maps?q=40.80761,26.31949) | 2024-10-11 11:21 | 330.41 | 3.82 | Orta | Gündüz |
| [40.80825, 26.32455](https://www.google.com/maps?q=40.80825,26.32455) | 2024-10-11 11:21 | 332.92 | 3.82 | Orta | Gündüz |
| [40.82653, 26.21683](https://www.google.com/maps?q=40.82653,26.21683) | 2024-10-11 11:21 | 329.56 | 2.88 | Orta | Gündüz |
| [40.84659, 26.29012](https://www.google.com/maps?q=40.84659,26.29012) | 2024-10-11 11:21 | 331.62 | 5.44 | Orta | Gündüz |
| [40.85005, 26.28935](https://www.google.com/maps?q=40.85005,26.28935) | 2024-10-11 11:21 | 330.76 | 4.87 | Orta | Gündüz |
| [40.85351, 26.28859](https://www.google.com/maps?q=40.85351,26.28859) | 2024-10-11 11:21 | 343.71 | 4.87 | Orta | Gündüz |
| [40.8548, 26.28679](https://www.google.com/maps?q=40.8548,26.28679) | 2024-10-11 11:21 | 345.55 | 7.57 | Orta | Gündüz |
| [40.86392, 26.27437](https://www.google.com/maps?q=40.86392,26.27437) | 2024-10-11 11:21 | 328.96 | 3.81 | Orta | Gündüz |
| [40.86864, 26.28373](https://www.google.com/maps?q=40.86864,26.28373) | 2024-10-11 11:21 | 333.46 | 5.66 | Orta | Gündüz |
| [40.88468, 26.26978](https://www.google.com/maps?q=40.88468,26.26978) | 2024-10-11 11:21 | 331.35 | 3.4 | Orta | Gündüz |
| [40.93998, 26.341](https://www.google.com/maps?q=40.93998,26.341) | 2024-10-11 11:21 | 347.54 | 10.72 | Orta | Gündüz |
| [41.02794, 30.55774](https://www.google.com/maps?q=41.02794,30.55774) | 2024-10-11 11:21 | 328.86 | 2.89 | Orta | Gündüz |
| [41.04913, 26.40363](https://www.google.com/maps?q=41.04913,26.40363) | 2024-10-11 11:21 | 334.22 | 3.73 | Orta | Gündüz |
| [41.05079, 29.95082](https://www.google.com/maps?q=41.05079,29.95082) | 2024-10-11 11:21 | 339.32 | 5.22 | Orta | Gündüz |
| [41.08504, 26.57618](https://www.google.com/maps?q=41.08504,26.57618) | 2024-10-11 11:21 | 331.35 | 6.51 | Orta | Gündüz |
| [41.13497, 27.10528](https://www.google.com/maps?q=41.13497,27.10528) | 2024-10-11 11:21 | 345.49 | 8.33 | Orta | Gündüz |
| [41.33524, 27.63923](https://www.google.com/maps?q=41.33524,27.63923) | 2024-10-11 11:21 | 329.03 | 3.46 | Orta | Gündüz |
| [41.5946, 35.88308](https://www.google.com/maps?q=41.5946,35.88308) | 2024-10-11 11:21 | 330.33 | 2.73 | Orta | Gündüz |
| [41.64544, 35.79952](https://www.google.com/maps?q=41.64544,35.79952) | 2024-10-11 11:21 | 326.16 | 7.37 | Orta | Gündüz |
| [41.64724, 35.79933](https://www.google.com/maps?q=41.64724,35.79933) | 2024-10-11 11:21 | 329.83 | 3.88 | Orta | Gündüz |
| [41.65343, 35.93928](https://www.google.com/maps?q=41.65343,35.93928) | 2024-10-11 11:21 | 343.62 | 5.81 | Orta | Gündüz |
| [41.65648, 35.93928](https://www.google.com/maps?q=41.65648,35.93928) | 2024-10-11 11:21 | 337.98 | 4.16 | Orta | Gündüz |
| [41.65938, 35.86843](https://www.google.com/maps?q=41.65938,35.86843) | 2024-10-11 11:21 | 325.04 | 3.59 | Orta | Gündüz |
| [41.66158, 35.86814](https://www.google.com/maps?q=41.66158,35.86814) | 2024-10-11 11:21 | 326.78 | 3.44 | Orta | Gündüz |
| [38.42759, 27.21547](https://www.google.com/maps?q=38.42759,27.21547) | 2024-10-11 00:48 | 307.03 | 0.65 | Orta | Gece |
| [38.45464, 27.26137](https://www.google.com/maps?q=38.45464,27.26137) | 2024-10-11 00:48 | 302.94 | 0.58 | Orta | Gece |
| [38.65768, 30.61743](https://www.google.com/maps?q=38.65768,30.61743) | 2024-10-11 00:48 | 297.4 | 1.72 | Orta | Gece |
| [38.65844, 30.61341](https://www.google.com/maps?q=38.65844,30.61341) | 2024-10-11 00:48 | 295.5 | 0.86 | Orta | Gece |
| [38.73804, 26.92892](https://www.google.com/maps?q=38.73804,26.92892) | 2024-10-11 00:48 | 302.21 | 0.57 | Orta | Gece |
| [38.73909, 26.94592](https://www.google.com/maps?q=38.73909,26.94592) | 2024-10-11 00:48 | 311.19 | 1.93 | Orta | Gece |
| [38.74989, 26.94635](https://www.google.com/maps?q=38.74989,26.94635) | 2024-10-11 00:48 | 299.86 | 1.14 | Orta | Gece |
| [39.11437, 27.51091](https://www.google.com/maps?q=39.11437,27.51091) | 2024-10-11 00:48 | 297.93 | 0.85 | Orta | Gece |
| [39.1668, 27.62977](https://www.google.com/maps?q=39.1668,27.62977) | 2024-10-11 00:48 | 301.69 | 0.94 | Orta | Gece |
| [39.16747, 27.62985](https://www.google.com/maps?q=39.16747,27.62985) | 2024-10-11 00:48 | 302.11 | 0.84 | Orta | Gece |
| [39.86654, 26.24351](https://www.google.com/maps?q=39.86654,26.24351) | 2024-10-11 00:48 | 305.8 | 1.7 | Orta | Gece |
| [39.86673, 26.24181](https://www.google.com/maps?q=39.86673,26.24181) | 2024-10-11 00:48 | 309.0 | 1.62 | Orta | Gece |
| [40.18659, 29.22306](https://www.google.com/maps?q=40.18659,29.22306) | 2024-10-11 00:48 | 301.23 | 0.45 | Orta | Gece |
| [41.01443, 27.96063](https://www.google.com/maps?q=41.01443,27.96063) | 2024-10-11 00:48 | 299.63 | 0.65 | Orta | Gece |
| [41.0186, 28.55392](https://www.google.com/maps?q=41.0186,28.55392) | 2024-10-11 00:48 | 299.79 | 0.73 | Orta | Gece |
| [41.21398, 27.87914](https://www.google.com/maps?q=41.21398,27.87914) | 2024-10-11 00:48 | 304.49 | 0.77 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
