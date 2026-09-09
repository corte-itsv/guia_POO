class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
class DiscountedOrder(Order):
    def discounted_total(self):
        return self.total * 0.90
order = DiscountedOrder("ORD001", 1200)
print("Order ID:", order.order_id)
print("Original Total:", order.total)
print("Discounted Total:", order.discounted_total())