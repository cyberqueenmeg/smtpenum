#!/usr/bin/python

import socket
import sys

# Get a list of target IP addresses from user input
target_ips_str = input("Enter a list of target IP addresses (comma-separated): ")
target_ips = target_ips_str.split(',')

# Loop through each IP address
for target_ip in target_ips:
    target_ip = target_ip.strip()  # Remove leading/trailing whitespace
    print(f"Scanning {target_ip}...")

    try:
        # Create a Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the Server
        connect = s.connect((target_ip,25))

        # Receive the banner
        banner = s.recv(1024)

        print(banner)

        # VRFY a user
        user = (sys.argv[1]).encode()
        s.send(b'VRFY ' + user + b'\r\n')
        result = s.recv(1024)

        print(result)

        # Close the socket
        s.close()
    except Exception as e:
        print(f"Error: {e}")
