import pandas as pd
import os

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

def load_data(filename):
    return pd.read_csv(os.path.join(RAW_DATA_PATH, filename))

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()
    # Fill missing numeric values with median
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())
    # Fill missing categorical values with mode
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

def save_data(df, filename):
    df.to_csv(os.path.join(PROCESSED_DATA_PATH, filename), index=False)

if __name__ == "__main__":
    sales = load_data("sales.csv")
    sales_clean = clean_data(sales)
    save_data(sales_clean, "sales_clean.csv")
    print("Sales data cleaned and saved.")
