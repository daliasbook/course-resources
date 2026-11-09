# Text Adventure: the player moves through places, makes choices
# and reaches one of several endings.
# Each place lives in its own file, written by a different team member.

from forest import play as play_forest
from river import play as play_river
from cave import play as play_cave
from castle import play as play_castle
from mountain import play as play_mountain
from village import play as play_village

TEAM_NAME = "The Explorers"
TEAM_MEMBERS = ["Mara", "Andrei", "Ioana", "Radu", "Elena", "Victor"]

print("=" * 30)
print("THE FORGOTTEN FOREST".center(30))
print("=" * 30)
print(f"Made by {TEAM_NAME}:")
for member in TEAM_MEMBERS:
    print(f"- {member}")
print()

player_name = input("What is your name? > ")
lives = 3
inventory = []
place = "forest"
print(f"Welcome, {player_name}! You have {lives} lives. Find the hidden treasure.")

while lives > 0 and place != "treasure":
    if place == "forest":
        lives, place = play_forest(lives, inventory)
    elif place == "river":
        lives, place = play_river(lives, inventory)
    elif place == "cave":
        lives, place = play_cave(lives, inventory)
    elif place == "castle":
        lives, place = play_castle(lives, inventory)
    elif place == "mountain":
        lives, place = play_mountain(lives, inventory)
    elif place == "village":
        lives, place = play_village(lives, inventory)
    print(f"Lives left: {lives}")

print()
if place == "treasure":
    print(f"*** GOOD ENDING: {player_name} found the treasure with {lives} lives left! ***")
else:
    print(f"*** GAME OVER: {player_name} ran out of lives. Try again! ***")

if len(inventory) > 0:
    print("Inventory:", ", ".join(inventory))
else:
    print("Inventory: empty")
