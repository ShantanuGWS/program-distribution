#Styling The Script 

import time
import colorama
import shutil
import os
import sys

logo = """   
                         ______        _____
                        / ___\ \      / / ___| 
                       | |  _ \ \ /\ / /\___ \ 
                       | |_| | \ V  V /  ___) |
                        \____|  \_/\_/  |____/ 
               
"""

red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

def anime(text):
  for txt in text:
    sys.stdout.write(txt)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1)
logoanm = colorama.Fore.YELLOW + logo
anime(logoanm)
print(colorama.Fore.RESET)

time.sleep(0.8)

anm = colorama.Fore.RED + f"{'='*26}[Created by GWS]{'='*26}"

anime(anm)

style = """

\033[92;1m[+]\033[93;1m Owner: ♣Gaming World Studio♣ OR ♥Mr.Unknown♥\033[0m

\033[92;1m[+]\033[5m Script Creater: ★Shantanu★

\033[92;1m[+]\033[94;1m YT Channel: http://www.youtube.com/@DCsArpit 

\033[92;1m[+]\033[95;1m Github: ShantanuGWS♠
"""

time.sleep(1)
sty = colorama.Fore.BLUE + style
anime(sty)
print(colorama.Fore.RESET)
dash = colorama.Fore.YELLOW + "_"*70
anime(dash)
print("\n")

time.sleep(0.8)

option = colorama.Fore.GREEN + "[+] Select An Option ::\n "
anime(option)
print(colorama.Fore.RESET)
first = colorama.Fore.BLUE + "[1] Instagram User Info Gathering\n"
anime(first)
time.sleep(0.6)
sec = "[2] Folder Creator\n"
anime(sec)
time.sleep(0.6)
third = "[3] QR CODE Generator\n"
anime(third)
time.sleep(0.6)
For = "[4] Turtle Drawing\n"
anime(For)
time.sleep(0.6)
ex = "[00] Exit\n"
anime(ex)
print(colorama.Fore.RESET)

#Scripts
while True:
 sc = input("\033[96;1m ===>\033[92;1m"+reset)

 if sc == "1":
  shutil.copy('InstaInfo.txt','/storage/emulated/0/GWS/instaInfo.txt')
  print("Working Please Wait.....")
  time.sleep(1.5)
  print("Success!!")

 elif sc == "2":
  shutil.copy('Folder.txt','/storage/emulated/0/GWS/Folder_Generator.txt')
  print("Working Please Wait.....")
  time.sleep(1.5)
  print("Success!!")

 elif sc == "3":
  shutil.copy('QR.txt','/storage/emulated/0/GWS/QR_Generator.txt')
  print("Working Please Wait.....")
  time.sleep(1.5)
  print("Success!!")

 elif sc == "4":
  shutil.copy('turtle_ex.txt','/storage/emulated/0/GWS/turtle_Ex.txt')
  print("Working Please Wait.....")
  time.sleep(1.5)
  print("Success!!")

 elif sc == "00":
  endmsg = green+"Thanks For Using Our Service\nDont Forget To Subscribe Our Channel\nhttp://www.youtube.com/@DCsArpit\n"+reset
  time.sleep(2)
  anime(endmsg)
  exit()
