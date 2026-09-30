class Carta:
    def __init__(self, list):
        self.list = list
        
    def __len__(self):
        items_quantity = len(self.list)
        return items_quantity
    

items_list = ["apple", "banana", "mango"]

c1 = Carta(items_list)
items_quantity = c1.__len__()

print(f"Number of items in cart: {items_quantity}")