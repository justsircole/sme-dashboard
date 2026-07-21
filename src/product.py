class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name} costs P{self.price}"


if __name__ == "__main__":
    p1 = Product("Maize Meal 10kg", 55)
    print(p1.describe())
