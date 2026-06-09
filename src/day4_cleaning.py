import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "data.csv")


df = pd.read_csv(DATA_PATH, on_bad_lines="skip")

df = df.dropna()
df = df.drop_duplicates()

df["password"] = df["password"].astype(str)
df["strength"] = df["strength"].astype(int)

os.makedirs("../data/processed", exist_ok=True)

PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_data.csv")

df.to_csv(PROCESSED_PATH, index=False)

print("Data cleaning complete!")