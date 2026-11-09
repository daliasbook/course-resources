# River: the player can swim (risky) or cross the bridge.


def play(lives, inventory):
    print()
    print("THE RIVER")
    print("A wide river blocks your way. There is an old bridge nearby.")
    print("1. Swim across")
    print("2. Cross the old bridge")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        print("The water is cold and fast. You lose a life!")
        lives -= 1
        return lives, "village"
    else:
        print("The bridge creaks, but you make it across.")
        return lives, "mountain"
