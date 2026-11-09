# Count the vowels: the program counts the vowels in a word.


def play():
    print()
    print("COUNT THE VOWELS")
    word = input("Type a word: > ").strip().lower()
    vowels = 0

    for letter in word:
        if letter in "aeiou":
            vowels += 1

    print(f"The word '{word}' has {vowels} vowels.")
    print("You get 1 point.")
    return 1
