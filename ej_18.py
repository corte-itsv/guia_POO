class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius=radius
    def area(self):
        return round(3.14159*self.radius**2 , 2)

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base=base
        self.height=height
    def area(self):
        return (self.height*self.base)/2

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side=side
    def area(self):
        return self.side ** 2

c = Circle(7)
s = Square(4)
t = Triangle(6,8)

print(f"Circle area: {c.area()}")
print(f"Square Area: {s.area()}")
print(f"Triangle Area: {t.area()}")