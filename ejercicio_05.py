class Product:
    def __init__(self, name, price, quantity):
        self.price = price
        self.quantity = quantity
        self.name = name

    def total_value(self):
        return self.price * self.quantity


p1 = Product("Laptop", 899.99, 5)
print(f"Total stock value of {p1.name}: ${p1.total_value():.2f}")