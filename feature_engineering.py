import pandas as pd
import os

PROCESSED_PATH = "data/processed/"
RAW_PATH = "data/raw/"

def add_features():
    # Load cleaned sales data
    sales = pd.read_csv(os.path.join(PROCESSED_PATH, "sales_clean.csv"))

    # Load products master (needed for price!)
    products = pd.read_csv(os.path.join(RAW_PATH, "products.csv"))

    # Merge to add product price information
    df = pd.merge(sales, products[["product_id", "price"]], on="product_id", how="left")

    # ----------------------------
    # FEATURE ENGINEERING
    # ----------------------------
    df["order_date"] = pd.to_datetime(df["order_date"])

    df["Total_Price"] = df["price"] * df["quantity"]

    df["Year"] = df["order_date"].dt.year
    df["Month"] = df["order_date"].dt.month
    df["Day"] = df["order_date"].dt.day

    df["profit_margin"] = (df["profit"] / df["sales"]).fillna(0)

    # Save final dataset
    output_path = os.path.join(PROCESSED_PATH, "sales_features.csv")
    df.to_csv(output_path, index=False)

    print("Features added and saved successfully.")

if __name__ == "__main__":
    add_features()
