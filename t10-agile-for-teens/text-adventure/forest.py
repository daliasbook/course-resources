# Forest: the starting place of the adventure.


def play(lives, inventory):
    print()
    print("THE FOREST")
    print("You are at the edge of a forgotten forest. You see two paths.")
    print("1. Walk towards the river")
    print("2. Walk towards the cave")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        return lives, "river"
    else:
        return lives, "cave"
