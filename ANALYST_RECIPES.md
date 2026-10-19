 # 📖 The Business Technologist's Recipe Book
*Your permanent "cheat sheet" for Excel, SQL, Pandas, and Git. Never write from a blank page again.*

---

## 🟢 PART 1: The Git & Terminal Recipes (Save & Upload)

| What You Want to Do | The Recipe (Copy-Paste) | Plain English Meaning |
| :--- | :--- | :--- |
| **Check what changed** | `git status` | *"Show me what files were added or edited."* |
| **Pack all files** | `git add .` | *"Pack everything in this folder into the staging box."* |
| **Save snapshot** | `git commit -m "Your clear note here"` | *"Seal the box with a timestamp and note."* |
| **Upload to cloud** | `git push` | *"Send all sealed snapshots to GitHub."* |
| **Cancel a typed command** | `Ctrl + C` | *"Wipe the current terminal line clean."* |

---

## 🟢 PART 2: Microsoft Excel Analyst Recipes

### 1. The Instant Table
* **Shortcut:** Click inside data ➔ **`Ctrl + T`** ➔ Check *"My table has headers"* ➔ Press **Enter**.
* **Why:** Unlocks automated calculated columns, alternating stripes, and filters.

### 2. Auto-Fit All Column Widths
* **Shortcut:** **`Ctrl + A`** (select all) ➔ **Double-click** the line between any two column headers.

### 3. Clean Messy Text (Spaces & Capitalization)
* **Recipe:** `=PROPER(TRIM(B2))`
* **Plain English:** *"Strip away annoying spaces, then capitalize the first letter of each word."*

### 4. Look Up Data from Another Table (XLOOKUP)
* **Recipe:** `=XLOOKUP([@Product], $M$2:$M$6, $N$2:$N$6)`
* **Plain English:** `XLOOKUP(what_to_search, where_to_look, what_to_bring_back)`
* *Pro Tip:* Always press **`F4`** on the reference ranges to add `$` signs so the table never moves!

### 5. Automated Decision (IF Logic)
* **Recipe:** `=IF([@Total_Revenue] >= 100000, "High Value", "Standard")`
* **Plain English:** `IF(condition_is_true, "what_to_show", "what_to_show_otherwise")`

### 6. Dynamic Sum based on Dropdown (SUMIFS)
* **Recipe:** `=SUMIFS(Table1[Total_Revenue], Table1[Region], Q1)`
* **Plain English:** `SUMIFS(column_to_add, column_to_filter, match_cell)`

### 7. Count Deals based on Dropdown (COUNTIFS)
* **Recipe:** `=COUNTIFS(Table1[Region], Q1)`
* **Plain English:** `COUNTIFS(column_to_filter, match_cell)`

---

## 🟢 PART 3: Python & Pandas Recipes

### 1. The Standard Setup
```python
import pandas as pd
df = pd.read_csv("your_filename.csv")

### 2. Calculated Column (Math on Columns)

# Recipe: df["New_Column"] = df["Col_A"] * df["Col_B"]
df["Total_Revenue"] = df["Unit_Price"] * df["Quantity"]

### 3. Clean Text (TRIM & Title Case in Pandas)

# Recipe: Strip spaces and Capitalize Words
df["Customer_Name"] = df["Customer_Name"].str.strip().str.title()

### 4. Filter Specific Rows (Boolean Masking)

# Recipe: filtered_df = df[df["Column_Name"] >= Number]
vip_orders = df[df["Final_Amount"] >= 10000]

• Plain English: "Keep only the rows where Final_Amount is 10,000 or bigger."

### 5. The Instant Pivot Table (.groupby)

# Recipe: df.groupby("Category_Column")["Metric_Column"].sum()
city_sales = df.groupby("City")["Total_Revenue"].sum()

### 6. Export Results to Excel/CSV for Management

# Recipe: Export cleaned table to a brand new file
df.to_csv("final_report.csv", index=False)
  ──────
## 🟢 PART 4: SQL Database Recipes

### 1. The Classic Select & Filter

SELECT Customer_City, Payment_Method, Order_Value
FROM orders
WHERE Order_Value >= 10000
ORDER BY Order_Value DESC;

• Plain English: "Show me these 3 columns from the orders table, only for orders >= 10,000, sorted highest to lowest."

### 2. The SQL Pivot Table (GROUP BY)

SELECT
    Customer_City,
    SUM(Order_Value) AS Total_Sales,
    COUNT(*) AS Order_Count
FROM orders
GROUP BY Customer_City
ORDER BY Total_Sales DESC;

• Plain English: "Group orders into city buckets, sum up the total sales, count
  the deals, and sort descending."

### 3. The Table Bridge (SQL JOIN = XLOOKUP)

SELECT
    o.Transaction_ID,
    o.Customer_City,
    m.Manager
FROM orders o
JOIN city_managers m ON o.Customer_City = m.City;

• Plain English: "Glue the orders table (o) and managers table (m) together wherever the City name matches."

---

## 🟢 PART 5: Microsoft Power BI Recipes (Executive Dashboards)

### 1. Ingest Raw CSV Data
* **Path:** `Home` tab ➔ `Get data` ➔ `Text/CSV` ➔ Pick file ➔ Click `Load`.
* **Plain English:** *"Brings tabular data directly into Power BI's in-memory engine."*

### 2. The Clustered Bar/Column Chart (Leaderboard)
* **Visual:** Click `Clustered column chart` 📊 in the Visualizations pane.
* **Fields:** Drag categorical column (e.g., `Customer_City`) to **X-axis**; drag numeric metric (e.g., `Order_Value`) to **Y-axis**.
* **Plain English:** *"Equivalent to SQL GROUP BY + ORDER BY DESC or Excel Pivot Chart."*

### 3. The Executive KPI Card (Hero Metric)
* **Visual:** Click `Card` (icon with `1 2 3`) in Visualizations pane.
* **Fields:** Drag numeric metric (e.g., `Order_Value`) to **Fields**.
* **Plain English:** *"Instant auto-sum displayed in bold, readable executive format (e.g., 144K)."*

### 4. Share of Total (Donut Chart)
* **Visual:** Click `Donut chart` 🍩 in Visualizations pane.
* **Fields:** Drag category (e.g., `Payment_Method`) to **Legend**; drag metric (e.g., `Order_Value`) to **Values**.
* **Plain English:** *"Displays percentage breakdown across segments."*

### 5. Interactive Slicer (Dynamic Cross-Filtering)
* **Visual:** Click `Slicer` (funnel/table icon) in Visualizations pane.
* **Fields:** Drag filter column (e.g., `Category`) to **Field**.
* **Plain English:** *"Clicking any item dynamically filters every chart on the dashboard in real time."*

