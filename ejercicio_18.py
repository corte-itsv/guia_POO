class Shape:

    def __init__(self):

     def area(self):
        pass

class Circle(Shape):

    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def area(self):
        resultado = round((3.141592 * self.radio ** 2), 2)
        return f"Circle area: {resultado}"

class Square(Shape):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f"Square area: {self.lado * self.lado}"
    
class Triangle(Shape):

    def __init__(self, base, altura):
            self.base = base
            self.altura = altura
    def area(self):
        return f"Triangle area: {(self.base * self.altura) / 2}"

circulo = Circle(7)
cuadrado = Square(4)
triangulo = Triangle(6, 8)
print(circulo.area())
print(cuadrado.area())
print(triangulo.area())