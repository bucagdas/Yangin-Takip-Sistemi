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
### Son Güncelleme: 2024-10-10 12:34:41 (UTC)

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
| [36.26289, 33.72833](https://www.google.com/maps?q=36.26289,33.72833) | 2024-10-10 10:21 | 330.7 | 3.33 | Orta | Gündüz |
| [36.72987, 36.21223](https://www.google.com/maps?q=36.72987,36.21223) | 2024-10-10 10:21 | 333.75 | 4.2 | Düşük | Gündüz |
| [36.79001, 39.38984](https://www.google.com/maps?q=36.79001,39.38984) | 2024-10-10 10:21 | 336.89 | 3.04 | Orta | Gündüz |
| [36.9268, 38.54788](https://www.google.com/maps?q=36.9268,38.54788) | 2024-10-10 10:21 | 340.35 | 2.67 | Orta | Gündüz |
| [36.97504, 38.74973](https://www.google.com/maps?q=36.97504,38.74973) | 2024-10-10 10:21 | 339.62 | 3.47 | Düşük | Gündüz |
| [37.08947, 41.38722](https://www.google.com/maps?q=37.08947,41.38722) | 2024-10-10 10:21 | 337.55 | 6.1 | Düşük | Gündüz |
| [37.09635, 35.57116](https://www.google.com/maps?q=37.09635,35.57116) | 2024-10-10 10:21 | 337.24 | 2.08 | Düşük | Gündüz |
| [37.09655, 39.65257](https://www.google.com/maps?q=37.09655,39.65257) | 2024-10-10 10:21 | 338.95 | 8.31 | Düşük | Gündüz |
| [37.13372, 36.08509](https://www.google.com/maps?q=37.13372,36.08509) | 2024-10-10 10:21 | 340.89 | 3.52 | Orta | Gündüz |
| [37.18684, 37.38868](https://www.google.com/maps?q=37.18684,37.38868) | 2024-10-10 10:21 | 336.81 | 3.54 | Orta | Gündüz |
| [37.18877, 35.13963](https://www.google.com/maps?q=37.18877,35.13963) | 2024-10-10 10:21 | 336.63 | 4.51 | Düşük | Gündüz |
| [37.22903, 40.13427](https://www.google.com/maps?q=37.22903,40.13427) | 2024-10-10 10:21 | 338.05 | 2.01 | Orta | Gündüz |
| [37.31075, 36.84414](https://www.google.com/maps?q=37.31075,36.84414) | 2024-10-10 10:21 | 337.0 | 2.1 | Orta | Gündüz |
| [37.37216, 37.03954](https://www.google.com/maps?q=37.37216,37.03954) | 2024-10-10 10:21 | 341.73 | 4.17 | Orta | Gündüz |
| [37.38643, 38.82464](https://www.google.com/maps?q=37.38643,38.82464) | 2024-10-10 10:21 | 343.83 | 3.54 | Orta | Gündüz |
| [37.45409, 37.00867](https://www.google.com/maps?q=37.45409,37.00867) | 2024-10-10 10:21 | 334.92 | 2.08 | Düşük | Gündüz |
| [37.47673, 38.72869](https://www.google.com/maps?q=37.47673,38.72869) | 2024-10-10 10:21 | 344.66 | 6.04 | Orta | Gündüz |
| [37.48808, 34.15922](https://www.google.com/maps?q=37.48808,34.15922) | 2024-10-10 10:21 | 347.34 | 9.58 | Orta | Gündüz |
| [37.49356, 35.73114](https://www.google.com/maps?q=37.49356,35.73114) | 2024-10-10 10:21 | 335.67 | 1.74 | Orta | Gündüz |
| [37.51387, 41.28205](https://www.google.com/maps?q=37.51387,41.28205) | 2024-10-10 10:21 | 354.6 | 13.28 | Orta | Gündüz |
| [37.51448, 41.28676](https://www.google.com/maps?q=37.51448,41.28676) | 2024-10-10 10:21 | 341.42 | 3.99 | Düşük | Gündüz |
| [37.5151, 39.05069](https://www.google.com/maps?q=37.5151,39.05069) | 2024-10-10 10:21 | 350.43 | 4.15 | Orta | Gündüz |
| [37.54821, 37.02257](https://www.google.com/maps?q=37.54821,37.02257) | 2024-10-10 10:21 | 340.84 | 1.82 | Orta | Gündüz |
| [37.55592, 38.24891](https://www.google.com/maps?q=37.55592,38.24891) | 2024-10-10 10:21 | 334.74 | 3.65 | Düşük | Gündüz |
| [37.55605, 36.81648](https://www.google.com/maps?q=37.55605,36.81648) | 2024-10-10 10:21 | 335.28 | 2.16 | Orta | Gündüz |
| [37.56466, 37.41554](https://www.google.com/maps?q=37.56466,37.41554) | 2024-10-10 10:21 | 335.27 | 4.53 | Düşük | Gündüz |
| [37.60355, 37.4423](https://www.google.com/maps?q=37.60355,37.4423) | 2024-10-10 10:21 | 339.47 | 2.88 | Orta | Gündüz |
| [37.60427, 37.44665](https://www.google.com/maps?q=37.60427,37.44665) | 2024-10-10 10:21 | 334.52 | 1.49 | Orta | Gündüz |
| [37.61496, 40.27728](https://www.google.com/maps?q=37.61496,40.27728) | 2024-10-10 10:21 | 338.05 | 2.68 | Orta | Gündüz |
| [37.6548, 38.62954](https://www.google.com/maps?q=37.6548,38.62954) | 2024-10-10 10:21 | 335.07 | 2.21 | Orta | Gündüz |
| [37.65744, 40.45858](https://www.google.com/maps?q=37.65744,40.45858) | 2024-10-10 10:21 | 338.27 | 3.84 | Orta | Gündüz |
| [37.6581, 38.62875](https://www.google.com/maps?q=37.6581,38.62875) | 2024-10-10 10:21 | 339.62 | 3.31 | Orta | Gündüz |
| [37.69436, 40.27132](https://www.google.com/maps?q=37.69436,40.27132) | 2024-10-10 10:21 | 348.8 | 16.73 | Orta | Gündüz |
| [37.70058, 37.45567](https://www.google.com/maps?q=37.70058,37.45567) | 2024-10-10 10:21 | 330.22 | 1.33 | Orta | Gündüz |
| [37.71106, 40.51911](https://www.google.com/maps?q=37.71106,40.51911) | 2024-10-10 10:21 | 338.09 | 2.06 | Orta | Gündüz |
| [37.71444, 40.51839](https://www.google.com/maps?q=37.71444,40.51839) | 2024-10-10 10:21 | 348.85 | 5.28 | Orta | Gündüz |
| [37.73333, 38.45448](https://www.google.com/maps?q=37.73333,38.45448) | 2024-10-10 10:21 | 345.58 | 4.03 | Orta | Gündüz |
| [37.75, 38.74232](https://www.google.com/maps?q=37.75,38.74232) | 2024-10-10 10:21 | 336.11 | 1.48 | Orta | Gündüz |
| [37.76506, 39.22773](https://www.google.com/maps?q=37.76506,39.22773) | 2024-10-10 10:21 | 338.94 | 5.15 | Orta | Gündüz |
| [37.77425, 38.85779](https://www.google.com/maps?q=37.77425,38.85779) | 2024-10-10 10:21 | 339.43 | 3.29 | Orta | Gündüz |
| [37.78084, 38.8562](https://www.google.com/maps?q=37.78084,38.8562) | 2024-10-10 10:21 | 334.6 | 1.29 | Düşük | Gündüz |
| [37.8008, 38.14705](https://www.google.com/maps?q=37.8008,38.14705) | 2024-10-10 10:21 | 338.42 | 3.95 | Düşük | Gündüz |
| [37.80342, 38.14191](https://www.google.com/maps?q=37.80342,38.14191) | 2024-10-10 10:21 | 340.89 | 3.95 | Orta | Gündüz |
| [37.82481, 40.0591](https://www.google.com/maps?q=37.82481,40.0591) | 2024-10-10 10:21 | 339.46 | 2.39 | Orta | Gündüz |
| [37.87048, 40.28204](https://www.google.com/maps?q=37.87048,40.28204) | 2024-10-10 10:21 | 337.04 | 4.72 | Düşük | Gündüz |
| [37.87309, 38.81775](https://www.google.com/maps?q=37.87309,38.81775) | 2024-10-10 10:21 | 337.09 | 2.14 | Orta | Gündüz |
| [37.94069, 40.36447](https://www.google.com/maps?q=37.94069,40.36447) | 2024-10-10 10:21 | 338.57 | 3.71 | Düşük | Gündüz |
| [37.97506, 40.66805](https://www.google.com/maps?q=37.97506,40.66805) | 2024-10-10 10:21 | 347.69 | 4.93 | Orta | Gündüz |
| [37.97846, 40.6673](https://www.google.com/maps?q=37.97846,40.6673) | 2024-10-10 10:21 | 342.19 | 5.12 | Düşük | Gündüz |
| [37.98247, 40.67118](https://www.google.com/maps?q=37.98247,40.67118) | 2024-10-10 10:21 | 347.81 | 27.96 | Düşük | Gündüz |
| [37.98586, 40.67043](https://www.google.com/maps?q=37.98586,40.67043) | 2024-10-10 10:21 | 342.02 | 6.92 | Orta | Gündüz |
| [37.98661, 41.12757](https://www.google.com/maps?q=37.98661,41.12757) | 2024-10-10 10:21 | 349.62 | 11.11 | Orta | Gündüz |
| [37.98953, 40.64597](https://www.google.com/maps?q=37.98953,40.64597) | 2024-10-10 10:21 | 341.61 | 3.87 | Düşük | Gündüz |
| [37.99005, 41.12685](https://www.google.com/maps?q=37.99005,41.12685) | 2024-10-10 10:21 | 339.45 | 4.19 | Orta | Gündüz |
| [37.99015, 40.65055](https://www.google.com/maps?q=37.99015,40.65055) | 2024-10-10 10:21 | 341.8 | 4.31 | Düşük | Gündüz |
| [38.00942, 41.11288](https://www.google.com/maps?q=38.00942,41.11288) | 2024-10-10 10:21 | 336.87 | 3.55 | Düşük | Gündüz |
| [38.01005, 41.11771](https://www.google.com/maps?q=38.01005,41.11771) | 2024-10-10 10:21 | 353.08 | 10.63 | Orta | Gündüz |
| [38.01266, 40.9231](https://www.google.com/maps?q=38.01266,40.9231) | 2024-10-10 10:21 | 344.84 | 6.8 | Orta | Gündüz |
| [38.02139, 40.1153](https://www.google.com/maps?q=38.02139,40.1153) | 2024-10-10 10:21 | 341.7 | 2.0 | Orta | Gündüz |
| [38.04004, 40.19955](https://www.google.com/maps?q=38.04004,40.19955) | 2024-10-10 10:21 | 349.62 | 25.34 | Orta | Gündüz |
| [38.05202, 39.81021](https://www.google.com/maps?q=38.05202,39.81021) | 2024-10-10 10:21 | 339.17 | 2.76 | Orta | Gündüz |
| [38.06752, 41.00014](https://www.google.com/maps?q=38.06752,41.00014) | 2024-10-10 10:21 | 350.71 | 4.98 | Orta | Gündüz |
| [38.06973, 40.99007](https://www.google.com/maps?q=38.06973,40.99007) | 2024-10-10 10:21 | 337.63 | 3.76 | Orta | Gündüz |
| [38.07095, 40.99941](https://www.google.com/maps?q=38.07095,40.99941) | 2024-10-10 10:21 | 336.16 | 4.98 | Düşük | Gündüz |
| [38.07155, 41.00411](https://www.google.com/maps?q=38.07155,41.00411) | 2024-10-10 10:21 | 341.13 | 4.98 | Orta | Gündüz |
| [38.08244, 41.0066](https://www.google.com/maps?q=38.08244,41.0066) | 2024-10-10 10:21 | 338.37 | 55.5 | Düşük | Gündüz |
| [38.0871, 41.01531](https://www.google.com/maps?q=38.0871,41.01531) | 2024-10-10 10:21 | 334.5 | 65.59 | Düşük | Gündüz |
| [38.0884, 40.47483](https://www.google.com/maps?q=38.0884,40.47483) | 2024-10-10 10:21 | 340.65 | 2.48 | Orta | Gündüz |
| [38.09994, 40.97882](https://www.google.com/maps?q=38.09994,40.97882) | 2024-10-10 10:21 | 332.3 | 1.58 | Düşük | Gündüz |
| [38.12546, 40.90566](https://www.google.com/maps?q=38.12546,40.90566) | 2024-10-10 10:21 | 339.28 | 2.77 | Orta | Gündüz |
| [38.17984, 40.45697](https://www.google.com/maps?q=38.17984,40.45697) | 2024-10-10 10:21 | 367.0 | 7.2 | Yüksek | Gündüz |
| [38.18385, 40.46085](https://www.google.com/maps?q=38.18385,40.46085) | 2024-10-10 10:21 | 342.24 | 7.04 | Orta | Gündüz |
| [38.1986, 40.59517](https://www.google.com/maps?q=38.1986,40.59517) | 2024-10-10 10:21 | 339.58 | 2.47 | Düşük | Gündüz |
| [38.202, 40.59443](https://www.google.com/maps?q=38.202,40.59443) | 2024-10-10 10:21 | 337.88 | 2.47 | Düşük | Gündüz |
| [38.20262, 40.59903](https://www.google.com/maps?q=38.20262,40.59903) | 2024-10-10 10:21 | 343.9 | 6.25 | Orta | Gündüz |
| [38.23363, 38.93761](https://www.google.com/maps?q=38.23363,38.93761) | 2024-10-10 10:21 | 331.85 | 2.6 | Orta | Gündüz |
| [37.39585, 32.01898](https://www.google.com/maps?q=37.39585,32.01898) | 2024-10-10 10:24 | 343.27 | 1.78 | Orta | Gündüz |
| [37.67373, 31.82346](https://www.google.com/maps?q=37.67373,31.82346) | 2024-10-10 10:24 | 337.71 | 2.94 | Orta | Gündüz |
| [37.74292, 31.73315](https://www.google.com/maps?q=37.74292,31.73315) | 2024-10-10 10:24 | 333.37 | 2.39 | Orta | Gündüz |
| [37.89223, 34.87896](https://www.google.com/maps?q=37.89223,34.87896) | 2024-10-10 10:24 | 342.24 | 11.32 | Orta | Gündüz |
| [38.10118, 37.09452](https://www.google.com/maps?q=38.10118,37.09452) | 2024-10-10 10:24 | 334.96 | 3.31 | Orta | Gündüz |
| [38.15404, 37.0261](https://www.google.com/maps?q=38.15404,37.0261) | 2024-10-10 10:24 | 333.49 | 8.4 | Orta | Gündüz |
| [38.15477, 37.03056](https://www.google.com/maps?q=38.15477,37.03056) | 2024-10-10 10:24 | 353.07 | 8.4 | Orta | Gündüz |
| [38.16325, 37.019](https://www.google.com/maps?q=38.16325,37.019) | 2024-10-10 10:24 | 341.5 | 9.58 | Orta | Gündüz |
| [38.16399, 37.02345](https://www.google.com/maps?q=38.16399,37.02345) | 2024-10-10 10:24 | 342.82 | 12.27 | Orta | Gündüz |
| [38.16732, 37.02257](https://www.google.com/maps?q=38.16732,37.02257) | 2024-10-10 10:24 | 337.24 | 12.27 | Orta | Gündüz |
| [38.17321, 37.01635](https://www.google.com/maps?q=38.17321,37.01635) | 2024-10-10 10:24 | 334.4 | 2.43 | Orta | Gündüz |
| [38.17395, 37.02081](https://www.google.com/maps?q=38.17395,37.02081) | 2024-10-10 10:24 | 344.87 | 11.47 | Orta | Gündüz |
| [38.21848, 37.10189](https://www.google.com/maps?q=38.21848,37.10189) | 2024-10-10 10:24 | 349.44 | 4.17 | Orta | Gündüz |
| [38.21921, 37.10634](https://www.google.com/maps?q=38.21921,37.10634) | 2024-10-10 10:24 | 335.3 | 4.17 | Orta | Gündüz |
| [38.22801, 36.17602](https://www.google.com/maps?q=38.22801,36.17602) | 2024-10-10 10:24 | 340.39 | 6.82 | Orta | Gündüz |
| [38.22881, 36.18063](https://www.google.com/maps?q=38.22881,36.18063) | 2024-10-10 10:24 | 343.44 | 6.82 | Orta | Gündüz |
| [38.23218, 36.17971](https://www.google.com/maps?q=38.23218,36.17971) | 2024-10-10 10:24 | 334.67 | 4.05 | Düşük | Gündüz |
| [38.2336, 37.08862](https://www.google.com/maps?q=38.2336,37.08862) | 2024-10-10 10:24 | 341.86 | 8.59 | Orta | Gündüz |
| [38.23618, 37.0833](https://www.google.com/maps?q=38.23618,37.0833) | 2024-10-10 10:24 | 335.37 | 2.86 | Orta | Gündüz |
| [38.23692, 37.08775](https://www.google.com/maps?q=38.23692,37.08775) | 2024-10-10 10:24 | 348.44 | 21.7 | Orta | Gündüz |
| [38.23765, 37.09221](https://www.google.com/maps?q=38.23765,37.09221) | 2024-10-10 10:24 | 336.26 | 21.7 | Orta | Gündüz |
| [38.23954, 37.23058](https://www.google.com/maps?q=38.23954,37.23058) | 2024-10-10 10:24 | 337.45 | 4.36 | Orta | Gündüz |
| [38.24896, 37.14019](https://www.google.com/maps?q=38.24896,37.14019) | 2024-10-10 10:24 | 339.17 | 2.72 | Orta | Gündüz |
| [38.24995, 37.13646](https://www.google.com/maps?q=38.24995,37.13646) | 2024-10-10 10:24 | 344.33 | 64.64 | Düşük | Gündüz |
| [38.25069, 37.14089](https://www.google.com/maps?q=38.25069,37.14089) | 2024-10-10 10:24 | 333.13 | 12.33 | Düşük | Gündüz |
| [38.25623, 37.11166](https://www.google.com/maps?q=38.25623,37.11166) | 2024-10-10 10:24 | 338.55 | 12.11 | Düşük | Gündüz |
| [38.2647, 37.10013](https://www.google.com/maps?q=38.2647,37.10013) | 2024-10-10 10:24 | 344.26 | 11.27 | Orta | Gündüz |
| [38.26801, 37.09925](https://www.google.com/maps?q=38.26801,37.09925) | 2024-10-10 10:24 | 339.59 | 11.27 | Orta | Gündüz |
| [38.28019, 37.0682](https://www.google.com/maps?q=38.28019,37.0682) | 2024-10-10 10:24 | 343.36 | 23.63 | Düşük | Gündüz |
| [38.28444, 35.10292](https://www.google.com/maps?q=38.28444,35.10292) | 2024-10-10 10:24 | 338.86 | 2.15 | Orta | Gündüz |
| [38.28828, 37.07534](https://www.google.com/maps?q=38.28828,37.07534) | 2024-10-10 10:24 | 334.71 | 3.39 | Orta | Gündüz |
| [38.29233, 37.07891](https://www.google.com/maps?q=38.29233,37.07891) | 2024-10-10 10:24 | 335.71 | 3.39 | Orta | Gündüz |
| [38.29486, 37.11533](https://www.google.com/maps?q=38.29486,37.11533) | 2024-10-10 10:24 | 332.29 | 4.12 | Düşük | Gündüz |
| [38.29745, 37.11002](https://www.google.com/maps?q=38.29745,37.11002) | 2024-10-10 10:24 | 333.5 | 4.12 | Düşük | Gündüz |
| [38.30122, 38.28534](https://www.google.com/maps?q=38.30122,38.28534) | 2024-10-10 10:24 | 347.75 | 7.92 | Orta | Gündüz |
| [38.38317, 36.9259](https://www.google.com/maps?q=38.38317,36.9259) | 2024-10-10 10:24 | 344.91 | 6.99 | Orta | Gündüz |
| [38.38649, 36.92502](https://www.google.com/maps?q=38.38649,36.92502) | 2024-10-10 10:24 | 344.09 | 7.73 | Orta | Gündüz |
| [38.3895, 32.59866](https://www.google.com/maps?q=38.3895,32.59866) | 2024-10-10 10:24 | 342.22 | 39.46 | Orta | Gündüz |
| [38.38953, 32.60017](https://www.google.com/maps?q=38.38953,32.60017) | 2024-10-10 10:24 | 337.59 | 29.29 | Düşük | Gündüz |
| [38.42006, 34.68941](https://www.google.com/maps?q=38.42006,34.68941) | 2024-10-10 10:24 | 350.52 | 8.73 | Orta | Gündüz |
| [38.43308, 37.84599](https://www.google.com/maps?q=38.43308,37.84599) | 2024-10-10 10:24 | 338.59 | 3.85 | Orta | Gündüz |
| [38.43592, 36.97266](https://www.google.com/maps?q=38.43592,36.97266) | 2024-10-10 10:24 | 337.94 | 4.27 | Orta | Gündüz |
| [38.45997, 35.98904](https://www.google.com/maps?q=38.45997,35.98904) | 2024-10-10 10:24 | 338.68 | 3.85 | Orta | Gündüz |
| [38.53683, 38.22998](https://www.google.com/maps?q=38.53683,38.22998) | 2024-10-10 10:24 | 330.73 | 1.68 | Orta | Gündüz |
| [38.54536, 38.21877](https://www.google.com/maps?q=38.54536,38.21877) | 2024-10-10 10:24 | 333.07 | 2.13 | Orta | Gündüz |
| [38.56008, 39.19557](https://www.google.com/maps?q=38.56008,39.19557) | 2024-10-10 10:24 | 367.0 | 14.61 | Yüksek | Gündüz |
| [38.56064, 39.22291](https://www.google.com/maps?q=38.56064,39.22291) | 2024-10-10 10:24 | 342.88 | 6.83 | Orta | Gündüz |
| [38.56212, 35.16586](https://www.google.com/maps?q=38.56212,35.16586) | 2024-10-10 10:24 | 347.57 | 3.54 | Orta | Gündüz |
| [38.56267, 35.16778](https://www.google.com/maps?q=38.56267,35.16778) | 2024-10-10 10:24 | 347.11 | 6.96 | Orta | Gündüz |
| [38.84315, 39.02652](https://www.google.com/maps?q=38.84315,39.02652) | 2024-10-10 10:24 | 338.49 | 4.27 | Orta | Gündüz |
| [38.84647, 36.04435](https://www.google.com/maps?q=38.84647,36.04435) | 2024-10-10 10:24 | 334.23 | 3.85 | Orta | Gündüz |
| [38.85065, 36.04812](https://www.google.com/maps?q=38.85065,36.04812) | 2024-10-10 10:24 | 345.17 | 6.4 | Orta | Gündüz |
| [38.87343, 36.30256](https://www.google.com/maps?q=38.87343,36.30256) | 2024-10-10 10:24 | 332.12 | 2.56 | Orta | Gündüz |
| [38.88915, 36.85917](https://www.google.com/maps?q=38.88915,36.85917) | 2024-10-10 10:24 | 330.44 | 51.04 | Düşük | Gündüz |
| [38.88989, 36.86364](https://www.google.com/maps?q=38.88989,36.86364) | 2024-10-10 10:24 | 367.0 | 51.04 | Düşük | Gündüz |
| [38.89454, 36.64123](https://www.google.com/maps?q=38.89454,36.64123) | 2024-10-10 10:24 | 338.21 | 4.62 | Orta | Gündüz |
| [38.9373, 37.65936](https://www.google.com/maps?q=38.9373,37.65936) | 2024-10-10 10:24 | 331.77 | 2.98 | Düşük | Gündüz |
| [38.93799, 37.66378](https://www.google.com/maps?q=38.93799,37.66378) | 2024-10-10 10:24 | 339.84 | 2.98 | Orta | Gündüz |
| [38.94128, 37.66293](https://www.google.com/maps?q=38.94128,37.66293) | 2024-10-10 10:24 | 334.08 | 3.56 | Orta | Gündüz |
| [39.00619, 37.01176](https://www.google.com/maps?q=39.00619,37.01176) | 2024-10-10 10:24 | 335.38 | 4.63 | Orta | Gündüz |
| [39.07338, 34.9043](https://www.google.com/maps?q=39.07338,34.9043) | 2024-10-10 10:24 | 339.36 | 2.1 | Orta | Gündüz |
| [39.13319, 38.201](https://www.google.com/maps?q=39.13319,38.201) | 2024-10-10 10:24 | 333.65 | 2.87 | Orta | Gündüz |
| [39.2212, 36.6793](https://www.google.com/maps?q=39.2212,36.6793) | 2024-10-10 10:24 | 334.13 | 3.72 | Orta | Gündüz |
| [40.03582, 44.24704](https://www.google.com/maps?q=40.03582,44.24704) | 2024-10-10 10:24 | 329.89 | 2.32 | Orta | Gündüz |
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
| [37.13815, 41.64458](https://www.google.com/maps?q=37.13815,41.64458) | 2024-10-10 09:07 | 350.0 | 10.38 | Orta | Gündüz |
| [37.14025, 41.65144](https://www.google.com/maps?q=37.14025,41.65144) | 2024-10-10 09:07 | 367.0 | 10.38 | Yüksek | Gündüz |
| [37.61632, 40.27496](https://www.google.com/maps?q=37.61632,40.27496) | 2024-10-10 09:07 | 343.3 | 9.83 | Orta | Gündüz |
| [37.61675, 40.27494](https://www.google.com/maps?q=37.61675,40.27494) | 2024-10-10 09:07 | 347.52 | 7.72 | Orta | Gündüz |
| [37.61922, 42.37705](https://www.google.com/maps?q=37.61922,42.37705) | 2024-10-10 09:07 | 331.83 | 2.74 | Orta | Gündüz |
| [37.86951, 40.28439](https://www.google.com/maps?q=37.86951,40.28439) | 2024-10-10 09:07 | 334.98 | 5.64 | Orta | Gündüz |
| [38.00246, 40.63558](https://www.google.com/maps?q=38.00246,40.63558) | 2024-10-10 09:07 | 334.7 | 5.83 | Orta | Gündüz |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
