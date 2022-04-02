import time
import os
import socket
from datetime import datetime

now = datetime.now()


login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()
print("""












































































      
██████╗░██╗░░░██╗░█████╗░██╗░░░░░░█████╗░██████╗░░██████╗░░░░░░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗██╔════╝
██║░░██║░╚████╔╝░██║░░╚═╝██║░░░░░██║░░██║██████╔╝╚█████╗░█████╗██║░░██║╚█████╗░
██║░░██║░░╚██╔╝░░██║░░██╗██║░░░░░██║░░██║██╔═══╝░░╚═══██╗╚════╝██║░░██║░╚═══██╗
██████╔╝░░░██║░░░╚█████╔╝███████╗╚█████╔╝██║░░░░░██████╔╝░░░░░░╚█████╔╝██████╔╝
╚═════╝░░░░╚═╝░░░░╚════╝░╚══════╝░╚════╝░╚═╝░░░░░╚═════╝░░░░░░░░╚════╝░╚═════╝░
""")
print("Welcome, " + l_n)
print("Today is: " + time.strftime("%m/%d/%y"))
current_time = now.strftime("%H:%M")
print("The time is: ", current_time)

print("""
Applications:
1. Terminal (MUST RESTART TO GO BACK TO HOME)
2. Shutdown
3. Dyluator (Calculator)
4. Music (complicated-ish)
5. Text Related Apps
6. Eaglercraft (minecraft 1.5.2)
""")

option = input("Select Via Number: ")

if option == "1":
  os.system('python apps/cmd.py')
elif option == "2":
  exit("Shutdown")
elif option == "3":
  os.system('python apps/calculator.py')
elif option == "4":
  os.system('python apps/music.py')
elif option == "5":
  os.system('python apps/text_apps.py')
elif option == "6":
  print("""
Servers:
1. https://vanilla.ligmasmp.repl.co/ - Link
2. wss://aeon-network.tk/aeon - IP
        
Game: https://g.eags.us/eaglercraft
        """)
  time.sleep(5)
  print("""
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
""")
  os.system('python home.py')