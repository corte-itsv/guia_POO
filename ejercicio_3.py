class Rectangle:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return 2 * (self.lenght + self.width)

rect = Rectangle(10, 4)

print("Area =", rect.area())
print("Perimeter =", rect.perimeter())


