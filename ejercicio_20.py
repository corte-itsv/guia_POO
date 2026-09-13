class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

    def display(self):
        print(f"Order ID: {self.order_id}")
        print(f"Original Total: {self.total}")

class DiscountedOrder(Order):
    def discounted_total(self):
        return self.total * 0.90

order = DiscountedOrder("ORD001", 1200)

order.display()
print(f"Discounted Total: {order.discounted_total()}")