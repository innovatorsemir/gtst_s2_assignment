# Network Scanning & Host Discovery Tools

A collection of Python and Bash network reconnaissance scripts developed for port scanning, host discovery, and automated Nmap Scripting Engine (NSE) execution.

## Scripts Overview

| File | Description |
| :--- | :--- |
| `socket_scanner.py` | Multi-threaded TCP port scanner built using Python's native `socket` library. |
| `nmap_scanner.py` | Service and version detection port scanner powered by `python-nmap`. |
| `host_discovery.py` | Detects the default gateway IP, identifies its IPv4 class (A–E), and sweeps the local `/24` subnet for active hosts. |
| `nse_scanner.sh` | Bash wrapper that accepts a target IP and NSE script name to run targeted Nmap scans. |

## Prerequisites

- **Python 3.x**
- **Nmap** (`sudo apt install nmap`)
- **python-nmap** (`pip install python-nmap`)

## Usage

```bash
# 1. Socket-based port scanner
python3 socket_scanner.py

# 2. python-nmap port scanner
python3 nmap_scanner.py

# 3. Gateway & host discovery
python3 host_discovery.py

# 4. Bash NSE script runner
chmod +x nse_scanner.sh
./nse_scanner.sh <TARGET_IP> <NSE_SCRIPT>