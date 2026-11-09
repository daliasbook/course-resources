# Castle: the treasure room is here, but you need a torch to see it.


def play(lives, inventory):
    print()
    print("THE CASTLE")
    print("You reach an old castle. A heavy door leads to a dark room.")
    print("1. Open the door")
    print("2. Go back to the forest")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        if "torch" in inventory:
            print("Your torch lights up the room: it is the TREASURE ROOM!")
            return lives, "treasure"
        else:
            print("It is too dark to see anything. You trip and lose a life!")
            lives -= 1
            return lives, "forest"
    else:
        return lives, "forest"
