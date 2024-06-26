# Defining variables to be used later on
import random
import os
import time
import msvcrt

levers_pulled = 0
player_gold = 0
bet_amount = 0
inventory = []

# Function to be called when blackjack is played, a function is a section of code that can be called at any time when needed.
def blackjack():
    # os.system('cls') will clear the screen when called. It is used so that the player's screen is not cluttered with text everytime something new is added.
    os.system('cls')
    global bet_amount
    global player_gold
    # If statement is used to check to see if the player has gold to bet with, if they don't have gold they get sent to the next area instead. An if statement checks whether  the player fulfils a certain or not and condition acts accordingly.
    if player_gold == 0:
        print("\nYou dont have any gold, I'll be waiting here when you get some.")
        print("*The skeleton pushes you into the next room*")
        # time.sleep(n) pauses the game for n seconds, this is used to give the player time to read important text before the screen clears
        time.sleep(3)
        while msvcrt.kbhit():
            input()
        cell_area_4_a_or_b()
    else:
        print("")
        print("--------------------------------")
        print("------Skeleton's BlackJack------")
        print("--------------------------------")
        print("")

        # Defining the hands of both players and the deck of cards.
        dealer_hand = []
        hand = []
        # A list is used to store the values for the cards in a more efficient way than listing every single possible card. A list is a collection of items stored in a single variable for ease of access.
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        #This combines both lists to form 1 list of correctly formatted cards.
        deck = [[v, "of", s] for s in suits for v in values]
        # Random.shuffle is used to shuffle the deck so that the cards dealt are different each time.
        random.shuffle(deck)

        # Error detection for player betting value. A while loop is a section of code that repeats indefinitely until a certain requirement is fulfilled. This loop repeats until it is broken so that the player can re-enter their response if it is invalid.
        while True:
            try:
                bet_amount = int(input(f"You have {player_gold} gold, place your bet or press 0 to exit the game\n: "))
                if bet_amount < 0:
                    print("Please enter a bet greater than zero.")
                elif bet_amount == 0:
                    exit_game()
                elif bet_amount > player_gold:
                    print("You don't have enough gold to place that bet.")
                else:
                    player_gold -= bet_amount
                    break
            except ValueError:
                print("Invalid bet amount.")

        # Dealing the player their initial 2 cards, appending them to the 'hand' list and removing them from the 'deck' list.
        print("\nYou were dealt a", " ".join(map(str, deck[0])), "and a", " ".join(map(str, deck[1])))
        # hand.append(deck[0]) takes the first card in the 'deck' list and adds it to the 'hand list'. This is used for a distinction in the player hand and deck of cards.
        hand.append(deck[0])
        hand.append(deck[1])
        total = blackjack_value(hand[0]) + blackjack_value(hand[1])
        if total <= 21:
            print("Your total is:", total, "\n")

        # Deck.remove(deck[0]) removes the first card from the deck. This loops twice to remove both the cards that were appended to the players hand to avoid duplication of cards.
        for i in range(1, 3):
            deck.remove(deck[0])

        # This is only here for if the player is dealt 2 aces on start, it sets the total to 12 and makes one of the ace's value equal to 1. This is to prevent the code from freaking out when the starting value is > 21
        if total > 21:
            print("Your total is: 12")
            hand[1][0] = "1"
            total = 12

        # Showing the player the skeleton's first card, appending it to the 'dealer_hand' list and removing it from the 'deck' list.
        print("The skeleton as a", " ".join(map(str, deck[0])), "and a face down card")
        dealer_hand.append(deck[0])
        dealer_total = blackjack_value(dealer_hand[0])
        print("The skeleton's total is:", dealer_total, "\n")
        deck.remove(deck[0])

        if total == 21:
            print("Your total is 21, you win!")
            blackjack_win()

        # This loops until the player busts or wins, and is where the hitting and standing happens.
        while total < 21 and dealer_total < 21:
            print("Press 1 to hit, 2 to stand or 0 to exit the game.")
            try:
                user_input = int(input(":"))
                if user_input == 1:
                    print("You were dealt a", " ".join(map(str, deck[0])))
                    hand.append(deck[0])
                    deck.remove(deck[0])
                    total += blackjack_value(hand[-1])
                    if total <= 21:
                        print("Your total is:", total)
                    # If the player goes over 21 it checks how many aces are in the player's hand then converts them into a 1 and reduces the total by 10.
                    if total > 21:
                        # Checking how many aces are in the players hand and need to be changed into a 1.
                        aces_to_convert = sum(1 for card in hand if "Ace" in card and blackjack_value(card) == 11)
                        while total > 21 and aces_to_convert > 0:
                            # Loops for however many cards the player has. A for loop is a loop that repeats a block of code a set amount of times. In this case, the loop runs once for each card in the player's hand.
                            for i in range(len(hand)):
                                # Checks if a given card is an ace and hasn't already been turned into a 1 to avoid counting the same ace twice.
                                if hand[i][0] == "Ace" and blackjack_value(hand[i]) == 11:
                                    # Converts ace into a 1 to avoid repeats.
                                    hand[i][0] = "1"
                                    # Minus 10 from total, converting 11 to 1 is a loss of 10 points.
                                    total -= 10
                                    aces_to_convert -= 1
                                    break

                        print("Your total is:", total)

                        if total > 21:
                            print("You bust and lose!")
                            print("\nAhaha! You lose!")
                            print("I'm keeping this gold!")
                            print(f"Current gold amount: {player_gold}")
                            blackjack_want_to_play()

                    if total == 21:
                        print("Your total is 21, you win!")
                        blackjack_win()

                elif user_input == 2:
                    break

                elif user_input == 0:
                    exit_game()

                else:
                    print("Please enter either 1 or 2.")

            except ValueError:
                print("Please enter a valid number.")

        while dealer_total < 17:
            if len(dealer_hand) == 1:
                print("The skeleton flips his card to reveal a", " ".join(map(str, deck[0])))
                dealer_hand.append(deck[0])
                dealer_total += blackjack_value(dealer_hand[-1])
                print("The skeleton's total is:", dealer_total, "\n")
                deck.remove(deck[0])

            elif dealer_total < 17:
                dealer_hand.append(deck[0])
                print("The skeleton draws a", " ".join(map(str, deck[0])))
                deck.remove(deck[0])
                dealer_total += blackjack_value(dealer_hand[-1])
                if dealer_total <= 21:
                    print("The skeleton's total is:", dealer_total, "\n")

                if dealer_total > 21:
                    # Same as player ace conversion code but for the dealer's hand instead.
                    aces_to_convert = sum(1 for card in dealer_hand if card[0] == "Ace" and blackjack_value(card) == 11)
                    while dealer_total > 21 and aces_to_convert > 0:
                        for i in range(len(dealer_hand)):
                            if dealer_hand[i][0] == "Ace" and blackjack_value(dealer_hand[i]) == 11:
                                dealer_hand[i][0] = "1"
                                dealer_total -= 10
                                aces_to_convert -= 1
                                break

                    print("The skeleton's total is:", dealer_total)

        if dealer_total > 21:
            print("The skeleton busts, you win!")
            blackjack_win()

        elif 21 >= dealer_total > total and dealer_total > 16:
            print("The skeleton must stand when their total is greater than 16")
            print("The skeleton's hand is closer to 21, they win!")
            print("\nAhaha! You lose!")
            print("I'm keeping this gold!")
            print(f"Current gold amount: {player_gold}")
            blackjack_want_to_play()

        elif 21 >= dealer_total == total and dealer_total > 16:
            print("It's a draw!")
            print("Your gold was returned")
            player_gold += bet_amount
            print(f"Current gold amount: {player_gold}")
            blackjack_want_to_play()

        elif 21 >= total > dealer_total > 16:
            print("The skeleton must stand when their total is greater than 16")
            print("Your hand is closer to 21, you win!")
            blackjack_win()


