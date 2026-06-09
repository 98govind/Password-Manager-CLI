# Password Manager CLI

A simple and secure Command Line Interface (CLI) Password Manager built with Python.

---

##  Features
- Store passwords securely
- Retrieve saved passwords
- Simple and lightweight CLI tool
- JSON-based local storage

---

##  Tech Stack
- Python 🐍
- Git & GitHub
- JSON (for data storage)

---

## 📂 Project Structure

Password-Manager-CLI/
│
├── src/            # Main source code
├── data/           # Stored passwords (JSON)
├── docs/           # Documentation
├── README.md       # Project info

---

## How to Run

```bash
# Clone repository
git clone https://github.com/98govind/Password-Manager-CLI.git

# Go to project folder
cd Password-Manager-CLI

# Run program
python src/main.py

## Approach

### Data Exploration
- Loaded dataset
- Checked shape, columns, and data types
- Identified missing values
- Created visualizations

### Data Cleaning
- Removed missing values
- Removed duplicate rows
- Saved cleaned dataset

### Feature Engineering
- Created password_length feature
- Created has_number feature
- Applied feature scaling
- Split data into train and test sets (80/20)

## Features Built So Far

* Password Strength Checker
* Strong Password Generator
* Credential Storage Manager
* Input Validation and Error Handling
* Basic Testing for Core Features

## Testing

Basic tests were added for:

* Weak password detection
* Medium password detection
* Strong password detection
* Empty password validation
* Password generation

## Current CLI Menu

1. Check Password Strength
2. Generate Strong Password
3. Add Credential
4. View Credentials
5. Exit

## Advanced Features

### Feature 1: Delete Credential

User saved credentials ko delete kar sakega.

### Feature 2: Search Credential

User service name se credential search kar sakega.

### Feature 3: Hide Password

View credentials me password ko hide/mask karke dikhaya jayega.

### Feature 4: Better Security

Password storage ko aur secure banaya jayega.

### Feature 5: Improved User Experience

CLI menu ko aur user-friendly banaya jayega.



