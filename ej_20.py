class Order:
    def __init__(self, precio):
        self.precio=precio

class DiscountedOrder(Order):
    def __init__(self, id, precio):
        super().__init__(precio)
        self.id=id
    def descontar(self):
        return self.precio * 0.9

orden = DiscountedOrder("ORD001", 1200)
print(f"ORDER ID: {orden.id}")
print(f"Original Total: {orden.precio}")
print(f"Discounted Price: {orden.descontar()}")
