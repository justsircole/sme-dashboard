import csv
from sale import Sale

sales = []

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            sale = Sale(row["date"], row["branch"],
                        row["product"], row["quantity_sold"], row["price"])
            sales.append(sale)
        except ValueError:
            print(f"Skipped a bad row: {row}")

for s in sales:
    print(f"{s.branch} sold {s.quantity_sold} of {s.product_name} for a total of P{s.total_revenue()}")
