# Student Assistant: an app that helps students at school.
# Each module lives in its own file, written by a different team member.

from grades import run as run_grades
from homework import run as run_homework
from timetable import run as run_timetable
from converter import run as run_converter
from password_checker import run as run_password_checker
from text_stats import run as run_text_stats

TEAM_NAME = "The Helpers"
TEAM_MEMBERS = ["Radu", "Ioana", "Mara", "Andrei", "Elena", "Victor"]

print("=" * 30)
print("STUDENT ASSISTANT".center(30))
print("=" * 30)
print(f"Made by {TEAM_NAME}:")
for member in TEAM_MEMBERS:
    print(f"- {member}")
print()

user_name = input("What is your name? > ")
print(f"Hi, {user_name}! How can I help you today?")

while True:
    print()
    print("1. Grade calculator")
    print("2. Homework list")
    print("3. Timetable")
    print("4. Converter")
    print("5. Password checker")
    print("6. Text statistics")
    print("0. Exit")
    choice = input("Your choice? > ").strip()

    if choice == "1":
        run_grades()
    elif choice == "2":
        run_homework()
    elif choice == "3":
        run_timetable()
    elif choice == "4":
        run_converter()
    elif choice == "5":
        run_password_checker()
    elif choice == "6":
        run_text_stats()
    elif choice == "0":
        break
    else:
        print("Please choose a number from the menu.")

print(f"Goodbye, {user_name}! Good luck with your studies!")
