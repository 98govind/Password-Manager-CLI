import pandas as pd
import os

df = pd.read_csv("../data/data.csv", on_bad_lines="skip")

df = df.dropna()
df = df.drop_duplicates()

df["password"] = df["password"].astype(str)
df["strength"] = df["strength"].astype(int)

os.makedirs("../data/processed", exist_ok=True)

df.to_csv("../data/processed/cleaned_data.csv", index=False)

print("Data cleaning complete!")