import requests
import socket
import subprocess
import re
import sys

print('''
                            ____ _               _    
                           / ___| |__   ___  ___| | __
                          | |   | '_ \ / _ \/ __| |/ /
                          | |___| | | |  __/ (__|   < 
                           \____|_| |_|\___|\___|_|\_\ 
====================================== check ======================================
                         Check your various IP addresses            
===================================================================================
''')

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            data = response.json()
            return data.get('origin')
        else:
            print(f"Request failed, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request exception: {e}")
    return None

def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except socket.error as e:
        print(f"Error occurred while getting local IP: {e}")
    return None

def get_gateway_ip_windows():
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        output = result.stdout
        pattern = r"Default Gateway.*?:\s*([\d\.]+)"
        match = re.search(pattern, output)
        if match:
            return match.group(1)
        else:
            print("Default gateway information not found.")
    except Exception as e:
        print(f"Error executing command: {e}")
    return None

def get_gateway_ip_linux_macos():
    try:
        result = subprocess.run(['netstat', '-rn'], capture_output=True, text=True)
        output = result.stdout
        pattern = r"default\s+([\d\.]+)"
        match = re.search(pattern, output)
        if match:
            return match.group(1)
        else:
            print("Default gateway information not found.")
    except Exception as e:
        print(f"Error executing command: {e}")
    return None

def check_main():
    if sys.platform == "win32":
        gateway_ip = get_gateway_ip_windows()
    elif sys.platform in ["linux", "darwin"]:
        gateway_ip = get_gateway_ip_linux_macos()
    else:
        print("This script does not support mobile systems.")
        sys.exit()

    if gateway_ip:
        print(f"Gateway IP address: {gateway_ip}")
    else:
        print("Could not retrieve gateway IP.")

    public_ip = get_public_ip()
    if public_ip:
        print("Public IP:", public_ip)
    else:
        print("Could not retrieve public IP.")

    local_ip = get_local_ip()
    if local_ip:
        print("Local IP:", local_ip)
    else:
        print("Could not retrieve local IP.")

if __name__ == "__main__":
    check_main()