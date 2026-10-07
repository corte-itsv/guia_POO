
class Order:
    def __init__(self, orderid, montoTotal):
        self.orderID = orderid
        self.monto = montoTotal


class DiscountedOrder(Order):
    def __init__(self, orderid, montoTotal):
        super().__init__(orderid, montoTotal)
        self.descuento = montoTotal * 10 / 100
        self.resultado = montoTotal - self.descuento

    def get_total(self):
        return self.resultado





order = DiscountedOrder("ORD001", 1200)
print("Order ID:", order.orderID)
print("Original Total:", order.monto)
print("Discounted Total:", order.get_total())