# Mini Games Arcade: a menu where you pick a short game.
# Each game lives in its own file, written by a different team member.

from riddle import play as play_riddle
from hidden_word import play as play_hidden_word
from odd_even import play as play_odd_even
from guess_number import play as play_guess_number
from times_table import play as play_times_table
from count_vowels import play as play_count_vowels

TEAM_NAME = "The Game Makers"
TEAM_MEMBERS = ["Ioana", "Mara", "Andrei", "Radu", "Elena", "Victor"]

print("=" * 30)
print("THE TEAM'S ARCADE".center(30))
print("=" * 30)
print(f"Made by {TEAM_NAME}:")
for member in TEAM_MEMBERS:
    print(f"- {member}")
print()

player_name = input("What is your name? > ")
print(f"Welcome, {player_name}! Which game do you want to play?")
total_points = 0

while True:
    print()
    print("1. The riddle")
    print("2. The hidden word")
    print("3. Odd or even")
    print("4. Guess the number")
    print("5. Times table")
    print("6. Count the vowels")
    print("0. Exit")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        total_points += play_riddle()
    elif choice == "2":
        total_points += play_hidden_word()
    elif choice == "3":
        total_points += play_odd_even()
    elif choice == "4":
        total_points += play_guess_number()
    elif choice == "5":
        total_points += play_times_table()
    elif choice == "6":
        total_points += play_count_vowels()
    elif choice == "0":
        break
    else:
        print("Please choose a number from the menu.")

print()
print(f"*** {player_name}, you collected {total_points} points in the arcade! ***")
