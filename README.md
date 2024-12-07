# DNS Hız Test Edici

DNS Hız Test Edici, Windows sistemlerde farklı DNS sunucularını test edip en hızlısını otomatik olarak ayarlayan bir araçtır.

Geliştirici: [webalet](https://github.com/webalet)

## Özellikler

- Modern ve kullanıcı dostu arayüz
- Popüler DNS sağlayıcılarını test etme
- Otomatik DNS hız testi
- En hızlı DNS'i otomatik ayarlama
- Detaylı test sonuçları
- Görsel ilerleme göstergeleri

## Desteklenen DNS Sağlayıcıları

- Google DNS (8.8.8.8, 8.8.4.4)
- Cloudflare (1.1.1.1, 1.0.0.1)
- OpenDNS (208.67.222.222, 208.67.220.220)
- Quad9 (9.9.9.9, 149.112.112.112)
- AdGuard DNS (94.140.14.14, 94.140.15.15)

## Kurulum

### Kaynak Koddan Çalıştırma

1. Python 3.7 veya üstü sürümü yükleyin
2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```
3. Programı çalıştırın:
```bash
python run.py
```

### Exe Oluşturma

1. PyInstaller'ı yükleyin:
```bash
pip install pyinstaller
```

2. Exe dosyasını oluşturun:
```bash
python build.py
```

3. Oluşturulan exe dosyası `dist` klasöründe olacaktır

## Kullanım

1. Programı yönetici olarak çalıştırın
2. Test etmek istediğiniz web sitesini girin (örn: google.com)
3. "DNS'leri Test Et" butonuna tıklayın
4. Test sonuçlarını bekleyin
5. En hızlı DNS otomatik olarak ayarlanacaktır

## Geliştirme

Proje modüler bir yapıda tasarlanmıştır:

- `dns_manager.py`: DNS ayarlarını yöneten modül
- `dns_speed_tester.py`: DNS hız testlerini yapan modül
- `dns_providers.py`: DNS sağlayıcı bilgilerini içeren modül
- `gui.py`: Grafiksel arayüz modülü

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin yeni-ozellik`)
5. Pull Request oluşturun

## İletişim

Sorularınız ve önerileriniz için:
- GitHub: [@webalet](https://github.com/webalet)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın. 