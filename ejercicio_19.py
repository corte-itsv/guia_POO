class Media:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    def describe(self):
        return f"{self.titulo} - Rs.{self.precio}"

class Book(Media):
    def __init__(self, titulo, precio, autor):
        super().__init__(titulo, precio)
        self.autor = autor

    def describe(self):
        return f"Book: {self.titulo} by {self.autor} - Rs.{self.precio}"

class Magazine(Media):
    def __init__(self, titulo, precio, frecuencia):
        super().__init__(titulo, precio)
        self.frecuencia = frecuencia

    def describe(self):
        return f"Magazine: {self.titulo} ({self.frecuencia}) - Rs.{self.precio}"

class DVD(Media):
    def __init__(self, titulo, precio, tiempo):
        super().__init__(titulo, precio)
        self.tiempo = tiempo

    def describe(self):
        return f"DVD: {self.titulo}, {self.tiempo} mins - Rs.{self.precio}"


tipos = [
    Book("Clean Code", 499, "Robert C. Martin"),
    Magazine("Wired", 150, "Monthly"),
    DVD("Inception", 299, 148)
]

for tipo in tipos:
    print(tipo.describe())