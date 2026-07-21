class Sale:
    def __init__(self, date, branch, product_name, quantity_sold, price):
        self.date = date
        self.branch = branch
        self.product_name = product_name
        self.quantity_sold = int(quantity_sold)
        self.price = float(price)

    def total_revenue(self):
        return self.quantity_sold * self.price


if __name__ == "__main__":
    s1 = Sale("2026-06-01", "Gaborone", "Maize Meal 10kg", "45", "55")
    print(s1.total_revenue())
