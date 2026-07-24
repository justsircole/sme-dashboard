import pandas as pd

df = pd.read_csv("data/sales.csv")
print(df)

df["total_revenue"] = df["quantity_sold"] * df["price"]
print(df)

revenue_by_branch = df.groupby("branch")["total_revenue"].sum()
print(revenue_by_branch)

quantity_by_product = df.groupby("product")["quantity_sold"].sum()
print(quantity_by_product.sort_values())
