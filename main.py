import random
slime_health = 50
player_health = 50
player_gold = 0
bet_amount = 0
slime_fight = 0
inventory = []


def blackjack():
    global bet_amount
    global player_gold
    if player_gold == 0:
        print("\nYou dont have any gold, I'll be waiting here when you get some.")
        print("*The skeleton pushes you into the next room*")
        cell_area_4_a_or_b()
    else:
        print("")
        print("--------------------------------")
        print("------Skeleton's BlackJack------")
        print("--------------------------------")
        print("")

        dealer_hand = []
        hand = []
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        deck = [[v, "of", s] for s in suits for v in values]
        random.shuffle(deck)

        while True:
            try:
                bet_amount = int(input(f"You have {player_gold} gold, place your bet: "))
                if bet_amount <= 0:
                    print("Please enter a bet greater than zero.")
                elif bet_amount > player_gold:
                    print("You don't have enough coins to place that bet.")
                else:
                    player_gold -= bet_amount
                    break
            except ValueError:
                print("Invalid bet amount.")

        print("\nYou were dealt a", " ".join(map(str, deck[0])), "and a", " ".join(map(str, deck[1])))
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
                    total += blackjack_value(hand[-1])
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
                            print("I'm keeping this gold!")
                            print(f"Current gold amount: {player_gold}")
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
                            dealer_total += blackjack_value(dealer_hand[-1])
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
                        print("I'm keeping this gold!")
                        print(f"Current gold amount: {player_gold}")
                        print("Want to go again?")
                        blackjack_want_to_play()

                    elif dealer_total > 21:
                        aces_to_convert = sum(1 for card in dealer_hand if "Ace" in card and blackjack_value(card) == 11)
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

                    elif 21 >= dealer_total == total:
                        print("It's a draw!")
                        print("Your gold was returned")
                        player_gold += bet_amount
                        print(f"Current gold amount: {player_gold}")
                        print("\nWould you like to play again?")
                        blackjack_want_to_play()

                    else:
                        print("The skeleton must stand when their total is greater than 16")
                        print("Your hand is closer to 21, you win!")
                        blackjack_win()
                else:
                    print("Please enter either 1 or 2")

            except ValueError:
                print("Please enter a valid number")


def blackjack_value(values):
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
            cell_area_4_a_or_b()
        else:
            print("Please enter yes or no.")


def blackjack_win():
    global player_gold
    print("\nCongratulations on beating me")
    player_gold += bet_amount * 2
    print(f"You were given {bet_amount*2} gold for winning!")
    print(f"Current gold amount: {player_gold}")
    print("\nWould you like to play again?")
    blackjack_want_to_play()


def knife_pickup():
    if "rusty knife" not in inventory:
        print("\nThe glistening was a rusty knife!")
        print("\nAvailable options.\nE: Pickup the knife.\nW: Leave the knife")
        while True:
            userinput = input(":").upper()
            if userinput == "E":
                print("You picked up the knife!")
                print("You can now defend yourself.")
                print("You look up to see...")
                inventory.append("rusty knife")
                explore_area(areas["area_2_info"])
            elif userinput == "W":
                print("You leave the knife behind.")
                print("You look up to see...")
                explore_area(areas["area_2_info"])
            else:
                print("Input error")
    else:
        explore_area(areas["area_2_info"])


def lever():
    print("You pull on the lever...")
    print("A slime falls from a trapdoor in the ceiling!")
    if "rusty knife" in inventory:
        explore_area(areas["slime_fight_info"])
    else:
        print("Without a knife to defend yourself, the slime knocks you out!")
        print("As you fade out of consciousness you hear it jump back into the ceiling")
        explore_area(areas["cell_area_4a_info"])


def slime_stab():
    global slime_fight
    slime_fight = 1
    print("You lunge forward and slash the slime!")
    damage = random.randint(10, 15)
    global slime_health
    slime_health -= damage
    print("You did", damage, "damage")
    if slime_health < 0:
        print("The slime now has 0 health."
              "\nYou have defeated the slime!"
              "\nIt seems that the slime had some gold in it..."
              "\nYou picked up 500 gold!")
        global player_gold
        player_gold = 500
        explore_area(areas["cell_area_4b_info"])

    else:
        print("The slime now has", slime_health, "health.")
    slime_attack = random.randint(10, 20)
    slime_attack_chance = random.randint(1, 2)
    if slime_attack_chance == 2:
        global player_health
        player_health -= slime_attack
        print("The slime lunges forward!")
        print("The slime does", slime_attack, "damage.")
        if player_health < 0:
            print("You now have 0 health."
                  "\nThe slime has defeated you!"
                  "\nAs you fade out of consciousness you hear it jump back into the ceiling")
            slime_fight = 0
            explore_area(areas["cell_area_4a_info"])
        else:
            print("You now have", player_health, "health.")
    else:
        print("The slime is loafing around")
    print("\nE:", "Stab the slime")
    print("Q", "Block the slime's next attack")


