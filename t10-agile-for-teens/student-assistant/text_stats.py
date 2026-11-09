# Text statistics: counts the words, letters and vowels in a sentence.


def run():
    print()
    print("TEXT STATISTICS")
    sentence = input("Type a sentence: > ")

    words = sentence.split()
    letters = 0
    vowels = 0
    for character in sentence.lower():
        if character.isalpha():
            letters += 1
        if character in "aeiou":
            vowels += 1

    print(f"Words: {len(words)}")
    print(f"Letters: {letters}")
    print(f"Vowels: {vowels}")
