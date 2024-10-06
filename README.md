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
### Son Güncelleme: 2024-10-06 11:56:14 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [37.69409, 38.08624](https://www.google.com/maps?q=37.69409,38.08624) | 2024-10-06 00:16 | 299.2 | 0.51 | Orta | Gece |
| [37.69485, 38.08654](https://www.google.com/maps?q=37.69485,38.08654) | 2024-10-06 00:16 | 299.49 | 0.85 | Orta | Gece |
| [37.7957, 38.37299](https://www.google.com/maps?q=37.7957,38.37299) | 2024-10-06 00:16 | 317.49 | 2.07 | Orta | Gece |
| [37.82244, 38.5468](https://www.google.com/maps?q=37.82244,38.5468) | 2024-10-06 00:16 | 304.72 | 0.94 | Orta | Gece |
| [37.83421, 40.43363](https://www.google.com/maps?q=37.83421,40.43363) | 2024-10-06 00:16 | 298.57 | 1.11 | Orta | Gece |
| [37.92904, 41.02959](https://www.google.com/maps?q=37.92904,41.02959) | 2024-10-06 00:16 | 297.3 | 0.83 | Orta | Gece |
| [38.04069, 41.06145](https://www.google.com/maps?q=38.04069,41.06145) | 2024-10-06 00:16 | 300.04 | 0.72 | Orta | Gece |
| [38.05902, 40.43876](https://www.google.com/maps?q=38.05902,40.43876) | 2024-10-06 00:16 | 296.09 | 1.29 | Orta | Gece |
| [38.17117, 40.93796](https://www.google.com/maps?q=38.17117,40.93796) | 2024-10-06 00:16 | 298.01 | 0.91 | Orta | Gece |
| [38.17296, 40.93306](https://www.google.com/maps?q=38.17296,40.93306) | 2024-10-06 00:16 | 295.7 | 1.28 | Orta | Gece |
| [38.21764, 40.38691](https://www.google.com/maps?q=38.21764,40.38691) | 2024-10-06 00:16 | 295.39 | 0.48 | Orta | Gece |
| [38.45197, 38.72854](https://www.google.com/maps?q=38.45197,38.72854) | 2024-10-06 00:16 | 297.69 | 1.0 | Orta | Gece |
| [39.38925, 35.57047](https://www.google.com/maps?q=39.38925,35.57047) | 2024-10-06 00:16 | 296.68 | 0.4 | Orta | Gece |
| [39.74596, 30.19877](https://www.google.com/maps?q=39.74596,30.19877) | 2024-10-06 00:16 | 296.29 | 0.88 | Orta | Gece |
| [40.08329, 32.79928](https://www.google.com/maps?q=40.08329,32.79928) | 2024-10-06 00:16 | 297.19 | 0.74 | Orta | Gece |
| [40.21715, 28.44893](https://www.google.com/maps?q=40.21715,28.44893) | 2024-10-06 00:16 | 340.02 | 6.29 | Orta | Gece |
| [40.75613, 31.7833](https://www.google.com/maps?q=40.75613,31.7833) | 2024-10-06 00:16 | 303.83 | 0.93 | Orta | Gece |
| [40.7574, 29.7625](https://www.google.com/maps?q=40.7574,29.7625) | 2024-10-06 00:16 | 302.93 | 1.47 | Orta | Gece |
| [40.78254, 29.60011](https://www.google.com/maps?q=40.78254,29.60011) | 2024-10-06 00:16 | 301.4 | 1.54 | Orta | Gece |
| [40.94472, 31.39551](https://www.google.com/maps?q=40.94472,31.39551) | 2024-10-06 00:16 | 299.09 | 0.68 | Orta | Gece |
| [41.17194, 32.63096](https://www.google.com/maps?q=41.17194,32.63096) | 2024-10-06 00:16 | 297.41 | 0.8 | Orta | Gece |
| [41.17608, 32.63276](https://www.google.com/maps?q=41.17608,32.63276) | 2024-10-06 00:16 | 311.31 | 1.26 | Orta | Gece |
| [41.18021, 32.63454](https://www.google.com/maps?q=41.18021,32.63454) | 2024-10-06 00:16 | 304.48 | 1.26 | Orta | Gece |
| [41.24159, 36.46719](https://www.google.com/maps?q=41.24159,36.46719) | 2024-10-06 00:16 | 304.04 | 1.07 | Orta | Gece |
| [41.24266, 36.46324](https://www.google.com/maps?q=41.24266,36.46324) | 2024-10-06 00:16 | 307.63 | 1.99 | Orta | Gece |
| [41.2566, 31.41206](https://www.google.com/maps?q=41.2566,31.41206) | 2024-10-06 00:16 | 316.33 | 1.45 | Orta | Gece |
| [41.2664, 31.42575](https://www.google.com/maps?q=41.2664,31.42575) | 2024-10-06 00:16 | 317.64 | 2.52 | Orta | Gece |
| [41.27033, 31.42726](https://www.google.com/maps?q=41.27033,31.42726) | 2024-10-06 00:16 | 300.84 | 0.42 | Orta | Gece |
| [36.26403, 33.73055](https://www.google.com/maps?q=36.26403,33.73055) | 2024-10-06 00:18 | 308.64 | 0.9 | Orta | Gece |
| [36.69378, 36.20667](https://www.google.com/maps?q=36.69378,36.20667) | 2024-10-06 00:18 | 310.83 | 1.72 | Orta | Gece |
| [36.7198, 36.20181](https://www.google.com/maps?q=36.7198,36.20181) | 2024-10-06 00:18 | 310.68 | 1.27 | Orta | Gece |
| [36.72954, 36.21119](https://www.google.com/maps?q=36.72954,36.21119) | 2024-10-06 00:18 | 308.77 | 1.78 | Orta | Gece |
| [36.74446, 36.20176](https://www.google.com/maps?q=36.74446,36.20176) | 2024-10-06 00:18 | 305.91 | 0.84 | Orta | Gece |
| [36.86726, 34.76103](https://www.google.com/maps?q=36.86726,34.76103) | 2024-10-06 00:18 | 303.32 | 1.09 | Orta | Gece |
| [37.01274, 36.10527](https://www.google.com/maps?q=37.01274,36.10527) | 2024-10-06 00:18 | 312.06 | 1.26 | Orta | Gece |
| [37.02023, 36.11013](https://www.google.com/maps?q=37.02023,36.11013) | 2024-10-06 00:18 | 304.05 | 1.32 | Orta | Gece |
| [37.02363, 36.10996](https://www.google.com/maps?q=37.02363,36.10996) | 2024-10-06 00:18 | 302.61 | 1.47 | Orta | Gece |
| [37.29383, 37.15765](https://www.google.com/maps?q=37.29383,37.15765) | 2024-10-06 00:18 | 304.77 | 1.31 | Orta | Gece |
| [37.34483, 38.75073](https://www.google.com/maps?q=37.34483,38.75073) | 2024-10-06 00:18 | 295.9 | 0.71 | Orta | Gece |
| [37.35334, 37.16197](https://www.google.com/maps?q=37.35334,37.16197) | 2024-10-06 00:18 | 299.74 | 1.31 | Orta | Gece |
| [37.89933, 30.49284](https://www.google.com/maps?q=37.89933,30.49284) | 2024-10-06 00:18 | 296.85 | 0.71 | Orta | Gece |
| [37.94798, 34.68542](https://www.google.com/maps?q=37.94798,34.68542) | 2024-10-06 00:18 | 296.92 | 0.27 | Orta | Gece |
| [38.42723, 27.21637](https://www.google.com/maps?q=38.42723,27.21637) | 2024-10-06 00:18 | 295.61 | 0.79 | Orta | Gece |
| [38.65985, 30.61775](https://www.google.com/maps?q=38.65985,30.61775) | 2024-10-06 00:18 | 307.9 | 0.92 | Orta | Gece |
| [39.16784, 27.63488](https://www.google.com/maps?q=39.16784,27.63488) | 2024-10-06 00:18 | 295.48 | 1.14 | Orta | Gece |
| [39.48557, 30.03908](https://www.google.com/maps?q=39.48557,30.03908) | 2024-10-06 00:18 | 304.71 | 1.38 | Orta | Gece |
| [36.67272, 37.50813](https://www.google.com/maps?q=36.67272,37.50813) | 2024-10-06 09:34 | 348.11 | 7.23 | Orta | Gündüz |
| [36.70054, 39.34051](https://www.google.com/maps?q=36.70054,39.34051) | 2024-10-06 09:34 | 342.59 | 2.99 | Orta | Gündüz |
| [36.79071, 39.34523](https://www.google.com/maps?q=36.79071,39.34523) | 2024-10-06 09:34 | 339.34 | 4.89 | Orta | Gündüz |
| [36.79597, 39.34321](https://www.google.com/maps?q=36.79597,39.34321) | 2024-10-06 09:34 | 341.73 | 2.08 | Orta | Gündüz |
| [36.83034, 34.91059](https://www.google.com/maps?q=36.83034,34.91059) | 2024-10-06 09:34 | 338.42 | 5.8 | Orta | Gündüz |
| [36.84065, 38.74057](https://www.google.com/maps?q=36.84065,38.74057) | 2024-10-06 09:34 | 353.74 | 8.6 | Orta | Gündüz |
| [36.87743, 35.0168](https://www.google.com/maps?q=36.87743,35.0168) | 2024-10-06 09:34 | 334.76 | 7.4 | Orta | Gündüz |
| [36.88181, 35.01601](https://www.google.com/maps?q=36.88181,35.01601) | 2024-10-06 09:34 | 343.82 | 6.05 | Orta | Gündüz |
| [36.89429, 38.14202](https://www.google.com/maps?q=36.89429,38.14202) | 2024-10-06 09:34 | 339.16 | 4.09 | Orta | Gündüz |
| [36.95716, 38.73298](https://www.google.com/maps?q=36.95716,38.73298) | 2024-10-06 09:34 | 355.03 | 15.72 | Düşük | Gündüz |
| [36.95838, 38.73746](https://www.google.com/maps?q=36.95838,38.73746) | 2024-10-06 09:34 | 367.0 | 18.81 | Yüksek | Gündüz |
| [36.96314, 38.6452](https://www.google.com/maps?q=36.96314,38.6452) | 2024-10-06 09:34 | 344.26 | 8.16 | Orta | Gündüz |
| [37.06628, 36.63611](https://www.google.com/maps?q=37.06628,36.63611) | 2024-10-06 09:34 | 342.33 | 12.03 | Orta | Gündüz |
| [37.15845, 40.55094](https://www.google.com/maps?q=37.15845,40.55094) | 2024-10-06 09:34 | 350.66 | 22.54 | Orta | Gündüz |
| [37.15936, 40.55455](https://www.google.com/maps?q=37.15936,40.55455) | 2024-10-06 09:34 | 333.82 | 12.43 | Düşük | Gündüz |
| [37.17992, 40.34156](https://www.google.com/maps?q=37.17992,40.34156) | 2024-10-06 09:34 | 354.97 | 8.04 | Orta | Gündüz |
| [37.18087, 40.34527](https://www.google.com/maps?q=37.18087,40.34527) | 2024-10-06 09:34 | 367.0 | 8.57 | Yüksek | Gündüz |
| [37.18488, 40.33969](https://www.google.com/maps?q=37.18488,40.33969) | 2024-10-06 09:34 | 335.76 | 8.04 | Orta | Gündüz |
| [37.18582, 40.34341](https://www.google.com/maps?q=37.18582,40.34341) | 2024-10-06 09:34 | 340.53 | 8.57 | Orta | Gündüz |
| [37.19886, 40.45836](https://www.google.com/maps?q=37.19886,40.45836) | 2024-10-06 09:34 | 367.0 | 8.1 | Yüksek | Gündüz |
| [37.2285, 39.03954](https://www.google.com/maps?q=37.2285,39.03954) | 2024-10-06 09:34 | 342.04 | 4.08 | Orta | Gündüz |
| [37.22998, 39.03822](https://www.google.com/maps?q=37.22998,39.03822) | 2024-10-06 09:34 | 343.95 | 4.22 | Orta | Gündüz |
| [37.30571, 37.02753](https://www.google.com/maps?q=37.30571,37.02753) | 2024-10-06 09:34 | 334.17 | 2.52 | Düşük | Gündüz |
| [37.32162, 38.92273](https://www.google.com/maps?q=37.32162,38.92273) | 2024-10-06 09:34 | 353.34 | 5.24 | Orta | Gündüz |
| [37.33069, 42.36546](https://www.google.com/maps?q=37.33069,42.36546) | 2024-10-06 09:34 | 349.75 | 9.93 | Orta | Gündüz |
| [37.3446, 39.65487](https://www.google.com/maps?q=37.3446,39.65487) | 2024-10-06 09:34 | 341.37 | 2.93 | Orta | Gündüz |
| [37.42467, 39.12851](https://www.google.com/maps?q=37.42467,39.12851) | 2024-10-06 09:34 | 335.48 | 7.23 | Düşük | Gündüz |
| [37.43127, 38.32109](https://www.google.com/maps?q=37.43127,38.32109) | 2024-10-06 09:34 | 342.77 | 4.99 | Orta | Gündüz |
| [37.43669, 38.31888](https://www.google.com/maps?q=37.43669,38.31888) | 2024-10-06 09:34 | 339.65 | 4.99 | Orta | Gündüz |
| [37.45449, 38.19429](https://www.google.com/maps?q=37.45449,38.19429) | 2024-10-06 09:34 | 340.44 | 3.94 | Düşük | Gündüz |
| [37.45737, 38.19561](https://www.google.com/maps?q=37.45737,38.19561) | 2024-10-06 09:34 | 350.55 | 7.57 | Orta | Gündüz |
| [37.45982, 41.44329](https://www.google.com/maps?q=37.45982,41.44329) | 2024-10-06 09:34 | 367.0 | 15.71 | Yüksek | Gündüz |
| [37.46535, 39.34612](https://www.google.com/maps?q=37.46535,39.34612) | 2024-10-06 09:34 | 335.69 | 3.64 | Orta | Gündüz |
| [37.49807, 37.99973](https://www.google.com/maps?q=37.49807,37.99973) | 2024-10-06 09:34 | 335.27 | 2.99 | Orta | Gündüz |
| [37.50041, 37.99943](https://www.google.com/maps?q=37.50041,37.99943) | 2024-10-06 09:34 | 336.57 | 2.46 | Orta | Gündüz |
| [37.50317, 40.0986](https://www.google.com/maps?q=37.50317,40.0986) | 2024-10-06 09:34 | 339.49 | 2.91 | Orta | Gündüz |
| [37.51366, 39.16932](https://www.google.com/maps?q=37.51366,39.16932) | 2024-10-06 09:34 | 344.46 | 8.17 | Orta | Gündüz |
| [37.53038, 39.35966](https://www.google.com/maps?q=37.53038,39.35966) | 2024-10-06 09:34 | 338.31 | 2.79 | Orta | Gündüz |
| [37.57545, 38.39227](https://www.google.com/maps?q=37.57545,38.39227) | 2024-10-06 09:34 | 342.45 | 4.0 | Orta | Gündüz |
| [37.57562, 39.4639](https://www.google.com/maps?q=37.57562,39.4639) | 2024-10-06 09:34 | 339.5 | 1.54 | Orta | Gündüz |
| [37.58009, 39.46089](https://www.google.com/maps?q=37.58009,39.46089) | 2024-10-06 09:34 | 344.32 | 3.58 | Orta | Gündüz |
| [37.58129, 38.91636](https://www.google.com/maps?q=37.58129,38.91636) | 2024-10-06 09:34 | 352.48 | 6.24 | Orta | Gündüz |
| [37.60776, 37.93532](https://www.google.com/maps?q=37.60776,37.93532) | 2024-10-06 09:34 | 337.77 | 4.79 | Düşük | Gündüz |
| [37.61089, 37.93427](https://www.google.com/maps?q=37.61089,37.93427) | 2024-10-06 09:34 | 342.09 | 2.34 | Orta | Gündüz |
| [37.62027, 38.29845](https://www.google.com/maps?q=37.62027,38.29845) | 2024-10-06 09:34 | 348.61 | 6.25 | Orta | Gündüz |
| [37.63543, 40.64625](https://www.google.com/maps?q=37.63543,40.64625) | 2024-10-06 09:34 | 339.77 | 9.22 | Orta | Gündüz |
| [37.64105, 40.64766](https://www.google.com/maps?q=37.64105,40.64766) | 2024-10-06 09:34 | 334.86 | 6.47 | Orta | Gündüz |
| [37.64265, 40.64861](https://www.google.com/maps?q=37.64265,40.64861) | 2024-10-06 09:34 | 341.7 | 5.95 | Orta | Gündüz |
| [37.65103, 38.00241](https://www.google.com/maps?q=37.65103,38.00241) | 2024-10-06 09:34 | 367.0 | 23.24 | Yüksek | Gündüz |
| [37.66771, 39.6656](https://www.google.com/maps?q=37.66771,39.6656) | 2024-10-06 09:34 | 338.07 | 2.26 | Orta | Gündüz |
| [37.67064, 38.00714](https://www.google.com/maps?q=37.67064,38.00714) | 2024-10-06 09:34 | 342.46 | 4.8 | Orta | Gündüz |
| [37.68176, 39.02163](https://www.google.com/maps?q=37.68176,39.02163) | 2024-10-06 09:34 | 340.65 | 7.38 | Orta | Gündüz |
| [37.6827, 39.63763](https://www.google.com/maps?q=37.6827,39.63763) | 2024-10-06 09:34 | 352.47 | 5.02 | Orta | Gündüz |
| [37.68292, 39.02594](https://www.google.com/maps?q=37.68292,39.02594) | 2024-10-06 09:34 | 367.0 | 7.38 | Yüksek | Gündüz |
| [37.68505, 39.02344](https://www.google.com/maps?q=37.68505,39.02344) | 2024-10-06 09:34 | 367.0 | 17.03 | Yüksek | Gündüz |
| [37.68816, 39.02395](https://www.google.com/maps?q=37.68816,39.02395) | 2024-10-06 09:34 | 340.43 | 5.03 | Orta | Gündüz |
| [37.69069, 42.83279](https://www.google.com/maps?q=37.69069,42.83279) | 2024-10-06 09:34 | 350.98 | 8.86 | Orta | Gündüz |
| [37.70276, 37.99112](https://www.google.com/maps?q=37.70276,37.99112) | 2024-10-06 09:34 | 331.26 | 3.47 | Düşük | Gündüz |
| [37.72958, 39.40921](https://www.google.com/maps?q=37.72958,39.40921) | 2024-10-06 09:34 | 351.45 | 5.38 | Orta | Gündüz |
| [37.7515, 39.17435](https://www.google.com/maps?q=37.7515,39.17435) | 2024-10-06 09:34 | 335.9 | 1.95 | Orta | Gündüz |
| [37.75298, 40.16219](https://www.google.com/maps?q=37.75298,40.16219) | 2024-10-06 09:34 | 346.78 | 2.7 | Orta | Gündüz |
| [37.75448, 40.16333](https://www.google.com/maps?q=37.75448,40.16333) | 2024-10-06 09:34 | 336.65 | 7.04 | Orta | Gündüz |
| [37.7644, 38.41156](https://www.google.com/maps?q=37.7644,38.41156) | 2024-10-06 09:34 | 338.38 | 3.67 | Orta | Gündüz |
| [37.78167, 38.51762](https://www.google.com/maps?q=37.78167,38.51762) | 2024-10-06 09:34 | 354.38 | 8.01 | Orta | Gündüz |
| [37.81669, 38.34396](https://www.google.com/maps?q=37.81669,38.34396) | 2024-10-06 09:34 | 336.67 | 4.94 | Orta | Gündüz |
| [37.82606, 38.55038](https://www.google.com/maps?q=37.82606,38.55038) | 2024-10-06 09:34 | 355.04 | 8.51 | Orta | Gündüz |
| [37.8564, 38.5536](https://www.google.com/maps?q=37.8564,38.5536) | 2024-10-06 09:34 | 334.41 | 3.29 | Düşük | Gündüz |
| [37.87669, 40.41518](https://www.google.com/maps?q=37.87669,40.41518) | 2024-10-06 09:34 | 353.38 | 6.79 | Orta | Gündüz |
| [37.89694, 40.28501](https://www.google.com/maps?q=37.89694,40.28501) | 2024-10-06 09:34 | 347.2 | 14.77 | Orta | Gündüz |
| [37.89749, 40.28598](https://www.google.com/maps?q=37.89749,40.28598) | 2024-10-06 09:34 | 367.0 | 29.6 | Yüksek | Gündüz |
| [37.89785, 40.28856](https://www.google.com/maps?q=37.89785,40.28856) | 2024-10-06 09:34 | 336.62 | 14.77 | Orta | Gündüz |
| [37.91816, 40.03107](https://www.google.com/maps?q=37.91816,40.03107) | 2024-10-06 09:34 | 332.5 | 1.65 | Düşük | Gündüz |
| [37.93587, 41.04033](https://www.google.com/maps?q=37.93587,41.04033) | 2024-10-06 09:34 | 335.68 | 25.12 | Düşük | Gündüz |
| [37.97746, 34.862](https://www.google.com/maps?q=37.97746,34.862) | 2024-10-06 09:34 | 336.32 | 6.43 | Orta | Gündüz |
| [37.99606, 41.1197](https://www.google.com/maps?q=37.99606,41.1197) | 2024-10-06 09:34 | 344.03 | 12.53 | Orta | Gündüz |
| [37.99663, 41.12194](https://www.google.com/maps?q=37.99663,41.12194) | 2024-10-06 09:34 | 367.0 | 21.16 | Yüksek | Gündüz |
| [37.99764, 41.12607](https://www.google.com/maps?q=37.99764,41.12607) | 2024-10-06 09:34 | 341.07 | 9.45 | Orta | Gündüz |
| [38.01799, 41.10527](https://www.google.com/maps?q=38.01799,41.10527) | 2024-10-06 09:34 | 337.99 | 5.87 | Düşük | Gündüz |
| [38.03127, 40.97242](https://www.google.com/maps?q=38.03127,40.97242) | 2024-10-06 09:34 | 344.2 | 26.85 | Orta | Gündüz |
| [38.03228, 40.16542](https://www.google.com/maps?q=38.03228,40.16542) | 2024-10-06 09:34 | 367.0 | 16.76 | Yüksek | Gündüz |
| [38.03599, 40.97075](https://www.google.com/maps?q=38.03599,40.97075) | 2024-10-06 09:34 | 352.6 | 26.85 | Orta | Gündüz |
| [38.05229, 40.41112](https://www.google.com/maps?q=38.05229,40.41112) | 2024-10-06 09:34 | 345.97 | 6.92 | Düşük | Gündüz |
| [38.05703, 40.24162](https://www.google.com/maps?q=38.05703,40.24162) | 2024-10-06 09:34 | 351.72 | 6.28 | Orta | Gündüz |
| [38.06014, 40.23281](https://www.google.com/maps?q=38.06014,40.23281) | 2024-10-06 09:34 | 335.42 | 8.53 | Orta | Gündüz |
| [38.06103, 40.2363](https://www.google.com/maps?q=38.06103,40.2363) | 2024-10-06 09:34 | 349.87 | 14.16 | Orta | Gündüz |
| [38.06499, 40.23087](https://www.google.com/maps?q=38.06499,40.23087) | 2024-10-06 09:34 | 367.0 | 8.53 | Yüksek | Gündüz |
| [38.06547, 39.81521](https://www.google.com/maps?q=38.06547,39.81521) | 2024-10-06 09:34 | 341.34 | 1.87 | Orta | Gündüz |
| [38.08217, 40.34082](https://www.google.com/maps?q=38.08217,40.34082) | 2024-10-06 09:34 | 346.41 | 5.52 | Orta | Gündüz |
| [38.08313, 40.3446](https://www.google.com/maps?q=38.08313,40.3446) | 2024-10-06 09:34 | 367.0 | 9.43 | Yüksek | Gündüz |
| [38.08982, 40.8398](https://www.google.com/maps?q=38.08982,40.8398) | 2024-10-06 09:34 | 352.84 | 57.73 | Orta | Gündüz |
| [38.0906, 40.45782](https://www.google.com/maps?q=38.0906,40.45782) | 2024-10-06 09:34 | 367.0 | 34.06 | Düşük | Gündüz |
| [38.09145, 40.46118](https://www.google.com/maps?q=38.09145,40.46118) | 2024-10-06 09:34 | 367.0 | 34.06 | Yüksek | Gündüz |
| [38.12524, 40.34327](https://www.google.com/maps?q=38.12524,40.34327) | 2024-10-06 09:34 | 339.02 | 1.52 | Orta | Gündüz |
| [38.12551, 40.34164](https://www.google.com/maps?q=38.12551,40.34164) | 2024-10-06 09:34 | 367.0 | 5.73 | Yüksek | Gündüz |
| [38.13008, 40.34142](https://www.google.com/maps?q=38.13008,40.34142) | 2024-10-06 09:34 | 338.25 | 0.91 | Orta | Gündüz |
| [38.13398, 40.99753](https://www.google.com/maps?q=38.13398,40.99753) | 2024-10-06 09:34 | 341.09 | 6.44 | Orta | Gündüz |
| [38.13833, 39.95618](https://www.google.com/maps?q=38.13833,39.95618) | 2024-10-06 09:34 | 346.1 | 5.2 | Orta | Gündüz |
| [38.13994, 39.95739](https://www.google.com/maps?q=38.13994,39.95739) | 2024-10-06 09:34 | 367.0 | 8.94 | Yüksek | Gündüz |
| [38.14326, 39.95429](https://www.google.com/maps?q=38.14326,39.95429) | 2024-10-06 09:34 | 367.0 | 5.2 | Yüksek | Gündüz |
| [38.14472, 40.58937](https://www.google.com/maps?q=38.14472,40.58937) | 2024-10-06 09:34 | 336.36 | 4.79 | Düşük | Gündüz |
| [38.1476, 40.66339](https://www.google.com/maps?q=38.1476,40.66339) | 2024-10-06 09:34 | 339.19 | 9.78 | Düşük | Gündüz |
| [38.15128, 37.02209](https://www.google.com/maps?q=38.15128,37.02209) | 2024-10-06 09:34 | 331.32 | 5.41 | Düşük | Gündüz |
| [38.1545, 39.35762](https://www.google.com/maps?q=38.1545,39.35762) | 2024-10-06 09:34 | 337.96 | 4.04 | Orta | Gündüz |
| [38.16837, 40.21756](https://www.google.com/maps?q=38.16837,40.21756) | 2024-10-06 09:34 | 336.84 | 6.47 | Düşük | Gündüz |
| [38.17017, 40.22465](https://www.google.com/maps?q=38.17017,40.22465) | 2024-10-06 09:34 | 346.36 | 5.12 | Orta | Gündüz |
| [38.17327, 40.2579](https://www.google.com/maps?q=38.17327,40.2579) | 2024-10-06 09:34 | 367.0 | 9.44 | Yüksek | Gündüz |
| [38.21957, 37.06154](https://www.google.com/maps?q=38.21957,37.06154) | 2024-10-06 09:34 | 333.78 | 3.88 | Orta | Gündüz |
| [38.22933, 40.56335](https://www.google.com/maps?q=38.22933,40.56335) | 2024-10-06 09:34 | 350.11 | 13.71 | Orta | Gündüz |
| [38.23406, 40.5614](https://www.google.com/maps?q=38.23406,40.5614) | 2024-10-06 09:34 | 336.88 | 5.0 | Düşük | Gündüz |
| [38.40623, 35.65148](https://www.google.com/maps?q=38.40623,35.65148) | 2024-10-06 09:34 | 335.09 | 6.26 | Orta | Gündüz |
| [38.41983, 37.32496](https://www.google.com/maps?q=38.41983,37.32496) | 2024-10-06 09:34 | 367.0 | 13.85 | Yüksek | Gündüz |
| [38.47684, 37.32421](https://www.google.com/maps?q=38.47684,37.32421) | 2024-10-06 09:34 | 337.9 | 3.43 | Orta | Gündüz |
| [38.53969, 38.27328](https://www.google.com/maps?q=38.53969,38.27328) | 2024-10-06 09:34 | 332.64 | 3.25 | Orta | Gündüz |
| [38.84788, 38.97773](https://www.google.com/maps?q=38.84788,38.97773) | 2024-10-06 09:34 | 335.7 | 4.85 | Orta | Gündüz |
| [38.94493, 37.22576](https://www.google.com/maps?q=38.94493,37.22576) | 2024-10-06 09:34 | 342.58 | 8.78 | Orta | Gündüz |
| [39.00656, 36.91127](https://www.google.com/maps?q=39.00656,36.91127) | 2024-10-06 09:34 | 330.73 | 5.68 | Düşük | Gündüz |
| [39.10844, 37.51223](https://www.google.com/maps?q=39.10844,37.51223) | 2024-10-06 09:34 | 334.67 | 3.39 | Orta | Gündüz |
| [39.28535, 37.5909](https://www.google.com/maps?q=39.28535,37.5909) | 2024-10-06 09:34 | 332.68 | 6.17 | Düşük | Gündüz |
| [39.75562, 42.93309](https://www.google.com/maps?q=39.75562,42.93309) | 2024-10-06 09:34 | 339.61 | 8.7 | Orta | Gündüz |
| [39.7567, 42.938](https://www.google.com/maps?q=39.7567,42.938) | 2024-10-06 09:34 | 347.87 | 12.96 | Orta | Gündüz |
| [39.75701, 42.93415](https://www.google.com/maps?q=39.75701,42.93415) | 2024-10-06 09:34 | 342.38 | 13.98 | Orta | Gündüz |
| [39.75812, 42.93904](https://www.google.com/maps?q=39.75812,42.93904) | 2024-10-06 09:34 | 334.07 | 7.05 | Orta | Gündüz |
| [40.01394, 44.0778](https://www.google.com/maps?q=40.01394,44.0778) | 2024-10-06 09:34 | 337.01 | 11.97 | Orta | Gündüz |
| [40.01481, 44.07939](https://www.google.com/maps?q=40.01481,44.07939) | 2024-10-06 09:34 | 345.01 | 12.4 | Orta | Gündüz |
| [38.56267, 34.38771](https://www.google.com/maps?q=38.56267,34.38771) | 2024-10-06 09:37 | 330.16 | 4.07 | Orta | Gündüz |
| [39.04664, 34.68779](https://www.google.com/maps?q=39.04664,34.68779) | 2024-10-06 09:37 | 333.1 | 6.7 | Orta | Gündüz |
| [39.04779, 34.68443](https://www.google.com/maps?q=39.04779,34.68443) | 2024-10-06 09:37 | 333.05 | 3.55 | Orta | Gündüz |
| [39.08073, 36.29729](https://www.google.com/maps?q=39.08073,36.29729) | 2024-10-06 09:37 | 341.13 | 8.37 | Orta | Gündüz |
| [39.17297, 34.79763](https://www.google.com/maps?q=39.17297,34.79763) | 2024-10-06 09:37 | 333.14 | 3.59 | Düşük | Gündüz |
| [39.1758, 34.79549](https://www.google.com/maps?q=39.1758,34.79549) | 2024-10-06 09:37 | 341.87 | 9.66 | Orta | Gündüz |
| [39.17855, 35.43645](https://www.google.com/maps?q=39.17855,35.43645) | 2024-10-06 09:37 | 340.07 | 4.58 | Orta | Gündüz |
| [39.17912, 35.37172](https://www.google.com/maps?q=39.17912,35.37172) | 2024-10-06 09:37 | 335.99 | 3.06 | Orta | Gündüz |
| [39.17913, 34.7725](https://www.google.com/maps?q=39.17913,34.7725) | 2024-10-06 09:37 | 367.0 | 19.35 | Yüksek | Gündüz |
| [39.18192, 34.77061](https://www.google.com/maps?q=39.18192,34.77061) | 2024-10-06 09:37 | 367.0 | 20.99 | Yüksek | Gündüz |
| [39.35759, 34.9627](https://www.google.com/maps?q=39.35759,34.9627) | 2024-10-06 09:37 | 352.84 | 11.15 | Orta | Gündüz |
| [39.36064, 34.95733](https://www.google.com/maps?q=39.36064,34.95733) | 2024-10-06 09:37 | 339.3 | 11.55 | Orta | Gündüz |
| [39.38895, 35.40122](https://www.google.com/maps?q=39.38895,35.40122) | 2024-10-06 09:37 | 350.26 | 8.88 | Orta | Gündüz |
| [39.43704, 35.45023](https://www.google.com/maps?q=39.43704,35.45023) | 2024-10-06 09:37 | 342.79 | 5.87 | Orta | Gündüz |
| [39.60045, 33.26807](https://www.google.com/maps?q=39.60045,33.26807) | 2024-10-06 09:37 | 340.32 | 7.25 | Orta | Gündüz |
| [39.72579, 37.31115](https://www.google.com/maps?q=39.72579,37.31115) | 2024-10-06 09:37 | 349.11 | 7.97 | Orta | Gündüz |
| [40.10206, 35.43139](https://www.google.com/maps?q=40.10206,35.43139) | 2024-10-06 09:37 | 342.06 | 6.46 | Orta | Gündüz |
| [40.112, 35.15186](https://www.google.com/maps?q=40.112,35.15186) | 2024-10-06 09:37 | 331.77 | 2.56 | Orta | Gündüz |
| [40.19888, 35.06134](https://www.google.com/maps?q=40.19888,35.06134) | 2024-10-06 09:37 | 335.73 | 4.26 | Orta | Gündüz |
| [40.37272, 40.16952](https://www.google.com/maps?q=40.37272,40.16952) | 2024-10-06 09:37 | 334.1 | 5.05 | Orta | Gündüz |
| [40.40799, 35.82195](https://www.google.com/maps?q=40.40799,35.82195) | 2024-10-06 09:37 | 330.71 | 3.56 | Orta | Gündüz |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
