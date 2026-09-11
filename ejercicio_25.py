class Cart:
    def __init__(self, lista):
        self.lista=lista
    def __len__(self):
        return len(self)

c1=["apple", "banana", "mango"]
print(f"Items en el carrito:", len(c1))