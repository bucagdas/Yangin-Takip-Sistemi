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
### Son Güncelleme: 2024-10-09 11:16:18 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.658, 30.62281](https://www.google.com/maps?q=38.658,30.62281) | 2024-10-09 01:00 | 295.18 | 1.75 | Orta | Gece |
| [39.48585, 30.03926](https://www.google.com/maps?q=39.48585,30.03926) | 2024-10-09 01:00 | 299.05 | 1.36 | Orta | Gece |
| [39.86287, 26.24636](https://www.google.com/maps?q=39.86287,26.24636) | 2024-10-09 01:00 | 298.38 | 0.67 | Orta | Gece |
| [39.8642, 26.24167](https://www.google.com/maps?q=39.8642,26.24167) | 2024-10-09 01:00 | 299.03 | 0.67 | Orta | Gece |
| [41.01852, 28.55115](https://www.google.com/maps?q=41.01852,28.55115) | 2024-10-09 01:00 | 296.65 | 1.1 | Orta | Gece |
| [41.17476, 32.63312](https://www.google.com/maps?q=41.17476,32.63312) | 2024-10-09 01:00 | 295.42 | 1.37 | Orta | Gece |
| [41.25723, 31.4273](https://www.google.com/maps?q=41.25723,31.4273) | 2024-10-09 01:00 | 295.28 | 1.06 | Orta | Gece |
| [41.26027, 31.42624](https://www.google.com/maps?q=41.26027,31.42624) | 2024-10-09 01:00 | 297.42 | 2.08 | Orta | Gece |
| [38.73525, 26.94477](https://www.google.com/maps?q=38.73525,26.94477) | 2024-10-09 01:02 | 307.9 | 1.29 | Orta | Gece |
| [38.73815, 26.94691](https://www.google.com/maps?q=38.73815,26.94691) | 2024-10-09 01:02 | 305.99 | 1.76 | Orta | Gece |
| [38.74086, 26.94767](https://www.google.com/maps?q=38.74086,26.94767) | 2024-10-09 01:02 | 300.87 | 1.29 | Orta | Gece |
| [38.74382, 26.94958](https://www.google.com/maps?q=38.74382,26.94958) | 2024-10-09 01:02 | 314.21 | 1.76 | Orta | Gece |
| [38.74649, 26.95049](https://www.google.com/maps?q=38.74649,26.95049) | 2024-10-09 01:02 | 316.08 | 1.29 | Orta | Gece |
| [39.86474, 26.24561](https://www.google.com/maps?q=39.86474,26.24561) | 2024-10-09 01:02 | 312.4 | 1.14 | Orta | Gece |
| [41.17396, 32.63101](https://www.google.com/maps?q=41.17396,32.63101) | 2024-10-09 00:35 | 304.2 | 1.45 | Orta | Gece |
| [41.2384, 36.46494](https://www.google.com/maps?q=41.2384,36.46494) | 2024-10-09 00:35 | 300.55 | 1.98 | Orta | Gece |
| [41.24302, 36.46657](https://www.google.com/maps?q=41.24302,36.46657) | 2024-10-09 00:35 | 308.67 | 3.02 | Orta | Gece |
| [37.89831, 34.87511](https://www.google.com/maps?q=37.89831,34.87511) | 2024-10-09 00:37 | 323.87 | 4.42 | Orta | Gece |
| [37.89923, 30.49264](https://www.google.com/maps?q=37.89923,30.49264) | 2024-10-09 00:37 | 295.26 | 0.8 | Orta | Gece |
| [38.4253, 27.21837](https://www.google.com/maps?q=38.4253,27.21837) | 2024-10-09 00:37 | 300.65 | 0.72 | Orta | Gece |
| [38.6594, 30.61952](https://www.google.com/maps?q=38.6594,30.61952) | 2024-10-09 00:37 | 316.37 | 1.72 | Orta | Gece |
| [38.73613, 26.9445](https://www.google.com/maps?q=38.73613,26.9445) | 2024-10-09 00:37 | 310.55 | 2.67 | Orta | Gece |
| [38.73663, 26.93263](https://www.google.com/maps?q=38.73663,26.93263) | 2024-10-09 00:37 | 302.78 | 2.5 | Orta | Gece |
| [38.73849, 26.94459](https://www.google.com/maps?q=38.73849,26.94459) | 2024-10-09 00:37 | 303.05 | 2.17 | Orta | Gece |
| [38.7397, 26.92908](https://www.google.com/maps?q=38.7397,26.92908) | 2024-10-09 00:37 | 309.44 | 1.41 | Orta | Gece |
| [38.74453, 26.94767](https://www.google.com/maps?q=38.74453,26.94767) | 2024-10-09 00:37 | 319.78 | 3.88 | Orta | Gece |
| [39.16717, 27.63098](https://www.google.com/maps?q=39.16717,27.63098) | 2024-10-09 00:37 | 307.45 | 1.41 | Orta | Gece |
| [39.48624, 30.04153](https://www.google.com/maps?q=39.48624,30.04153) | 2024-10-09 00:37 | 313.33 | 1.54 | Orta | Gece |
| [39.60861, 27.87789](https://www.google.com/maps?q=39.60861,27.87789) | 2024-10-09 00:37 | 297.95 | 0.45 | Orta | Gece |
| [39.86631, 26.24439](https://www.google.com/maps?q=39.86631,26.24439) | 2024-10-09 00:37 | 314.78 | 2.27 | Orta | Gece |
| [41.01751, 28.55664](https://www.google.com/maps?q=41.01751,28.55664) | 2024-10-09 00:37 | 299.72 | 1.66 | Orta | Gece |
| [41.26463, 31.42499](https://www.google.com/maps?q=41.26463,31.42499) | 2024-10-09 00:37 | 296.32 | 0.7 | Orta | Gece |
| [41.79562, 26.70242](https://www.google.com/maps?q=41.79562,26.70242) | 2024-10-09 00:37 | 300.57 | 0.84 | Orta | Gece |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
