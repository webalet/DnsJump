import socket
import time
from urllib.parse import urlparse

class DNSSpeedTester:
    """DNS hız testlerini yöneten sınıf"""
    
    @staticmethod
    def test_dns_speed(url):
        """Belirtilen URL için DNS çözümleme hızını test eder"""
        try:
            # URL'yi düzenle
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            domain = urlparse(url).netloc
            if not domain:
                return float('inf')
            
            # Hız testi
            start_time = time.time()
            socket.gethostbyname(domain)
            end_time = time.time()
            
            return end_time - start_time
        except Exception:
            return float('inf') 