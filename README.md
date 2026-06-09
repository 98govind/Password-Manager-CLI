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

