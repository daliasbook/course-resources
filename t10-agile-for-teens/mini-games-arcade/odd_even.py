# Odd or even: the program says if a number is odd or even.


def play():
    print()
    print("ODD OR EVEN")
    text = input("Type a whole number: > ").strip()

    if not text.lstrip("-").isdigit():
        print("That is not a whole number.")
        return 0

    number = int(text)
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    print("You get 1 point.")
    return 1
