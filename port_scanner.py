
import socket
import sys
from datetime import datetime

target = "127.0.0.1"
start_port = 1
end_port = 1024

print("-" * 50)
print("       PYTHON TCP PORT SCANNER")
print("-" * 50)

print(f"Target IP: {target}")
print(f"Scan started: {datetime.now()}")
print("-" * 50)

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port}: OPEN")

    sock.close()

print("-" * 50)
print("Scan completed!")
print(f"Scan finished: {datetime.now()}")