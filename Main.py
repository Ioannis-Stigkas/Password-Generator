from generator import generate_password
from checker import check_password

while True:
    print("\n--- Password Tool ---")
    print("1. Generate a password")
    print("2. Check a password")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        generate_password()
    elif choice == "2":
        check_password()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("invalid option. Please try again.")      