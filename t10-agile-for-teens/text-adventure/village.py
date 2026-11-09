# Village: the player can rest and get a life back.


def play(lives, inventory):
    print()
    print("THE VILLAGE")
    print("You arrive in a small village. A friendly baker waves at you.")
    print("1. Rest at the bakery")
    print("2. Keep walking to the forest")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        print("You eat warm bread and feel better. You get a life back!")
        lives += 1
        return lives, "forest"
    else:
        return lives, "forest"
