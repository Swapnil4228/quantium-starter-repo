import pandas as pd

# List of input CSV files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Read and combine all files
df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# Keep only pink morsels
df = df[df["product"] == "pink morsel"]

# Remove the $ sign and convert price to a number
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create the Sales column
df["Sales"] = df["price"] * df["quantity"]

# Keep only the required columns
output = df[["Sales", "date", "region"]]

# Rename columns
output.columns = ["Sales", "Date", "Region"]

# Save the new CSV file
output.to_csv("formatted_sales_data.csv", index=False)

print("Done! File saved as formatted_sales_data.csv")