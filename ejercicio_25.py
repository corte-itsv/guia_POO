class Cart:
    def __init__(self):
        self.list = []

    def add_item(self, item):
        self.list.append(item)

    def __len__(self):
        return len(self.list)


cart = Cart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("mango")

print("Number of items in cart:", len(cart))