class Cart:
    def __init__(self):
        self.lista = []
        
    def add_item(self, item):
        self.lista.append(item)
        
    def __len__(self):
        return len(self.lista)
    
cart = Cart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("mango")
    
print(f"Number of items in cart: {len(cart)}")