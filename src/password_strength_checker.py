"""
Password Manager CLI - Core Features

Feature 1: Password Strength Checker
Feature 2: Password Generator
Feature 3: Password Storage Manager

Day 11: Input Validation + Error Handling
"""

import string
import random
import json
import os

DATA_FILE = "../data/passwords.json"


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
    elif score <= 4:
        return "Medium Password"
    else:
        return "Strong Password"


def generate_password(length=12):
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = "".join(
        random.choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(length - 4)
    )

    password_list = list(uppercase + lowercase + digit + special + remaining)
    random.shuffle(password_list)

    return "".join(password_list)


def load_passwords():
    try:
        if not os.path.exists(DATA_FILE):
            return {}

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except Exception as e:
        print("Error loading passwords:", e)
        return {}


def save_passwords(passwords):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(passwords, file, indent=4)

    except Exception as e:
        print("Error saving passwords:", e)


def add_credential():
    service = input("Enter service name: ").strip()
    username = input("Enter username/email: ").strip()
    password = input("Enter password: ").strip()

    if not service:
        print("Service name cannot be empty.")
        return

    if not username:
        print("Username cannot be empty.")
        return

    if not password:
        print("Password cannot be empty.")
        return

    strength = check_password_strength(password)

    passwords = load_passwords()
    passwords[service] = {
        "username": username,
        "password": password,
        "strength": strength
    }

    save_passwords(passwords)

    print("Credential saved successfully!")
    print("Password Strength:", strength)


def view_credentials():
    passwords = load_passwords()

    if not passwords:
        print("No saved credentials found.")
        return

    print("\nSaved Credentials:")

    for service, details in passwords.items():
        print("-------------------------")
        print("Service:", service)
        print("Username:", details["username"])
        print("Password:", details["password"])
        print("Strength:", details["strength"])


while True:
    print("\nPassword Manager CLI")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Add Credential")
    print("4. View Credentials")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if not choice:
        print("Choice cannot be empty.")
        continue

    if choice == "1":
        user_password = input("Enter your password: ").strip()
        result = check_password_strength(user_password)
        print("Password Strength:", result)

    elif choice == "2":
        generated_password = generate_password()
        print("Generated Password:", generated_password)
        strength = check_password_strength(generated_password)
        print("Generated Password Strength:", strength)

    elif choice == "3":
        add_credential()

    elif choice == "4":
        view_credentials()

    elif choice == "5":
        print("Thank you for using Password Manager CLI.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")