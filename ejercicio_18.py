import math
class Shape:
    def area(self):
        return 0
    
class Circle:
    def __init__(self,radio):
        self.radio = radio
    def area(self):
        return round((self.radio**2 * math.pi), 2)
    
class Square:
    def __init__(self,lado):
            self.lado = lado
    def area(self):
            return self.lado * self.lado
        
class Triangle:
    def __init__(self,base, altura):
            self.base = base
            self.altura = altura
    def area(self):
            return (self.base * self.altura)/2
    
c1 = Circle(7)
s1 = Square(4)
t1 = Triangle(6, 8)

print(f"Circle area: {c1.area()}")
print(f"Square area: {s1.area()}")
print(f"Triangle area: {t1.area()}")


