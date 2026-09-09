class Media:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        pass

class Book(Media):
    def __init__(self, name, price, autor):
        super().__init__(name, price)
        self.autor = autor

    def describe(self):
        return f"{self.name} by {self.autor} - Rs.{self.price}"

class Magazine(Media):
    def __init__(self, name, price, periodo):
        super().__init__(name, price)
        self.periodo = periodo

    def describe(self):
            return f"{self.name} ({self.periodo}) - Rs.{self.price}"

class DVD(Media):
    def __init__(self, name, price, duracion):
        super().__init__(name, price)
        self.duracion = duracion

    def describe(self):
            return f"{self.name}, {self.duracion} - Rs.{self.price}"

multimedia = [Book("Clean Code", 499, "Robert C. Martin"), Magazine("Wired", 150, "Monthly"), DVD("Inception", 299, 148)]
for media in multimedia:
    print(f"{type(media).__name__}: {media.describe()}")