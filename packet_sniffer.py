from scapy.all import sniff, IP, TCP, UDP


def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if proto == 6:
            protocol = "TCP"
        elif proto == 17:
            protocol = "UDP"
        else:
            protocol = "Other"

        print(f"Source: {ip_src} -> Destination: {ip_dst} | Protocol: {protocol}")


if __name__ == "__main__":
    # Define your network interface here
    interface = "en0"  # Change this to your Wi-Fi interface name

    # Start sniffing
    print(f"Starting packet sniffer on interface {interface}...")
    sniff(prn=packet_callback, iface=interface, count=10)  # Change count to 0 to sniff indefinitely
