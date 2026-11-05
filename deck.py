import random

RANK_CHARS = {1: "A", 10: "X", 11: "J", 12: "Q", 13: "K"}
decks = 1
removed = ""

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
    rank = RANK_CHARS.get(rank, rank)
    return str(rank) + suit

def draw():
    global deck, cur, removed

    while cur < len(deck):
        card = deck[cur]
        cur += 1

        rank = card % 13 + 1
        rankChar = {1: "A", 10: "X", 11: "J", 12: "Q", 13: "K"}.get(rank, str(rank))

        if rankChar not in removed:
            return rank, numToCard(card)

    return None

def printDeck():
    global cards
    tmp = 0

    for i in range(cards):
        if draw() is not None:
            tmp += 1

    print(f"Total: {tmp}")
