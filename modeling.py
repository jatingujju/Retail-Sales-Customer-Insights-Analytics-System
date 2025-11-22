import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Paths
INPUT_PATH = "data/processed/sales_features.csv"
MODEL_PATH = "outputs/models/"
os.makedirs(MODEL_PATH, exist_ok=True)

def train_model():
    print("Loading data for modeling...")
    df = pd.read_csv(INPUT_PATH)

    # Select Features and Target
    # We predict 'Total_Price' based on other metrics
    # Dropping ID columns and 'sales' (since sales is directly correlated to price)
    features = ["quantity", "discount", "profit", "Year", "Month", "Day"]
    target = "Total_Price"

    X = df[features]
    y = df[target]

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Model
    print("Training Random Forest Model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save Model
    joblib.dump(model, os.path.join(MODEL_PATH, "sales_model.pkl"))
    print(f"Model saved to {MODEL_PATH}sales_model.pkl")

if __name__ == "__main__":
    train_model()