import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CLEANED_FILE = BASE_DIR / "Cleaned_Financial_Data.xlsx"
RAW_FILE = BASE_DIR / "Sample data (1).xlsx"

if CLEANED_FILE.exists():
    input_file = CLEANED_FILE
    print(f"Reading cleaned data from: {input_file}")
elif RAW_FILE.exists():
    input_file = RAW_FILE
    print(f"Cleaned data not found; reading raw data from: {input_file}")
else:
    raise FileNotFoundError("No data file found. Create or place Sample data (1).xlsx in the project folder.")

# Load data using openpyxl
import_file_str = str(input_file)
df = pd.read_excel(import_file_str, engine="openpyxl")

df.columns = df.columns.str.strip()

sales_col = "Sales" if "Sales" in df.columns else " Sales"
if sales_col not in df.columns:
    raise KeyError("Could not find a sales column in the data.")

for required in ["Profit", "Country", "Product", "Segment", "Month Name"]:
    if required not in df.columns:
        raise KeyError(f"Required column missing: {required}")

print("Total Sales")
print(df[sales_col].sum())

print("Total Profit")
print(df["Profit"].sum())

print("\nSales by Country")
print(df.groupby("Country")[sales_col].sum())

print("\nProfit by Product")
print(df.groupby("Product")["Profit"].sum())

print("\nSales by Segment")
print(df.groupby("Segment")[sales_col].sum())

print("\nMonthly Sales")
print(df.groupby("Month Name")[sales_col].sum())