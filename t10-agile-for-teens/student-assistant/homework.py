# Homework list: add homework, see all of it, remove what is done.

homework_list = ["Exercises 1-5 in math"]


def run():
    while True:
        print()
        print("HOMEWORK LIST")
        print("1. Add homework")
        print("2. See all homework")
        print("3. I finished a homework")
        print("0. Back")
        choice = input("Your choice? > ").strip()

        if choice == "1":
            task = input("What homework do you have? > ").strip()
            homework_list.append(task)
            print("Homework added.")
        elif choice == "2":
            if len(homework_list) == 0:
                print("No homework. Enjoy your free time!")
            for i in range(len(homework_list)):
                print(f"{i + 1}. {homework_list[i]}")
        elif choice == "3":
            task = input("Which homework did you finish? > ").strip()
            if task in homework_list:
                homework_list.remove(task)
                print("Well done! Homework removed.")
            else:
                print("That homework is not on the list.")
        elif choice == "0":
            break
        else:
            print("Please choose a number from the menu.")
