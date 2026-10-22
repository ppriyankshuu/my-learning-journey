import duckdb
import pandas as pd 
con = duckdb.connect()
con.execute("""
    CREATE TABLE transactions AS
    SELECT * FROM read_csv_auto('ecommerce_transactions.csv')
""")
print("=" * 65)
print("🐘 ENTERPRISE POSTGRESQL ANALYTICS ENGINE")
print("=" * 65)
query_window = """
WITH RankedDeals AS (
    SELECT
        Transaction_ID,
        Customer_City,
        Category,
        Order_Value,
        Payment_Method,
        RANK() OVER (
            PARTITION BY Category
            ORDER BY Order_Value DESC
        ) as Category_Rank
    FROM transactions
)
SELECT
    Category,
    Category_Rank,
    Order_Value,
    Customer_City,
    Payment_Method
FROM RankedDeals
WHERE Category_Rank = 1
ORDER BY Order_Value DESC;
"""
print("\n🏆 #1 TOP TRANSACTION IN EACH CATEGORY (WINDOW FUNCTION):")
top_deals = con.execute(query_window).df()
print(top_deals)
query_case = """
SELECT
    Transaction_ID,
    Customer_City,
    Category,   
    Order_Value,
    CASE
        WHEN Order_Value >= 15000 THEN '💎 High-Ticket VIP'
        WHEN Order_Value >= 5000 THEN '🟢 Mid-Tier'
        ELSE '⚪ Standard Order'
    END AS Customer_Segment
FROM transactions
ORDER BY Order_Value DESC
LIMIT 8;
"""
print("\n🏷️ DYNAMIC CUSTOMER SEGMENTATION (CASE WHEN):")
segmented = con.execute(query_case).df()
print(segmented)
