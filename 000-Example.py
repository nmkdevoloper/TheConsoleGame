import time
import os
from os import system
import sys
os.remove("TheIndex.py") 

system("title " + "The Console Game - 000. Example")
def printtodisplay(printtext: str):
    for char in printtext:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces the print to display each character immediately
        time.sleep(0.05)
    print()  # Move to the next line after the loop finishes

printtodisplay("Welcome back! Can you see the ""000-Example.txt""?")
printtodisplay("Open this file and type answer here!")
while(input() != "1234"):
    os.system('cls')
    printtodisplay("Wrong answer, try again!")
os.system('cls')
printtodisplay("Good job! You passed this level!")
printtodisplay("Loading...")
