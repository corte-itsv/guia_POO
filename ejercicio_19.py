class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price
class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author
    def describe(self):
        return f"Book: {self.title} by {self.author} - Rs.{self.price}"
class Magazine(Media):
    def __init__(self, title, price, frequency):
        super().__init__(title, price)
        self.frequency = frequency
    def describe(self):
        return f"Magazine: {self.title} ({self.frequency}) - Rs.{self.price}"
class DVD(Media):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self.duration = duration
    def describe(self):
        return f"DVD: {self.title}, {self.duration} mins - Rs.{self.price}"
book = Book("Clean Code", 499, "Robert C. Martin")
magazine = Magazine("Wired", 150, "Monthly")
dvd = DVD("Inception", 299, 148)
print(book.describe())
print(magazine.describe())
print(dvd.describe())