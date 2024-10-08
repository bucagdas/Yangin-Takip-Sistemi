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
### Son Güncelleme: 2024-10-08 03:15:23 (UTC)

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

## Yazar

[sarusadgac](https://x.com/sarusadgac)
