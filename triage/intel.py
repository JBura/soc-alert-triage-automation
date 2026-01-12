# Simulated threat intelligence data
KNOWN_MALICIOUS_IPS = {
    "185.220.101.4",
    "45.133.1.9",
    "103.214.5.77"
}

def check_ip_reputation(ip_address):
    """
    Simulates threat intelligence lookup.
    Returns True if IP is known malicious.
    """
    if ip_address in KNOWN_MALICIOUS_IPS:
        return {
            "malicious": True,
            "confidence": 0.9,
            "source": "Simulated Threat Intel"
        }

    return {
        "malicious": False,
        "confidence": 0.0,
        "source": "Simulated Threat Intel"
    }
