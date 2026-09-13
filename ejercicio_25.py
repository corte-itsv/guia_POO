class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


cart = Cart(["apple", "banana", "mango"])

print(f"Number of items in cart: {len(cart)}")