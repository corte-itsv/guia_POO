class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(3.14159 * self.radio ** 2, 2)

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
        return 0.5 * self.base * self.altura


cir = Circle(7)
sq = Square(4)
tr = Triangle(6, 8)
print(f"Circle area: {cir.area()} ")
print(f"Square area: {sq.area()} ")
print(f"Circle area: {tr.area()} ")