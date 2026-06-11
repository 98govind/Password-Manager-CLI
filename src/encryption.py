from cryptography.fernet import Fernet
import os
import time

KEY_FILE = "secret.key"
PASSWORD_FILE = "passwords.txt"


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

    with open(KEY_FILE, "rb") as f:
        return f.read()


def save_password(website, password):
    encrypted_password = fernet.encrypt(password.encode()).decode()

    with open(PASSWORD_FILE, "a") as f:
        f.write(f"{website},{encrypted_password}\n")


def view_passwords():
    if not os.path.exists(PASSWORD_FILE) or os.path.getsize(PASSWORD_FILE) == 0:
        print("No saved passwords found. Add a password first.")
        return

    with open(PASSWORD_FILE, "r") as f:
        print("\nSaved Passwords")
        print("Below are your decrypted saved passwords:")
        print("-" * 35)

        for line in f:
            try:
                website, encrypted_password = line.strip().split(",")
                decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

                print(f"Website: {website}")
                print(f"Password: {decrypted_password}")
                print("-" * 35)

            except Exception:
                print("Error: One saved password record is corrupted. Skipping it.")


key = load_key()
fernet = Fernet(key)


while True:
    print("\n" + "=" * 35)
    print("      PASSWORD MANAGER CLI")
    print("=" * 35)
    print("Select an option by entering 1, 2, or 3")
    print("1. Save New Password")
    print("2. View Saved Passwords")
    print("3. Exit")
    print("=" * 35)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Opening save password section...")
        time.sleep(0.5)

        website = input("Website Name: ")
        password = input("Password: ")

        if website.strip() == "" or password.strip() == "":
            print("Error: Website name and password cannot be empty.")
            continue

        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")
        print("Weak = Easy to guess | Medium = Better | Strong = Recommended")

        print("Saving password securely...")
        time.sleep(0.5)

        save_password(website, password)

        print("Password saved successfully and encrypted securely.")

    elif choice == "2":
        print("Loading saved passwords...")
        time.sleep(0.5)

        view_passwords()

    elif choice == "3":
        print("Closing Password Manager...")
        time.sleep(0.5)
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")