#base by GWS(QR_Code_Generator.)
#re-upload? recode? copy code? give credit :)
#YouTube: http://www.youtube.com/@DCsArpit
#Instagram: @dcsradioyt12
#Telegram: t.me/gws143
#GitHub: @ShantanuGWS
#WhatsApp: +918090541900
#want more free scripts? subscribe to my youtube channel: https://youtube.com/@DCsArpit
#owner: GWS - Unknown Gamer
#Author: Shantanu Patel


#User Recaptcha
import os
import time
import colorama
import string
import random

red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

os.system("clear")

if __name__ == "__main__":
    
    #s1 = string.ascii_uppercase
   
    s2 = string.ascii_lowercase
    
    s3 = string.digits
    
    #s4 = string.punctuation
    
    
    try:
       plen = int(input(red +"\n [+] Enter an number:"+green + reset))
    except:
        print(colorama.Fore.RED + "\n[!] Invalid Character")
        print("[-] Please Restart This Program!!!")
        print(colorama.Fore.RESET)
    s = []
    s.extend(list(s2))
    s.extend(list(s3))       
    random.shuffle(s)
    recaptcha = "".join(s[0:plen])
    print(blue+"\n[*] Your recaptcha ↓"+yellow+reset)
    print(colorama.Fore.WHITE + f"\n\t\t{recaptcha}\n")
    print(colorama.Fore.RESET)
    user = input(magenta+"[+]\033[5m Enter given recaptcha:"+reset)
    if user == recaptcha:
       time.sleep(1)
       print(colorama.Fore.GREEN + "\nVerifying Recaptcha....\n")
       time.sleep(1)
       print("Successfull✓\n")
       time.sleep(1)
       print("Importing All Scripts....\n")
       time.sleep(3)
       print("Creating Environment.....")
       time.sleep(3)
       os.system("clear")
       try:
           os.mkdir("/storage/emulated/0/GWS")
           import Scripts
       except:
            print("\nFolder Already Exists!!")
            os.system("clear")
            import Scripts

    else:
        print(colorama.Fore.RED + "\n[x] Wrong recaptcha ")
        print(colorama.Fore.RESET)
