player_name = 0
inventory = []

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
            print("You can't go that way".)
        else:
            print("Input error".)

def cell_area_2():
    print("")
    print("--------------------------------")
    print("------The Strange Skeleton------")
    print("--------------------------------")
    print("")
    while True:
        print("Further down the cell block you find a skeleton.")
        print("It appears to have a deck of cards.")
        print("As you get closer, the skeleton springs to life!")
        print("Walk all the way up to it to talk.")
        user_input = input(":").upper()
        if user_input == "W":
            skeleton_encounter()
        elif user_input == "S":
            cell_area_1()
        elif user_input == "S" or user_input == "D":
            print("You can't go that way.")
        else:
            print("Input error.")
    print("")
def skeleton_encounter():
    print("Hello traveler...")
    print("Would you care for a game of Blackjack? I can make it worth your while...")
def swamp_area_1():
    print("swamp")

intro()

