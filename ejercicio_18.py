class Shape:
    def area(self):
        pass

class circle(Shape):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2


class Square(Shape):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Triangle(Shape):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

circulo = circle(7)
cuadrado = Square(4) 
triangulo = Triangle(6, 8)

print(f"Circle area: {circulo.area()}") 
print(f"Square area: {cuadrado.area()}") 
print(f"Triangle area: {triangulo.area()}")
