class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(3.14159 * self.radio ** 2, 2)

class Square(Shape):
    def __init__(self, lado):
            self.lado = lado

    def area(self):
        return round(self.lado ** 2, 2)

class Triangle(Shape):
    def __init__(self, base, altura):
            self.base = base
            self.altura = altura

    def area(self):
        return round(self.base * self.altura / 2, 2)

circle = Circle(7)
square = Square(4)
triangle = Triangle(6, 8)

shapes = [circle, square, triangle]
for shape in shapes:
     print(f"{type(shape).__name__} area: {shape.area()}")