# Function to calculate the value of a card. Because I use index position for values, face cards and aces need to be set as 10 and 11 respectively.
def blackjack_value(values):
    if values[0] in ["Jack", "Queen", "King"]:
        return 10
    elif values[0] in ["Ace"]:
        return 11
    else:
        return int(values[0])


# Asks the player if the want to go again, made it a function to save on repeat code.
def blackjack_want_to_play():
    while True:
        print("\nWould you like to play again?\nAvailable options:\nY: Play again\nN: Don't play again\n0: Exit the game")
        user_input = input(":").upper()
        if user_input == "Y":
            blackjack()
        elif user_input == "N":
            print("\nOh well.")
            print("I suppose you best get moving then.")
            print("*The skeleton pushes you into the next room.*")
            time.sleep(3)
            while msvcrt.kbhit():
                input()
            cell_area_4_a_or_b()
        elif user_input == "0":
            exit_game()
        else:
            print("Please enter yes or no.")


# This calculates how much gold is to be given to the player when they win.
def blackjack_win():
    global player_gold
    print("\nCongratulations on beating me")
    player_gold += bet_amount * 2
    print(f"You were given {bet_amount * 2} gold for winning!")
    print(f"Current gold amount: {player_gold}")
    blackjack_want_to_play()


# A little unscrambling puzzle to give the player their first gold.
def lever():
    print("\nYou pull on the lever...")
    print("A mysterious box falls from the ceiling!")
    global player_gold
    global levers_pulled
    levers_pulled = 1
    print("The box seems to have a puzzle-based lock on it.")
    # List of possible words for the puzzle.
    puzzle_words = ['apple', 'chair', 'bread', 'dream', 'house', 'music', 'river', 'table', 'zebra']
    puzzle_word = random.choice(puzzle_words)
    letters = list(puzzle_word)
    random.shuffle(letters)
    scrambled_word = ''.join(letters)
    print(f"The box has a scrambled word on it: {scrambled_word}\nIf you can unscramble the word, the box might open!\nInput your answer to open the box, or enter 0 to exit the game.")
    # Loops until the player gets the puzzle correct.
    while True:
        user_input = input(":").lower()
        if user_input == puzzle_word:
            print("\nCorrect!\nThe box springs open to reveal 200 gold!")
            player_gold += 200
            print(f"Current gold amount: {player_gold}")
            time.sleep(3)
            while msvcrt.kbhit():
                input()
            cell_area_4_a_or_b()
        elif user_input == "0":
            exit_game()
        else:
            print("Incorrect! Have another try.")


