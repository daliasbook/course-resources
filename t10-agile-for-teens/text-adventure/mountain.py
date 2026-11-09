# Mountain: the player can find a map that leads to the castle.


def play(lives, inventory):
    print()
    print("THE MOUNTAIN")
    print("You climb a steep mountain. At the top, you see an old chest.")
    print("1. Open the chest")
    print("2. Climb down to the village")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        print("Inside, you find a map. It shows the way to the castle.")
        inventory.append("map")
        return lives, "castle"
    else:
        return lives, "village"
