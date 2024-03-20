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
    print("Welcome", player_name, ", adventure awaits")
    area_1()


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
        if user_input == "W":
            print("The glistening was a knife!")
            while True:
                print("press E to collect the knife")
                user_input_knife=input(":").upper()
                if user_input_knife == "E":
                    print("You can now defend yourself.")
                    inventory.append("rusty knife")
                    area_2()
                else:
                    print("input error")

        elif user_input == "D" or user_input == "A" or user_input == "S":
            print("you can't go that way")
        else:
            print("input error")

def area_2():
    print("")
    print("--------------------------------")
    print("------The Murky Crossroads------")
    print("--------------------------------")
    print("")
    while True:
        print("After collecing the knife you approach a 3-way split in the corridor.")
        print("You can travel in any direction from this point..")
        user_input = input(":").upper()
        if user_input == "W":
            print("The glistening was a knife!")
            while True:
                print("press E to collect the knife")
                user_input_knife = input(":").upper()
                if user_input_knife == "E":
                    print("You can now defend yourself.")
                    inventory.append("rusty knife")
                    area_2()
                else:
                    print("input error")

        elif user_input == "D" or user_input == "A" or user_input == "S":
            print("you can't go that way")
        else:
            print("input error")
intro()

