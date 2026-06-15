import random
import string

def generate_password(length=16, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not characters:
        print("Please select at least one character type!")
        return None

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


print("Welcome to Password Generator!")
print("-" * 30)

length = int(input("Enter password length (e.g. 16): "))

print("\nChoose character types:")
use_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
use_lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols)

if password:
    print("\nYour generated password:")
    print("-" * 30)
    print(password)
    print("-" * 30)

    another = input("\nGenerate another password? (yes/no): ").lower()
    while another == "yes":
        password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols)
        print("\nYour new password:", password)
        another = input("Generate another? (yes/no): ").lower()

print("\nGoodbye!")