class Order():
    def __init__(self, order_id, initial_amount):
        self.order_id = order_id
        self.initial_amount = initial_amount
        
class DiscountedOrder(Order):
    def discount_applied(self):
        final_amount = self.initial_amount - (self.initial_amount * 0.1)
        return final_amount
    
o1 = DiscountedOrder("ORD001", 1200)
final_amount = o1.discount_applied()

print(f"Order ID: {o1.order_id}")
print(f"Original Total: {o1.initial_amount}")
print(f"Discounted Total: {final_amount}")