class Order:
    def __init__(self, orden, total):
        self.orden = orden
        self.total = total

    def get_total(self):
        return self.total

class DiscountedOrder(Order):
    def __init__(self, orden, total):
        super().__init__(orden, total)

    def get_total(self):
        return self.total * 0.90


orden = DiscountedOrder("ORD001", 1200)
print("Order ID:", orden.order_id)
print("Original Total:", orden.total)
print("Discounted Total:", orden.get_total())