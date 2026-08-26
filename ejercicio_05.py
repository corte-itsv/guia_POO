class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        valor_total = self.price * self.quantity
        return valor_total
    
p1 = Product("Laptop", 899.99, 5)
valor = p1.total_value()
print(f"Total stock value of {p1.name}: ${valor}")