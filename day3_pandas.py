import pandas as pd
df = pd.read_csv('sales_data.csv')
df["Customer_Name"] = df["Customer_Name"].str.upper().str.title()
df["Total_Revenue"] = df["Unit_Price"]*df["Quantity"]
region_summary = df.groupby("Region")["Total_Revenue"].sum()

print("=== CLEANED SALES DATA ===")
print(df[["Customer_Name", "Region", "Product", "Total_Revenue"]])

print("\n=== TOTAL REVENUE BY REGION (PIVOT TABLE) ===")
print(region_summary)
