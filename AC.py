import os
from colorama import init, Fore, Style
import sys
import platform

# Initialize colorama
init()

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

system = platform.system()
init_ANS_plugins()

#This is for the title
print('''
       A              CCCCC          ttttttt     ooo       ooo      l            sssss
      A A             C                ttt      o   o     o   o     l           s
     A   A            C                ttt      o   o     o   o     l            sssss
    AAAAAAA           C                ttt      o   o     o   o     l                 s
   A       A          CCCCC            ttt        ooo       ooo      lllll      sssss
''')

# Define help tutorial with colors
help_tutorial = f"""   _   _______ _      ____  
                      | | | |____|| |   |  _ \ 
                      | |_| |  _| | |   | |_) |
                      |  _  | |___| |___|  __/ 
                      |_| |_|_____|_____|_|    
================================ codes ================================
exit     ---   exit the program                                   
----------------------------------------------------------------------
check    ---   Check your information                                          
attack   ---   DOS attack                                                                                         
listen   ---   Monitor the port status of the IP host                                              
port     ---   Check the open ports of the IP   
spy      ---   Make a spyware                                                                                                                     
======================================================================

"""
print("This is a simple tool for you to learn hacking")
print("Do not do anything illegal")
print("You will have all the responsibility when using")
print("Creator: Angus Chiu")

print(Fore.CYAN + "Type 'help' for assistance" + Style.RESET_ALL)

def program_code_body():
    """Main program loop to handle user input."""
    while True:
        try:
            program_input = input(Fore.GREEN + "AC [+ Windows +] <<" + Style.RESET_ALL + " ) ")
            if program_input.lower() == "help":
                print(help_tutorial)
            elif program_input.lower() == "exit":
                print(Fore.RED + "Exiting the program." + Style.RESET_ALL)
                break
            elif program_input.lower() == "listen":
                from Codes import listen
                listen.listen_1_main() 
            elif program_input.lower() == "check":
                from Codes import check
                check.check_main()
            elif program_input.lower() == "port":
                from Codes import port
                port.port_1_main()
            elif program_input.lower() == "attack":
                from Codes import attack
                attack.attack_1_main()
            elif program_input.lower() == "spy":
                print(Fore.YELLOW + "cd to Codes and type python3 spyware.py yourself" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Unknown command: {program_input}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error:\n{e}" + Style.RESET_ALL)

if __name__ == "__main__":
    program_code_body()