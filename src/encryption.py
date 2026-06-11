from cryptography.fernet import Fernet
import os

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

# Generate key if not exists
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

# Load key
with open(KEY_FILE, "rb") as f:
    key = f.read()

fernet = Fernet(key)

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        website = input("Website Name: ")
        password = input("Password: ")

        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")

        encrypted_password = fernet.encrypt(password.encode()).decode()

        with open(PASSWORD_FILE, "a") as f:
            f.write(f"{website},{encrypted_password}\n")

        print("Password Saved Successfully!")

    elif choice == "2":
        if not os.path.exists(PASSWORD_FILE):
            print("No passwords found.")
        else:
            with open(PASSWORD_FILE, "r") as f:
                for line in f:
                    website, encrypted_password = line.strip().split(",")

                    decrypted_password = (
                        fernet.decrypt(encrypted_password.encode())
                        .decode()
                    )

                    print(f"Website: {website}")
                    print(f"Password: {decrypted_password}")
                    print("-" * 30)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")