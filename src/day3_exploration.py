import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/data.csv", on_bad_lines="skip")
df = df.dropna()

print("Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())

df["password_length"] = df["password"].apply(len)

print("\nGraph code is running...")

df["strength"].value_counts().plot(kind="bar")
plt.title("Password Strength Distribution")
plt.show()

df["password_length"].plot(kind="hist", bins=30)
plt.title("Password Length Distribution")
plt.show()

df.boxplot(column="password_length")
plt.title("Password Length Boxplot")
plt.show()