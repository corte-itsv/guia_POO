class media:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def describe(self):
        return f"{self.title} - Rs.{self.price}"

class book(media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author

    def describe(self):
        return f"Book: {self.title} by {self.author} - Rs.{self.price}"

class magazine(media):
    def __init__(self, title, price, frequency):
        super().__init__(title, price)
        self.frequency = frequency

    def describe(self):
        return f"Magazine: {self.title} ({self.frequency}) - Rs.{self.price}"

class DVD(media):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self.duration = duration

    def describe(self):
        return f"DVD: {self.title}, {self.duration} mins - Rs.{self.price}"
items = [
    book("Clean Code", 499, "Robert C. Martin"),
    magazine("Wired", 150, "Monthly"),
    DVD("Inception", 299, 148)
]

for item in items:
    print(item.describe())