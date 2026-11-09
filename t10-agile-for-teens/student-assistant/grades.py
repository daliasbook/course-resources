# Grade calculator: the student types grades, the program shows the average.


def run():
    print()
    print("GRADE CALCULATOR")
    text = input("Type your grades, separated by spaces: > ")
    grades = []

    for part in text.split():
        try:
            grades.append(float(part.replace(",", ".")))
        except ValueError:
            print(f"'{part}' is not a number, I will skip it.")

    if len(grades) == 0:
        print("You did not type any grades.")
        return

    average = sum(grades) / len(grades)
    print(f"Your average is {round(average, 2)}")
    print(f"Highest grade: {max(grades)}, lowest grade: {min(grades)}")
