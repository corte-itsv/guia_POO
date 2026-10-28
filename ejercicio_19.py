class Media:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        pass

class Book(Media):

    def __init__(self, name, price, author):
        self.author = author
        super().__init__(name, price)

    def describe(self):
        return f"Book: {self.name} by {self.author} - Rs.{self.price}"

class Magazine(Media):

    def __init__(self, name, price, publish):
            self.publish = publish
            super().__init__(name, price)
    
    def describe(self):
        return f"Magazine: {self.name} ({self.publish}) - Rs.{self.price}"

class DVD(Media):

    def __init__(self, name, price, duration):
                self.duration = duration
                super().__init__(name, price)
        
    def describe(self):
        return f"Magazine: {self.name}, {self.duration} - Rs.{self.price}"

items = [
    Book("Clean Code", 499, "Robert C. Martin"),
    Magazine("Wired", 150, "Monthly"),
    DVD("Inception", 299, 148)
]

for item in items:
    print(item.describe())