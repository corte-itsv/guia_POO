class  Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def average(self):
        prom_alumno = 0
        suma_total = 0
        for nota in self.marks:
            suma_total = suma_total + nota
        prom_alumno = suma_total / len(self.marks)
        return prom_alumno

s1 = Student("Alice", [85, 90, 78, 92, 88])
promedio = s1.average()
print(f"{s1.name}´s Average Grade: {promedio}")