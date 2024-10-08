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
### Son Güncelleme: 2024-10-08 12:44:19 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [37.09537, 41.4151](https://www.google.com/maps?q=37.09537,41.4151) | 2024-10-08 09:20 | 342.44 | 3.14 | Orta | Gündüz |
| [37.10096, 41.41292](https://www.google.com/maps?q=37.10096,41.41292) | 2024-10-08 09:20 | 355.06 | 5.43 | Orta | Gündüz |
| [37.11822, 41.68196](https://www.google.com/maps?q=37.11822,41.68196) | 2024-10-08 09:20 | 341.56 | 2.92 | Orta | Gündüz |
| [37.1195, 41.68673](https://www.google.com/maps?q=37.1195,41.68673) | 2024-10-08 09:20 | 334.01 | 2.92 | Düşük | Gündüz |
| [37.12006, 41.68252](https://www.google.com/maps?q=37.12006,41.68252) | 2024-10-08 09:20 | 345.11 | 6.07 | Orta | Gündüz |
| [37.12626, 41.68921](https://www.google.com/maps?q=37.12626,41.68921) | 2024-10-08 09:20 | 338.41 | 1.75 | Orta | Gündüz |
| [37.12754, 41.69398](https://www.google.com/maps?q=37.12754,41.69398) | 2024-10-08 09:20 | 333.23 | 1.75 | Düşük | Gündüz |
| [37.12816, 41.68978](https://www.google.com/maps?q=37.12816,41.68978) | 2024-10-08 09:20 | 337.12 | 3.52 | Orta | Gündüz |
| [37.15728, 41.66254](https://www.google.com/maps?q=37.15728,41.66254) | 2024-10-08 09:20 | 353.74 | 17.34 | Orta | Gündüz |
| [37.15857, 41.66726](https://www.google.com/maps?q=37.15857,41.66726) | 2024-10-08 09:20 | 367.0 | 15.4 | Yüksek | Gündüz |
| [37.16407, 41.66507](https://www.google.com/maps?q=37.16407,41.66507) | 2024-10-08 09:20 | 344.35 | 15.4 | Orta | Gündüz |
| [37.17679, 38.27976](https://www.google.com/maps?q=37.17679,38.27976) | 2024-10-08 09:20 | 346.95 | 7.25 | Orta | Gündüz |
| [37.18254, 41.71041](https://www.google.com/maps?q=37.18254,41.71041) | 2024-10-08 09:20 | 344.73 | 7.8 | Orta | Gündüz |
| [37.48967, 38.7042](https://www.google.com/maps?q=37.48967,38.7042) | 2024-10-08 09:20 | 330.55 | 4.49 | Orta | Gündüz |
| [37.52298, 40.42817](https://www.google.com/maps?q=37.52298,40.42817) | 2024-10-08 09:20 | 367.0 | 17.22 | Yüksek | Gündüz |
| [37.58678, 37.42574](https://www.google.com/maps?q=37.58678,37.42574) | 2024-10-08 09:20 | 330.61 | 5.5 | Düşük | Gündüz |
| [37.70734, 38.74922](https://www.google.com/maps?q=37.70734,38.74922) | 2024-10-08 09:20 | 339.28 | 7.78 | Orta | Gündüz |
| [37.86568, 38.85421](https://www.google.com/maps?q=37.86568,38.85421) | 2024-10-08 09:20 | 339.46 | 7.63 | Orta | Gündüz |
| [37.86804, 38.85753](https://www.google.com/maps?q=37.86804,38.85753) | 2024-10-08 09:20 | 332.87 | 8.56 | Düşük | Gündüz |
| [38.00077, 40.93001](https://www.google.com/maps?q=38.00077,40.93001) | 2024-10-08 09:20 | 347.97 | 7.6 | Orta | Gündüz |
| [38.03622, 40.3922](https://www.google.com/maps?q=38.03622,40.3922) | 2024-10-08 09:20 | 331.3 | 7.82 | Orta | Gündüz |
| [38.03775, 40.39756](https://www.google.com/maps?q=38.03775,40.39756) | 2024-10-08 09:20 | 335.29 | 6.65 | Orta | Gündüz |
| [38.08292, 40.93512](https://www.google.com/maps?q=38.08292,40.93512) | 2024-10-08 09:20 | 343.55 | 4.55 | Orta | Gündüz |
| [38.23359, 37.06223](https://www.google.com/maps?q=38.23359,37.06223) | 2024-10-08 09:20 | 345.49 | 7.61 | Orta | Gündüz |
| [38.23359, 37.06357](https://www.google.com/maps?q=38.23359,37.06357) | 2024-10-08 09:20 | 341.28 | 9.24 | Orta | Gündüz |
| [38.27639, 37.52702](https://www.google.com/maps?q=38.27639,37.52702) | 2024-10-08 09:20 | 342.13 | 8.53 | Orta | Gündüz |
| [38.27966, 37.52688](https://www.google.com/maps?q=38.27966,37.52688) | 2024-10-08 09:20 | 339.08 | 8.46 | Orta | Gündüz |
| [38.29313, 37.0845](https://www.google.com/maps?q=38.29313,37.0845) | 2024-10-08 09:20 | 332.41 | 4.4 | Orta | Gündüz |
| [38.56992, 36.01773](https://www.google.com/maps?q=38.56992,36.01773) | 2024-10-08 09:20 | 341.04 | 5.63 | Orta | Gündüz |
| [38.57451, 36.01976](https://www.google.com/maps?q=38.57451,36.01976) | 2024-10-08 09:20 | 354.95 | 12.65 | Orta | Gündüz |
| [39.19258, 42.78712](https://www.google.com/maps?q=39.19258,42.78712) | 2024-10-08 09:20 | 329.96 | 3.03 | Orta | Gündüz |
| [39.19356, 42.79086](https://www.google.com/maps?q=39.19356,42.79086) | 2024-10-08 09:20 | 346.54 | 4.56 | Orta | Gündüz |
| [39.64146, 35.37622](https://www.google.com/maps?q=39.64146,35.37622) | 2024-10-08 09:22 | 329.4 | 4.43 | Orta | Gündüz |
| [39.86818, 37.44444](https://www.google.com/maps?q=39.86818,37.44444) | 2024-10-08 09:22 | 342.51 | 9.79 | Orta | Gündüz |
| [39.87028, 37.45115](https://www.google.com/maps?q=39.87028,37.45115) | 2024-10-08 09:22 | 352.86 | 12.95 | Orta | Gündüz |
| [40.0503, 35.04031](https://www.google.com/maps?q=40.0503,35.04031) | 2024-10-08 09:22 | 331.67 | 5.75 | Orta | Gündüz |
| [36.34941, 32.56463](https://www.google.com/maps?q=36.34941,32.56463) | 2024-10-08 11:00 | 330.39 | 3.73 | Orta | Gündüz |
| [36.34995, 32.56888](https://www.google.com/maps?q=36.34995,32.56888) | 2024-10-08 11:00 | 332.11 | 3.73 | Orta | Gündüz |
| [36.71982, 29.35951](https://www.google.com/maps?q=36.71982,29.35951) | 2024-10-08 11:00 | 332.64 | 1.74 | Orta | Gündüz |
| [36.72311, 29.35873](https://www.google.com/maps?q=36.72311,29.35873) | 2024-10-08 11:00 | 330.43 | 1.74 | Orta | Gündüz |
| [36.81475, 35.11102](https://www.google.com/maps?q=36.81475,35.11102) | 2024-10-08 11:00 | 331.84 | 3.77 | Orta | Gündüz |
| [36.82418, 30.35959](https://www.google.com/maps?q=36.82418,30.35959) | 2024-10-08 11:00 | 345.36 | 5.51 | Orta | Gündüz |
| [36.9273, 37.65456](https://www.google.com/maps?q=36.9273,37.65456) | 2024-10-08 11:00 | 338.24 | 2.79 | Orta | Gündüz |
| [36.94234, 35.83154](https://www.google.com/maps?q=36.94234,35.83154) | 2024-10-08 11:00 | 341.27 | 2.92 | Orta | Gündüz |
| [36.95467, 35.8297](https://www.google.com/maps?q=36.95467,35.8297) | 2024-10-08 11:00 | 335.71 | 3.28 | Orta | Gündüz |
| [37.0367, 36.69052](https://www.google.com/maps?q=37.0367,36.69052) | 2024-10-08 11:00 | 347.81 | 4.64 | Orta | Gündüz |
| [37.0962, 35.88452](https://www.google.com/maps?q=37.0962,35.88452) | 2024-10-08 11:00 | 343.49 | 4.83 | Orta | Gündüz |
| [37.11459, 36.15742](https://www.google.com/maps?q=37.11459,36.15742) | 2024-10-08 11:00 | 332.32 | 2.57 | Orta | Gündüz |
| [37.16611, 41.87387](https://www.google.com/maps?q=37.16611,41.87387) | 2024-10-08 11:00 | 352.6 | 4.1 | Orta | Gündüz |
| [37.18692, 41.70924](https://www.google.com/maps?q=37.18692,41.70924) | 2024-10-08 11:00 | 333.39 | 6.81 | Orta | Gündüz |
| [37.26991, 37.0713](https://www.google.com/maps?q=37.26991,37.0713) | 2024-10-08 11:00 | 338.62 | 4.0 | Düşük | Gündüz |
| [37.2748, 37.0761](https://www.google.com/maps?q=37.2748,37.0761) | 2024-10-08 11:00 | 344.11 | 5.19 | Orta | Gündüz |
| [37.28729, 36.81818](https://www.google.com/maps?q=37.28729,36.81818) | 2024-10-08 11:00 | 341.04 | 4.31 | Orta | Gündüz |
| [37.37949, 37.0058](https://www.google.com/maps?q=37.37949,37.0058) | 2024-10-08 11:00 | 340.26 | 2.8 | Orta | Gündüz |
| [37.42317, 39.23537](https://www.google.com/maps?q=37.42317,39.23537) | 2024-10-08 11:00 | 342.16 | 6.08 | Orta | Gündüz |
| [37.44875, 39.02718](https://www.google.com/maps?q=37.44875,39.02718) | 2024-10-08 11:00 | 349.47 | 10.2 | Orta | Gündüz |
| [37.45024, 39.64534](https://www.google.com/maps?q=37.45024,39.64534) | 2024-10-08 11:00 | 341.2 | 5.09 | Orta | Gündüz |
| [37.45048, 39.64906](https://www.google.com/maps?q=37.45048,39.64906) | 2024-10-08 11:00 | 367.0 | 11.35 | Yüksek | Gündüz |
| [37.48541, 39.55451](https://www.google.com/maps?q=37.48541,39.55451) | 2024-10-08 11:00 | 352.53 | 5.12 | Orta | Gündüz |
| [37.56254, 39.51314](https://www.google.com/maps?q=37.56254,39.51314) | 2024-10-08 11:00 | 338.13 | 1.69 | Orta | Gündüz |
| [37.56591, 39.48679](https://www.google.com/maps?q=37.56591,39.48679) | 2024-10-08 11:00 | 339.21 | 2.21 | Orta | Gündüz |
| [37.62209, 39.60611](https://www.google.com/maps?q=37.62209,39.60611) | 2024-10-08 11:00 | 354.54 | 5.22 | Orta | Gündüz |
| [37.62535, 39.60693](https://www.google.com/maps?q=37.62535,39.60693) | 2024-10-08 11:00 | 355.87 | 5.19 | Orta | Gündüz |
| [37.62997, 39.65008](https://www.google.com/maps?q=37.62997,39.65008) | 2024-10-08 11:00 | 340.38 | 3.06 | Orta | Gündüz |
| [37.64779, 37.55703](https://www.google.com/maps?q=37.64779,37.55703) | 2024-10-08 11:00 | 336.0 | 5.27 | Düşük | Gündüz |
| [37.66959, 40.64009](https://www.google.com/maps?q=37.66959,40.64009) | 2024-10-08 11:00 | 349.99 | 3.9 | Orta | Gündüz |
| [37.67692, 38.03432](https://www.google.com/maps?q=37.67692,38.03432) | 2024-10-08 11:00 | 343.55 | 6.41 | Orta | Gündüz |
| [37.70602, 38.74792](https://www.google.com/maps?q=37.70602,38.74792) | 2024-10-08 11:00 | 344.72 | 8.25 | Orta | Gündüz |
| [37.71307, 38.31607](https://www.google.com/maps?q=37.71307,38.31607) | 2024-10-08 11:00 | 335.15 | 2.79 | Orta | Gündüz |
| [37.80285, 38.56065](https://www.google.com/maps?q=37.80285,38.56065) | 2024-10-08 11:00 | 342.88 | 6.93 | Orta | Gündüz |
| [37.84953, 38.79923](https://www.google.com/maps?q=37.84953,38.79923) | 2024-10-08 11:00 | 357.19 | 12.74 | Orta | Gündüz |
| [37.85003, 38.80626](https://www.google.com/maps?q=37.85003,38.80626) | 2024-10-08 11:00 | 330.66 | 4.43 | Düşük | Gündüz |
| [37.85442, 38.7986](https://www.google.com/maps?q=37.85442,38.7986) | 2024-10-08 11:00 | 347.41 | 13.73 | Orta | Gündüz |
| [38.12948, 40.17955](https://www.google.com/maps?q=38.12948,40.17955) | 2024-10-08 11:00 | 333.86 | 4.63 | Orta | Gündüz |
| [38.12972, 40.18366](https://www.google.com/maps?q=38.12972,40.18366) | 2024-10-08 11:00 | 337.29 | 6.17 | Orta | Gündüz |
| [38.18544, 40.99519](https://www.google.com/maps?q=38.18544,40.99519) | 2024-10-08 11:00 | 334.2 | 5.02 | Orta | Gündüz |
| [38.19093, 40.99358](https://www.google.com/maps?q=38.19093,40.99358) | 2024-10-08 11:00 | 348.81 | 6.95 | Orta | Gündüz |
| [37.66272, 31.82718](https://www.google.com/maps?q=37.66272,31.82718) | 2024-10-08 11:02 | 334.0 | 1.8 | Orta | Gündüz |
| [37.87268, 28.11791](https://www.google.com/maps?q=37.87268,28.11791) | 2024-10-08 11:02 | 334.22 | 1.41 | Orta | Gündüz |
| [37.91863, 31.92079](https://www.google.com/maps?q=37.91863,31.92079) | 2024-10-08 11:02 | 337.81 | 5.77 | Orta | Gündüz |
| [38.0676, 27.50119](https://www.google.com/maps?q=38.0676,27.50119) | 2024-10-08 11:02 | 338.67 | 1.95 | Orta | Gündüz |
| [38.22414, 37.11306](https://www.google.com/maps?q=38.22414,37.11306) | 2024-10-08 11:02 | 341.66 | 2.74 | Orta | Gündüz |
| [38.22886, 37.0615](https://www.google.com/maps?q=38.22886,37.0615) | 2024-10-08 11:02 | 357.13 | 9.39 | Orta | Gündüz |
| [38.23379, 37.06646](https://www.google.com/maps?q=38.23379,37.06646) | 2024-10-08 11:02 | 334.76 | 9.39 | Düşük | Gündüz |
| [38.26649, 29.77826](https://www.google.com/maps?q=38.26649,29.77826) | 2024-10-08 11:02 | 337.05 | 4.28 | Düşük | Gündüz |
| [38.2723, 37.53362](https://www.google.com/maps?q=38.2723,37.53362) | 2024-10-08 11:02 | 342.55 | 5.37 | Orta | Gündüz |
| [38.27629, 40.34125](https://www.google.com/maps?q=38.27629,40.34125) | 2024-10-08 11:02 | 330.05 | 4.28 | Orta | Gündüz |
| [38.27781, 37.5445](https://www.google.com/maps?q=38.27781,37.5445) | 2024-10-08 11:02 | 342.45 | 15.49 | Orta | Gündüz |
| [38.29532, 37.078](https://www.google.com/maps?q=38.29532,37.078) | 2024-10-08 11:02 | 341.82 | 5.79 | Orta | Gündüz |
| [38.29578, 37.08363](https://www.google.com/maps?q=38.29578,37.08363) | 2024-10-08 11:02 | 344.03 | 5.79 | Orta | Gündüz |
| [38.29898, 37.12305](https://www.google.com/maps?q=38.29898,37.12305) | 2024-10-08 11:02 | 342.22 | 5.57 | Orta | Gündüz |
| [38.37271, 32.13105](https://www.google.com/maps?q=38.37271,32.13105) | 2024-10-08 11:02 | 344.07 | 8.49 | Orta | Gündüz |
| [38.46095, 35.0112](https://www.google.com/maps?q=38.46095,35.0112) | 2024-10-08 11:02 | 335.29 | 21.23 | Düşük | Gündüz |
| [38.47722, 29.39595](https://www.google.com/maps?q=38.47722,29.39595) | 2024-10-08 11:02 | 343.04 | 3.68 | Orta | Gündüz |
| [38.47787, 29.40033](https://www.google.com/maps?q=38.47787,29.40033) | 2024-10-08 11:02 | 342.29 | 8.98 | Orta | Gündüz |
| [38.73844, 26.93077](https://www.google.com/maps?q=38.73844,26.93077) | 2024-10-08 11:02 | 344.06 | 3.98 | Orta | Gündüz |
| [38.79462, 37.50568](https://www.google.com/maps?q=38.79462,37.50568) | 2024-10-08 11:02 | 342.48 | 5.47 | Orta | Gündüz |
| [38.91259, 34.59695](https://www.google.com/maps?q=38.91259,34.59695) | 2024-10-08 11:02 | 335.94 | 2.91 | Orta | Gündüz |
| [38.93704, 32.02728](https://www.google.com/maps?q=38.93704,32.02728) | 2024-10-08 11:02 | 334.75 | 1.98 | Düşük | Gündüz |
| [39.11954, 37.47653](https://www.google.com/maps?q=39.11954,37.47653) | 2024-10-08 11:02 | 335.44 | 24.84 | Düşük | Gündüz |
| [39.12003, 37.48278](https://www.google.com/maps?q=39.12003,37.48278) | 2024-10-08 11:02 | 337.05 | 24.84 | Orta | Gündüz |
| [39.12416, 37.47599](https://www.google.com/maps?q=39.12416,37.47599) | 2024-10-08 11:02 | 354.91 | 24.84 | Orta | Gündüz |
| [39.12466, 37.48229](https://www.google.com/maps?q=39.12466,37.48229) | 2024-10-08 11:02 | 351.78 | 24.84 | Orta | Gündüz |
| [39.34951, 34.91089](https://www.google.com/maps?q=39.34951,34.91089) | 2024-10-08 11:02 | 347.16 | 5.21 | Orta | Gündüz |
| [39.35355, 34.91032](https://www.google.com/maps?q=39.35355,34.91032) | 2024-10-08 11:02 | 345.5 | 5.21 | Orta | Gündüz |
| [39.42287, 32.30914](https://www.google.com/maps?q=39.42287,32.30914) | 2024-10-08 11:02 | 340.36 | 3.43 | Orta | Gündüz |
| [39.44176, 35.40675](https://www.google.com/maps?q=39.44176,35.40675) | 2024-10-08 11:02 | 336.42 | 2.1 | Orta | Gündüz |
| [39.54721, 35.3937](https://www.google.com/maps?q=39.54721,35.3937) | 2024-10-08 11:02 | 342.1 | 7.52 | Orta | Gündüz |
| [39.61154, 32.6241](https://www.google.com/maps?q=39.61154,32.6241) | 2024-10-08 11:02 | 341.19 | 3.78 | Orta | Gündüz |
| [39.74158, 29.44422](https://www.google.com/maps?q=39.74158,29.44422) | 2024-10-08 11:02 | 335.6 | 2.93 | Orta | Gündüz |
| [39.75248, 27.96142](https://www.google.com/maps?q=39.75248,27.96142) | 2024-10-08 11:02 | 340.3 | 5.98 | Orta | Gündüz |
| [39.80329, 37.66984](https://www.google.com/maps?q=39.80329,37.66984) | 2024-10-08 11:02 | 334.84 | 6.54 | Düşük | Gündüz |
| [39.80692, 37.67166](https://www.google.com/maps?q=39.80692,37.67166) | 2024-10-08 11:02 | 331.08 | 4.84 | Düşük | Gündüz |
| [39.80799, 37.66933](https://www.google.com/maps?q=39.80799,37.66933) | 2024-10-08 11:02 | 334.55 | 9.76 | Düşük | Gündüz |
| [39.81163, 37.67127](https://www.google.com/maps?q=39.81163,37.67127) | 2024-10-08 11:02 | 335.93 | 4.84 | Düşük | Gündüz |
| [39.83176, 36.94193](https://www.google.com/maps?q=39.83176,36.94193) | 2024-10-08 11:02 | 330.81 | 5.22 | Orta | Gündüz |
| [39.86497, 26.2452](https://www.google.com/maps?q=39.86497,26.2452) | 2024-10-08 11:02 | 335.91 | 1.93 | Orta | Gündüz |
| [39.93633, 26.23092](https://www.google.com/maps?q=39.93633,26.23092) | 2024-10-08 11:02 | 332.3 | 1.38 | Orta | Gündüz |
| [39.9398, 26.21023](https://www.google.com/maps?q=39.9398,26.21023) | 2024-10-08 11:02 | 336.59 | 2.34 | Orta | Gündüz |
| [39.95913, 26.19968](https://www.google.com/maps?q=39.95913,26.19968) | 2024-10-08 11:02 | 331.01 | 1.72 | Orta | Gündüz |
| [39.96087, 26.18933](https://www.google.com/maps?q=39.96087,26.18933) | 2024-10-08 11:02 | 340.85 | 9.06 | Orta | Gündüz |
| [40.14174, 27.95273](https://www.google.com/maps?q=40.14174,27.95273) | 2024-10-08 11:02 | 334.19 | 2.64 | Orta | Gündüz |
| [40.16389, 28.27303](https://www.google.com/maps?q=40.16389,28.27303) | 2024-10-08 11:02 | 331.34 | 1.01 | Orta | Gündüz |
| [40.23795, 27.89574](https://www.google.com/maps?q=40.23795,27.89574) | 2024-10-08 11:02 | 330.56 | 2.01 | Düşük | Gündüz |
| [40.25654, 27.77391](https://www.google.com/maps?q=40.25654,27.77391) | 2024-10-08 11:02 | 336.6 | 2.22 | Orta | Gündüz |
| [40.30805, 27.88791](https://www.google.com/maps?q=40.30805,27.88791) | 2024-10-08 11:02 | 336.82 | 3.76 | Orta | Gündüz |
| [40.71091, 30.6621](https://www.google.com/maps?q=40.71091,30.6621) | 2024-10-08 11:02 | 330.86 | 2.52 | Orta | Gündüz |
| [40.71433, 30.66132](https://www.google.com/maps?q=40.71433,30.66132) | 2024-10-08 11:02 | 337.35 | 2.52 | Orta | Gündüz |
| [40.71497, 30.66621](https://www.google.com/maps?q=40.71497,30.66621) | 2024-10-08 11:02 | 331.64 | 2.52 | Orta | Gündüz |
| [40.73215, 30.582](https://www.google.com/maps?q=40.73215,30.582) | 2024-10-08 11:02 | 334.36 | 4.28 | Orta | Gündüz |
| [40.75865, 26.13249](https://www.google.com/maps?q=40.75865,26.13249) | 2024-10-08 11:02 | 341.4 | 3.4 | Orta | Gündüz |
| [40.76011, 36.46033](https://www.google.com/maps?q=40.76011,36.46033) | 2024-10-08 11:02 | 333.1 | 3.2 | Orta | Gündüz |
| [40.7666, 30.44425](https://www.google.com/maps?q=40.7666,30.44425) | 2024-10-08 11:02 | 331.07 | 2.6 | Orta | Gündüz |
| [40.77728, 30.47173](https://www.google.com/maps?q=40.77728,30.47173) | 2024-10-08 11:02 | 329.13 | 1.77 | Düşük | Gündüz |
| [40.78259, 30.49322](https://www.google.com/maps?q=40.78259,30.49322) | 2024-10-08 11:02 | 339.7 | 3.72 | Orta | Gündüz |
| [40.78392, 30.49519](https://www.google.com/maps?q=40.78392,30.49519) | 2024-10-08 11:02 | 344.06 | 5.81 | Orta | Gündüz |
| [40.79079, 26.15427](https://www.google.com/maps?q=40.79079,26.15427) | 2024-10-08 11:02 | 337.17 | 4.1 | Orta | Gündüz |
| [40.82076, 26.26836](https://www.google.com/maps?q=40.82076,26.26836) | 2024-10-08 11:02 | 331.76 | 4.13 | Orta | Gündüz |
| [40.82598, 26.23739](https://www.google.com/maps?q=40.82598,26.23739) | 2024-10-08 11:02 | 342.45 | 4.51 | Orta | Gündüz |
| [40.89384, 29.29025](https://www.google.com/maps?q=40.89384,29.29025) | 2024-10-08 11:02 | 337.33 | 4.11 | Orta | Gündüz |
| [40.98558, 30.51943](https://www.google.com/maps?q=40.98558,30.51943) | 2024-10-08 11:02 | 342.86 | 3.88 | Orta | Gündüz |
| [41.01717, 27.50978](https://www.google.com/maps?q=41.01717,27.50978) | 2024-10-08 11:02 | 330.1 | 1.47 | Orta | Gündüz |
| [41.03822, 26.66448](https://www.google.com/maps?q=41.03822,26.66448) | 2024-10-08 11:02 | 335.27 | 5.57 | Düşük | Gündüz |
| [41.0602, 26.39253](https://www.google.com/maps?q=41.0602,26.39253) | 2024-10-08 11:02 | 337.37 | 5.06 | Orta | Gündüz |
| [41.07797, 26.58193](https://www.google.com/maps?q=41.07797,26.58193) | 2024-10-08 11:02 | 332.51 | 2.17 | Orta | Gündüz |
| [41.08335, 28.00237](https://www.google.com/maps?q=41.08335,28.00237) | 2024-10-08 11:02 | 335.53 | 1.41 | Düşük | Gündüz |
| [41.13078, 35.504](https://www.google.com/maps?q=41.13078,35.504) | 2024-10-08 11:02 | 341.68 | 4.08 | Orta | Gündüz |
| [41.17768, 32.63659](https://www.google.com/maps?q=41.17768,32.63659) | 2024-10-08 11:02 | 337.71 | 5.44 | Orta | Gündüz |
| [41.29388, 26.78811](https://www.google.com/maps?q=41.29388,26.78811) | 2024-10-08 11:02 | 332.16 | 1.93 | Düşük | Gündüz |
| [41.29718, 26.78716](https://www.google.com/maps?q=41.29718,26.78716) | 2024-10-08 11:02 | 351.05 | 8.59 | Orta | Gündüz |
| [41.30296, 27.1216](https://www.google.com/maps?q=41.30296,27.1216) | 2024-10-08 11:02 | 339.43 | 15.37 | Orta | Gündüz |
| [41.81167, 26.76877](https://www.google.com/maps?q=41.81167,26.76877) | 2024-10-08 11:02 | 338.75 | 2.86 | Orta | Gündüz |
| [41.89735, 26.75074](https://www.google.com/maps?q=41.89735,26.75074) | 2024-10-08 11:02 | 334.93 | 4.14 | Orta | Gündüz |
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
