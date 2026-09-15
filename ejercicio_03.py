

class Rectangle:
    def __init__(self, lenght, witdh):
        self.lenght = lenght
        self.width = witdh

    def area(self):
        return self.lenght * self.width

    def perimetro(self):
        return 2 * (self.lenght + self.width)


rect1 = Rectangle(10, 4)

print(f'Area: {rect1.area()}')
print(f'perimetro: {rect1.perimetro()}')