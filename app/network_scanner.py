from scapy.all import ARP, Ether, srp


def scan_network(network_range="172.20.10.0/28"):
    devices = []

    arp = ARP(pdst=network_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]

    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices