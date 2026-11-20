#!/usr/bin/env bash

# Check if nmap is installed
if ! command -v nmap &> /dev/null; then
    echo "[-] Error: nmap is not installed. Install it using: sudo apt install nmap"
    exit 1
fi

# Accept arguments via CLI flags/positional args OR prompt the user
TARGET_IP="$1"
NSE_SCRIPT="$2"

if [[ -z "$TARGET_IP" ]]; then
    read -rp "Enter Target IP address: " TARGET_IP
fi

if [[ -z "$NSE_SCRIPT" ]]; then
    read -rp "Enter NSE script name (e.g., http-title, vuln, smb-os-discovery): " NSE_SCRIPT
fi

# Validate non-empty inputs
if [[ -z "$TARGET_IP" || -z "$NSE_SCRIPT" ]]; then
    echo "Usage: $0 <TARGET_IP> <NSE_SCRIPT_NAME>"
    exit 1
fi

echo "--------------------------------------------------"
echo "[*] Target IP  : $TARGET_IP"
echo "[*] NSE Script : $NSE_SCRIPT"
echo "--------------------------------------------------"

# Run nmap with the specified NSE script (-sV helps version-dependent scripts)
nmap -sV --script="$NSE_SCRIPT" "$TARGET_IP"