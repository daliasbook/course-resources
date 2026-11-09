# Converter: turns minutes into hours or kilometers into meters.


def minutes_to_hours(minutes):
    return minutes / 60


def km_to_meters(km):
    return km * 1000


def run():
    print()
    print("CONVERTER")
    print("1. Minutes to hours")
    print("2. Kilometers to meters")
    choice = input("Your choice? > ").strip()

    if choice != "1" and choice != "2":
        print("Please choose 1 or 2.")
        return

    try:
        if choice == "1":
            minutes = float(input("How many minutes? > ").replace(",", "."))
            print(f"{minutes} minutes = {round(minutes_to_hours(minutes), 2)} hours")
        else:
            km = float(input("How many kilometers? > ").replace(",", "."))
            print(f"{km} km = {km_to_meters(km)} meters")
    except ValueError:
        print("Please type a number, for example 90 or 2.5.")
