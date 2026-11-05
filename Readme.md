# Basic Network Sniffer

A Python-based network sniffer developed as part of the **CodeAlpha Cyber Security Internship – Task 1**.

## Overview

A network sniffer is a tool that captures and analyzes network packets transmitted over a network. It helps understand network communication by examining packet headers, identifying protocols, and extracting relevant information.

This project uses **Python and Scapy** to capture and analyze IPv4 network traffic.

## Features

- Capture IPv4 packets.
- Extract source and destination IP addresses.
- Identify TCP, UDP, and ICMP protocols.
- Extract TCP and UDP source and destination ports.
- Inspect raw payload data and display up to 32 bytes in hexadecimal format.
- Limit packet capture to 20 packets.
- Handle permission errors, keyboard interruptions, and other runtime exceptions.

## Technologies Used

- **Python 3**
- **Scapy** – Packet capture and network analysis.
- **Networking fundamentals** – IPv4, TCP, UDP, ICMP, ports, and packet structure.

## Project Structure

```text
CodeAlpha_NetworkSniffer/
│
├── net_sniff.py
└── Readme.md
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Abdesslam-OMA/CodeAlpha_NetworkSniffer.git
```

### 2. Navigate to the project directory

```bash
cd CodeAlpha_NetworkSniffer
```

### 3. Install Scapy

```bash
python -m pip install scapy
```

### 4. Run the program

```bash
python net_sniff.py
```

**Note:** Packet capture may require administrator/root privileges. Windows users may also need to install Npcap.

## How It Works

The program uses Scapy's `sniff()` function to capture IPv4 packets.

Each captured packet is passed to the `analyze_packet()` function through the `prn` parameter.

The analysis process consists of the following steps:

1. **Packet validation:** Checks whether the packet contains an IPv4 layer using `haslayer(IP)`.
2. **IP extraction:** Retrieves the source and destination IP addresses.
3. **Protocol identification:** Detects TCP, UDP, and ICMP.
4. **Port extraction:** Retrieves source and destination ports for TCP and UDP packets.
5. **Payload inspection:** Checks for a Raw layer and displays up to 32 bytes of its payload in hexadecimal format.

The capture uses `count=20` to stop after 20 packets and `store=False` to avoid retaining all captured packets in memory.

## Example Output

```text
Starting network sniffer...

========== PACKET ==========
Source IP: 192.168.1.10
Destination IP: 8.8.8.8
Protocol: UDP
Source Port: 53000
Destination Port: 53
Payload (hex): ...
==============================

Capture completed.
```

*The output above is illustrative. Actual results depend on captured network traffic.*

## Learning Objectives

This project demonstrates practical understanding of:

- Network packet structure and encapsulation.
- Ethernet and IPv4 fundamentals.
- TCP, UDP, and ICMP protocols.
- Packet capture and dissection using Scapy.
- IP address and port extraction.
- Python functions, modules, and exception handling.

## Security and Ethical Considerations

This project is intended for educational purposes and authorized network analysis only.

Packet capture should only be performed on networks and devices for which permission has been granted.

Payload inspection is limited to a small hexadecimal sample. HTTPS application data is generally encrypted and cannot normally be read as plaintext through ordinary packet capture.

## Author

Developed as part of the **CodeAlpha Cyber Security Internship – Task 1: Basic Network Sniffer**.

**GitHub Repository:** https://github.com/Abdesslam-OMA/CodeAlpha_NetworkSniffer
