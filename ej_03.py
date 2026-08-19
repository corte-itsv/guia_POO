class Rectangle:
    def __init__(self,length, width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimetro(self):
        return 2*(self.width+self.length)

rect = Rectangle(10, 4)
print("Area =" , rect.area())
print("Perimetro=", rect.perimetro())