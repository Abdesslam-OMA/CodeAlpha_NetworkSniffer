from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def analyze_packet(packet):

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        print("\n========== PACKET ==========")
        print("Source IP:", source_ip)
        print("Destination IP:", destination_ip)

        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")

        else:
            print("Protocol: Other")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print("Payload (hex):", payload[:32].hex())

        print("=" * 30)


try:
    print("Starting network sniffer...")

    sniff(
        filter="ip",
        prn=analyze_packet,
        count=20,
        store=False
    )

    print("Capture completed.")

except PermissionError:
    print("Permission denied. Run with appropriate privileges.")

except KeyboardInterrupt:
    print("\nCapture stopped by user.")

except Exception as error:
    print("Error:", error)
