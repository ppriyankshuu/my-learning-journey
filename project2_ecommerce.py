import pandas as pd
df = pd.read_csv("ecommerce_transactions.csv")
df["Final_Amount"] = df["Order_Value"] * (1 - df["Discount_Percent"])
print("=== FIRST 5 ORDERS ===")
print(df[["Transaction_ID", "Customer_City", "Category", "Final_Amount"]].head())
payment_summary = df.groupby("Payment_Method")["Final_Amount"].sum()
print("\n=== REVENUE BY PAYMENT METHOD ===")
print(payment_summary)
vip_orders = df[df["Final_Amount"] >=10000]
print("\n=== VIP ORDERS (>= 10,000) ===")
print(vip_orders[["Transaction_ID", "Customer_City", "Payment_Method", "Final_Amount"]])
vip_orders.to_csv("vip_customers_report.csv", index=False)
print("\n>>> SUCCESS: 'vip_customers_report.csv' has been generated for management!")