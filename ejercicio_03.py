class rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return 2 * (self.lenght + self.width)
    
rect = rectangle(10, 4)
print("Area = ",rect.area())
print("Perimeter = ",rect.perimeter())
