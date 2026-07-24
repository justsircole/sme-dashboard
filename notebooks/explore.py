import pandas as pd

df = pd.read_csv("data/sales.csv")
df["total_revenue"] = df["quantity_sold"] * df["price"]
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

print("=== Revenue by branch ===")
print(df.groupby("branch")["total_revenue"].sum())

print("\n=== Quantity sold by product (slowest first) ===")
print(df.groupby("product")["quantity_sold"].sum().sort_values())

print("\n=== Revenue by month ===")
print(df.groupby("month")["total_revenue"].sum())
