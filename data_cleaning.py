import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "Sample data (1).xlsx"
OUTPUT_FILE = BASE_DIR / "Cleaned_Financial_Data.xlsx"

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

# Load data using openpyxl
print(f"Reading input file: {INPUT_FILE}")
df = pd.read_excel(INPUT_FILE, engine="openpyxl")

# Normalize column names and inspect data
df.columns = df.columns.str.strip()
print(df.head())
print(df.info())
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column if present
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Save cleaned data
df.to_excel(OUTPUT_FILE, index=False)
print(f"Cleaning completed! Cleaned file saved to: {OUTPUT_FILE}")