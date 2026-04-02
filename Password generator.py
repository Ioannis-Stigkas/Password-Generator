import random
import string

length = int(input("How many characters do you want your password to have? "))

use_digits = input("Do you want digits to be included? (yes/no) ")
use_symbols = input("Do you want symbols to be included? (yes/no) ")

characters = string.ascii_letters

if use_digits == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

password = ""

for i in range(length):
    password=password + random.choice(characters)
print("Your password is: " + password)