class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length*self.width
        return area

    def perimetro(self):
        perimetro = (self.length+self.width)*2
        return perimetro

rect = Rectangle(10, 4)
print(f"Area = {rect.area()}")
print(f"Perimeter = {rect.perimetro()}")