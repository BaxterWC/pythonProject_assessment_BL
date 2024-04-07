import random

def blackjack():
    print("")
    print("--------------------------------")
    print("------Skeleton's BlackJack------")
    print("--------------------------------")
    print("")

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
    if total <= 21:
        print("Your total is:", total, "\n")

    for i in range(1, 3):
        deck.remove(deck[0])

    if total > 21:
        print("Your total is: 12")
        hand[1][0] = "1"
        total = 12

    print("The skeleton  has a", " ".join(map(str, deck[0])), "and a face down card")
    dealer_hand.append(deck[0])
    dealer_total = blackjack_value(dealer_hand[0])
    print("The skeleton's total is:", dealer_total, "\n")
    deck.remove(deck[0])

    if total == 21:
        print("Your total is 21, you win!")
        blackjack_win()


    while total < 21 and dealer_total < 21:
        print("Press 1 to hit or 2 to stand.")
        try:
            user_input = int(input(":"))
            if user_input == 1:
                print("You were dealt a", " ".join(map(str, deck[0])))
                hand.append(deck[0])
                deck.remove(deck[0])
                total += blackjack_value(hand[n])
                if total <= 21:
                    print("Your total is:", total)
                if total > 21:
                    aces_to_convert = sum(1 for card in hand if "Ace" in card and blackjack_value(card) == 11)
                    while total > 21 and aces_to_convert > 0:
                        for i in range(len(hand)):
                            if hand[i][0] == "Ace" and blackjack_value(hand[i]) == 11:
                                hand[i][0] = "1"
                                total -= 10
                                aces_to_convert -= 1
                                break

                    print("Your total is:", total)

                    if total > 21:
                        print("You bust and lose!")
                        print("\nAhaha! You lose!")
                        print("Want to go again?")
                        blackjack_want_to_play()

                if total == 21:
                    print("Your total is 21, you win!")
                    blackjack_win()

            elif user_input == 2:
                while dealer_total < 17:
                    if len(dealer_hand) > 1:
                        dealer_hand.append(deck[0])
                        print("The skeleton draws a", " ".join(map(str, deck[0])))
                        deck.remove(deck[0])
                        dealer_total += blackjack_value(dealer_hand[dn])
                        print("The skeleton's total is:", dealer_total, "\n")

                    else:
                        print("The skeleton flips his card to reveal a", " ".join(map(str, deck[0])))
                        dealer_hand.append(deck[0])
                        dealer_total += blackjack_value(dealer_hand[1])
                        print("The skeleton's total is:", dealer_total, "\n")
                        deck.remove(deck[0])

                if 21 >= dealer_total > total:
                    print("The skeleton must stand when their total is greater than 16")
                    print("The skeleton's hand is closer to 21, they win!")
                    print("\nAhaha! You lose!")
                    print("Want to go again?")
                    blackjack_want_to_play()
                if dealer_total <= 21:
                    print("the skeleton's total is:", dealer_total)
                if dealer_total > 21:
                    aces_to_convert = sum(1 for card in dealer_hand if "Ace" in card and blackjack_value(card) == 11)
                    while total > 21 and aces_to_convert > 0:
                        for i in range(len(dealer_hand)):
                            if dealer_hand[i][0] == "Ace" and blackjack_value(dealer_hand[i]) == 11:
                                dealer_hand[i][0] = "1"
                                total -= 10
                                aces_to_convert -= 1
                                break

                    print("The skeleton's total is:", dealer_total)

                    if dealer_total > 21:
                        blackjack_win()
                else:
                    print("The skeleton must stand when their total is greater than 16")
                    print("Your hand is closer to 21, you win!")
                    blackjack_win()
            else:
                print("Please enter either 1 or 2")

        except ValueError:
            print("Please enter a valid number")


def blackjack_value(values):
    global ace_check
    if values[0] in ["Jack", "Queen", "King"]:
        return 10
    elif values[0] in ["Ace"]:
        return 11
    else:
        return int(values[0])


