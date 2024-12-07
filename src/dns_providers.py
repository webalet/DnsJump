class DNSProviders:
    """DNS sağlayıcıları ve ayarları"""
    
    PROVIDERS = {
        "Google DNS": {
            "servers": ["8.8.8.8", "8.8.4.4"],
            "color": "#4285F4"  # Google Mavi
        },
        "Cloudflare": {
            "servers": ["1.1.1.1", "1.0.0.1"],
            "color": "#F48120"  # Cloudflare Turuncu
        },
        "OpenDNS": {
            "servers": ["208.67.222.222", "208.67.220.220"],
            "color": "#6BC133"  # OpenDNS Yeşil
        },
        "Quad9": {
            "servers": ["9.9.9.9", "149.112.112.112"],
            "color": "#1E4488"  # Quad9 Lacivert
        },
        "AdGuard DNS": {
            "servers": ["94.140.14.14", "94.140.15.15"],
            "color": "#66B574"  # AdGuard Yeşil
        }
    } 