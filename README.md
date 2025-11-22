# 🛒 Retail Sales & Customer Insights Analytics System

This project is an **end-to-end Data Analytics Pipeline** for a retail business. It automates the entire workflow—from generating data to training a predictive machine learning model and extracting actionable business insights.

The entire process is orchestrated by a single command, demonstrating modularity, robustness, and production readiness.

## ⚙️ System Architecture (The Pipeline)
The `main.py` runner executes the following six modular Python scripts in sequence:

| Step | Script | Description | Input | Output |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `sample_data.py` | Generates synthetic transactional and product data. | N/A | `data/raw/sales.csv` |
| **2** | `data_cleaning.py` | Handles missing values, performs type conversion, and removes duplicates. | `data/raw/sales.csv` | `data/processed/sales_clean.csv` |
| **3** | `feature_engineering.py` | Derives new features like `Total_Price` and extracts temporal components (Year, Month, Day). | `data/processed/sales_clean.csv` | `data/processed/sales_features.csv` |
| **4** | `visualization.py` | Generates exploratory charts (e.g., daily trends, profit by category). | `data/processed/sales_features.csv` | `outputs/charts/*.png` |
| **5** | `modeling.py` | Trains a **Random Forest Regressor** to predict the `Total_Price` of a transaction. | `data/processed/sales_features.csv` | `outputs/models/sales_model.pkl` |
| **6** | `model_insights.py` | Extracts and visualizes **Feature Importance** from the trained model. | `outputs/models/sales_model.pkl` | `outputs/charts/feature_importance.png` |
---
## 🚀 Key Results & Insights
After running the pipeline, the following key artifacts are generated:

### Predictive Model
* **Model Type:** Random Forest Regressor
* **Target Variable:** `Total_Price` (Predicted transaction value)
* **Model Location:** `outputs/models/sales_model.pkl`

### Actionable Insights
The **Feature Importance** analysis (saved as `outputs/charts/feature_importance.png`) reveals the primary factors driving transaction value:
* **[Insert Primary Driver]:** The most influential factor, accounting for [Insert %] of the model's predictive power.
* **[Insert Secondary Driver]:** Also a strong indicator, demonstrating the value of [Insert business context].

*(**Note:** You may want to manually check your chart and insert the actual results here, e.g., "Quantity" and "Profit".)*
---
## 💻 Setup and Execution
To run this project locally, ensure you have Python 3.x installed.

### 1. Clone the repository
```bash
git clone [https://github.com/jatingujju/Retail-Sales-Customer-Insights-Analytics-System.git](https://github.com/jatingujju/Retail-Sales-Customer-Insights-Analytics-System.git)
cd Retail-Sales-Customer-Insights-Analytics-System
