class Media:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio
    def describe(self):
        return 0

class Book(Media):
    def __init__(self, titulo, precio, autor):
        super().__init__(titulo, precio)
        self.autor=autor
    def describe(self):
        return f"{self.titulo} by {self.autor} - Rs. {self.precio}"

class Magazine(Media):
    def __init__(self, titulo, precio, frecuencia):
        super().__init__(titulo, precio)
        self.frecuencia=frecuencia
    def describe(self):
        return f"{self.titulo}({self.frecuencia})- Rs.{self.precio}"

class DVD(Media):
    def __init__(self, titulo, precio, duracion):
        super().__init__(titulo, precio)
        self.duracion=duracion
    def describe(self):
        return f"{self.titulo}, {self.duracion} mins - Rs. {self.precio}"

libro = Book("Clean Code", 499, "Robert C. Martin")
revista = Magazine("Wired", 150, "Monthly")
disco = DVD("Inception", 299, 148)
print(f"Book: {libro.describe()}")
print(f"Magazine: {revista.describe()}")
print(f"DVD: {disco.describe()}")