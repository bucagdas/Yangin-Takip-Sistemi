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
### Son Güncelleme: 2024-10-08 10:49:50 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.42433, 27.21338](https://www.google.com/maps?q=38.42433,27.21338) | 2024-10-08 00:56 | 300.68 | 0.76 | Orta | Gece |
| [38.73687, 26.94236](https://www.google.com/maps?q=38.73687,26.94236) | 2024-10-08 00:56 | 305.23 | 2.12 | Orta | Gece |
| [38.74214, 26.94476](https://www.google.com/maps?q=38.74214,26.94476) | 2024-10-08 00:56 | 299.62 | 1.27 | Orta | Gece |
| [38.74737, 26.94728](https://www.google.com/maps?q=38.74737,26.94728) | 2024-10-08 00:56 | 301.9 | 1.27 | Orta | Gece |
| [38.74985, 26.93819](https://www.google.com/maps?q=38.74985,26.93819) | 2024-10-08 00:56 | 306.8 | 1.43 | Orta | Gece |
| [39.10963, 27.59366](https://www.google.com/maps?q=39.10963,27.59366) | 2024-10-08 00:56 | 301.21 | 0.78 | Orta | Gece |
| [39.48393, 30.03833](https://www.google.com/maps?q=39.48393,30.03833) | 2024-10-08 00:56 | 299.47 | 2.62 | Orta | Gece |
| [39.48542, 30.03987](https://www.google.com/maps?q=39.48542,30.03987) | 2024-10-08 00:56 | 302.37 | 1.87 | Orta | Gece |
| [39.60813, 27.87942](https://www.google.com/maps?q=39.60813,27.87942) | 2024-10-08 00:56 | 298.36 | 0.61 | Orta | Gece |
| [39.86337, 26.2429](https://www.google.com/maps?q=39.86337,26.2429) | 2024-10-08 00:56 | 318.88 | 1.93 | Orta | Gece |
| [39.86598, 26.24699](https://www.google.com/maps?q=39.86598,26.24699) | 2024-10-08 00:56 | 302.66 | 1.26 | Orta | Gece |
| [39.867, 26.24306](https://www.google.com/maps?q=39.867,26.24306) | 2024-10-08 00:56 | 302.84 | 1.47 | Orta | Gece |
| [41.01854, 28.55681](https://www.google.com/maps?q=41.01854,28.55681) | 2024-10-08 00:56 | 303.13 | 1.11 | Orta | Gece |
| [41.2537, 31.41209](https://www.google.com/maps?q=41.2537,31.41209) | 2024-10-08 00:56 | 313.89 | 2.67 | Orta | Gece |
| [41.26347, 31.42525](https://www.google.com/maps?q=41.26347,31.42525) | 2024-10-08 00:56 | 300.31 | 2.18 | Orta | Gece |
| [41.79639, 26.70056](https://www.google.com/maps?q=41.79639,26.70056) | 2024-10-08 00:56 | 296.23 | 0.61 | Orta | Gece |
| [36.26195, 33.7273](https://www.google.com/maps?q=36.26195,33.7273) | 2024-10-08 00:03 | 303.48 | 1.0 | Orta | Gece |
| [36.26617, 33.72871](https://www.google.com/maps?q=36.26617,33.72871) | 2024-10-08 00:03 | 302.48 | 0.35 | Orta | Gece |
| [36.73125, 36.20831](https://www.google.com/maps?q=36.73125,36.20831) | 2024-10-08 00:03 | 305.24 | 2.25 | Orta | Gece |
| [36.74389, 36.19888](https://www.google.com/maps?q=36.74389,36.19888) | 2024-10-08 00:03 | 307.0 | 2.25 | Orta | Gece |
| [36.96375, 35.45155](https://www.google.com/maps?q=36.96375,35.45155) | 2024-10-08 00:03 | 302.39 | 1.17 | Orta | Gece |
| [37.12355, 41.68253](https://www.google.com/maps?q=37.12355,41.68253) | 2024-10-08 00:03 | 298.98 | 1.54 | Orta | Gece |
| [37.12541, 41.67636](https://www.google.com/maps?q=37.12541,41.67636) | 2024-10-08 00:03 | 312.79 | 2.38 | Orta | Gece |
| [37.57013, 38.42611](https://www.google.com/maps?q=37.57013,38.42611) | 2024-10-08 00:03 | 297.01 | 0.39 | Orta | Gece |
| [37.57291, 38.42799](https://www.google.com/maps?q=37.57291,38.42799) | 2024-10-08 00:03 | 301.32 | 0.65 | Orta | Gece |
| [37.71047, 38.16589](https://www.google.com/maps?q=37.71047,38.16589) | 2024-10-08 00:03 | 298.59 | 2.01 | Orta | Gece |
| [37.75613, 38.48461](https://www.google.com/maps?q=37.75613,38.48461) | 2024-10-08 00:03 | 312.54 | 1.86 | Orta | Gece |
| [37.75976, 38.48412](https://www.google.com/maps?q=37.75976,38.48412) | 2024-10-08 00:03 | 304.74 | 0.78 | Orta | Gece |
| [37.77009, 27.43848](https://www.google.com/maps?q=37.77009,27.43848) | 2024-10-08 00:03 | 302.27 | 0.68 | Orta | Gece |
| [37.77889, 38.73455](https://www.google.com/maps?q=37.77889,38.73455) | 2024-10-08 00:03 | 298.3 | 0.61 | Orta | Gece |
| [37.7799, 38.73077](https://www.google.com/maps?q=37.7799,38.73077) | 2024-10-08 00:03 | 296.6 | 0.61 | Orta | Gece |
| [37.78531, 38.35199](https://www.google.com/maps?q=37.78531,38.35199) | 2024-10-08 00:03 | 297.57 | 0.28 | Orta | Gece |
| [37.86425, 29.37118](https://www.google.com/maps?q=37.86425,29.37118) | 2024-10-08 00:03 | 303.13 | 0.94 | Orta | Gece |
| [37.89786, 30.49359](https://www.google.com/maps?q=37.89786,30.49359) | 2024-10-08 00:03 | 295.95 | 0.87 | Orta | Gece |
| [38.06315, 40.9088](https://www.google.com/maps?q=38.06315,40.9088) | 2024-10-08 00:03 | 309.39 | 2.03 | Orta | Gece |
| [38.06373, 40.88447](https://www.google.com/maps?q=38.06373,40.88447) | 2024-10-08 00:03 | 297.64 | 2.38 | Orta | Gece |
| [38.06471, 40.90339](https://www.google.com/maps?q=38.06471,40.90339) | 2024-10-08 00:03 | 313.2 | 3.57 | Orta | Gece |
| [38.06538, 40.87875](https://www.google.com/maps?q=38.06538,40.87875) | 2024-10-08 00:03 | 296.27 | 2.33 | Orta | Gece |
| [38.06697, 40.87328](https://www.google.com/maps?q=38.06697,40.87328) | 2024-10-08 00:03 | 325.09 | 2.33 | Orta | Gece |
| [38.07104, 40.88147](https://www.google.com/maps?q=38.07104,40.88147) | 2024-10-08 00:03 | 317.57 | 2.33 | Orta | Gece |
| [38.29308, 36.9427](https://www.google.com/maps?q=38.29308,36.9427) | 2024-10-08 00:03 | 296.52 | 0.62 | Orta | Gece |
| [38.29585, 36.9448](https://www.google.com/maps?q=38.29585,36.9448) | 2024-10-08 00:03 | 299.2 | 0.95 | Orta | Gece |
| [38.42796, 27.21742](https://www.google.com/maps?q=38.42796,27.21742) | 2024-10-08 00:03 | 319.31 | 1.98 | Orta | Gece |
| [38.4551, 27.26081](https://www.google.com/maps?q=38.4551,27.26081) | 2024-10-08 00:03 | 306.81 | 0.6 | Orta | Gece |
| [38.66078, 30.61689](https://www.google.com/maps?q=38.66078,30.61689) | 2024-10-08 00:03 | 308.0 | 0.84 | Orta | Gece |
| [38.66336, 39.23138](https://www.google.com/maps?q=38.66336,39.23138) | 2024-10-08 00:03 | 296.31 | 2.17 | Orta | Gece |
| [38.68014, 27.76727](https://www.google.com/maps?q=38.68014,27.76727) | 2024-10-08 00:03 | 299.28 | 0.39 | Orta | Gece |
| [38.73703, 26.94855](https://www.google.com/maps?q=38.73703,26.94855) | 2024-10-08 00:03 | 309.62 | 1.79 | Orta | Gece |
| [38.73772, 26.94418](https://www.google.com/maps?q=38.73772,26.94418) | 2024-10-08 00:03 | 326.82 | 1.79 | Orta | Gece |
| [38.73978, 26.93108](https://www.google.com/maps?q=38.73978,26.93108) | 2024-10-08 00:03 | 330.05 | 3.43 | Orta | Gece |
| [38.74151, 26.96334](https://www.google.com/maps?q=38.74151,26.96334) | 2024-10-08 00:03 | 315.7 | 0.81 | Orta | Gece |
| [38.74306, 26.93192](https://www.google.com/maps?q=38.74306,26.93192) | 2024-10-08 00:03 | 303.89 | 0.71 | Orta | Gece |
| [38.74754, 26.9467](https://www.google.com/maps?q=38.74754,26.9467) | 2024-10-08 00:03 | 307.63 | 0.84 | Orta | Gece |
| [38.75219, 26.93881](https://www.google.com/maps?q=38.75219,26.93881) | 2024-10-08 00:03 | 306.18 | 0.71 | Orta | Gece |
| [39.11199, 27.59394](https://www.google.com/maps?q=39.11199,27.59394) | 2024-10-08 00:03 | 306.34 | 0.79 | Orta | Gece |
| [39.11357, 27.52103](https://www.google.com/maps?q=39.11357,27.52103) | 2024-10-08 00:03 | 299.26 | 0.85 | Orta | Gece |
| [39.11499, 27.51225](https://www.google.com/maps?q=39.11499,27.51225) | 2024-10-08 00:03 | 300.01 | 0.5 | Orta | Gece |
| [39.11819, 37.46764](https://www.google.com/maps?q=39.11819,37.46764) | 2024-10-08 00:03 | 298.94 | 0.89 | Orta | Gece |
| [39.16731, 27.63191](https://www.google.com/maps?q=39.16731,27.63191) | 2024-10-08 00:03 | 310.45 | 1.07 | Orta | Gece |
| [39.16803, 27.62751](https://www.google.com/maps?q=39.16803,27.62751) | 2024-10-08 00:03 | 299.71 | 0.43 | Orta | Gece |
| [39.18214, 27.49813](https://www.google.com/maps?q=39.18214,27.49813) | 2024-10-08 00:03 | 307.28 | 0.86 | Orta | Gece |
| [39.46936, 35.1744](https://www.google.com/maps?q=39.46936,35.1744) | 2024-10-08 00:03 | 303.61 | 1.15 | Orta | Gece |
| [39.48436, 30.04043](https://www.google.com/maps?q=39.48436,30.04043) | 2024-10-08 00:03 | 315.18 | 1.84 | Orta | Gece |
| [39.60892, 27.87932](https://www.google.com/maps?q=39.60892,27.87932) | 2024-10-08 00:03 | 299.38 | 0.4 | Orta | Gece |
| [39.74612, 30.19887](https://www.google.com/maps?q=39.74612,30.19887) | 2024-10-08 00:03 | 299.98 | 0.61 | Orta | Gece |
| [39.83701, 30.30221](https://www.google.com/maps?q=39.83701,30.30221) | 2024-10-08 00:03 | 300.73 | 1.31 | Orta | Gece |
| [39.85788, 32.29027](https://www.google.com/maps?q=39.85788,32.29027) | 2024-10-08 00:03 | 303.34 | 1.27 | Orta | Gece |
| [39.86702, 26.24467](https://www.google.com/maps?q=39.86702,26.24467) | 2024-10-08 00:03 | 325.68 | 2.51 | Orta | Gece |
| [39.94481, 33.18868](https://www.google.com/maps?q=39.94481,33.18868) | 2024-10-08 00:03 | 296.46 | 0.96 | Orta | Gece |
| [40.04987, 32.64972](https://www.google.com/maps?q=40.04987,32.64972) | 2024-10-08 00:03 | 298.2 | 0.79 | Orta | Gece |
| [40.08284, 32.798](https://www.google.com/maps?q=40.08284,32.798) | 2024-10-08 00:03 | 297.99 | 0.63 | Orta | Gece |
| [40.26188, 30.04204](https://www.google.com/maps?q=40.26188,30.04204) | 2024-10-08 00:03 | 298.92 | 0.71 | Orta | Gece |
| [40.44387, 27.13922](https://www.google.com/maps?q=40.44387,27.13922) | 2024-10-08 00:03 | 316.51 | 2.23 | Orta | Gece |
| [41.02062, 28.55376](https://www.google.com/maps?q=41.02062,28.55376) | 2024-10-08 00:03 | 316.43 | 1.95 | Orta | Gece |
| [41.25638, 31.41478](https://www.google.com/maps?q=41.25638,31.41478) | 2024-10-08 00:03 | 328.66 | 2.8 | Orta | Gece |
| [41.26135, 31.42748](https://www.google.com/maps?q=41.26135,31.42748) | 2024-10-08 00:03 | 303.36 | 0.98 | Orta | Gece |
| [41.2658, 31.42345](https://www.google.com/maps?q=41.2658,31.42345) | 2024-10-08 00:03 | 314.75 | 2.67 | Orta | Gece |
| [41.63587, 27.50676](https://www.google.com/maps?q=41.63587,27.50676) | 2024-10-08 00:03 | 303.33 | 0.86 | Orta | Gece |
| [41.79751, 26.70331](https://www.google.com/maps?q=41.79751,26.70331) | 2024-10-08 00:03 | 299.5 | 0.55 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
