class Employee:

    def __init__(self, name):
        self.name = name
    
class Full_time(Employee):

    def __init__(self, name, monto):
        self.monto = monto
        super().__init__(name)

    def calcular_salario(self):
        return f"{self.name}'s monthly pay: {self.monto / 12}"

class Part_time(Employee):

    def __init__(self,name , monto, horas):
        self.monto = monto
        self.horas = horas
        super().__init__(name)

    def calcular_salario(self):
        return f"{self.name}'s monthly pay: {self.monto * self.horas}"


bo = Part_time("Bob", 500, 20)
ali = Full_time("Alice", 60000)
print(ali.calcular_salario())
print(bo.calcular_salario())
