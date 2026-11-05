# Basic Network Sniffer

## Overview

This project is a basic network sniffer developed in Python as part of the CodeAlpha Cyber Security Internship.

A network sniffer is a tool used to capture and analyze network packets transmitted over a network interface. It helps understand network communication by inspecting packet headers, identifying protocols, and extracting relevant information.

This project uses **Scapy**, a Python library for packet manipulation and network analysis.

## Features

- Capture IPv4 network packets.
- Extract source and destination IP addresses.
- Identify transport protocols: TCP, UDP, and ICMP.
- Extract TCP and UDP source and destination ports.
- Inspect raw packet payloads and display a limited sample in hexadecimal format.
- Limit packet capture to 20 packets.
- Handle common runtime errors and user interruptions.

## Technologies Used

- **Python 3** – Main programming language.
- **Scapy** – Network packet capture and analysis.
- **Socket and Networking Concepts** – Understanding IP addresses, ports, protocols, and packet structures.

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd CodeAlpha_BasicNetworkSniffer
   ```

3. Install Scapy:

   ```bash
   python -m pip install scapy
   ```

4. Run the program with the appropriate privileges:

   ```bash
   python sniffer.py
   ```

**Note:** Depending on your operating system, packet capture may require administrator/root privileges and an appropriate packet-capture backend, such as Npcap on Windows.

## How It Works

The program uses Scapy's `sniff()` function to capture IPv4 packets.

Each captured packet is passed to the `analyze_packet()` function through the `prn` parameter.

The program then:

1. Checks whether the packet contains an IPv4 layer.
2. Extracts the source and destination IP addresses.
3. Identifies whether the packet uses TCP, UDP, or ICMP.
4. Extracts source and destination ports when TCP or UDP is detected.
5. Checks for a raw payload layer and displays up to 32 bytes in hexadecimal format.

The capture is limited to 20 packets, and `store=False` prevents Scapy from retaining all captured packets in memory.

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

*Note: This is an illustrative example. Actual output depends on the network traffic captured.*

## Learning Objectives

Through this project, I explored:

- Network packet structure and encapsulation.
- Ethernet and IPv4 headers.
- TCP, UDP, and ICMP protocols.
- Packet capture and dissection using Scapy.
- Python functions, modules, and exception handling.
- Extraction and interpretation of network traffic information.

## Security and Ethical Considerations

This tool is intended for educational purposes and authorized network analysis only.

Network traffic can contain sensitive information. Packet capture should only be performed on networks and devices for which permission has been granted.

Payload inspection is limited to a small hexadecimal sample. HTTPS application data is generally encrypted and cannot be read as plaintext through ordinary packet capture.

## Author

Developed as part of the **CodeAlpha Cyber Security Internship – Task 1: Basic Network Sniffer**.
