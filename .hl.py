#!/usr/bin/python3
import random
import string
import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def init():
    global cur, decks, cards, deck, removed
    cur = 0
    cards = decks*52
    deck = [0]*cards
    for i in range(cards):
        deck[i] = i

def shuf():
    global deck, cur
    cur = 0
    random.shuffle(deck)

def numToCard(num):
    suit = chr(9824 + ((num // 13) % 4))
    rank = num % 13 + 1
    if rank == 1:
        rank = "A"
    if rank == 11:
        rank = "J"
    if rank == 12:
        rank = "Q"
    if rank == 13:
        rank = "K"
    return str(rank)+suit

def draw():
    global deck, cur, removed
    rank = str(deck[cur] % 13 + 1)
    rank = {"1": "A", "11": "J", "12": "Q", "13": "K"}.get(rank, rank)
    if rank not in removed:
        print(numToCard(deck[cur]))
    cur+=1
    return deck[cur] % 13 + 1

def printDeck():
    global cards
    tmp = 0
    for i in range(cards):
        if draw():
            tmp += 1
            
    print(f"Total: {tmp}")


####Pages####

def settings():
    clearScreen()
    global decks, removed
    if(int(input("1. Customize Amount of Decks     2. Default\n")) == 1):
        decks = int(input("How many decks will you use?\n"))
    if(int(input("1. Customize Cards in Decks    2. Default\n")) == 1):
        removed = input("Which cards should be blocked? (e.g. AJQK, 23456789X)\n").upper()
    mainPage()

def gameLoop():
    global cards
    wins = 0
    loses = 0
    def win():
        nonlocal wins
        wins+=1
        input("\nYou Win!\n")
    def lose():
        nonlocal loses
        loses+=1
        input("\nYou Lose...\n")
    init()
    shuf()
    for i in range(cards // 2):
        clearScreen()
        print(f"You: {wins}     Me: {loses}\n")
        playerRank = draw()
        if(playerRank == 0): playerRank = 20
        choice = int(input("1. Higher     2. Lower\n"))
        compRank = draw()
        if(compRank == 0): compRank = 20
        
        if choice == 1:
            if compRank > playerRank:
                win()
            else:
                lose()
        else:
            if playerRank > compRank:
                win()
            else:
                lose()
    choice = int(input("1. Play Again    2. Home\n"))
    if choice == 1: gameLoop()
    else: mainPage()

def mainPage():
    global decks, removed
    decks = 1
    removed = ""
    clearScreen()
    print("----Welcome to High Low----")
    choice = int(input("1. Play     2. Settings     3. Quit\n"))
    if choice == 1: gameLoop()
    elif choice == 2: settings()
    else: exit()

mainPage()
