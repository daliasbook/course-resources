# Riddle: the player has 3 tries to guess the answer.


def play():
    print()
    print("THE RIDDLE")
    print("What has teeth but cannot bite?")
    tries = 3

    while tries > 0:
        answer = input("> ").strip().lower()
        if answer == "comb" or answer == "a comb":
            print("Correct! You get 3 points.")
            return 3
        tries -= 1
        print(f"Not quite. Tries left: {tries}")

    print("The answer was: a comb.")
    return 0
