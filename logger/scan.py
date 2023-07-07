from dotenv import load_dotenv
import time


# Load environment variables from .env file
load_dotenv()

# Function to perform ARP scan
def arp_scan(ip_range):
    from scapy.all import ARP, Ether, srp

    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request
    # Send the packet and capture the response
    result = srp(packet, timeout=3, verbose=0)[0]
    # Process the response and extract IP and MAC addresses
    devices = []
    for sent, received in result:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})
    return devices

def get_ip_address():
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address
    
# Run the program
if __name__ == "__main__":
    from utils import login, validate_token, refresh_token, log_event

    tokens = login()
    while True:
        wifi_ip = get_ip_address()
        subnet = ".".join(wifi_ip.split(".")[:-1]) + ".0/24"
        ip_range = subnet
        # Perform ARP scan
        devices = arp_scan(ip_range)
        # Log the discovered devices
        if not validate_token(tokens["access"]):
            tokens = refresh_token(tokens["refresh"])
            if tokens is None:
                tokens = login()
        for device in devices:
            print(f"IP  : {device['ip']}")
            print(f"MAC : {device['mac']}")
            try:
                log_event(device, tokens['access'])
            except Exception:
                pass
        time.sleep(17)
