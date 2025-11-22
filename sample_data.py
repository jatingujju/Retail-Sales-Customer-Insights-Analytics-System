import pandas as pd
import os

RAW_DATA_PATH = "data/raw/"

# Ensure the folder exists
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# ----- Sales Data -----
sales_data = {
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [101, 102, 103, 104, 105],
    "product_id": [1001, 1002, 1003, 1004, 1005],
    "order_date": ["2025-01-05", "2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09"],
    "sales": [500, 1500, 200, 700, 1200],
    "quantity": [2, 5, 1, 3, 4],
    "discount": [0.05, 0.10, 0, 0.15, 0.05],
    "profit": [50, 300, 20, 100, 200],
    "category": ["Electronics", "Furniture", "Office Supplies", "Electronics", "Furniture"]
}
sales_df = pd.DataFrame(sales_data)
sales_df.to_csv(os.path.join(RAW_DATA_PATH, "sales.csv"), index=False)
print("sales.csv generated.")

# ----- Customers Data -----
customers_data = {
    "customer_id": [101, 102, 103, 104, 105],
    "customer_name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Brown", "Charlie Lee"],
    "segment": ["Consumer", "Corporate", "Home Office", "Consumer", "Corporate"],
    "region": ["West", "East", "South", "North", "East"]
}
customers_df = pd.DataFrame(customers_data)
customers_df.to_csv(os.path.join(RAW_DATA_PATH, "customers.csv"), index=False)
print("customers.csv generated.")

# ----- Products Data -----
products_data = {
    "product_id": [1001, 1002, 1003, 1004, 1005],
    "product_name": ["Smartphone", "Office Chair", "Paper", "Laptop", "Desk"],
    "category": ["Electronics", "Furniture", "Office Supplies", "Electronics", "Furniture"],
    "sub_category": ["Mobile", "Seating", "Stationery", "Computer", "Tables"],
    "price": [250, 300, 20, 700, 300]
}
products_df = pd.DataFrame(products_data)
products_df.to_csv(os.path.join(RAW_DATA_PATH, "products.csv"), index=False)
print("products.csv generated.")
