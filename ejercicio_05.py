class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        total = self.price * self.quantity
        return total

p1 = product("Laptop", 899.99, 5)
print(f"Total stock value of {p1.name}: {p1.total_value()}")