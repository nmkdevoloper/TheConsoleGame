import time
import os
from os import system
import sys
import urllib.request
system("title " + "The Console Game")


def printtodisplay(printtext: str):
    for char in printtext:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces the print to display each character immediately
        time.sleep(0.05)
    print()  # Move to the next line after the loop finishes

printtodisplay("Hello there!")
printtodisplay("Welcome to The Console Game!")
printtodisplay("Press [Enter] to continue!")
enter = input()
os.system('cls')
printtodisplay("In this game, you need find the answer with hints given!")
printtodisplay("Type ""yes"" to continue or ""no"" to close!")
choice = str(input())
if choice == 'yes':
    os.system('cls')
    printtodisplay("Loading...")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/nmkdevoloper/TheConsoleGame/main/000-Example.txt", "000-Example.txt")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/nmkdevoloper/TheConsoleGame/main/000-Example.py", "000-Example.py")
elif choice == 'no':
    exit()
os.system('cls')
printtodisplay("Loading completed!")
printtodisplay("Please open file 000-Example.py! Press [Enter] to continue!")
input()