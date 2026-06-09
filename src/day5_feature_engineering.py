import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_data.csv")

df = pd.read_csv(CLEANED_DATA_PATH)

# New Features
df["password_length"] = df["password"].apply(len)
df["has_number"] = df["password"].str.contains(r"\d").astype(int)

X = df[["password_length", "has_number"]]
y = df["strength"]

scaler = StandardScaler()
X["password_length"] = scaler.fit_transform(X[["password_length"]])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Feature engineering complete!")
print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)