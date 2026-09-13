class Media:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio
        
    
class Book(Media):
    def __init__(self, titulo, precio, autor):
        super().__init__(titulo, precio)    
        self.autor = autor

    def mostrar(self): 
        return f"{self.titulo} by {self.autor} - ${self.precio}"
    
class Magazine(Media):
    def __init__(self, titulo, precio, periodo):
        super().__init__(titulo, precio)    
        self.periodo = periodo

    def mostrar(self): 
        return f"{self.titulo}({self.periodo}) - ${self.precio}"
    
class DVD(Media):
    def __init__(self, titulo, precio, duracion):
        super().__init__(titulo, precio)    
        self.duracion = duracion

    def mostrar(self): 
        return f"{self.titulo}, {self.duracion} - ${self.precio}"
    

c1 = Book("Clean Code", 499, "Robert C. Martin")
c2 = Magazine("Wired", 150, "Monthly")
c3 = DVD("Inception", 299, 148)

print(c1.mostrar())
print(c2.mostrar())    
print(c3.mostrar())