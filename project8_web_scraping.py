import requests
from bs4 import BeautifulSoup
import pandas as pd
import duckdb

print("=" * 65)
print("🌐 LIVE FINANCIAL WEB SCRAPER & SQL INGESTION PIPELINE")
print("=" * 65)

# 1. Fetch live market data from sample endpoint
url = "https://www.scrapethissite.com/pages/forms/"
headers = {"User-Agent": "Mozilla/5.0"}

print(f"📡 Requesting live data from: {url} ...")
response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:
    print("✅ HTTP 200 OK: Successfully connected to server!\n")
else:
    print(f"❌ Failed to connect: Status {response.status_code}")
    exit()

# 2. Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the tabular data rows
table = soup.find("table", class_="table")
rows = table.find_all("tr")

data = []
# Loop through table rows (skip header row 0)
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 6:
        team_name = cols[0].text.strip()
        year = cols[1].text.strip()
        wins = int(cols[2].text.strip())
        losses = int(cols[3].text.strip())
        win_pct = float(cols[5].text.strip())
        
        data.append({
            "Entity_Name": team_name,
            "Year": year,
            "Wins": wins,
            "Losses": losses,
            "Win_Percentage": win_pct
        })

# 3. Load into Pandas DataFrame
df = pd.DataFrame(data)
print(f"📊 Extracted {len(df)} live records directly from the web!\n")

# 4. Connect to Enterprise PostgreSQL (DuckDB) & Ingest
con = duckdb.connect()
con.execute("CREATE TABLE live_web_data AS SELECT * FROM df")

# 5. Run SQL Analytical Window Query on Scraped Data
query = """
SELECT 
    Entity_Name,
    Year,
    Wins,
    Losses,
    Win_Percentage,
    CASE 
        WHEN Win_Percentage >= 0.60 THEN '🥇 Elite Performer'
        WHEN Win_Percentage >= 0.45 THEN '🥈 Balanced Competitor'
        ELSE '🥉 Underperforming'
    END AS Performance_Tier,
    RANK() OVER (ORDER BY Win_Percentage DESC) as Global_Rank
FROM live_web_data
LIMIT 10;
"""

print("🐘 SQL ANALYTICS ON LIVE SCRAPED DATA (WINDOW FUNCTION + CASE):")
analytics_result = con.execute(query).df()
print(analytics_result)

# 6. Export to CSV
analytics_result.to_csv("scraped_market_report.csv", index=False)
print("\n✅ Cleaned live dataset auto-exported to 'scraped_market_report.csv'!")
