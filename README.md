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
### Son Güncelleme: 2024-10-07 11:18:27 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [39.86436, 26.246](https://www.google.com/maps?q=39.86436,26.246) | 2024-10-07 01:13 | 295.18 | 0.97 | Orta | Gece |
| [38.73795, 26.94567](https://www.google.com/maps?q=38.73795,26.94567) | 2024-10-07 01:15 | 298.28 | 2.59 | Orta | Gece |
| [38.7388, 26.94717](https://www.google.com/maps?q=38.7388,26.94717) | 2024-10-07 01:15 | 298.55 | 1.2 | Orta | Gece |
| [36.77579, 39.3457](https://www.google.com/maps?q=36.77579,39.3457) | 2024-10-07 09:15 | 332.77 | 4.85 | Düşük | Gündüz |
| [36.86814, 39.42882](https://www.google.com/maps?q=36.86814,39.42882) | 2024-10-07 09:15 | 332.94 | 7.81 | Orta | Gündüz |
| [36.96685, 39.66362](https://www.google.com/maps?q=36.96685,39.66362) | 2024-10-07 09:15 | 341.27 | 15.36 | Orta | Gündüz |
| [37.13266, 39.46749](https://www.google.com/maps?q=37.13266,39.46749) | 2024-10-07 09:15 | 334.08 | 5.08 | Orta | Gündüz |
| [37.16397, 41.69198](https://www.google.com/maps?q=37.16397,41.69198) | 2024-10-07 09:15 | 334.57 | 12.07 | Orta | Gündüz |
| [37.16556, 41.69752](https://www.google.com/maps?q=37.16556,41.69752) | 2024-10-07 09:15 | 367.0 | 12.07 | Yüksek | Gündüz |
| [37.17137, 41.69504](https://www.google.com/maps?q=37.17137,41.69504) | 2024-10-07 09:15 | 367.0 | 19.36 | Yüksek | Gündüz |
| [37.25735, 42.64337](https://www.google.com/maps?q=37.25735,42.64337) | 2024-10-07 09:15 | 367.0 | 17.14 | Yüksek | Gündüz |
| [37.25798, 42.64129](https://www.google.com/maps?q=37.25798,42.64129) | 2024-10-07 09:15 | 367.0 | 15.55 | Yüksek | Gündüz |
| [37.27065, 42.44252](https://www.google.com/maps?q=37.27065,42.44252) | 2024-10-07 09:15 | 349.95 | 8.28 | Orta | Gündüz |
| [37.28446, 42.38019](https://www.google.com/maps?q=37.28446,42.38019) | 2024-10-07 09:15 | 344.14 | 4.54 | Orta | Gündüz |
| [37.44448, 39.07103](https://www.google.com/maps?q=37.44448,39.07103) | 2024-10-07 09:15 | 342.58 | 8.61 | Orta | Gündüz |
| [37.47618, 39.47619](https://www.google.com/maps?q=37.47618,39.47619) | 2024-10-07 09:15 | 340.34 | 9.9 | Orta | Gündüz |
| [37.49474, 38.65252](https://www.google.com/maps?q=37.49474,38.65252) | 2024-10-07 09:15 | 333.09 | 13.56 | Orta | Gündüz |
| [37.49604, 38.65269](https://www.google.com/maps?q=37.49604,38.65269) | 2024-10-07 09:15 | 336.34 | 20.27 | Orta | Gündüz |
| [37.65258, 38.29291](https://www.google.com/maps?q=37.65258,38.29291) | 2024-10-07 09:15 | 338.64 | 14.62 | Orta | Gündüz |
| [37.65369, 38.29518](https://www.google.com/maps?q=37.65369,38.29518) | 2024-10-07 09:15 | 334.21 | 10.25 | Orta | Gündüz |
| [37.6906, 40.47544](https://www.google.com/maps?q=37.6906,40.47544) | 2024-10-07 09:15 | 330.9 | 5.03 | Orta | Gündüz |
| [37.70132, 39.6298](https://www.google.com/maps?q=37.70132,39.6298) | 2024-10-07 09:15 | 332.21 | 4.94 | Orta | Gündüz |
| [37.73348, 38.80359](https://www.google.com/maps?q=37.73348,38.80359) | 2024-10-07 09:15 | 331.51 | 4.68 | Orta | Gündüz |
| [37.75193, 40.43914](https://www.google.com/maps?q=37.75193,40.43914) | 2024-10-07 09:15 | 335.87 | 9.12 | Orta | Gündüz |
| [37.7535, 40.19369](https://www.google.com/maps?q=37.7535,40.19369) | 2024-10-07 09:15 | 331.18 | 4.1 | Orta | Gündüz |
| [37.75463, 40.43758](https://www.google.com/maps?q=37.75463,40.43758) | 2024-10-07 09:15 | 367.0 | 18.04 | Yüksek | Gündüz |
| [37.75785, 40.43604](https://www.google.com/maps?q=37.75785,40.43604) | 2024-10-07 09:15 | 353.41 | 9.12 | Orta | Gündüz |
| [37.96112, 41.04786](https://www.google.com/maps?q=37.96112,41.04786) | 2024-10-07 09:15 | 341.8 | 5.89 | Orta | Gündüz |
| [37.98623, 41.04331](https://www.google.com/maps?q=37.98623,41.04331) | 2024-10-07 09:15 | 331.45 | 16.68 | Orta | Gündüz |
| [37.98782, 41.04873](https://www.google.com/maps?q=37.98782,41.04873) | 2024-10-07 09:15 | 367.0 | 16.68 | Yüksek | Gündüz |
| [37.99099, 41.12686](https://www.google.com/maps?q=37.99099,41.12686) | 2024-10-07 09:15 | 331.24 | 4.53 | Orta | Gündüz |
| [38.0038, 40.94506](https://www.google.com/maps?q=38.0038,40.94506) | 2024-10-07 09:15 | 367.0 | 17.32 | Yüksek | Gündüz |
| [38.00487, 40.94678](https://www.google.com/maps?q=38.00487,40.94678) | 2024-10-07 09:15 | 367.0 | 19.64 | Yüksek | Gündüz |
| [38.00969, 40.94249](https://www.google.com/maps?q=38.00969,40.94249) | 2024-10-07 09:15 | 348.46 | 7.35 | Orta | Gündüz |
| [38.03655, 40.20902](https://www.google.com/maps?q=38.03655,40.20902) | 2024-10-07 09:15 | 331.96 | 4.81 | Orta | Gündüz |
| [38.06155, 40.91387](https://www.google.com/maps?q=38.06155,40.91387) | 2024-10-07 09:15 | 367.0 | 19.47 | Yüksek | Gündüz |
| [38.07917, 40.88334](https://www.google.com/maps?q=38.07917,40.88334) | 2024-10-07 09:15 | 367.0 | 10.46 | Yüksek | Gündüz |
| [38.07999, 40.88624](https://www.google.com/maps?q=38.07999,40.88624) | 2024-10-07 09:15 | 352.55 | 9.32 | Orta | Gündüz |
| [38.08253, 40.3829](https://www.google.com/maps?q=38.08253,40.3829) | 2024-10-07 09:15 | 331.46 | 3.48 | Orta | Gündüz |
| [38.08579, 40.32597](https://www.google.com/maps?q=38.08579,40.32597) | 2024-10-07 09:15 | 333.5 | 4.83 | Düşük | Gündüz |
| [38.11976, 41.32242](https://www.google.com/maps?q=38.11976,41.32242) | 2024-10-07 09:15 | 340.69 | 15.53 | Orta | Gündüz |
| [38.12278, 41.32272](https://www.google.com/maps?q=38.12278,41.32272) | 2024-10-07 09:15 | 340.14 | 18.5 | Orta | Gündüz |
| [38.12301, 41.33372](https://www.google.com/maps?q=38.12301,41.33372) | 2024-10-07 09:15 | 351.99 | 15.75 | Orta | Gündüz |
| [38.12471, 39.77808](https://www.google.com/maps?q=38.12471,39.77808) | 2024-10-07 09:15 | 330.46 | 1.52 | Orta | Gündüz |
| [38.12611, 41.33407](https://www.google.com/maps?q=38.12611,41.33407) | 2024-10-07 09:15 | 367.0 | 26.44 | Yüksek | Gündüz |
| [38.12869, 41.33094](https://www.google.com/maps?q=38.12869,41.33094) | 2024-10-07 09:15 | 367.0 | 15.75 | Yüksek | Gündüz |
| [38.14295, 40.94125](https://www.google.com/maps?q=38.14295,40.94125) | 2024-10-07 09:15 | 333.5 | 6.33 | Düşük | Gündüz |
| [38.1598, 41.0465](https://www.google.com/maps?q=38.1598,41.0465) | 2024-10-07 09:15 | 333.15 | 5.91 | Orta | Gündüz |
| [38.16002, 41.04332](https://www.google.com/maps?q=38.16002,41.04332) | 2024-10-07 09:15 | 337.79 | 5.76 | Orta | Gündüz |
| [38.16881, 39.66999](https://www.google.com/maps?q=38.16881,39.66999) | 2024-10-07 09:15 | 353.33 | 8.38 | Orta | Gündüz |
| [38.16975, 39.67046](https://www.google.com/maps?q=38.16975,39.67046) | 2024-10-07 09:15 | 351.93 | 7.91 | Orta | Gündüz |
| [39.185, 42.08452](https://www.google.com/maps?q=39.185,42.08452) | 2024-10-07 09:15 | 337.87 | 5.07 | Orta | Gündüz |
| [39.20628, 37.01396](https://www.google.com/maps?q=39.20628,37.01396) | 2024-10-07 09:15 | 367.0 | 24.23 | Yüksek | Gündüz |
| [39.96741, 42.4338](https://www.google.com/maps?q=39.96741,42.4338) | 2024-10-07 09:15 | 331.28 | 4.65 | Orta | Gündüz |
| [40.82919, 39.22511](https://www.google.com/maps?q=40.82919,39.22511) | 2024-10-07 09:15 | 335.8 | 5.01 | Orta | Gündüz |
| [36.69537, 36.20151](https://www.google.com/maps?q=36.69537,36.20151) | 2024-10-07 00:22 | 304.24 | 2.59 | Orta | Gece |
| [36.71651, 36.1978](https://www.google.com/maps?q=36.71651,36.1978) | 2024-10-07 00:22 | 314.94 | 1.82 | Orta | Gece |
| [36.73285, 36.20795](https://www.google.com/maps?q=36.73285,36.20795) | 2024-10-07 00:22 | 305.61 | 1.94 | Orta | Gece |
| [36.86938, 34.75883](https://www.google.com/maps?q=36.86938,34.75883) | 2024-10-07 00:22 | 301.96 | 1.26 | Orta | Gece |
| [37.01575, 36.10273](https://www.google.com/maps?q=37.01575,36.10273) | 2024-10-07 00:22 | 306.48 | 1.14 | Orta | Gece |
| [37.01651, 36.10246](https://www.google.com/maps?q=37.01651,36.10246) | 2024-10-07 00:22 | 305.4 | 1.45 | Orta | Gece |
| [37.35179, 37.15852](https://www.google.com/maps?q=37.35179,37.15852) | 2024-10-07 00:22 | 301.89 | 1.18 | Orta | Gece |
| [37.4204, 38.71975](https://www.google.com/maps?q=37.4204,38.71975) | 2024-10-07 00:22 | 295.58 | 1.36 | Orta | Gece |
| [37.56284, 37.36121](https://www.google.com/maps?q=37.56284,37.36121) | 2024-10-07 00:22 | 297.17 | 0.94 | Orta | Gece |
| [37.56437, 37.36372](https://www.google.com/maps?q=37.56437,37.36372) | 2024-10-07 00:22 | 295.46 | 0.93 | Orta | Gece |
| [37.71218, 39.62312](https://www.google.com/maps?q=37.71218,39.62312) | 2024-10-07 00:22 | 305.81 | 1.52 | Orta | Gece |
| [37.71371, 39.62346](https://www.google.com/maps?q=37.71371,39.62346) | 2024-10-07 00:22 | 301.14 | 1.36 | Orta | Gece |
| [37.73806, 38.17754](https://www.google.com/maps?q=37.73806,38.17754) | 2024-10-07 00:22 | 295.72 | 0.95 | Orta | Gece |
| [37.73972, 38.17695](https://www.google.com/maps?q=37.73972,38.17695) | 2024-10-07 00:22 | 300.62 | 0.75 | Orta | Gece |
| [37.75072, 38.18311](https://www.google.com/maps?q=37.75072,38.18311) | 2024-10-07 00:22 | 295.11 | 0.54 | Orta | Gece |
| [37.75237, 38.18257](https://www.google.com/maps?q=37.75237,38.18257) | 2024-10-07 00:22 | 296.59 | 0.65 | Orta | Gece |
| [37.76781, 38.10897](https://www.google.com/maps?q=37.76781,38.10897) | 2024-10-07 00:22 | 299.55 | 1.44 | Orta | Gece |
| [37.76869, 38.10287](https://www.google.com/maps?q=37.76869,38.10287) | 2024-10-07 00:22 | 305.67 | 2.19 | Orta | Gece |
| [37.76991, 38.10212](https://www.google.com/maps?q=37.76991,38.10212) | 2024-10-07 00:22 | 304.22 | 2.23 | Orta | Gece |
| [37.85414, 38.80787](https://www.google.com/maps?q=37.85414,38.80787) | 2024-10-07 00:22 | 301.81 | 1.76 | Orta | Gece |
| [37.85779, 38.80428](https://www.google.com/maps?q=37.85779,38.80428) | 2024-10-07 00:22 | 304.27 | 1.33 | Orta | Gece |
| [37.95127, 34.68346](https://www.google.com/maps?q=37.95127,34.68346) | 2024-10-07 00:22 | 295.56 | 0.42 | Orta | Gece |
| [38.23485, 39.20516](https://www.google.com/maps?q=38.23485,39.20516) | 2024-10-07 00:22 | 304.33 | 0.99 | Orta | Gece |
| [38.23693, 39.20382](https://www.google.com/maps?q=38.23693,39.20382) | 2024-10-07 00:22 | 301.2 | 1.29 | Orta | Gece |
| [38.42557, 27.21623](https://www.google.com/maps?q=38.42557,27.21623) | 2024-10-07 00:22 | 308.67 | 2.24 | Orta | Gece |
| [38.45552, 38.71887](https://www.google.com/maps?q=38.45552,38.71887) | 2024-10-07 00:22 | 297.94 | 1.55 | Orta | Gece |
| [38.45712, 38.72061](https://www.google.com/maps?q=38.45712,38.72061) | 2024-10-07 00:22 | 301.6 | 1.45 | Orta | Gece |
| [38.57057, 36.2023](https://www.google.com/maps?q=38.57057,36.2023) | 2024-10-07 00:22 | 299.02 | 1.59 | Orta | Gece |
| [38.57135, 36.20541](https://www.google.com/maps?q=38.57135,36.20541) | 2024-10-07 00:22 | 308.82 | 1.43 | Orta | Gece |
| [38.66109, 30.61796](https://www.google.com/maps?q=38.66109,30.61796) | 2024-10-07 00:22 | 300.0 | 1.29 | Orta | Gece |
| [38.73703, 26.94598](https://www.google.com/maps?q=38.73703,26.94598) | 2024-10-07 00:22 | 318.32 | 1.62 | Orta | Gece |
| [38.73816, 26.94037](https://www.google.com/maps?q=38.73816,26.94037) | 2024-10-07 00:22 | 302.42 | 1.62 | Orta | Gece |
| [38.74037, 26.9293](https://www.google.com/maps?q=38.74037,26.9293) | 2024-10-07 00:22 | 314.2 | 2.21 | Orta | Gece |
| [38.74796, 26.94956](https://www.google.com/maps?q=38.74796,26.94956) | 2024-10-07 00:22 | 304.27 | 0.67 | Orta | Gece |
| [38.75383, 26.93958](https://www.google.com/maps?q=38.75383,26.93958) | 2024-10-07 00:22 | 301.32 | 0.92 | Orta | Gece |
| [38.76257, 36.58544](https://www.google.com/maps?q=38.76257,36.58544) | 2024-10-07 00:22 | 304.01 | 0.98 | Orta | Gece |
| [39.09291, 27.5109](https://www.google.com/maps?q=39.09291,27.5109) | 2024-10-07 00:22 | 302.7 | 1.71 | Orta | Gece |
| [39.48316, 30.04098](https://www.google.com/maps?q=39.48316,30.04098) | 2024-10-07 00:22 | 311.01 | 1.72 | Orta | Gece |
| [39.60814, 27.87565](https://www.google.com/maps?q=39.60814,27.87565) | 2024-10-07 00:22 | 299.19 | 0.67 | Orta | Gece |
| [39.86575, 26.24127](https://www.google.com/maps?q=39.86575,26.24127) | 2024-10-07 00:22 | 308.69 | 0.86 | Orta | Gece |
| [40.04577, 34.87502](https://www.google.com/maps?q=40.04577,34.87502) | 2024-10-07 00:22 | 295.19 | 0.38 | Orta | Gece |
| [40.44155, 27.14017](https://www.google.com/maps?q=40.44155,27.14017) | 2024-10-07 00:22 | 306.59 | 1.02 | Orta | Gece |
| [41.24519, 36.4604](https://www.google.com/maps?q=41.24519,36.4604) | 2024-10-07 00:22 | 301.62 | 1.93 | Orta | Gece |
| [41.79901, 26.7009](https://www.google.com/maps?q=41.79901,26.7009) | 2024-10-07 00:22 | 298.2 | 0.63 | Orta | Gece |
| [36.26534, 33.72834](https://www.google.com/maps?q=36.26534,33.72834) | 2024-10-07 00:24 | 304.52 | 0.67 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