def slime_block():
    global slime_fight
    slime_fight = 1
    print("You raise your knife to defend against an attack.")
    slime_attack_chance = random.randint(1, 2)
    if slime_attack_chance == 2:
        print("The slime tried to attack but was blocked!")
    else:
        print("The slime is loafing around.")
    print("\nE:", "Stab the slime.")
    print("Q", "Block the slime's attack.")


def blackjack_rules():
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
    "\nIf neither you nor the dealer get blackjack or bust, the closer hand to 21 wins.")
    "\nIf you and the dealer tie, your bet is returned."

    explore_area(areas["cell_area_3_info"])


def cell_area_4_a_or_b():
    if slime_fight == 1:
        explore_area(areas["cell_area_4b_info"])
    else:
        explore_area(areas["cell_area_4a_info"])


def buy_key():
    global player_gold
    if "key_1" not in inventory:
        if player_gold >= 1000:
            inventory.append("key_2")
            player_gold -= 1000
            print("You bought the key! Is there anything else you would like to do?")
            print(f"Current gold: {player_gold}")
            if "fishing_rod" not in inventory:
                areas["merchant_area_1_info"][2] = [('E', "Buy the fishing rod (500 gold)", buy_fishing_rod), ('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info")]
                print("\nAvailable options:\nE: Buy the fishing rod (100 gold)\nW: Sell fish\nS: Exit the shop")
            else:
                areas["merchant_area_1_info"][2] = [('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info")]
                print("\nAvailable options:\nW: Sell fish\nS: Exit the shop")

        elif player_gold < 1000:
            print("You do not have enough gold to buy the key, is there anything else you would like to do?")

    else:
        print("Input error")


def buy_fishing_rod():
    global player_gold
    if "fishing_rod" not in inventory:
        if player_gold >= 100:
            inventory.append("fishing_rod")
            player_gold -= 100
            print("You bought the fishing rod! Is there anything else you would like to do?")
            print(f"Current gold: {player_gold}")
            if "key_1" not in inventory:
                areas["merchant_area_1_info"][2] = [('Q', "Buy the key (1000 gold)", buy_key), ('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info")]
                print("\nAvailable options:\nQ: Buy the key (1000 gold)\nW: Sell fish\nS: Exit the shop")
            else:
                areas["merchant_area_1_info"][2] = [('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info")]
                print("\nAvailable options:\nW: Sell fish\nS: Exit the shop")

        elif player_gold < 100:
            print("You do not have enough gold to buy the key, is there anything else you would like to do?")

    else:
        print("Input error")


def sell_fish():
    if "fish" in inventory:
        num_fish = 0
        print(f"You have {inventory.count("fish")} fish.")
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

        for i in range(num_fish):
            inventory.remove("fish")

        global player_gold
        player_gold += num_fish * 100
        print(f"You sold {num_fish} fish and gained {num_fish * 100} gold.")
        print(f"Current gold: {player_gold}")
        print("Would you like to do anything else?")
        print("\nAvailable options:\nQ: Buy the key (1000 gold)\nW: Sell more fish\nS: Exit the shop")
    else:
        print("You don't have any fish to sell. Is there anything else you would like to do?")


def fishing_game(item):
    if "fishing_rod" in inventory:
        print("You cast your line into the pond...")
        if "key" in inventory or item == "fish":
            catch = random.choice(["fish", "boot", "seaweed", "old tin can"])
        else:
            catch = random.choice([item, "boot", "seaweed", "old tin can"])
        if catch == item:
            print(f"Congratulations! You caught a {item}!")
            inventory.append(item)
            print("\nAvailable options:\nQ: Go fishing\nS: Exit the pond")
        else:
            print(f"You caught a {catch}! Unlucky.. maybe the next one will be something more valuable?")
            print("\nAvailable options:\nQ: Go fishing\nS: Exit the pond")
    else:
        print("You do not have a fishing rod, perhaps a merchant might sell one?")
        print("\nAvailable options:\nQ: Go fishing\nS: Exit the pond")


def key_check():
    if "key_2" and "key" in inventory:
        print("You open the doors and walk up the steps to freedom")
        print("")
        print("---------------------------------")
        print("-------------The End-------------")
        print("---------------------------------")
        while True:
            input("")
    else:
        print("The door is locked, seems like you need two keys to open it!")

areas = {
    "intro_info": ["The Dungeon", "How to play:\nUse W,A,S,D to move around\nUse E and Q to interact with the world when prompted", [('W', "Start the adventure", "area_1_info")]],
    "area_1_info": ["The Dungeon's Entrance", "The dungeon is dark and gloomy, you look around but can't see much. But you can see something shining in the distance.\nYou can only move forward, for fear of the unknown all around you.", [('W', "Go forward towards the glistening", knife_pickup), ('A', "Go left into the darkness", None), ('S', "Go back into the darkness", None), ('D', "Go right into the darkness", None)]],
    "area_2_info": ["The Murky Crossroads", "You approach a 3-way split in the corridor.\nStraight ahead is a large set of double doors with 2 keyholes.\nTo the left is what appears to be an abandoned cell block.\nTo the right is a sewer system.", [('W', "Go straight towards the door", key_check), ('A', "Go left towards the cells", "cell_area_1_info"), ('S', "Go back the way you came", "area_1_info"), ('D', "Go right towards the sewers", "sewer_area_1_info")]],
    "cell_area_1_info": ["The Abandoned Cell block", "You head to the left, towards what appears to be an old cell block.\nThe corridor is narrow, so you can only go forward or back.", [('W', "Go forward, further down the corridor", "cell_area_2_info"), ('A', "Go left into a wall", None), ('S', "Go back the way you came", "area_2_info"), ('D', "Go right into a wall", None)]],
    "cell_area_2_info": ["The Skeleton's Cell", "Further down the cell block you find a skeleton. It appears to have a deck of cards...\nThe corridor is narrow, so you can only go forward or back.", [('W', "Talk to the skeleton", "cell_area_3_info"),  ('A', "Go left into a wall", None), ('S', "Go back the way you came", "cell_area_1_info"), ('D', "Go right into a wall", None)]],
    "cell_area_3_info": ["The Skeleton", "Hello traveller, would you care for a game of blackjack?\nI can make it worth your while...", [('E', "Play a game of blackjack", blackjack), ('Q', "Learn the rules of blackjack", blackjack_rules), ('W', "Walk past the skeleton", cell_area_4_a_or_b), ('A', "Go left into a wall", None), ('S', "Go back the way you came", "cell_area_2_info"), ('D', "Go right into a wall", None)]],
    "cell_area_4a_info": ["A Suspicious Room", "You find yourself in a large open room.\nThere seems to be a suspicious lever in the middle.\nTo the left locked door, perhaps the lever opens is?.\nTo the right is a locked door, perhaps the lever opens it?", [('W', "Walk up to the lever", lever), ('S', "Go back the way you came", "cell_area_3_info"), ('A', "Go left towards a locked door", None), ('D', "Go right towards a locked door", None)]],
    "slime_fight_info": ["Slime Battle!", "Oh no! This slime is going to kill you! Good thing you brought that knife...", [('E', "Stab the slime", slime_stab), ('Q', "Block the slime's incoming attack", slime_block)]],
    "cell_area_4b_info": ["A Suspicious Room", "The lever cannot be moved anymore.\nThe doors on the left and the right are open!\nThrough the left door is a fishing pond.\nThrough the right door is a merchant.", [('W', "Go forward into a wall", None), ('A', "Go left to the pond", "fishing_area_1_info"), ('S', "Go Back the way you came", "cell_area_3_info"), ('D', "Go right to the merchant", "merchant_area_1_info")]],
    "merchant_area_1_info": ["The Merchant", "Hello traveller! I am a humble merchant.\nBut the last group that came by bought out all my stock except for 2 item!\nAll I can sell you is a strange key and a fishing rod\nIf you're in need of extra gold, I will buy fish from you (100 gold per fish).", [('Q', "Buy the key (1,000 gold)", buy_key), ('E', "Buy the fishing rod (100 gold)", buy_fishing_rod), ('W', "Sell fish", sell_fish), ('S', "Exit the shop", "cell_area_4b_info")]],
    "fishing_area_1_info": ["The Fishing Pond", "There is a small pond in which you could fish.\nBut you are in a dungeon... so dont expect too many fish.", [('Q', "Go fishing ", lambda: fishing_game("fish")), ('S', "Go back the way you came", "cell_area_4b_info")]],
    "sewer_area_1_info": ["The Sludgy Sewers", "The sewer is rather smelly and slimy, currently you can only move forward or back.", [('W', "Go deeper into the sewer", "sewer_area_2_info"), ('A', "Go left into a wall", None), ('S', "Go back the way you came", "area_2_info"), ('D', "Go right into a wall", None)]],
    "sewer_area_2_info": ["The Toxic pond", "You reach a large (and probably toxic) pond.\nYou see something glint at the bottom of the pond, possibly a key?.", [('Q', "Go fishing", lambda: fishing_game("key")), ('S', "Go back the way you came", "sewer_area_1_info")]]
}

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

