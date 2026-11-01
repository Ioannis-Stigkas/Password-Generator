import string

def check_password():
    password = input("Please enter your password:")
    if len(password) < 8:
        print("Password is too short.")
    has_upper = False
    for char in password:
        if char in string.ascii_uppercase:
            has_upper = True

    if not has_upper:
        print("Password is too weak. It should contain at least one uppercase letter.")

    has_lower = False
    for char in password:
        if char in string.ascii_lowercase:
            has_lower = True

    if not has_lower:
        print("Password is too weak. It should contain at least one lowercase letter.")

    has_digit = False
    for char in password:
        if char in string.digits:
            has_digit = True

    if not has_digit:
        print("Password is too weak. It should contain at least one digit.")

    has_symbol = False
    for char in password:
        if char in string.punctuation:
            has_symbol = True

    if not has_symbol:
        print("Password is too weak. It should contain at least one symbol.")