def blackjack_rules():
    os.system('cls')
    print("The aim of the game is to get a score of 21 or as close to it as possible without going over."
          "\nYou can bet as much money as you like, and if you win, you get twice what you bet back!"
          "\nFace cards (Jack, Queen, King) are worth 10 points."
          "\nNumber cards are worth their face value."
          "\nAn Ace can be worth either 1 or 11 points, whichever is more advantageous."
          "\nAfter receiving your initial two cards, you can choose to 'hit' to receive another card or 'stand' to keep your current total."
          "\nIf you go over 21, you 'bust' and lose the round."
          "\nIf you get blackjack (21 with your first two cards), you win instantly."
          "\nThe dealer starts with 1 card shown to you, and another card hidden."
          "\nThe dealer will continue to draw cards until their total is greater than 16, where they will stand."
          "\nIf neither you nor the dealer get blackjack or bust, the closer hand to 21 wins."
          "\nIf you and the dealer tie, your bet is returned.")

    while True:
        print("\n\nAvailable options:\nE: Finish reading\n0: Exit the game")
        userinput = input(":").upper()
        if userinput == "E":
            os.system('cls')
            explore_area(areas["cell_area_3_info"])
        elif userinput == "0":
            exit_game()
        else:
            print("Please enter Y")



# This is to make sure that when going from another room back into the suspicious room after the player has done the unscrambling puzzle, it takes them into suspicious room b (where the lever has already been pulled).
def cell_area_4_a_or_b():
    os.system('cls')
    if levers_pulled == 1:
        explore_area(areas["cell_area_4b_info"])
    else:
        explore_area(areas["cell_area_4a_info"])


