import random
import string

def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        print("Invalid input.Please enter 'yes' or 'no'.")

def generate_password():
    length = int(input("How many characters do you want your password to have? "))

    use_digits = ask_yes_no("Do you want digits to be included? (yes/no) ")
    use_symbols = ask_yes_no("Do you want symbols to be included? (yes/no) ")

    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password = password + random.choice(characters)
    print("Your password is: " + password)