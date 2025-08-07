import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile

#Constants
Zip_FILE = "monthly_budget_data.zip"
EXRACT_DIR = "data"

#1.Extract Zip file
def extract_zip(zip_path, extract_to):
    if not os.path.exists(zip_path):
        print(f"[ERROR] {zip_path} not found.")
        return False
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"[INFO] Extracting {zip_path} to {extract_to}")
    return True

#2.Load all CSVs files  into a Dataframe
def load_all_csvs(folder_path):
    all_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
    dataframes = []

    for file in all_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        df['Month'] = os.path.splitext(file)[0].capitalize()
        dataframes.append(df)

    if not dataframes:
        print("[ERROR] No CSV files found in the data folder.")
        return pd.DataFrame()  # Return an empty DataFrame to avoid crashing
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

#3.Analyze and Plot
def analyze_and_plot(df):
    #Basic validation
    if 'Category' not in df or 'Amount' not in df or 'Month' not in df:
        print("[ERROR] CSV file must contain a 'Category', 'Month' and 'Amount' column.")
        return

    #Ensure 'Amount' is numeric
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df.dropna(subset=['Amount'], inplace=True)

    # Create pivot table; Category vs Month
    pivot = pd.pivot_table(df, values='Amount' , index='Category', columns='Month', aggfunc='sum', fill_value=0)

    #Print summary table
    print("\n📊 Monthly Expense Summary📊\n")
    print(pivot)

    #Plote bar chart
    pivot.T.plot(kind='bar', figsize = (12,6))
    plt.title("Monthly Expense by Category")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

#4.Run the program
def main():
    if extract_zip(Zip_FILE, EXRACT_DIR):
        df = load_all_csvs(EXRACT_DIR)
        analyze_and_plot(df)

if __name__ == "__main__":
    main()