# Buying a key from the merchant
def buy_key():
    global player_gold
    # Checks to see if the player already has a key, if they do, they get an 'input error' for trying to re-buy the key because the option is hidden.
    if "key_1" not in inventory:
        if player_gold >= 1000:
            inventory.append("key_2")
            player_gold -= 1000
            print("\nYou bought the key! Is there anything else you would like to do?")
            print(f"Current gold: {player_gold}")
            # Changing the merchant's shop based on what items have been bought so that already purchased items are hidden and can't be re-bought.
            if "fishing_rod" not in inventory:
                areas["merchant_area_1_info"][2] = [('E', "Buy the fishing rod (100 gold)", buy_fishing_rod), ('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info"), ('0', "Exit game", exit_game)]
                print("\nAvailable options:\nE: Buy the fishing rod (100 gold)\nW: Sell fish\nS: Exit the shop\n0: Exit game")
            else:
                areas["merchant_area_1_info"][2] = [('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info"), ('0', "Exit game", exit_game)]
                print("\nAvailable options:\nW: Sell fish\nS: Exit the shop\n0: Exit game")

        elif player_gold < 1000:
            print("You do not have enough gold to buy the key, is there anything else you would like to do?")

    else:
        print("Input error")


# Buying a fishing rod from the merchant
def buy_fishing_rod():
    global player_gold
    # Checks to see if the player already has a fishing rod, if they do, they get an 'input error' for trying to re-buy the key because the option is hidden.
    if "fishing_rod" not in inventory:
        if player_gold >= 100:
            inventory.append("fishing_rod")
            player_gold -= 100
            print("\nYou bought the fishing rod! Is there anything else you would like to do?")
            print(f"Current gold: {player_gold}")
            # Changing the merchant's shop based on what items have been bought so that already purchased items are hidden and can't be re-bought.
            if "key_2" not in inventory:
                areas["merchant_area_1_info"][2] = [('Q', "Buy the key (1000 gold)", buy_key), ('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info"), ('0', "Exit game", exit_game)]
                print("\nAvailable options:\nQ: Buy the key (1000 gold)\nW: Sell fish\nS: Exit the shop\n0: Exit game")
            else:
                areas["merchant_area_1_info"][2] = [('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info"), ('0', "Exit game", exit_game)]
                print("\nAvailable options:\nW: Sell fish\nS: Exit the shop")

        elif player_gold < 100:
            print("You do not have enough gold to buy the key, is there anything else you would like to do?")

    else:
        print("Input error")


# Selling fish to the merchant.
def sell_fish():
    if "fish" in inventory:
        num_fish = 0
        # Tells the player how many fish they have available to sell.
        print("You have", inventory.count("fish"), "fish")
        # Error detection for the player's input on how many fish they want to sell.
        while True:
            try:
                num_fish = int(input("How many fish would you like to sell?: "))
                if num_fish < 0:
                    print("Please enter a positive number.")
                elif num_fish > inventory.count("fish"):
                    print("You don't have that many fish to sell.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Removing sold fish from the player's inventory.
        for i in range(num_fish):
            inventory.remove("fish")

        global player_gold
        player_gold += num_fish * 100
        print(f"You sold {num_fish} fish and gained {num_fish * 100} gold.")
        print(f"Current gold: {player_gold}")
        print("Would you like to do anything else?")
        if "key" not in inventory:
            print("\nAvailable options:\nQ: Buy the key (1000 gold)\nW: Sell more fish\nS: Exit the shop")
        else:
            print("\nAvailable options:\nW: Sell more fish\nS: Exit the shop")
    else:
        print("You don't have any fish to sell. Is there anything else you would like to do?")


# Fishing general function, that subs in key or fish to the 'item' variable based on where the player is fishing.
def fishing_game(item):
    if "fishing_rod" in inventory:
        os.system('cls')
        print("\nYou cast your line into the pond...")
        time.sleep(random.randint(1, 5))
        # mscrvt.kbhit catches any inputs buffered during the time.sleep and prints them later to avoid spammed valid inputs during time.sleep being accepted as valid
        while msvcrt.kbhit():
            input()
        # This stops the player from fishing up multiple keys
        if "key" in inventory or item == "fish":
            catch = random.choice(["fish", "boot", "seaweed", "old tin can"])
        else:
            catch = random.choice([item, "boot", "seaweed", "old tin can"])
        # Alerts the player that they have caught a desirable item.
        if catch == item:
            print(f"Congratulations! You caught a {item}!")
            inventory.append(item)
            # Keeps track of how many fish the player has caught, but only when fishing for fish (not a key).
            if item == "fish":
                print("Current number of fish:", inventory.count("fish"))
            print("\nAvailable options:\nQ: Go fishing\nS: Leave the pond\n0: Exit game")
        else:
            print(f"You caught a {catch}! Unlucky.. maybe the next one will be something more valuable?")
            if item == "fish":
                print("Current number of fish:", inventory.count("fish"))
            print("\nAvailable options:\nQ: Go fishing\nS: Leave the pond\n0: Exit game")

    else:
        print("You do not have a fishing rod, perhaps a merchant might sell one?")
        print("\nAvailable options:\nQ: Go fishing\nS: Leave the pond\n0: Exit game")


# Checks if the player has both keys required to beat the game.
def key_check():
    if "key_2" and "key" in inventory:
        print("You open the doors and walk up the steps to freedom.")
        print("")
        print("---------------------------------")
        print("-------------The End-------------")
        print("---------------------------------")
        while True:
            input("")
    else:
        print("The door is locked, seems like you need two keys to open it!")


# Function for exiting the game, it resets all the global variables and clears the screen.
def exit_game():
    global player_gold
    global inventory
    global levers_pulled
    levers_pulled = 0
    player_gold = 0
    inventory = []
    areas["merchant_area_1_info"][2] = [('Q', "Buy the key (1000 gold)", buy_key), ('E', "Buy the fishing rod (100 gold)", buy_fishing_rod), ('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info"), ('0', "Exit game", exit_game)]
    os.system('cls')
    explore_area(areas["intro_info"])


# Dictionary that defines all of the of the games areas. It contains the area's name, description, and actions. A dictionary is used to store key-value pairs, where each key is associated with a corresponding value. In this context, the dictionary stores the names of the areas and pairs them with a list containing a description and user options.
areas = {
    "intro_info": ["The Dungeon", "How to play:\nUse W,A,S,D to move around\nUse E and Q to interact with the world when prompted.\nPress 0 at any time to exit.", [('W', "Start the adventure", "area_1_info"), ('0', "Exit game", exit_game)]],
    "area_1_info": ["The Dungeon's Entrance", "The dungeon is dark and gloomy, you look around but can't see much. But you can see something in the distance.\nYou can only move forward, for fear of the unknown all around you.", [('W', "Go forwards", "area_2_info"), ('A', "Go left into the darkness", None), ('S', "Go back into the darkness", None), ('D', "Go right into the darkness", None), ('0', "Exit game", exit_game)]],
    "area_2_info": ["The Murky Crossroads", "You approach a 3-way split in the corridor.\nStraight ahead is a large set of double doors with 2 keyholes.\nTo the left is what appears to be an abandoned cell block.\nTo the right is a sewer system.", [('W', "Go straight towards the door", key_check), ('A', "Go left towards the cells", "cell_area_1_info"), ('S', "Go back towards the dungeon's entrance", "area_1_info"), ('D', "Go right towards the sewers", "sewer_area_1_info"), ('0', "Exit game", exit_game)]],
    "cell_area_1_info": ["The Abandoned Cell block", "You head to the left, towards what appears to be an old cell block.\nThe corridor is narrow, so you can only go forward or back.", [('W', "Go forward, further down the corridor", "cell_area_2_info"), ('A', "Go left into a wall", None), ('S', "Go back to the crossroads", "area_2_info"), ('D', "Go right into a wall", None), ('0', "Exit game", exit_game)]],
    "cell_area_2_info": ["The Skeleton's Cell", "A skeleton sits in front of you, it appears to have a deck of cards...\nThe corridor is narrow, so you can only go forward or back.", [('W', "Talk to the skeleton", "cell_area_3_info"),  ('A', "Go left into a wall", None), ('S', "Go back to the entrance of the cell block", "cell_area_1_info"), ('D', "Go right into a wall", None), ('0', "Exit game", exit_game)]],
    "cell_area_3_info": ["The Skeleton", "Hello traveller, would you care for a game of blackjack?\nI can make it worth your while...", [('E', "Play a game of blackjack", blackjack), ('Q', "Learn the rules of blackjack", blackjack_rules), ('W', "Walk past the skeleton", cell_area_4_a_or_b), ('A', "Go left into a wall", None), ('S', "Stop talking to the skeleton", "cell_area_2_info"), ('D', "Go right into a wall", None), ('0', "Exit game", exit_game)]],
    "cell_area_4a_info": ["A Suspicious Room", "You find yourself in a large open room.\nThere seems to be a suspicious lever in the middle.\nTo the left locked door, perhaps the lever opens is?.\nTo the right is a locked door, perhaps the lever opens it?", [('W', "Walk up to the lever", lever), ('S', "Go back to the skeleton's cell", "cell_area_3_info"), ('A', "Go left towards a locked door", None), ('D', "Go right towards a locked door", None), ('0', "Exit game", exit_game)]],
    "cell_area_4b_info": ["A Suspicious Room", "The lever cannot be moved anymore.\nThe doors on the left and the right are open!\nThrough the left door is a fishing pond.\nThrough the right door is a merchant.", [('W', "Go forward into a wall", None), ('A', "Go left to the pond", "fishing_area_1_info"), ('S', "Go back to the skeleton's cell", "cell_area_3_info"), ('D', "Go right to the merchant", "merchant_area_1_info"), ('0', "Exit game", exit_game)]],
    "merchant_area_1_info": ["The Merchant", "Hello traveller! I am a humble merchant.\nBut the last group that came by bought out all my stock except for 2 item!\nAll I can sell you is a strange key and a fishing rod\nIf you're in need of extra gold, I will buy fish from you (100 gold per fish).", [('Q', "Buy the key (1,000 gold)", buy_key), ('E', "Buy the fishing rod (100 gold)", buy_fishing_rod), ('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info"), ('0', "Exit game", exit_game)]],
    "fishing_area_1_info": ["The Fishing Pond", "There is a small pond in which you could fish.\nBut you are in a dungeon... so dont expect too many fish.", [('Q', "Go fishing ", lambda: fishing_game("fish")), ('S', "Go back to suspicious room", "cell_area_4b_info"), ('0', "Exit game", exit_game)]],  # Lambda is used here to call the specific fishing_game(fish) function so that the player will fish for fish instead of a key.
    "sewer_area_1_info": ["The Sludgy Sewers", "The sewer is rather smelly and slimy, currently you can only move forward or back.", [('W', "Go deeper into the sewer", "sewer_area_2_info"), ('A', "Go left into a wall", None), ('S', "Go back to the crossroads", "area_2_info"), ('D', "Go right into a wall", None), ('0', "Exit game", exit_game)]],
    "sewer_area_2_info": ["The Toxic pond", "You reach a large (and probably toxic) pond.\nYou see something glint at the bottom of the pond, possibly a key?.", [('Q', "Go fishing", lambda: fishing_game("key")), ('S', "Leave the pond", "sewer_area_1_info"), ('0', "Exit game", exit_game)]]
}


# This is the area general function that areas from the previous dictionary get subbed into.
def explore_area(area_info):
    name, description, options = area_info
    name_length = len(name)
    padding = (30 - name_length) // 2
    middle_length = name_length + 2 * padding
    # This is to make the title of the area a symmetrical box of "--" around the name for aesthetic purposes.
    print("\n" + "-" * middle_length)
    print(f"{'-' * padding}{name}{'-' * padding}")
    print("-" * middle_length)
    print("\n" + description)
    print("\nAvailable options:")
    # This for loop prints the player's available options.
    for key, text, i in options:
        print(f"{key}: {text}")
    # This first checks what the player's input is and whether it is a valid input. Then checks if it is a function or an area name.
    while True:
        user_input = input(":").upper()
        for key, i, next_area in options:
            if user_input == key:
                if next_area:
                    if next_area in areas:
                        os.system('cls')
                        explore_area(areas[next_area])
                    elif callable(next_area):
                        next_area()
                else:
                    print("You can't go that way.")
                break
        else:
            print("Input error.")


# Calls the first area (intro).
explore_area(areas["intro_info"])
