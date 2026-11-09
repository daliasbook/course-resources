# Password checker: says if a password is strong.


def is_strong(password):
    has_digit = False
    has_upper = False
    for character in password:
        if character.isdigit():
            has_digit = True
        if character.isupper():
            has_upper = True
    return len(password) >= 8 and has_digit and has_upper


def run():
    print()
    print("PASSWORD CHECKER")
    password = input("Type a password to check: > ")

    if is_strong(password):
        print("Strong password!")
    else:
        print("Weak password. Use at least 8 characters, a digit and a capital letter.")
