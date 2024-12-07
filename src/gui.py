import customtkinter as ctk
import threading
import webbrowser
from .dns_manager import DNSManager
from .dns_speed_tester import DNSSpeedTester
from .dns_providers import DNSProviders

class DNSSpeedTesterGUI:
    """DNS Hız Test Edici'nin grafiksel arayüzü"""
    
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("DNS Hız Test Edici")
        self.window.geometry("800x750")
        self.window.resizable(False, False)
        
        # Tema ayarları
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # DNS sağlayıcıları
        self.dns_servers = DNSProviders.PROVIDERS
        
        # DNS test sonuçları
        self.dns_results = {}
        
        # DNS yöneticisi
        self.dns_manager = DNSManager()
        
        # DNS test edici
        self.dns_tester = DNSSpeedTester()
        
        # GUI elemanları
        self.dns_cards = {}
        self.setup_ui()
        
    def setup_ui(self):
        """GUI elemanlarını oluşturur"""
        # Ana frame
        main_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Başlık
        title_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        title_frame.pack(fill="x", pady=(0, 20))
        
        title = ctk.CTkLabel(
            title_frame,
            text="DNS Hız Test Edici",
            font=("Segoe UI", 28, "bold"),
            text_color="#3B8ED0"
        )
        title.pack()
        
        subtitle = ctk.CTkLabel(
            title_frame,
            text="En hızlı DNS sunucusunu bulun",
            font=("Segoe UI", 12),
            text_color="#666666"
        )
        subtitle.pack()
        
        # Website giriş alanı
        input_frame = ctk.CTkFrame(main_frame, fg_color="#2B2B2B", corner_radius=10)
        input_frame.pack(fill="x", pady=15, padx=10)
        
        url_label = ctk.CTkLabel(
            input_frame,
            text="Web sitesi adresi:",
            font=("Segoe UI", 12, "bold")
        )
        url_label.pack(side="left", padx=15, pady=15)
        
        self.url_var = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(
            input_frame,
            textvariable=self.url_var,
            width=450,
            height=35,
            font=("Segoe UI", 12),
            placeholder_text="Örnek: google.com"
        )
        self.url_entry.pack(side="left", padx=15)
        
        # Buton frame
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=15)
        
        # Test butonu
        self.test_button = ctk.CTkButton(
            button_frame,
            text="DNS'leri Test Et",
            command=self.start_dns_test,
            width=180,
            height=40,
            font=("Segoe UI", 13, "bold"),
            fg_color="#3B8ED0",
            hover_color="#2B6FA0"
        )
        self.test_button.pack(side="left", padx=5)
        
        # Hakkında butonu
        about_button = ctk.CTkButton(
            button_frame,
            text="Hakkında",
            command=self.show_about,
            width=100,
            height=40,
            font=("Segoe UI", 13),
            fg_color="#2B2B2B",
            hover_color="#1B1B1B"
        )
        about_button.pack(side="left", padx=5)
        
        # DNS kartları için frame
        self.dns_cards_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        self.dns_cards_frame.pack(fill="x", pady=10)
        
        # Her DNS için kart oluştur
        for dns_name, dns_info in self.dns_servers.items():
            card = self.create_dns_card(dns_name, dns_info["color"])
            self.dns_cards[dns_name] = card
        
        # Ana progress bar
        progress_frame = ctk.CTkFrame(main_frame, fg_color="#2B2B2B", corner_radius=10)
        progress_frame.pack(fill="x", pady=15, padx=10)
        
        self.progress_label = ctk.CTkLabel(
            progress_frame,
            text="Test İlerlemesi",
            font=("Segoe UI", 12, "bold")
        )
        self.progress_label.pack(pady=(10, 0))
        
        self.progress_bar = ctk.CTkProgressBar(
            progress_frame,
            width=700,
            height=12,
            corner_radius=5,
            fg_color="#1B1B1B",
            progress_color="#3B8ED0"
        )
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        
        # Log alanı
        log_frame = ctk.CTkFrame(main_frame, fg_color="#2B2B2B", corner_radius=10)
        log_frame.pack(fill="both", expand=True, pady=15, padx=10)
        
        log_label = ctk.CTkLabel(
            log_frame,
            text="Test Sonuçları",
            font=("Segoe UI", 12, "bold")
        )
        log_label.pack(pady=(10, 0))
        
        self.log_text = ctk.CTkTextbox(
            log_frame,
            width=700,
            height=120,
            font=("Segoe UI", 11),
            fg_color="#1B1B1B",
            text_color="#FFFFFF"
        )
        self.log_text.pack(pady=10, padx=10)
        
    def show_about(self):
        """Hakkında penceresini gösterir"""
        about_window = ctk.CTkToplevel(self.window)
        about_window.title("Hakkında")
        about_window.geometry("400x300")
        about_window.resizable(False, False)
        
        # İçerik frame
        content_frame = ctk.CTkFrame(about_window, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Başlık
        title = ctk.CTkLabel(
            content_frame,
            text="DNS Hız Test Edici",
            font=("Segoe UI", 20, "bold"),
            text_color="#3B8ED0"
        )
        title.pack(pady=10)
        
        # Versiyon
        version = ctk.CTkLabel(
            content_frame,
            text="Versiyon 1.0.0",
            font=("Segoe UI", 12)
        )
        version.pack()
        
        # Geliştirici
        developer = ctk.CTkLabel(
            content_frame,
            text="Geliştirici: webalet",
            font=("Segoe UI", 12)
        )
        developer.pack(pady=10)
        
        # GitHub linki
        def open_github():
            webbrowser.open("https://github.com/webalet")
        
        github_button = ctk.CTkButton(
            content_frame,
            text="GitHub Profili",
            command=open_github,
            width=150,
            height=35,
            font=("Segoe UI", 12),
            fg_color="#2B2B2B",
            hover_color="#1B1B1B"
        )
        github_button.pack(pady=20)
        
        # Telif hakkı
        copyright_label = ctk.CTkLabel(
            content_frame,
            text="© 2024 webalet\nMIT Lisansı altında lisanslanmıştır.",
            font=("Segoe UI", 11),
            text_color="#666666"
        )
        copyright_label.pack(pady=20)
        
    def create_dns_card(self, dns_name, color):
        """Her DNS için bir kart oluşturur"""
        card_frame = ctk.CTkFrame(self.dns_cards_frame, fg_color="#2B2B2B", corner_radius=10)
        card_frame.pack(fill="x", padx=10, pady=3)
        
        icon_label = ctk.CTkLabel(
            card_frame,
            text="●",
            font=("Segoe UI", 18),
            text_color=color
        )
        icon_label.pack(side="left", padx=10)
        
        name_label = ctk.CTkLabel(
            card_frame,
            text=dns_name,
            font=("Segoe UI", 12, "bold")
        )
        name_label.pack(side="left", padx=10)
        
        speed_label = ctk.CTkLabel(
            card_frame,
            text="Bekleniyor...",
            font=("Segoe UI", 11),
            text_color="#888888"
        )
        speed_label.pack(side="right", padx=15)
        
        progress = ctk.CTkProgressBar(
            card_frame,
            width=250,
            height=8,
            corner_radius=5,
            fg_color="#1B1B1B",
            progress_color=color
        )
        progress.pack(side="right", padx=15, pady=12)
        progress.set(0)
        
        return {
            "frame": card_frame,
            "speed_label": speed_label,
            "progress": progress,
            "color": color
        }
        
    def log_message(self, message):
        """Mesajları text alanına ekler"""
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")
        
    def update_progress(self, dns_name, progress_value):
        """DNS kartındaki progress bar'ı günceller"""
        if dns_name in self.dns_cards:
            self.dns_cards[dns_name]["progress"].set(progress_value)
            self.window.update()
            
    def update_speed_label(self, dns_name, speed):
        """DNS kartındaki hız etiketini günceller"""
        if dns_name in self.dns_cards:
            if speed == float('inf'):
                self.dns_cards[dns_name]["speed_label"].configure(
                    text="Başarısız",
                    text_color="#FF4444"
                )
            else:
                self.dns_cards[dns_name]["speed_label"].configure(
                    text=f"{speed:.3f} sn",
                    text_color=self.dns_cards[dns_name]["color"]
                )
            self.window.update()
            
    def start_dns_test(self):
        """DNS testini başlatır"""
        url = self.url_var.get().strip()
        if not url:
            self.log_message("Lütfen bir web sitesi adresi girin!")
            return
        
        # Test butonunu devre dışı bırak
        self.test_button.configure(
            state="disabled",
            text="Test Ediliyor...",
            fg_color="#666666"
        )
        
        # Progress barları sıfırla
        for card in self.dns_cards.values():
            card["progress"].set(0)
            card["speed_label"].configure(text="Bekleniyor...", text_color="#888888")
        
        def run_tests():
            total_tests = len(self.dns_servers) + 1  # +1 for initial test
            current_test = 0
            
            self.log_message(f"\nTest başlatılıyor: {url}")
            
            # İlk test (DNS olmadan)
            self.log_message("\nMevcut ayarlarla test yapılıyor...")
            initial_speed = self.dns_tester.test_dns_speed(url)
            if initial_speed != float('inf'):
                self.log_message(f"Mevcut hız: {initial_speed:.3f} saniye")
                self.dns_results["Mevcut"] = initial_speed
            else:
                self.log_message("Mevcut ayarlarla bağlantı başarısız!")
            
            current_test += 1
            self.progress_bar.set(current_test / total_tests)
            
            # Ana adaptörü bul
            interface = self.dns_manager.get_main_interface()
            if not interface:
                self.log_message("Ana internet adaptörü bulunamadı!")
                return
            
            # Her DNS için test
            for dns_name, dns_info in self.dns_servers.items():
                self.log_message(f"\n{dns_name} test ediliyor...")
                
                # DNS'i değiştir
                if not self.dns_manager.change_dns(interface, dns_info["servers"][0], 
                    dns_info["servers"][1] if len(dns_info["servers"]) > 1 else None):
                    continue
                
                # DNS değişikliğinin etkili olması için bekle
                import time
                time.sleep(2)
                
                # Test yap
                speed = self.dns_tester.test_dns_speed(url)
                if speed != float('inf'):
                    self.dns_results[dns_name] = speed
                    self.update_speed_label(dns_name, speed)
                    self.log_message(f"Hız: {speed:.3f} saniye")
                else:
                    self.update_speed_label(dns_name, float('inf'))
                    self.log_message("Test başarısız!")
                
                current_test += 1
                self.progress_bar.set(current_test / total_tests)
                self.update_progress(dns_name, 1.0)
            
            # En hızlı DNS'i bul ve ayarla
            if self.dns_results:
                fastest_dns = min(self.dns_results.items(), key=lambda x: x[1])
                if fastest_dns[0] != "Mevcut":
                    self.log_message(f"\nEn hızlı DNS: {fastest_dns[0]} ({fastest_dns[1]:.3f} saniye)")
                    self.log_message("\nEn hızlı DNS ayarlanıyor...")
                    dns_info = self.dns_servers[fastest_dns[0]]
                    self.dns_manager.change_dns(interface, dns_info["servers"][0],
                        dns_info["servers"][1] if len(dns_info["servers"]) > 1 else None)
                else:
                    self.log_message("\nMevcut DNS ayarları en hızlı sonucu verdi.")
                
                self.log_message("İşlem tamamlandı!")
            else:
                self.log_message("\nHiçbir DNS ile bağlantı kurulamadı!")
            
            # Test butonunu tekrar aktif et
            self.test_button.configure(
                state="normal",
                text="DNS'leri Test Et",
                fg_color="#3B8ED0"
            )
        
        # Test işlemini ayrı bir thread'de başlat
        threading.Thread(target=run_tests, daemon=True).start()
        
    def run(self):
        """Uygulamayı başlatır"""
        # Pencereyi ekranın ortasına konumlandır
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 800
        window_height = 750
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.window.mainloop() 