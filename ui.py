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

def cardLines(label):
    if label is None:
        return ["┌───────┐"] + ["│░░░░░░░│"] * 5 + ["└───────┘"]

    rank, suit = label[:-1], label[-1]
    if rank == "X": rank = "10"

    return [
        "┌───────┐",
        f"│{rank:<7}│",
        "│       │",
        f"│{suit:^7}│",
        "│       │",
        f"│{rank:>7}│",
        "└───────┘",
    ]

def printCards(*labels):
    for row in zip(*(cardLines(l) for l in labels)):
        print("  ".join(row))
