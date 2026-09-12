class Order:
    def __init__(self, orden_id, monto_total):
        self.monto_total = monto_total
        self.orden_id = orden_id
    
    def mostrar_total(self):
        return self.total
        
class DiscountedOrder(Order): 
    def __init__(self, orden_id, monto_total):
        super().__init__(orden_id, monto_total)
        
        
    def mostrar_total(self):
        discounted_t = self.monto_total * 0.9
        return discounted_t
    
c1 = DiscountedOrder("ORD001", 1200)
print(f"Order ID: {c1.orden_id}")
print(f"Origina total: {c1.monto_total}")
print(f"Discounted total: {c1.mostrar_total()}")