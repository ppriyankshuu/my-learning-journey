import pandas as pd
import duckdb
print("=" * 65)
print("💰 🛵 BITESWIFT FOOD DELIVERY - UNIT ECONOMICS & MARGIN ENGINE")
print("=" * 65)
df = pd.read_csv("biteswift_delivery_data.csv")
df["Commission_Revenue"] = df["Food_Bill_INR"] * df["Commission_Rate"].round(1)
df["Platform_Net_Revenue"] = df["Commission_Revenue"] + df["Cust_Delivery_Fee_INR"]
df["Total_Cost"] = df["Rider_Payout_INR"] + df["Discount_Voucher_INR"]
df["Contribution_Margin_INR"] = df["Platform_Net_Revenue"] - df["Total_Cost"].round(1)
df["Is_Profitable"] = df["Contribution_Margin_INR"] > 0
total_orders = len(df)
profit_orders = df[df["Is_Profitable"] == True]
loss_orders = df[df["Is_Profitable"] == False]
total_gmv = df["Food_Bill_INR"].sum()
total_net_cm = df["Contribution_Margin_INR"].sum()
loss_pct = (len(loss_orders) / total_orders) * 100
avg_cm_per_order = df["Contribution_Margin_INR"].mean()
print(f"Total Gross Merchandise Value (GMV) : ₹{total_gmv:,.0f}")
print(f"Total Net Contribution Margin (Profit) : ₹{total_net_cm:,.0f}")
print(f"Average Contribution Margin per Order : ₹{avg_cm_per_order:,.0f}")
print(f"Orders Burning Cash (Negative Margin) : {len(loss_orders)} of {total_orders} ({loss_pct: .1f}%)")
print("=" * 65)
con = duckdb.connect()
con.execute("CREATE TABLE orders AS SELECT * FROM df")
query_city = """
SELECT
    City,
    COUNT(*) AS Order_Volume,
    ROUND(SUM(Food_Bill_INR), 0) as City_GMV,
    ROUND(SUM(Contribution_Margin_INR), 1) as City_Net_Profit,
    ROUND(AVG(Contribution_Margin_INR), 1) as Avg_Profit_Per_Order,
FROM orders
GROUP BY City
ORDER BY City_Net_Profit DESC;
"""
print("\n🏙️ CITY-LEVEL PROFITABILITY LEADERBOARD (SQL):")
city_summary = con.execute(query_city).df()
print(city_summary)
query_weather = """
SELECT
    Weather,
    COUNT(*) as Total_Deliveries,
    ROUND(AVG(Rider_Payout_INR), 1) as Avg_Rider_Payout,
    ROUND(AVG(Contribution_Margin_INR), 1) as Avg_Net_Margin
FROM orders
GROUP BY Weather
ORDER BY Avg_Net_Margin ASC;
"""
print("\n🌦️ WEATHER IMPACT ON FULFILLMENT COST & MARGINS (SQL):")
weather_summary = con.execute(query_weather).df()
print(weather_summary)
loss_orders.to_csv("bleeding_orders_audit.csv", index=False)
print("\n🚨 Bleeding Orders Audit exported to 'bleeding_orders_audit.csv'!")
