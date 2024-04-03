player_name = 0
inventory = []
ace_check = 0
dealer_ace_check = 0
import random

def intro():
    print("--------------------------------")
    print("----------The Dungeon-----------")
    print("--------------------------------")
    print()
    print("How to play:")
    print("Use W,A,S,D to move around the dungeon.")
    print("Use E to collect items.")
    print()
    print("Please enter your name.")
    player_name = input(":")
    print("Welcome", player_name, ", adventure awaits.")
    area_1()

def knife():
    print("The glistening was a knife!")
    while True:
        print("press E to collect the knife.")
        user_input_knife = input(":").upper()
        if user_input_knife == "E":
            print("You can now defend yourself.")
            inventory.append("rusty knife.")
            area_2()
        else:
            print("input error")
def area_1():
    print("")
    print("--------------------------------")
    print("-----The Dungeon's Entrance-----")
    print("--------------------------------")
    print("")
    while True:
        print("The dungeon is dark and gloomy, you look around but cant see much.")
        print("You see something barely glistening in the distance ahead.")
        user_input = input(":").upper()
        if user_input == "W" and len(inventory) == 0:
            knife()
        elif user_input == "W" and len(inventory) > 0:
            area_2()
        elif user_input == "D" or user_input == "A" or user_input == "S":
            print("you can't go that way.")
        else:
            print("input error.")

def area_2():
    print("")
    print("--------------------------------")
    print("------The Murky Crossroads------")
    print("--------------------------------")
    print("")
    while True:
        print("After collecting the knife you approach a 3-way split in the corridor.")
        print("You can travel in any direction from this point..")
        print("Straight ahead is a large foreboding door.")
        print("To the right looks damp and sewer-like")
        print("To the left looks almost like a prison, with cells in the distance.")
        user_input = input(":").upper()
        if user_input == "W":
            print("you try the door, but it is locked! It seems two keys are needed to unlock it.")
        elif user_input == "A":
            cell_area_1()
        elif user_input == "S":
            area_1()
        elif user_input == "D":
            swamp_area_1()
        else:
            print("Input error.")
def cell_area_1():
    print("")
    print("--------------------------------")
    print("----The Abandoned Cell block----")
    print("--------------------------------")
    print("")
    while True:
        print("You head to the right, towards what appears to be an old cell block.")
        print("You can only travel forward or backwards from this point.")
        print("Straight ahead is more cells, the end is still shrouded in darkness.")
        user_input = input(":").upper()
        if user_input == "W":
            cell_area_2()
        elif user_input == "S":
            area_2()
        elif user_input == "S" or user_input == "D":
            print("You can't go that way.")
        else:
            print("Input error.")

def cell_area_2():
    print("")
    print("--------------------------------")
    print("------The Strange Skeleton------")
    print("--------------------------------")
    print("")
    while True:
        print("Further down the cell block you find a skeleton.")
        print("It appears to have a deck of cards...")
        print("As you get closer, the skeleton springs to life!")
        print("Walk all the way up to it to talk.")
        user_input = input(":").upper()
        if user_input == "W":
            print("Hello traveler...")
            print("Would you care for a game of Blackjack? I can make it worth your while...")
            while True:
                print("I'm a skeleton so a yes or no answer is all I can accept.")
                user_input = input(":").upper()
                if user_input == "YES":
                    blackjack()
                elif user_input == "NO":
                    print("Oh well.")
                    print("I suppose you best get moving then.")
                    print("*The skeleton pushes you into the next room.*")
                    cell_area_3()
                else:
                    print("Input error.")
        elif user_input == "S":
            cell_area_1()
        elif user_input == "S" or user_input == "D":
            print("You can't go that way.")
        else:
            print("Input error.")

def blackjack():
    ace_check = 0
    dealer_ace_check = 0
    dealer_hand = []
    hand = []
    n = len(hand) - 1
    dn = len(dealer_hand) - 1
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    deck = [[v, "of", s] for s in suits for v in values]
    random.shuffle(deck)
    print("You were dealt a", " ".join(map(str, deck[0])), "and a", " ".join(map(str, deck[1])))
    hand.append(deck[0])
    hand.append(deck[1])
    total = blackjack_value(hand[0]) + blackjack_value(hand[1])
    print("Your total is:", total, "\n")
    for i in range(1, 3):
        deck.remove(deck[0])

    print("The skeleton  has a", " ".join(map(str, deck[0])), "and a face down card")
    dealer_hand.append(deck[0])
    dealer_total = dealer_blackjack_value(dealer_hand[0])
    print("The skeleton's total is:", dealer_total, "\n")
    deck.remove(deck[0])

    while total < 21:
        print("Press 1 to hit or 2 to stand.")
        user_input = int(input(":"))
        if user_input == 1:
            print("You were dealt a", " ".join(map(str, deck[0])))
            hand.append(deck[0])
            deck.remove(deck[0])
            total += blackjack_value(hand[n])
            print("Your total is:", total)
            if total > 21:
                for i in range(len(hand)):
                    if "Ace" in hand[i]:
                        ace_check += 1
                        hand.remove(hand.index(["Ace"]))
                if ace_check >= 1:
                    print("Your ace turns from an 11 to a 1")
                    ace_check -= 1
                    total -= 10
                    print("Your total is:", total)
                else:
                    print("You bust and lose!")

        if user_input == 2:
            while dealer_total < 17:
                if len(dealer_hand) > 1:
                    dealer_hand.append(deck[0])
                    print("The skeleton draws a", " ".join(map(str, deck[0])))
                    deck.remove(deck[0])
                    dealer_total += dealer_blackjack_value(dealer_hand[dn])
                    print("The skeleton's total is:", dealer_total, "\n")

                else:
                    print("The skeleton flips his card to reveal a", " ".join(map(str, deck[0])))
                    dealer_hand.append(deck[0])
                    dealer_total += dealer_blackjack_value(dealer_hand[1])
                    print("The skeleton's total is:", dealer_total, "\n")
                    deck.remove(deck[0])

            if  21 >= dealer_total > total:
                print("The skeleton must stand when their total is > 17")
                print("The skeleton's hand is closer to 21, they win!")
            elif dealer_total > 21:
                for i in range(len(dealer_hand)):
                    if "Ace" in dealer_hand[i]:
                        dealer_ace_check += 1
                if dealer_ace_check >= 1:
                    print("Your ace turns from an 11 to a 1")
                    dealer_ace_check -= 1
                    total -= 10
                    print("The skeleton's total is:", total)
                else:
                    print("The Skeleton busts! You win!")
            else:
                print("Your hand is closer to 21, you win!")

def blackjack_value(values):
    global ace_check
    if values[0] in ["Jack", "Queen", "King"]:
        return 10
    elif values[0] in ["Ace"]:
        ace_check += 1
        return 11
    else:
        return int(values[0])
def dealer_blackjack_value(values):
    global dealer_ace_check
    if values[0] in ["Jack", "Queen", "King"]:
        return 10
    elif values[0] in ["Ace"]:
        dealer_ace_check += 1
        return 11
    else:
        return int(values[0])

def swamp_area_1():
    print("swamp")

def cell_area_3():
    print("celly 3")

while True:
    print("")
    blackjack()

