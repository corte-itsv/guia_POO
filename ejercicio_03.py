class rectangle:
    def __init__(self, lenght, widht):
        self.lenght = lenght
        self.widht = widht
    def area(self):
        return self.lenght * self.widht
    def perimeter(self):
        return 2 * (self.lenght + self.widht)

rect = rectangle(10, 4)
print("Area:", rect.area()) 
print("Perimeter:", rect.perimeter())