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
### Son Güncelleme: 2024-10-06 06:28:47 (UTC)

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

## Yazar

[sarusadgac](https://x.com/sarusadgac)
