class shape:
    def area():
        pass

class circle:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(3.1416 * self.radio ** 2, 2)

class square:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class triangle:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

formas = [circle(7), square(4), triangle(6, 8)]
for i in formas:
    print(f"{type(i).__name__} area: {i.area()}")