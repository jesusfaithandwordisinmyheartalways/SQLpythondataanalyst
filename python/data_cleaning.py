import pandas as pd

# 1. Load raw data
df = pd.read_csv("../data/raw_sales_data.csv")

# 2. Fill missing customer names
df["Customer"].fillna("Unknown", inplace=True)

# 3. Fill missing quantities with 1
df["Quantity"].fillna(1, inplace=True)

# 4. Recalculate total column
df["Total"] = df["Quantity"] * df["Price"]

# 5. Drop duplicate rows
df.drop_duplicates(inplace=True)

# 6. Save cleaned file
df.to_csv("../data/cleaned_sales_data.csv", index=False)

# Optional: print first 5 rows to check
print("CSV file completed. First 5 rows:")
print(df.head())