class Order:
    def __init__(self, id, monto):
        self.monto = monto
        self.id = id

class DiscountedOrder(Order):
    def __init__(self, id, monto):
        super().__init__(id, monto)

    def descontar(self):
        montodescontado = (self.monto - (self.monto * 0.10))
        return montodescontado

x = DiscountedOrder("ORD001", 1200)

print(f"Order ID: {x.id}")
print(f"Original Total: {x.monto}")
print(f"Discounted Total: {x.descontar()}")