import sqlite3
import pandas as pd
print(">>> [STAGE 1] INGETSING & CLANING RAW MONDAY SALRS DATA")
df = pd.read_csv("weekly_raw_sales.csv")
df["Customer_Name"] = df["Customer_Name"].str.strip().str.title()
df["Sales_Rep"] = df["Sales_Rep"].str.strip().str.title()
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
print("✓ Cleaned customer names, standardized sales reps, and calculated revenue.")
print("\n>>> [Stage 2] LOADING INTO RELATIONAL SQL DATABASE")
conn = sqlite3.connect("weekly_report.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
print("✓ Successfully loaded data into 'sales' table in weekly_report.db")
print("\n>>> [Stage 3] EXECUTING EXECUTIVE SQL QUERIES")
rep_query = """
SELECT Sales_Rep, SUM(Revenue) AS Total_Revenue, COUNT(*) AS Deals_Closed, ROUND(AVG(Revenue), 2) AS Avg_Deal_Size
FROM sales
GROUP BY Sales_Rep
ORDER BY Total_Revenue DESC;
"""
rep_leaderboard = pd.read_sql_query(rep_query, conn)
print("=== SALES REP LEADERBOARD ===")
print(rep_leaderboard)
category_query = """
SELECT City, Category, SUM(Revenue) AS Category_Revenue
FROM sales
GROUP BY City, Category
ORDER BY City, Category_Revenue DESC;
"""
city_category_summary = pd.read_sql_query(category_query, conn)
print("\n=== REVENUE BY CITY & CATEGORY ===")
print(city_category_summary)
print("\n>>> [Stage 4] EXPORTING EXECUTIVE REPORTS FOR MANAGEMENT")
rep_leaderboard.to_csv("weekly_executive_summary.csv", index=False)
print("✓ Exported 'weekly_executive_summary.csv' - Ready to email to leadership!")
conn.close()