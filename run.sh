#!/bin/bash

echo "======================================"
echo " HTTP Basic Authentication Lab"
echo "======================================"

echo "[+] Starting server..."
echo "[+] URL: http://127.0.0.1:8080/admin"
echo "[+] Username: john"
echo "[+] Password: 123456"
echo
echo "[+] Press Ctrl+C to stop the server."
echo

python3 server.py
