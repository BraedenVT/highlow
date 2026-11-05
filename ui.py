import readchar as rc
import os
import sys

FILLER = "="*20

def ask(str):
    print(f"{str}")
    tmp = rc.readchar()
    if tmp == "`": sys.exit()
    return tmp

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
