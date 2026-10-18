import sqlite3
import pandas as pd
conn=sqlite3.connect("company.db")
df=pd.read_csv("ecommerce_transactions.csv")
df.to_sql("orders", conn, if_exists="replace", index=False)
query = """
SELECT Payment_Method, SUM(Order_Value) AS Total_Sales, COUNT(*) AS Order_Count
FROM orders
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;
"""
result = pd.read_sql_query(query, conn)
print("=== SQL QUERY RESULTS ===")
print(result)
conn.close()

import sqlite3
import pandas as pd
conn=sqlite3.connect("company.db")
df=pd.read_csv("ecommerce_transactions.csv")
df.to_sql("orders", conn, if_exists="replace", index=False)
manager_data = {
    "City": ["Mumbai", "Delhi", "Bangalore", "Hyderabad"],
    "Manager": ["Riya Sharma", "Arjun Mehta", "Priya Nair", "Vikram Reddy"],
    "Region_Target": [50000, 40000, 70000, 35000]
}
manager_df = pd.DataFrame(manager_data)
manager_df.to_sql("city_managers", conn, if_exists="replace", index=False)
query = """
SELECT
    o.Transaction_ID,
    o.Customer_City,
    o.Order_Value,
    m.Manager,
    m.Region_Target
FROM orders o
JOIN city_managers m ON o.Customer_City = m.City
ORDER BY o.Order_Value DESC;
"""

result = pd.read_sql_query(query, conn)
print("=== ORDERS WITH ASSIGNED MANAGERS ===")
print(result)
conn.close()