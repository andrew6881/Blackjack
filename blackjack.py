import random

cardlist = {
    "Ace" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
    "Six" : 6,
    "Seven" : 7,
    "Eight" : 8,
    "Nine" : 9,
    "Ten" : 10,
    "King" : 10,
    "Queen" : 10
}

playerpts = 0
dealerpts = 0

playerhand = {}
dealerhand = {}

checkScore = 0

# -------------------------------------------------------------------------------------

def checkScore(playerpts, dealerpts, playerhand, dealerhand): # helper function to check player and dealer score
    if playerpts > 21:
        print("Game over! Player score exceeds 21")
        print("Player cards: " + str(playerhand))
        print("Final player points: " + str(playerpts))
        print("Dealer cards: " + str(dealerhand))
        print("Final dealer points: " + str(dealerpts))
    if playerpts == 21:
        print("You win! Player score equals 21")
        print("Player cards: " + str(playerhand))
        print("Final player points: " + str(playerpts))
        print("Dealer cards: " + str(dealerhand))
        print("Final dealer points: " + str(dealerpts))
    if dealerpts > 21:
        print("You win! Dealer score exceeds 21")
        print("Player cards: " + str(playerhand))
        print("Final player points: " + str(playerpts))
        print("Dealer cards: " + str(dealerhand))
        print("Final dealer points: " + str(dealerpts))
    if dealerpts > 17:
        if dealerpts == 21:
            print("Game over! Dealer score equals 21")
            print("Player cards: " + str(playerhand))
            print("Final player points: " + str(playerpts))
            print("Dealer cards: " + str(dealerhand))
            print("Final dealer points: " + str(dealerpts))
        elif playerpts == dealerpts:
            print("Game over in a tie! Player and dealer scores are equivalent")
            print("Player cards: " + str(playerhand))
            print("Final player points: " + str(playerpts))
            print("Dealer cards: " + str(dealerhand))
            print("Final dealer points: " + str(dealerpts))
        elif playerpts > dealerpts and playerpts < 22:
            print("You win! Player score exceeds dealer score")
            print("Player cards: " + str(playerhand))
            print("Final player points: " + str(playerpts))
            print("Dealer cards: " + str(dealerhand))
            print("Final dealer points: " + str(dealerpts))
        elif dealerpts > playerpts:
            print("Game over! Dealer score exceeds player score")
            print("Player cards: " + str(playerhand))
            print("Final player points: " + str(playerpts))
            print("Dealer cards: " + str(dealerhand))
            print("Final dealer points: " + str(dealerpts))

print("Dealer is dealing a card...")
for i in range(2): # the first round of card dealing
    picker = random.choice(list(cardlist.keys()))
    playerhand[picker] = cardlist.get(picker)
    playerpts += cardlist.get(picker)
picker = random.choice(list(cardlist.keys()))
dealerhand[picker] = cardlist.get(picker)
dealerpts += cardlist.get(picker)

dealerhand["???"] = "???"

print("Player cards: " + str(playerhand))
print("Player points: " + str(playerpts))
print("Dealer cards: " + str(dealerhand))
print("Dealer points: " + str(dealerpts))

while True:

    choice = input("Enter H to hit, enter S to stand ")
    if choice == "H":
        picker = random.choice(list(cardlist.keys())) # chooses a random key in cardlist that determines which card is being dealt
        if cardlist.get(picker) + playerpts > 21:
            playerpts += cardlist.get(picker)
            playerhand[picker] = cardlist.get(picker)
            checkScore(playerpts, dealerpts, playerhand, dealerhand)
            break
        playerhand[picker] = cardlist.get(picker)
        playerpts += cardlist.get(picker)
        print("")
        print("Player cards: " + str(playerhand))
        print("Player points: " + str(playerpts))
        print("Dealer cards: " + str(dealerhand))
        print("Dealer points: " + str(dealerpts))
    elif choice == "S":
        if dealerhand["???"] == "???":
            dealerhand.pop("???", "???")
            picker = random.choice(list(cardlist.keys()))
            dealerhand[picker] = cardlist.get(picker)
            dealerpts += cardlist.get(picker)
        while dealerpts < 17:
            picker = random.choice(list(cardlist.keys())) # chooses a random key in cardlist that determines which card is being dealt
            dealerpts += cardlist.get(picker)
            if dealerpts > 21:
                checkScore(playerpts, dealerpts, playerhand, dealerhand)
                break
            dealerhand[picker] = cardlist.get(picker)
        checkScore(playerpts, dealerpts, playerhand, dealerhand)
        break
    else:
        print("Choose either of the options listed")
