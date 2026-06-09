"""
Core Feature 1: Password Strength Checker

This feature checks the strength of a password entered by the user.
It checks password length, numbers, uppercase letters, lowercase letters,
and special characters. Based on these rules, it returns Weak, Medium, or Strong.
"""

import string

def check_password_strength(password):
    # Empty input check
    if not password:
        return "Password cannot be empty."

    # Wrong type check
    if not isinstance(password, str):
        return "Invalid input. Password must be text."

    score = 0

    # Rule 1: Length check
    if len(password) >= 8:
        score += 1

    # Rule 2: Number check
    if any(char.isdigit() for char in password):
        score += 1

    # Rule 3: Uppercase check
    if any(char.isupper() for char in password):
        score += 1

    # Rule 4: Lowercase check
    if any(char.islower() for char in password):
        score += 1

    # Rule 5: Special character check
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Password"
    else:
        return "Strong Password"


# Manual testing with user input
password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)