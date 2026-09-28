class Media():
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return self.name

class Book(Media):
    def __init__(self, name, price, author):
        super().__init__(name)
        self.author = author
        self.price = price
    
    def describe_media(self):
        super().describe()
        return(f"{self.name} by {self.author} - Rs.{self.price}")
    
class Magazine(Media):
    def __init__(self, name, price, often):
        super().__init__(name)
        self.often = often
        self.price = price
    
    def describe_media(self):
        super().describe()
        return (f"{self.name} ({self.often}) - Rs.{self.price}")

class DVD(Media):
    def __init__(self, name, price, duration):
        super().__init__(name)
        self.duration = duration
        self.price = price
    
    def describe_media(self):
        super().describe()
        return (f"{self.name}, {self.duration} mins - Rs.{self.price}")

m1 = Book("Clean Code", 499, "Robert C. Martin")
m2 = Magazine("Wired", 150, "Monthly")
m3 = DVD("Inception", 299, 148)

book_describe = m1.describe_media()
print(f"Book: {book_describe}")

magazine_describe = m2.describe_media()
print(f"Magazine: {magazine_describe}")

dvd_describe = m3.describe_media()
print(f"DVD: {dvd_describe}")