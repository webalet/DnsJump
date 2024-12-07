import subprocess

class DNSManager:
    """DNS ayarlarını yöneten sınıf"""
    
    @staticmethod
    def get_main_interface():
        """Ana internet adaptörünü tespit eder"""
        try:
            result = subprocess.run('ipconfig /all', shell=True, capture_output=True, text=True, encoding='cp857')
            output = result.stdout
            
            current_adapter = None
            for line in output.split('\n'):
                line = line.strip()
                if "adapter" in line and ":" in line:
                    current_adapter = line.split("adapter ")[-1].split(":")[0].strip()
                if current_adapter and "Default Gateway" in line and "192.168." in line:
                    return current_adapter
            return None
        except Exception as e:
            print(f"Ana adaptör tespitinde hata: {str(e)}")
            return None
            
    @staticmethod
    def change_dns(interface, primary_dns, secondary_dns=None):
        """DNS ayarlarını değiştirir"""
        try:
            # Birincil DNS
            cmd = f'netsh interface ipv4 set dns name="{interface}" static {primary_dns} primary'
            subprocess.run(cmd, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
            # İkincil DNS
            if secondary_dns:
                cmd = f'netsh interface ipv4 add dns name="{interface}" {secondary_dns} index=2'
                subprocess.run(cmd, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
            # DNS önbelleğini temizle
            subprocess.run('ipconfig /flushdns', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
            return True
            
        except Exception as e:
            print(f"DNS değiştirme hatası: {str(e)}")
            return False 