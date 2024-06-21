#!/bin/bash

red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

clear

echo
echo
echo
echo "
      ━━━━━━━━━━━━━━━━━━━━━━━━━ [★] L O G I N [★] ━━━━━━━━━━━━━━━━━━━>
echo
echo "
                 ██╗  ██╗ █████╗  █████╗ ██╗  ██╗███████╗██████╗
                 ██║  ██║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
                 ███████║███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
                 ██╔══██║██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
                 ██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
                 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  "|>
echo
echo "
     ━━━━━━━━━━━━━━━━━━━━━━━━━ [★] W E L C O M E [★] ━━━━━━━━━━━━━━━━>
echo
echo


termux-setup-storage

echo "\033[91;1m[+] Installing Python..."
pkg install python
echo "\033[92;1m[✓] Successfully Installed"


echo "\033[91;1m[+] Installing colorama..."
pkg install colorama
echo "\033[92;1m[✓] Successfully Installed"


python ProgramDistributer.py


