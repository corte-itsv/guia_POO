from math import pi

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        area = round((pi * (self.r**2)), 2)
        return area

class Square(Shape):
    def __init__(self, l):
        super().__init__()
        self.l = l

    def area(self):
        area = (self.l**2)
        return area

class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__()
        self.b = b
        self.h = h

    def area(self):
        area = ((self.b * self.h) / 2)
        return area

formas = [Circle(7), Square(4), Triangle(6, 8)]

for forma in formas:
    print(f"{type(forma).__name__} area: {forma.area()}")