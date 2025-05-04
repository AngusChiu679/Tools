import os
from colorama import init, Fore
import sys
import platform
import socket
import signal
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the tutorial content before using it
plugins_tutorial = "Welcome to the plugin system! Here you can add your plugins."

def init_ANS_plugins():
    """Initialize the plugins directory and tutorial."""
    if not os.path.exists("plugins"):
        os.mkdir("plugins")
    if not os.path.exists("plugins/plugins_list.txt"):
        with open("plugins/plugins_list.txt", 'w', encoding='utf-8') as file:
            file.write("")
    if not os.path.exists("plugins/plugins_tutorial.txt"):
        with open("plugins/plugins_tutorial.txt", 'w', encoding='utf-8') as file:
            file.write(plugins_tutorial)

def help_tutorial():
    print("""
================================ codes ================================                                         
exit     ---   exit the program                                   
----------------------------------------------------------------------
check    ---   check                                              
attack   ---   attack                                                                                         
listen   ---   listen                                             
port     ---   port                                                                                                                               
======================================================================
""")

def program_code_body():
    """Main program loop to handle user input."""
    while True:
        try:
            program_input = input(">>> ")  # Added a space for better readability
            if program_input.lower() == "help":
                help_tutorial()
            elif program_input.lower() == "exit":
                print("Exiting the program.")
                break  # Added exit command
            elif program_input.lower() == "listen":
                from Codes import listen
                listen.listen_1_main() 
            elif program_input.lower() == "check":
                from Codes import check
                check.check_main()
            elif program_input.lower() == "port":
                port_1_main()  # Call the function directly
            else:
                print(f"Unknown command: {program_input}")
        except Exception as e:
            print(f"Error:\n{e}")

def port_1_main():
    """Main function to check open ports."""
    print ("""
                                      ____            _   
                                     |  _ \ ___  _ __| |_
                                     | |_) / _ \| '__| __|
                                     |  __/ (_) | |  | |_
                                     |_|   \___/|_|   \__|
============================================= port =============================================
                                Check the open ports of the IP                             
================================================================================================
""")

    global running
    running = True

    def signal_handler(sig, frame):
        global running
        running = False
        print("\nStopping the port checking...")

    def check_open_port(ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for the connection attempt
            result = s.connect_ex((ip, port))
            return port if result == 0 else None

    def check_open_ports(ip, port_range):
        open_ports = []
        total_ports = len(port_range)
        
        with ThreadPoolExecutor(max_workers=1000) as executor:
            futures = {executor.submit(check_open_port, ip, port): port for port in port_range}
            for i, future in enumerate(as_completed(futures), start=1):
                if not running:
                    break  # Stop checking if the running flag is set
                
                port = future.result()
                if port is not None:
                    open_ports.append(port)
                    
                # Progress bar
                progress = (i / total_ports) * 100
                bar_length = 50  # Length of the progress bar
                block = int(bar_length * progress // 100)
                progress_bar = '=' * block + '>' + ' ' * (bar_length - block - 1)
                print(f'\r|{progress_bar}| {i}/{total_ports} ports checked', end='')

        print()  # New line after progress
        return open_ports

    # Set up signal handler for graceful exit
    signal.signal(signal.SIGINT, signal_handler)

    ip_address = input("Enter the IP address to check: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    ports_to_check = range(start_port, end_port + 1)
    open_ports = check_open_ports(ip_address, ports_to_check)
    
    if open_ports:
        print(f"Open ports on {ip_address}: {open_ports}")
    else:
        print(f"No open ports found on {ip_address}.")

if __name__ == "__main__":
    init_ANS_plugins()
    init()
    print("Type 'help' for assistance")
    program_code_body()
    port_1_main