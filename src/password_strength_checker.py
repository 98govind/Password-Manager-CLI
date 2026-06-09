"""
Core Feature 1 + Core Feature 2

Feature 1: Password Strength Checker
Feature 2: Password Generator

This program can:
1. Check password strength
2. Generate a strong password
3. Check strength of generated password
"""

import string
import random


def check_password_strength(password):
    if not password:
        return "Password cannot be empty."

    if not isinstance(password, str):
        return "Invalid input. Password must be text."

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Password"
    else:
        return "Strong Password"


def generate_password(length=12):
    if length < 8:
        return "Password length should be at least 8."

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    return password


print("Password Manager CLI")
print("1. Check Password Strength")
print("2. Generate Strong Password")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print("Password Strength:", result)

elif choice == "2":
    generated_password = generate_password()
    print("Generated Password:", generated_password)

    strength = check_password_strength(generated_password)
    print("Generated Password Strength:", strength)

else:
    print("Invalid choice. Please enter 1 or 2.")