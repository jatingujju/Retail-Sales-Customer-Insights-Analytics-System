"""
MAIN PIPELINE RUNNER

This script executes the complete retail analytics workflow:

1. Generate sample dataset          → sample_data.py
2. Clean raw data                   → data_cleaning.py
3. Feature engineering              → feature_engineering.py
4. Visualizations (Charts)          → visualization.py
5. Train ML model                   → modeling.py
6. Feature importance charts        → model_insights.py

Make sure you have the following folders:
data/raw
data/processed
outputs/charts
"""
import matplotlib
matplotlib.use('Agg')   # Disable interactive mode
import os
import subprocess


# Utility to run a python script safely
def run_script(filename):
    print(f"\n🚀 Running {filename} ...")
    result = subprocess.run(["python", filename], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("⚠️ Errors/Warnings:\n", result.stderr)


# Ensure required folders exist
def create_folders():
    folders = [
        "data/raw",
        "data/processed",
        "outputs/charts"
    ]
    for f in folders:
        os.makedirs(f, exist_ok=True)
    print("📁 Folder structure verified.")


if __name__ == "__main__":
    print("\n===================================")
    print(" RETAIL SALES ANALYTICS PIPELINE ")
    print("===================================")

    create_folders()

    # 1. Generate sample data
    run_script("sample_data.py")

    # 2. Clean data
    run_script("data_cleaning.py")

    # 3. Feature engineering
    run_script("feature_engineering.py")

    # 4. Generate visualizations
    run_script("visualization.py")

    # 5. Train ML model
    run_script("modeling.py")

    # 6. Generate feature importance chart
    run_script("model_insights.py")

    print("\n🎉 ALL STEPS COMPLETED SUCCESSFULLY!")
    print("Check:")
    print(" - data/raw")
    print(" - data/processed")
    print(" - outputs/charts")
    print("Your project is now ready for GitHub and interviews!")