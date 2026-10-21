import pandas as pd
df = pd.read_csv("inventory_darkstore_data.csv")
df["Product_Name"] = df["Product_Name"].str.strip().str.title()
df["Holding_Valuation_INR"] = df["Current_Stock"] * df["Unit_Cost_INR"]
df["Days_Of_Supply"] = (df["Current_Stock"] / df["Daily_Demand"]).round(1)
df["Stockout_Alert"] = df["Current_Stock"] < df["Safety_Stock"]
df["Recommended_Reordering_Units"] = ((df["Daily_Demand"] * 2) + df["Safety_Stock"] - df["Current_Stock"]).clip(lower=0)
total_skus = len(df)
total_inventory_value = df["Holding_Valuation_INR"].sum()
critical_skus = df[df["Stockout_Alert"] == True]
pct_stockout_risk = (len(critical_skus) / total_skus) * 100
print("=" * 60)
print("⚡ FLASHCART 10-MIN DARK STORE - INVENTORY OPS REPORT")
print("=" * 60)
print(f"Total Active SKUs Tracked       : {total_skus}")
print(f"Total Inventory Capital Tied    : ₹{total_inventory_value:,.0f}")
print(f"SKUs with Critical Stockout Risk: {len(critical_skus)} of {total_skus} ({pct_stockout_risk:.1f}%)")
print("=" * 60)
print("\n📊 CAPITAL ALLOCATION & BY CATEGORY:")
cat_summary = df.groupby("Category").agg(
    Total_SKUs=("SKU_ID", "count"),
    Avg_Days_Supply=("Days_Of_Supply", "mean"),
    Total_Capital=("Holding_Valuation_INR", "sum")
).round(1)
print(cat_summary)
procurement_order = critical_skus[["SKU_ID", "Product_Name", "Category", "Current_Stock", "Safety_Stock", "Daily_Demand", "Recommended_Reordering_Units"]]
procurement_order.to_csv("urgent_restock_order.csv", index=False)
print("\n🚨 Urgent Restock Purchase Order exported to 'urgent_restock_order.csv'!")
