class Cart:
    def __init__(self):
        self.items = []

    def añadir(self, obj):
        self.items.append(obj)

    def __len__(self):
        return len(self.items)


carrito = Cart()
carrito.añadir("apple")
carrito.añadir("banana")
carrito.añadir("mango")

print("Number of items in cart:", len(carrito))
