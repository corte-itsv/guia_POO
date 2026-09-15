
class Media:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    def describe(self):
        return f'{self.titulo} price {self.precio}'


class Book(Media):
    def __init__(self, titulo, precio, autor):
        super().__init__(titulo, precio)
        self.autor = autor

    def describe(self):
        return f'Book: {self.titulo} by {self.autor} - price {self.precio}'


class Magazine(Media):
    def __init__(self, titulo, precio, frequency):
        super().__init__(titulo, precio)
        self.frequency = frequency

    def describe(self):
        return f'Magazine: {self.titulo} ({self.frequency}) price {self.precio}'


class DVD(Media):
    def __init__(self, titulo, precio, time):
        super().__init__(titulo, precio)
        self.time = time

    def describe(self):
        return f'DVD: {self.titulo}, {self.time}mins price {self.precio}'


book1 = Book("Clean Code", 499, "Robert C. Martin")
magazine1 = Magazine("Wired", 150, "Monthly")
dvd1 = DVD("Inception", 299, 148)


print(book1.describe())
print(magazine1.describe())
print(dvd1.describe())