def blackjack_want_to_play():
    while True:
        print("I'm a skeleton so a yes or no answer is all I can accept.")
        user_input = input(":").upper()
        if user_input == "YES":
            blackjack()
        elif user_input == "NO":
            print("Oh well.")
            print("I suppose you best get moving then.")
            print("*The skeleton pushes you into the next room.*")
            explore_area(areas["cell_area_3_info"])
        else:
            print("Please enter yes or no.")


def blackjack_win():
    print("\nCongratulations on beating me")
    print("As a reward, I'll give you my key")
    print("*You take the key and head onwards*")
    inventory.append("Key")
    explore_area(areas["cell_area_3_info"])


def knife_pickup():
    print("You can now defend yourself.")
    print("You look up to see...")
    inventory.append("rusty knife.")
    explore_area(areas["area_2_info"])


def lever():
    print("You pull on the leaver...")
    print("A slime falls from a trapdoor in the ceiling!")
    explore_area(areas["slime_fight_info"])

areas = {
    "intro_info": ["The Dungeon", "How to play:\nUse W,A,S,D to move around\nUse E to interact with the world", [('W', "Start the adventure", "area_1_info")]],
    "area_1_info": ["The Dungeon's Entrance", "The dungeon is dark and gloomy, you look around but can't see much. But you can see something shining in the distance.", [('W', "Go forward", "knife_area_info"), ('A', "Go left", None), ('S', "Go back", None),('D', "Go right", None)]],
    "knife_area_info": ["Knife Pickup", "The glistening was a knife!", [('E', "Collect the knife", knife_pickup)]],
    "area_2_info": ["The Murky Crossroads", "After collecting the knife you approach a 3-way split in the corridor.\nStraight ahead is a large set of double doors with 2 keyholes.\nTo the left is what appears to be an abandoned cell block.\nTo the right is a sewer system.", [('W', "Go straight", None), ('A', "Go left", "cell_area_1_info"), ('S', "Go back", "area_1_info"),('D', "Go right", None)]],
    "cell_area_1_info": ["The Abandoned Cell block", "You head to the left, towards what appears to be an old cell block.\nThe corridoor is narrow, so you can only go fordard or back.", [('W', "Go forward", "cell_area_2_info"), ('S', "Go back", "area_2_info"),('A', "Go left", None), ('D', "Go right", None)]],
    "cell_area_2_info": ["The Strange Skeleton", "Further down the cell block you find a skeleton. It appears to have a deck of cards...\nThe corridoor is narrow, so you can only go fordard or back.", [('W', "Talk to the skeleton", blackjack), ('S', "Go back", "cell_area_1_info"),('A', "Go left", None), ('D', "Go right", None)]],
    "cell_area_3_info": ["The Suspicious Room", "After leaving the skeleton behind, you enter a large and spacious room.\nThere seems to be a suspicious lever in the middle.\nTo the left is a cracked doorway that leads to a pond.\nTo the right is a locked door, perhaps the lever opens it?", [('W', "Walk up to the leaver", lever), ('S', "Go back", "cell_area_1_info"), ('A', "Go left", "cell_area_4_info"), ('D', "Go right", "cell_area_5_info")]],
    "slime_fight_info": ["Slime Battle!", "Oh no! This slime is going to kill you! Good thing you brought that knife...",[("E", "Stab the slime", slime_stab)]]
}

inventory = []

def explore_area(area_info):
    name, description, options = area_info
    name_length = len(name)
    padding = (30 - name_length) // 2
    middle_length = name_length + 2 * padding
    print("\n" + "-" * middle_length)
    print(f"{'-' * padding}{name}{'-' * padding}")
    print("-" * middle_length)
    print("\n" + description)
    print("\nAvailable options:")
    for key, text, _ in options:
        print(f"{key}: {text}")
    while True:
        user_input = input(":").upper()
        for key, _, next_area in options:
            if user_input == key:
                if next_area:
                    if next_area in areas:
                        explore_area(areas[next_area])
                    elif callable(next_area):
                        next_area()
                else:
                    print("You can't go that way.")
                break
        else:
            print("Input error.")


explore_area(areas["intro_info"])

