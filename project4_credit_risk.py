import pandas as pd
df = pd.read_csv("loan_portfolio_data.csv")
df["Borrower_Name"] = df["Borrower_Name"].str.strip().str.title()
df["Salary_Multiple"] = (df["Loan_Amount"] / df["Monthly_Income"]).round(1)
total_loans = len(df)
total_disbursed = df["Loan_Amount"].sum()
defaulted_df = df[df["Loan_Status"] == "Defaulted"]
total_defaulted_amount = defaulted_df["Loan_Amount"].sum()
default_rate_pct = (len(defaulted_df) / total_loans) * 100
print("=" * 50)
print("🏦 FINPULSE NBFC - EXECUTIVE CREDIT RISK REPORT")
print("=" * 50)
print(f"Total Loans Disbursed   : ₹{total_disbursed:,.0f} ({total_loans} accounts)")
print(f"Total Defaulted Capital : ₹{total_defaulted_amount:,.0f} ({len(defaulted_df)} accounts)")
print(f"Portfolio Default Rate  : {default_rate_pct:.1f}%")
print("=" * 50)
print("\n📊 RISK BREAKDOWN BY EMPLOYMENT TYPE:")
emp_risk = df.groupby("Employment_Type").agg(
    Total_Borrowers=("Loan_ID", "count"),
    Average_Credit_Score=("Credit_Score", "mean"),
    Total_Lent=("Loan_Amount", "sum")
)
print(emp_risk)
watchlist = defaulted_df[["Loan_ID", "Borrower_Name", "Credit_Score", "Monthly_Income", "Loan_Amount", "Salary_Multiple"]]
watchlist.to_csv("collections_watchlist.csv", index=False)
print("\n✅ High-Risk Collections Watchlist exported to 'collections_watchlist.csv'!")