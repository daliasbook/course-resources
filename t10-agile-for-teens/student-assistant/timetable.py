# Timetable: pick a day, see the classes for that day.

timetable = {
    "monday": ["Math", "Romanian", "English", "PE", "Computer Science"],
    "tuesday": ["Physics", "History", "Math", "Art"],
    "wednesday": ["Biology", "Romanian", "Geography", "Music"],
    "thursday": ["Chemistry", "English", "Math", "Computer Science"],
    "friday": ["Romanian", "History", "PE", "Math"],
}


def run():
    print()
    print("TIMETABLE")
    day = input("Which day? > ").strip().lower()

    if day in timetable:
        print(f"On {day.capitalize()} you have: {', '.join(timetable[day])}")
    elif day == "saturday" or day == "sunday":
        print("No classes that day. Enjoy the weekend!")
    else:
        print("I don't know that day. Try, for example: monday.")
