import pandas as pd
df = pd.read_csv("saas_customer_churn.csv")
df["Company_Name"] = df["Company_Name"].str.strip().str.title()
total_accounts = len(df)
churned_df = df[df["Status"] == "Churned"]
active_df = df[df["Status"] == "Active"]
churn_rate = (len(churned_df) / total_accounts) * 100
total_active_mrr = active_df["Monthly_Fee"].sum()
annual_run_rate_arr = total_active_mrr * 12
print("=" * 55)
print("💻 CLOUDFLOW SAAS - EXECUTIVE RETENTION & MRR REPORT")
print("=" * 55)
print(f"Total Accounts Analyzed : {total_accounts}")
print(f"Active Accounts         : {len(active_df)}")
print(f"Churned Accounts        : {len(churned_df)}")
print(f"Portfolio Churn Rate    : {churn_rate:.1f}%")
print(f"Monthly Recurring (MRR) : ${total_active_mrr:,.0f} / month")
print(f"Annual Run Rate (ARR)   : ${annual_run_rate_arr:,.0f} / year")
print("=" * 55)
print("\n📊 RETENTION BREAKDOWN BY SUBSCRIPTION TIER:")
tier_metrics = df.groupby("Tier").agg(
    Total_Customers=("Customer_ID", "count"),
    Avg_Tenure_Months=("Tenure_Months", "mean"),
    Avg_Support_Ticket=("Support_Tickets", "mean")
).round(1)
print(tier_metrics)
at_risk = active_df[active_df["Support_Tickets"] >= 3]
at_risk.to_csv("customer_success_intervention.csv", index=False)
print("\n✅ Customer Success Intervention list exported to 'customer_success_intervention.csv'!")