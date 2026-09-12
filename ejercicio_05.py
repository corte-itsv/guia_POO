class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        valor_total = self.quantity * self. price
        return valor_total
    
    
p1 = Product("Laptop", 899.99, 5)
print(f"Total stock value of {p1.name}: ${p1.total_value()}")