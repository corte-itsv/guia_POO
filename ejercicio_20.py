class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

    def get_total(self):
        return self.total

class DiscountedOrder(Order):
    def __init__(self, order_id, total):
        super().__init__(order_id, total)

    def get_total(self):
        return self.total * 0.90


order = DiscountedOrder("ORD001", 1200)
print("Order ID:", order.order_id)
print("Original Total:", order.total)
print("Discounted Total:", order.get_total())