class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        res = self.length * self.width
        return res
    
    def perimeter(self):
        res = (self.length * 2) + (self.width)
        return res

rect = Rectangle(10, 4)
rect.area()
rect.perimeter()
print(f"El área de la figura es: {rect.area()}")
print(f"El perímetro de la figura es: {rect.perimeter()}")