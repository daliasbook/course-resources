# Hidden word: the player guesses the missing letter.


def play():
    print()
    print("THE HIDDEN WORD")
    word = "python"
    hidden = "pyt_on"
    print(f"Which letter is missing? {hidden}")
    letter = input("> ").strip().lower()

    if letter == word[3]:
        print(f"Correct! The word is {word}. You get 2 points.")
        return 2
    else:
        print(f"Wrong! The word was {word}.")
        return 0
