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
### Son Güncelleme: 2024-10-13 11:38:56 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.73752, 26.9477](https://www.google.com/maps?q=38.73752,26.9477) | 2024-10-13 01:02 | 299.34 | 1.52 | Orta | Gece |
| [38.7431, 26.95066](https://www.google.com/maps?q=38.7431,26.95066) | 2024-10-13 01:02 | 299.03 | 1.52 | Orta | Gece |
| [39.86452, 26.24288](https://www.google.com/maps?q=39.86452,26.24288) | 2024-10-13 01:02 | 307.68 | 1.39 | Orta | Gece |
| [37.12003, 41.64391](https://www.google.com/maps?q=37.12003,41.64391) | 2024-10-13 09:05 | 367.0 | 139.01 | Yüksek | Gündüz |
| [37.12156, 41.64454](https://www.google.com/maps?q=37.12156,41.64454) | 2024-10-13 09:05 | 367.0 | 67.83 | Yüksek | Gündüz |
| [37.12402, 41.63263](https://www.google.com/maps?q=37.12402,41.63263) | 2024-10-13 09:05 | 349.47 | 105.65 | Orta | Gündüz |
| [37.12558, 41.6332](https://www.google.com/maps?q=37.12558,41.6332) | 2024-10-13 09:05 | 354.65 | 330.59 | Orta | Gündüz |
| [37.12671, 41.64089](https://www.google.com/maps?q=37.12671,41.64089) | 2024-10-13 09:05 | 317.11 | 139.01 | Düşük | Gündüz |
| [37.12936, 41.64903](https://www.google.com/maps?q=37.12936,41.64903) | 2024-10-13 09:05 | 367.0 | 139.01 | Yüksek | Gündüz |
| [37.13083, 41.64966](https://www.google.com/maps?q=37.13083,41.64966) | 2024-10-13 09:05 | 367.0 | 140.34 | Yüksek | Gündüz |
| [37.29031, 42.43595](https://www.google.com/maps?q=37.29031,42.43595) | 2024-10-13 09:05 | 338.12 | 7.29 | Orta | Gündüz |
| [37.34447, 41.82109](https://www.google.com/maps?q=37.34447,41.82109) | 2024-10-13 09:05 | 342.3 | 8.69 | Orta | Gündüz |
| [38.00673, 41.00857](https://www.google.com/maps?q=38.00673,41.00857) | 2024-10-13 09:05 | 336.95 | 8.88 | Orta | Gündüz |
| [38.00872, 41.00898](https://www.google.com/maps?q=38.00872,41.00898) | 2024-10-13 09:05 | 346.14 | 14.25 | Orta | Gündüz |
| [38.01342, 41.00544](https://www.google.com/maps?q=38.01342,41.00544) | 2024-10-13 09:05 | 338.06 | 8.88 | Orta | Gündüz |
| [38.01546, 41.00596](https://www.google.com/maps?q=38.01546,41.00596) | 2024-10-13 09:05 | 328.71 | 3.64 | Düşük | Gündüz |
| [38.04552, 41.0555](https://www.google.com/maps?q=38.04552,41.0555) | 2024-10-13 09:05 | 367.0 | 26.53 | Yüksek | Gündüz |
| [38.04716, 41.05589](https://www.google.com/maps?q=38.04716,41.05589) | 2024-10-13 09:05 | 367.0 | 33.65 | Yüksek | Gündüz |
| [38.1779, 40.85252](https://www.google.com/maps?q=38.1779,40.85252) | 2024-10-13 09:05 | 332.77 | 8.33 | Orta | Gündüz |
| [38.18532, 40.8572](https://www.google.com/maps?q=38.18532,40.8572) | 2024-10-13 09:05 | 342.05 | 16.31 | Orta | Gündüz |
| [38.18771, 40.8588](https://www.google.com/maps?q=38.18771,40.8588) | 2024-10-13 09:05 | 337.13 | 8.33 | Orta | Gündüz |
| [38.22269, 40.66574](https://www.google.com/maps?q=38.22269,40.66574) | 2024-10-13 09:05 | 367.0 | 20.17 | Yüksek | Gündüz |
| [39.9794, 44.21943](https://www.google.com/maps?q=39.9794,44.21943) | 2024-10-13 09:05 | 347.38 | 11.85 | Orta | Gündüz |
| [40.02058, 44.10076](https://www.google.com/maps?q=40.02058,44.10076) | 2024-10-13 09:05 | 338.06 | 6.91 | Orta | Gündüz |
| [40.02113, 44.10191](https://www.google.com/maps?q=40.02113,44.10191) | 2024-10-13 09:05 | 347.15 | 6.77 | Orta | Gündüz |

## Yazar

[sarusadgac](https://x.com/sarusadgac)
