import pandas as pd
import matplotlib.pyplot as plt

# Dataset load
df = pd.read_csv("../data/data.csv", on_bad_lines="skip")

# Missing values remove
df = df.dropna()

print("Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())

# Password length feature
df["password_length"] = df["password"].apply(len)

print("\nGraph code is running...")

# Graph 1: Password Strength Distribution
df["strength"].value_counts().plot(kind="bar")
plt.title("Password Strength Distribution")
plt.xlabel("Strength")
plt.ylabel("Count")
plt.savefig("../docs/password_strength_distribution.png")
plt.show()

# Graph 2: Password Length Distribution
df["password_length"].plot(kind="hist", bins=30)
plt.title("Password Length Distribution")
plt.xlabel("Password Length")
plt.savefig("../docs/password_length_distribution.png")
plt.show()

# Graph 3: Password Length Boxplot
df.boxplot(column="password_length")
plt.title("Password Length Boxplot")
plt.show()