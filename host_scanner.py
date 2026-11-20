import socket
import sys

def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")

    except KeyboardInterrupt:
        print("\nExiting script.")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nCould not connect to server.")
        sys.exit()

if __name__ == "__main__":
    target = input("Enter target IP or hostname (e.g., 127.0.0.1): ").strip()
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    target_ip = socket.gethostbyname(target)
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

    print("\nScan complete.")