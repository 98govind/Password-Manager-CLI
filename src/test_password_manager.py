from password_strength_checker import check_password_strength, generate_password

print("Running Day 12 tests...")

# Test 1
assert check_password_strength("abc") == "Weak Password"

# Test 2
assert check_password_strength("pandey12345") == "Medium Password"

# Test 3
assert check_password_strength("Govind@123") == "Strong Password"

# Test 4
assert check_password_strength("") == "Password cannot be empty."

# Test 5
password = generate_password()
assert len(password) == 12
assert check_password_strength(password) == "Strong Password"

print("All basic tests passed successfully!")