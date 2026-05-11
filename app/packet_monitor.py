from scapy.all import sniff
from collections import Counter


def capture_packets(packet_count=20):

    packets = sniff(count=packet_count)

    ip_counter = Counter()

    for packet in packets:

        if packet.haslayer("IP"):

            src_ip = packet["IP"].src

            ip_counter[src_ip] += 1

    return ip_counter