# Yangın Verileri Takip Sistemi

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
Bu script, çekilen son verileri işleyerek, **README.md** dosyasına bir tablo halinde kaydeder. Tabloda yangınların enlem, boylam, sıcaklık, güven seviyesi ve gündüz/gece bilgileri yer alır. Güncellemeler her çalıştırıldığında otomatik olarak yapılır ve dosyanın üzerine yazılır, böylece en güncel veriler her zaman README.md dosyasında bulunur. Verilerin nasıl kullanılabileceğine bir örnektir.

## Son Yangın Verileri
### Son Güncelleme: 2024-10-03 10:33:20 (UTC)

| Koordinatlar (Enlem, Boylam) | Tarih ve Saat | Sıcaklık | FRP | Güven Seviyesi | Gündüz/Gece |
|-----------------------------|----------------|----------|-----|----------------|-------------|
| [38.73819, 26.9503](https://www.google.com/maps?q=38.73819,26.9503) | 2024-10-03 01:13 | 298.7 | 1.46 | Orta | Gece |
| [38.7401, 26.94492](https://www.google.com/maps?q=38.7401,26.94492) | 2024-10-03 01:13 | 297.34 | 1.47 | Orta | Gece |
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
