import socket
import threading
import time
import sys
import os

print("""
                              _     _     _
                             | |   (_)___| |_ ___ _ __
                             | |   | / __| __/ _ \ '_ \ 
                             | |___| \__ \ ||  __/ | | |
                             |_____|_|___/\__\___|_| |_|
====================================== listen ======================================
                        Monitor the port status of the IP host                 
====================================================================================
""")



# Detect the operating system
is_windows = os.name == "nt"
is_linux = os.name == "posix" and sys.platform.startswith("linux")
is_macos = os.name == "posix" and sys.platform.startswith("darwin")

# Define global variables
running = False
monitor_thread = None

# Check if a single port is open
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        return result == 0
    except Exception:
        return False
    finally:
        sock.close()

# Monitor multiple ports on a single host
def monitor_host_ports(host, ports):
    results = []
    for port in ports:
        open_status = check_port(host, port)
        results.append((port, open_status))
    return results

# Monitor multiple hosts and multiple ports
def monitor_multiple_hosts_ports(hosts, ports):
    all_results = []
    for host in hosts:
        host_results = monitor_host_ports(host, ports)
        all_results.extend([(host, port, status) for port, status in host_results])
    return all_results

# Display results in the terminal in real-time
def display_results(results):
    # Clear terminal content
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

    # Print results
    print(f"{'Host':<15} {'Port':<5} {'Status':<8}")
    print("-" * 30)
    for host, port, status in results:
        status_text = "Open" if status else "Closed"
        print(f"{host:<15} {port:<5} {status_text:<8}")

# Continuous monitoring thread
def continuous_monitoring(hosts, ports):
    global running
    while running:
        start_time = time.time()
        results = monitor_multiple_hosts_ports(hosts, ports)
        display_results(results)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < 5:
            time.sleep(5 - elapsed_time)

# Handle Ctrl+C to exit
def handle_ctrl_c(signal, frame):
    global running
    print("\nReceived Ctrl+C, exiting the program...")
    running = False  # Set global variable to notify the thread to stop running

    # Wait for the thread to finish
    if monitor_thread is not None and monitor_thread.is_alive():
        monitor_thread.join(timeout=5)  # Set timeout to avoid blocking
        if monitor_thread.is_alive():
            print("Monitoring thread did not stop in time, forcing exit...")
            sys.exit(1)  # Force exit the program
    print("Program has exited successfully")

# Main function to start the program
def listen_1_main():
    global running
    global monitor_thread
    running = True

    # If no input is provided, get it from the user
    hosts_input = input("Enter the hosts to monitor, separated by commas: ")
    ports_input = input("Enter the ports to monitor, separated by commas: ")

    # Parse hosts and ports
    hosts = [host.strip() for host in hosts_input.split(',')]
    ports = [int(port.strip()) for port in ports_input.split(',')]

    # Start monitoring thread
    monitor_thread = threading.Thread(target=continuous_monitoring, args=(hosts, ports))
    monitor_thread.start()

    # Register signal handler
    import signal
    signal.signal(signal.SIGINT, handle_ctrl_c)

    # Block main thread until user interrupts
    try:
        while running:
            time.sleep(1)  # Keep the main thread running, waiting for the thread to finish
    except KeyboardInterrupt:
        handle_ctrl_c(None, None)  # Catch KeyboardInterrupt in the main thread

if __name__ == "__main__":
    listen_1_main()