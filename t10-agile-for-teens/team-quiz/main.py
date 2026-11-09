# Team Quiz: the player picks a category, answers questions and sees the score.
# Each category lives in its own file, written by a different team member.

from sports import play as play_sports
from animals import play as play_animals
from video_games import play as play_video_games
from science import play as play_science
from music import play as play_music
from geography import play as play_geography

TEAM_NAME = "The Lightning Bolts"
TEAM_MEMBERS = ["Andrei", "Ioana", "Mara", "Radu", "Elena", "Victor"]

print("=" * 30)
print("TEAM QUIZ".center(30))
print("=" * 30)
print(f"Made by {TEAM_NAME}:")
for member in TEAM_MEMBERS:
    print(f"- {member}")
print()
print("How to play: pick a category and answer the questions.")
print("You get 1 point for every correct answer.")
print()

player_name = input("What is your name? > ")
print(f"Hi, {player_name}!")

total_score = 0

while True:
    print()
    print("Pick a category:")
    print("1. Sports")
    print("2. Animals")
    print("3. Video games")
    print("4. Science")
    print("5. Music")
    print("6. Geography")
    print("0. Exit")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        total_score += play_sports(player_name)
    elif choice == "2":
        total_score += play_animals(player_name)
    elif choice == "3":
        total_score += play_video_games(player_name)
    elif choice == "4":
        total_score += play_science(player_name)
    elif choice == "5":
        total_score += play_music(player_name)
    elif choice == "6":
        total_score += play_geography(player_name)
    elif choice == "0":
        break
    else:
        print("Please choose a number from the menu.")

print()
print(f"*** Total score: {total_score} points ***")
print(f"Goodbye, {player_name}!")
