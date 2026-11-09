# Cave: the player can find a torch.


def play(lives, inventory):
    print()
    print("THE CAVE")
    print("It is dark inside. Something shiny lies on the ground.")
    print("1. Pick up the shiny object")
    print("2. Leave the cave")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        print("It is a torch! You add it to your inventory.")
        inventory.append("torch")
        print("A bat flies at you in the dark. You lose a life!")
        lives -= 1
        return lives, "castle"
    else:
        return lives, "river"
