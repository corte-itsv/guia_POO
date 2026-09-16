class Employee:
    def __init__(self, nombre):
         self.nombre = nombre

    def calculo(self, nombre):
         pass

class FullTimeEmployee(Employee):
    def __init__(self, nombre, monto):
        super().__init__(nombre)
        self.monto = monto

    def calculo(self):
        return self.monto / 12
                


class PartTimeEmployee(Employee):
    def __init__(self, nombre, rate, horas):
            super().__init__(nombre)
            self.rate = rate
            self.horas = horas

    def calculo(self):
         return self.rate * self.horas
full = FullTimeEmployee("Alice", 60000)
part = PartTimeEmployee("Bob", 500, 20)
print (f"{full.nombre}'s monthly pay: {full.calculo()}")
print (f"{part.nombre}'s monthly pay: {part.calculo()}")