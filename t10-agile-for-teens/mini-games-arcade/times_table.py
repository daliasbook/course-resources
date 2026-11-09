# Times table: the program asks a multiplication and checks the answer.


def play():
    print()
    print("TIMES TABLE")
    a = 7
    b = 8
    text = input(f"How much is {a} x {b}? > ").strip()

    if text.isdigit() and int(text) == a * b:
        print("Correct! You get 2 points.")
        return 2
    print(f"Wrong! {a} x {b} = {a * b}.")
    return 0
