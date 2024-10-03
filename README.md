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
Bu script verilerin nasıl kullanılabileceğine bir örnektir. Script, çekilen son verileri işleyerek, **README.md** dosyasına bir tablo halinde kaydeder. Tabloda yangınların enlem, boylam, sıcaklık, güven seviyesi ve gündüz/gece bilgileri yer alır. Güncellemeler her çalıştırıldığında otomatik olarak yapılır ve dosyanın üzerine yazılır, böylece en güncel veriler her zaman README.md dosyasında bulunur.

## Son Yangın Verileri
### Son Güncelleme: 2024-10-03 11:27:56 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.73819, 26.9503](https://www.google.com/maps?q=38.73819,26.9503) | 2024-10-03 01:13 | 298.7 | 1.46 | Orta | Gece |
| [38.7401, 26.94492](https://www.google.com/maps?q=38.7401,26.94492) | 2024-10-03 01:13 | 297.34 | 1.47 | Orta | Gece |
| [37.12869, 40.26756](https://www.google.com/maps?q=37.12869,40.26756) | 2024-10-03 09:13 | 334.41 | 6.85 | Orta | Gündüz |
| [37.13634, 41.76789](https://www.google.com/maps?q=37.13634,41.76789) | 2024-10-03 09:13 | 334.45 | 2.42 | Orta | Gündüz |
| [37.14835, 41.71803](https://www.google.com/maps?q=37.14835,41.71803) | 2024-10-03 09:13 | 337.01 | 2.83 | Orta | Gündüz |
| [37.15191, 38.30959](https://www.google.com/maps?q=37.15191,38.30959) | 2024-10-03 09:13 | 330.09 | 4.57 | Orta | Gündüz |
| [37.18744, 41.74007](https://www.google.com/maps?q=37.18744,41.74007) | 2024-10-03 09:13 | 336.43 | 2.54 | Orta | Gündüz |
| [37.18754, 41.74012](https://www.google.com/maps?q=37.18754,41.74012) | 2024-10-03 09:13 | 335.78 | 3.29 | Orta | Gündüz |
| [37.20907, 41.76926](https://www.google.com/maps?q=37.20907,41.76926) | 2024-10-03 09:13 | 330.97 | 4.31 | Düşük | Gündüz |
| [37.21062, 41.77523](https://www.google.com/maps?q=37.21062,41.77523) | 2024-10-03 09:13 | 330.31 | 5.17 | Düşük | Gündüz |
| [37.21074, 41.77505](https://www.google.com/maps?q=37.21074,41.77505) | 2024-10-03 09:13 | 330.52 | 8.94 | Düşük | Gündüz |
| [37.21227, 41.78104](https://www.google.com/maps?q=37.21227,41.78104) | 2024-10-03 09:13 | 333.2 | 5.9 | Düşük | Gündüz |
| [37.21241, 41.78082](https://www.google.com/maps?q=37.21241,41.78082) | 2024-10-03 09:13 | 334.46 | 8.94 | Orta | Gündüz |
| [37.21491, 41.76675](https://www.google.com/maps?q=37.21491,41.76675) | 2024-10-03 09:13 | 342.09 | 4.31 | Orta | Gündüz |
| [37.21826, 41.77833](https://www.google.com/maps?q=37.21826,41.77833) | 2024-10-03 09:13 | 344.43 | 8.94 | Orta | Gündüz |
| [37.21994, 41.78416](https://www.google.com/maps?q=37.21994,41.78416) | 2024-10-03 09:13 | 367.0 | 45.7 | Yüksek | Gündüz |
| [37.22903, 39.20626](https://www.google.com/maps?q=37.22903,39.20626) | 2024-10-03 09:13 | 334.65 | 4.11 | Orta | Gündüz |
| [37.23703, 39.94902](https://www.google.com/maps?q=37.23703,39.94902) | 2024-10-03 09:13 | 336.12 | 5.02 | Orta | Gündüz |
| [37.34816, 42.67153](https://www.google.com/maps?q=37.34816,42.67153) | 2024-10-03 09:13 | 341.57 | 2.91 | Orta | Gündüz |
| [37.44964, 39.55047](https://www.google.com/maps?q=37.44964,39.55047) | 2024-10-03 09:13 | 342.69 | 7.0 | Orta | Gündüz |
| [37.45387, 39.55024](https://www.google.com/maps?q=37.45387,39.55024) | 2024-10-03 09:13 | 356.71 | 15.28 | Orta | Gündüz |
| [37.45607, 39.54771](https://www.google.com/maps?q=37.45607,39.54771) | 2024-10-03 09:13 | 335.09 | 3.82 | Düşük | Gündüz |
| [37.49263, 38.63774](https://www.google.com/maps?q=37.49263,38.63774) | 2024-10-03 09:13 | 352.41 | 10.95 | Orta | Gündüz |
| [37.49322, 38.63807](https://www.google.com/maps?q=37.49322,38.63807) | 2024-10-03 09:13 | 352.89 | 10.49 | Orta | Gündüz |
| [37.56564, 39.44144](https://www.google.com/maps?q=37.56564,39.44144) | 2024-10-03 09:13 | 357.11 | 12.29 | Orta | Gündüz |
| [37.57595, 38.33802](https://www.google.com/maps?q=37.57595,38.33802) | 2024-10-03 09:13 | 343.23 | 6.6 | Orta | Gündüz |
| [37.5777, 38.33797](https://www.google.com/maps?q=37.5777,38.33797) | 2024-10-03 09:13 | 367.0 | 17.62 | Yüksek | Gündüz |
| [37.58265, 38.33489](https://www.google.com/maps?q=37.58265,38.33489) | 2024-10-03 09:13 | 334.56 | 6.6 | Orta | Gündüz |
| [37.60367, 38.86669](https://www.google.com/maps?q=37.60367,38.86669) | 2024-10-03 09:13 | 335.59 | 5.53 | Orta | Gündüz |
| [37.68843, 38.75557](https://www.google.com/maps?q=37.68843,38.75557) | 2024-10-03 09:13 | 330.29 | 4.54 | Düşük | Gündüz |
| [37.73503, 39.50811](https://www.google.com/maps?q=37.73503,39.50811) | 2024-10-03 09:13 | 331.74 | 4.36 | Orta | Gündüz |
| [37.75083, 39.41772](https://www.google.com/maps?q=37.75083,39.41772) | 2024-10-03 09:13 | 333.2 | 4.85 | Düşük | Gündüz |
| [37.75413, 39.41478](https://www.google.com/maps?q=37.75413,39.41478) | 2024-10-03 09:13 | 336.61 | 5.85 | Orta | Gündüz |
| [37.77857, 40.95592](https://www.google.com/maps?q=37.77857,40.95592) | 2024-10-03 09:13 | 338.07 | 5.2 | Orta | Gündüz |
| [37.9133, 41.03225](https://www.google.com/maps?q=37.9133,41.03225) | 2024-10-03 09:13 | 338.84 | 2.99 | Orta | Gündüz |
| [37.92535, 40.34058](https://www.google.com/maps?q=37.92535,40.34058) | 2024-10-03 09:13 | 330.69 | 1.96 | Orta | Gündüz |
| [37.9442, 40.73191](https://www.google.com/maps?q=37.9442,40.73191) | 2024-10-03 09:13 | 352.94 | 10.32 | Orta | Gündüz |
| [37.95466, 40.8808](https://www.google.com/maps?q=37.95466,40.8808) | 2024-10-03 09:13 | 347.46 | 7.66 | Orta | Gündüz |
| [37.95585, 40.87947](https://www.google.com/maps?q=37.95585,40.87947) | 2024-10-03 09:13 | 351.19 | 6.71 | Orta | Gündüz |
| [38.02731, 40.43969](https://www.google.com/maps?q=38.02731,40.43969) | 2024-10-03 09:13 | 345.28 | 13.73 | Orta | Gündüz |
| [38.02924, 40.44603](https://www.google.com/maps?q=38.02924,40.44603) | 2024-10-03 09:13 | 367.0 | 23.84 | Yüksek | Gündüz |
| [38.0312, 40.44028](https://www.google.com/maps?q=38.0312,40.44028) | 2024-10-03 09:13 | 367.0 | 13.59 | Yüksek | Gündüz |
| [38.03309, 40.44665](https://www.google.com/maps?q=38.03309,40.44665) | 2024-10-03 09:13 | 349.83 | 13.59 | Orta | Gündüz |
| [38.0451, 40.44082](https://www.google.com/maps?q=38.0451,40.44082) | 2024-10-03 09:13 | 333.19 | 2.15 | Orta | Gündüz |
| [38.0581, 40.93503](https://www.google.com/maps?q=38.0581,40.93503) | 2024-10-03 09:13 | 332.06 | 3.54 | Düşük | Gündüz |
| [38.07834, 41.16386](https://www.google.com/maps?q=38.07834,41.16386) | 2024-10-03 09:13 | 330.33 | 2.96 | Orta | Gündüz |
| [38.14664, 40.8357](https://www.google.com/maps?q=38.14664,40.8357) | 2024-10-03 09:13 | 330.05 | 3.65 | Düşük | Gündüz |
| [38.14833, 40.83749](https://www.google.com/maps?q=38.14833,40.83749) | 2024-10-03 09:13 | 345.72 | 5.65 | Orta | Gündüz |
| [38.16621, 40.72025](https://www.google.com/maps?q=38.16621,40.72025) | 2024-10-03 09:13 | 334.91 | 3.61 | Orta | Gündüz |
| [38.18007, 40.65279](https://www.google.com/maps?q=38.18007,40.65279) | 2024-10-03 09:13 | 367.0 | 12.87 | Yüksek | Gündüz |
| [38.1813, 40.99614](https://www.google.com/maps?q=38.1813,40.99614) | 2024-10-03 09:13 | 349.33 | 6.74 | Orta | Gündüz |
| [38.18224, 40.99984](https://www.google.com/maps?q=38.18224,40.99984) | 2024-10-03 09:13 | 340.17 | 10.74 | Orta | Gündüz |
| [38.19507, 40.79477](https://www.google.com/maps?q=38.19507,40.79477) | 2024-10-03 09:13 | 333.89 | 4.23 | Düşük | Gündüz |
| [38.2604, 40.48585](https://www.google.com/maps?q=38.2604,40.48585) | 2024-10-03 09:13 | 332.17 | 4.25 | Orta | Gündüz |
| [38.99628, 41.89825](https://www.google.com/maps?q=38.99628,41.89825) | 2024-10-03 09:13 | 334.53 | 4.43 | Orta | Gündüz |
| [39.00167, 41.89528](https://www.google.com/maps?q=39.00167,41.89528) | 2024-10-03 09:13 | 333.54 | 4.43 | Orta | Gündüz |
| [39.29448, 42.20452](https://www.google.com/maps?q=39.29448,42.20452) | 2024-10-03 09:13 | 327.44 | 2.93 | Düşük | Gündüz |
| [40.02575, 44.09805](https://www.google.com/maps?q=40.02575,44.09805) | 2024-10-03 09:13 | 328.7 | 2.93 | Orta | Gündüz |
| [40.02764, 44.10538](https://www.google.com/maps?q=40.02764,44.10538) | 2024-10-03 09:13 | 326.61 | 3.02 | Orta | Gündüz |
| [40.02858, 44.10906](https://www.google.com/maps?q=40.02858,44.10906) | 2024-10-03 09:13 | 347.11 | 3.02 | Orta | Gündüz |
| [40.03062, 44.09594](https://www.google.com/maps?q=40.03062,44.09594) | 2024-10-03 09:13 | 334.19 | 2.93 | Orta | Gündüz |
| [38.42823, 27.2177](https://www.google.com/maps?q=38.42823,27.2177) | 2024-10-03 00:50 | 302.29 | 0.63 | Orta | Gece |
| [38.45515, 27.26358](https://www.google.com/maps?q=38.45515,27.26358) | 2024-10-03 00:50 | 299.54 | 0.62 | Orta | Gece |
| [38.6581, 30.62074](https://www.google.com/maps?q=38.6581,30.62074) | 2024-10-03 00:50 | 295.93 | 1.49 | Orta | Gece |
| [38.73544, 26.94617](https://www.google.com/maps?q=38.73544,26.94617) | 2024-10-03 00:50 | 306.24 | 1.33 | Orta | Gece |
| [38.7364, 26.94244](https://www.google.com/maps?q=38.7364,26.94244) | 2024-10-03 00:50 | 303.39 | 1.33 | Orta | Gece |
| [38.73929, 26.93132](https://www.google.com/maps?q=38.73929,26.93132) | 2024-10-03 00:50 | 308.72 | 1.27 | Orta | Gece |
| [38.74521, 26.95043](https://www.google.com/maps?q=38.74521,26.95043) | 2024-10-03 00:50 | 300.08 | 0.78 | Orta | Gece |
| [38.75395, 26.93768](https://www.google.com/maps?q=38.75395,26.93768) | 2024-10-03 00:50 | 306.99 | 0.98 | Orta | Gece |
| [39.16906, 27.63123](https://www.google.com/maps?q=39.16906,27.63123) | 2024-10-03 00:50 | 296.85 | 0.91 | Orta | Gece |
| [39.48186, 30.0418](https://www.google.com/maps?q=39.48186,30.0418) | 2024-10-03 00:50 | 301.08 | 1.36 | Orta | Gece |
| [39.60614, 27.87868](https://www.google.com/maps?q=39.60614,27.87868) | 2024-10-03 00:50 | 295.3 | 0.55 | Orta | Gece |
| [40.18538, 29.22371](https://www.google.com/maps?q=40.18538,29.22371) | 2024-10-03 00:50 | 295.66 | 0.45 | Orta | Gece |
| [41.02023, 28.55343](https://www.google.com/maps?q=41.02023,28.55343) | 2024-10-03 00:50 | 300.88 | 1.18 | Orta | Gece |
| [41.25662, 31.41563](https://www.google.com/maps?q=41.25662,31.41563) | 2024-10-03 00:50 | 301.5 | 1.66 | Orta | Gece |
| [41.51484, 32.16695](https://www.google.com/maps?q=41.51484,32.16695) | 2024-10-03 00:50 | 300.57 | 1.06 | Orta | Gece |
| [41.79681, 26.70323](https://www.google.com/maps?q=41.79681,26.70323) | 2024-10-03 00:50 | 295.11 | 1.22 | Orta | Gece |
