revenue = 250000
deals = 2

avg_deal = revenue / deals

print("=== EXECUTIVE REPORT ===")
print("Total Revenue:", revenue)
print("Total Deals:", deals)
print("Average Deal Size:", avg_deal)

if avg_deal > 100000:
    print("Territory Status: High Value Territory")
else:
    print("Territory Status: Standard Territory")        