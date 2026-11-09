# Guess the number: the secret number is written in the code.


def play():
    print()
    print("GUESS THE NUMBER")
    secret = 7
    tries = 0
    print("I am thinking of a number between 1 and 20.")

    while True:
        text = input("Your guess? > ").strip()
        if not text.isdigit():
            print("Please type a whole number.")
            continue
        guess = int(text)
        tries += 1
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print(f"You got it in {tries} tries!")
            break

    if tries <= 3:
        print("You get 3 points.")
        return 3
    print("You get 1 point.")
    return 1
