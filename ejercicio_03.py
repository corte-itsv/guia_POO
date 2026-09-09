class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimetro =  2 * (self.length + self.width)
        return perimetro

rect = Rectangle(10, 4)
print(f"Area: {rect.area()} y Perimetro: {rect.perimeter()}")

