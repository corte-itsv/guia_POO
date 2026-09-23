## Ejercicio 4: Clase Student con promedio de notas

##**Pista:**
##- Acepta `name` y `marks` (una lista) en el método `__init__` y asígnalos a `self`.
##- En el método `average()`, usa `sum(self.marks) / len(self.marks)` para calcular la media.
##- Usa `round()` si quieres controlar la cantidad de decimales en la salida.

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
        

s1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"Alice's Average Grade: {s1.average()}")