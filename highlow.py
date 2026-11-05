import sys
import deck
from deck import init, shuf
from ui import ask, clearScreen, printCards, FILLER

#### Pages ####

def settings():
    clearScreen()

    if ask("1. Customize Amount of Decks     2. Default\n") == "1":
        try:
            deck.decks = max(1, int(input("How many decks will you use?\n>")))
        except ValueError:
            deck.decks = 1

    if ask("1. Customize Cards in Decks    2. Default\n") == "1":
        deck.removed = input("Which cards should be blocked? (e.g. AJQK, 23456789X)\n>").upper()

def gameLoop():
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

        playable = (13 - sum(deck.removed.count(rank) > 0 for rank in "A23456789XJQK")) * 4
        playable *= deck.decks

        if playable < 2:
            print("Not enough playable cards!")
            ask("Press any key to continue...")
            return

        for i in range(playable // 2):
            clearScreen()
            print(f"{FILLER}\nYou: {wins}     Me: {loses}\n{FILLER}\n")

            player = deck.draw()
            if player is None:
                break
            playerRank, playerCard = player
            printCards(playerCard, None)

            if playerRank == 1:
                playerRank = 20

            choice = ask(f"\n{FILLER}\n1. Higher     2. Lower\n{FILLER}\n")
            while choice not in ("1", "2"):
                choice = ask("Invalid choice. 1. Higher     2. Lower\n")

            comp = deck.draw()
            if comp is None:
                break
            compRank, compCard = comp

            if compRank == 1:
                compRank = 20

            clearScreen()
            print(f"{FILLER}\nYou: {wins}     Me: {loses}\n{FILLER}\n")
            printCards(playerCard, compCard)

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
            return

def mainPage():
    while True:
        clearScreen()
        print("----Welcome to High Low----")

        choice = ask("1. Play     2. Settings     3. Quit\n")

        if choice == "1":
            gameLoop()
        elif choice == "2":
            settings()
        elif choice == "3":
            sys.exit()


mainPage()
