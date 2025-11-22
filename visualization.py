import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Paths
# -----------------------------
PROCESSED_DATA_PATH = "data/processed/"
OUTPUT_PATH = "outputs/charts/"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_PATH, exist_ok=True)

# -----------------------------
# Functions
# -----------------------------
def plot_sales_trend(df):
    """Plot daily sales trend and save as PNG"""
    plt.figure(figsize=(10,6))
    df.groupby('order_date')['sales'].sum().plot()
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "sales_trend.png"))
    plt.close()
    print("Saved: sales_trend.png")

def plot_category_profit(df):
    """Plot total profit by product category and save as PNG"""
    plt.figure(figsize=(10,6))
    profit_by_cat = df.groupby('category')['profit'].sum().reset_index()
    sns.barplot(x='category', y='profit', data=profit_by_cat)
    plt.title("Profit by Category")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "category_profit.png"))
    plt.close()
    print("Saved: category_profit.png")

def plot_quantity_by_category(df):
    """Optional: plot total quantity sold by category"""
    plt.figure(figsize=(10,6))
    quantity_by_cat = df.groupby('category')['quantity'].sum().reset_index()
    sns.barplot(x='category', y='quantity', data=quantity_by_cat)
    plt.title("Quantity Sold by Category")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "quantity_by_category.png"))
    plt.close()
    print("Saved: quantity_by_category.png")

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    df = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "sales_features.csv"))
    
    plot_sales_trend(df)
    plot_category_profit(df)
    plot_quantity_by_category(df)
    
    print("All visualizations saved successfully in 'outputs/charts/'")
