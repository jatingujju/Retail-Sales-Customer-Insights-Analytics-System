import pandas as pd
import matplotlib.pyplot as plt
import os
import joblib
import numpy as np

# Paths
DATA_PATH = "data/processed/sales_features.csv"
MODEL_PATH = "outputs/models/sales_model.pkl"
OUTPUT_PATH = "outputs/charts/"

def show_insights():
    # Load Data (just for feature names)
    df = pd.read_csv(DATA_PATH)
    features = ["quantity", "discount", "profit", "Year", "Month", "Day"]
    
    # Load Model
    if not os.path.exists(MODEL_PATH):
        print("❌ Model not found! Run modeling.py first.")
        return

    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")

    # Get Feature Importance
    importances = model.feature_importances_
    indices = np.argsort(importances)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.title("Feature Importance (What drives Sales?)")
    plt.barh(range(len(indices)), importances[indices], align="center")
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel("Relative Importance")
    
    # Save Plot
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "feature_importance.png"))
    print(f"Insight chart saved to {OUTPUT_PATH}feature_importance.png")

if __name__ == "__main__":
    show_insights()
Summary