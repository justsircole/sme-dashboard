import csv
import random
from datetime import date, timedelta

branches = ["Gaborone", "Francistown", "Maun"]

products = {
    "Maize Meal 10kg": 55,
    "Cooking Oil 2L": 35,
    "Sugar 2kg": 22,
    "Rice 5kg": 60,
}

start_date = date(2026, 4, 1)
end_date = date(2026, 7, 31)

rows = []
current_date = start_date

while current_date <= end_date:
    for branch in branches:
        for product, price in products.items():
            if random.random() < 0.6:
                quantity = random.randint(5, 50)
                rows.append([current_date.isoformat(),
                            branch, product, quantity, price])
    current_date += timedelta(days=1)

with open("data/sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "branch", "product", "quantity_sold", "price"])
    writer.writerows(rows)

print(f"Generated {len(rows)} rows, from {start_date} to {end_date}")
