## Ejercicio 5: Clase Product con calculadora de valor de stock

##**Pista:**
##- Define `__init__` con `name`, `price` y `quantity` como parámetros y asigna cada uno a `self`.
##- En `total_value()`, retorna `self.price * self.quantity`.
##- Usa un f-string con formato `:.2f` para mostrar el resultado como un valor monetario con dos decimales.

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


p1 = Product("Laptop", 899.99, 5)      
print(f"Total stock value of Laptop: {p1.total_value()}")