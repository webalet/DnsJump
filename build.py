import PyInstaller.__main__
import os

def build_exe():
    """Uygulamayı exe dosyasına dönüştürür"""
    print("Exe dosyası oluşturuluyor...")
    
    # Build parametreleri
    params = [
        'run.py',                        # Ana dosya
        '--onefile',                     # Tek dosya olarak paketle
        '--noconsole',                   # Konsol penceresi gösterme
        '--name=DNS_Hiz_Test',           # Exe adı
        '--clean',                       # Temiz build
        '--add-data=src;src'             # Kaynak kodları dahil et
    ]
    
    # Build işlemini başlat
    PyInstaller.__main__.run(params)
    
    print("\nExe dosyası oluşturuldu!")
    print("Konum: dist/DNS_Hiz_Test.exe")

if __name__ == "__main__":
    build_exe() 