
import nmap

# Create Nmap scanner object
scanner = nmap.PortScanner()

# Define target
target = "127.0.0.1"

# Define port range
ports = "1-1024"

print("=" * 50)
print("       PYTHON NMAP PORT SCANNER")
print("=" * 50)

print(f"Target: {target}")
print(f"Ports: {ports}")

try:
    # Start scanning
    scanner.scan(
        hosts=target,
        ports=ports,
        arguments="-sT -T3"
    )

    # Display scan results
    for host in scanner.all_hosts():

        print("\nHost:", host)
        print("Status:", scanner[host].state())

        # Get available protocols
        for protocol in scanner[host].all_protocols():

            print(f"\nProtocol: {protocol}")

            # Get scanned ports
            port_list = scanner[host][protocol].keys()

            for port in sorted(port_list):

                state = scanner[host][protocol][port]["state"]
                service = scanner[host][protocol][port]["name"]

                print(f"Port {port}: {state.upper()} | Service: {service}")

    print("\nScan completed!")

except nmap.PortScannerError as error:
    print("Nmap error:", error)

except KeyboardInterrupt:
    print("\nScan interrupted by user.")