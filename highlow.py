import readchar as rc
import random
import os
import sys

FILLER = "="*20
decks = 1
removed = ""

def ask(str):
    print(f"{str}")
    tmp = rc.readchar()
    if tmp == "`": sys.exit()
    return tmp

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def init():
    global cur, cards, deck
    cur = 0
    cards = decks * 52
    deck = list(range(cards))

def shuf():
    global deck, cur
    cur = 0
    random.shuffle(deck)

def numToCard(num):
    suit = chr(9824 + ((num // 13) % 4))
    rank = num % 13 + 1
    rank = {1: "A", 10: "X", 11: "J", 12: "Q", 13: "K"}.get(rank, rank)
    return str(rank) + suit

def draw():
    global deck, cur, removed

    while cur < len(deck):
        card = deck[cur]
        cur += 1

        rank = card % 13 + 1
        rankChar = {1: "A", 10: "X", 11: "J", 12: "Q", 13: "K"}.get(rank, str(rank))

        if rankChar not in removed:
            print(numToCard(card))
            return rank

    return None

def printDeck():
    global cards
    tmp = 0

    for i in range(cards):
        if draw() is not None:
            tmp += 1

    print(f"Total: {tmp}")


#### Pages ####

def settings():
    global decks, removed

    clearScreen()

    if ask("1. Customize Amount of Decks     2. Default\n") == "1":
        decks = int(input("How many decks will you use?\n>"))
        if decks < 1:
            decks = 1

    if ask("1. Customize Cards in Decks    2. Default\n") == "1":
        removed = input("Which cards should be blocked? (e.g. AJQK, 23456789X)\n>").upper()

    mainPage()

def gameLoop():
    global cards

    while True:
        wins = 0
        loses = 0

        def win():
            nonlocal wins
            wins += 1
            ask("\nYou Win!\n")

        def lose():
            nonlocal loses
            loses += 1
            ask("\nYou Lose...\n")

        init()
        shuf()

        playable = 52 - sum(removed.count(rank) > 0 for rank in "A23456789XJQK") 
        playable *= decks

        if playable < 2:
            print("Not enough playable cards!")
            ask("Press any key to continue...")
            mainPage()
            return

        for i in range(playable // 2):
            clearScreen()
            print(f"{FILLER}\nYou: {wins}     Me: {loses}\n{FILLER}\n")

            playerRank = draw()

            if playerRank is None:
                break

            if playerRank == 1:
                playerRank = 20

            choice = ask(f"\n{FILLER}\n1. Higher     2. Lower\n{FILLER}\n")

            while choice not in ("1", "2"):
                choice = ask("Invalid choice. 1. Higher     2. Lower\n")

            compRank = draw()

            if compRank is None:
                break

            if compRank == 1:
                compRank = 20

            if choice == "1":
                if compRank > playerRank:
                    win()
                else:
                    lose()
            else:
                if playerRank > compRank:
                    win()
                else:
                    lose()

        clearScreen()
        print(f"Final Score: You: {wins}     Me: {loses}\n")

        choice = ask("1. Play Again    2. Home\n")

        if choice != "1":
            mainPage()
            return

def mainPage():
    clearScreen()
    print("----Welcome to High Low----")

    choice = ask("1. Play     2. Settings     3. Quit\n")

    if choice == "1":
        gameLoop()
    elif choice == "2":
        settings()
    elif choice == "3":
        sys.exit()
    else:
        mainPage()


mainPage()

