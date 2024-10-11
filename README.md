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
### Son Güncelleme: 2024-10-11 05:47:03 (UTC)

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

## Yazar

[sarusadgac](https://x.com/sarusadgac)
