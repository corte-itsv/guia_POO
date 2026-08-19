## Ejercicio 3: Clase Rectangle con área y perímetro

##**Pista:**
##- Almacena `length` y `width` como atributos de instancia dentro de `__init__`.
##- Define `area(self)` que retorne `self.length * self.width`.
##- Define `perimeter(self)` que retorne `2 * (self.length + self.width)`.

class rectangle():
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width
    def perimeter(self):
        return self.lenght*2 + self.width*2

rect = rectangle(10,4)
print(f"`Area = {rect.area()}` y `Perimeter = {rect.perimeter()}`")        

