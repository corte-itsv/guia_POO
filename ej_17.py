class Employee:
    def __init__(self, name):
        self.name = name

    def calcularpago(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, name, sal_anual):
        super().__init__(name)
        self.sal_anual = sal_anual

    def calcularpago(self):
        pago = (self.sal_anual / 12)
        return pago

class PartTimeEmployee(Employee):
    def __init__(self, name, salxhora, horas):
        super().__init__(name)
        self.salxhora = salxhora
        self.horas = horas

    def calcularpago(self):
        pago = self.salxhora * self.horas
        return pago

a = FullTimeEmployee("Alice", 60000)
b = PartTimeEmployee("Bob", 500, 20)

print(f"{a.name}'s monthly pay: {a.calcularpago()}")
print(f"{b.name}'s monthly pay: {b.calcularpago()}")