class Shape:
    def __init__(self, medida):
        self.medida = medida
        
    def area(self):
        return self.medida
    
class Circle(Shape):
    def circle_area(self):
        super().area()
        real_area = (self.medida ** 2) * 3.14
        return real_area
    
class Square(Shape):
    def square_area(self):
        super().area()
        real_area = self.medida * self.medida
        return real_area

class Triangle(Shape):
    def __init__(self, medida, altura):
        super().__init__(medida)
        self.altura = altura
        
    def triangle_area(self):
        super().area()
        real_area = (self.medida * self.altura) / 2
        return real_area


s1 = Circle(7)
s2 = Square(4)
s3 = Triangle(6, 8)

final_circle_area = s1.circle_area()
print(f"Circle area: {final_circle_area}")

final_square_area = s2.square_area()
print(f"Square area: {final_square_area}")

final_triangle_square = s3.triangle_area()
print(f"Triangle area: {final_triangle_square}")