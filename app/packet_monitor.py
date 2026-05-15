from scapy.all import sniff
from collections import Counter
from threading import Thread

# ---------------- GLOBAL TRAFFIC STORAGE ----------------
traffic_stats = Counter()

# ---------------- PACKET PROCESSOR ----------------
def process_packet(packet):

    try:

        if packet.haslayer("IP"):

            src_ip = packet["IP"].src

            traffic_stats[src_ip] += 1

    except:
        pass

# ---------------- START SNIFFER ----------------
def start_sniffing():

    sniff(
        prn=process_packet,
        store=False,
        count=50
    )

# ---------------- BACKGROUND THREAD ----------------
def run_packet_monitor():

    sniffer_thread = Thread(target=start_sniffing)

    sniffer_thread.daemon = True

    sniffer_thread.start()

# ---------------- FETCH LIVE STATS ----------------
def get_traffic_stats():

    return dict(traffic_stats)