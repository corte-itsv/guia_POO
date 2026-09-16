class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self): 
        return self.length * 2 + self.width * 2
    
rect = Rectangle(10, 4)
print(f"`Area = {rect.area()}` y `Perimeter = {rect.perimeter()}`")