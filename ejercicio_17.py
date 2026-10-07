
class Employee:
    def __init__(self, empleado):
        self.empleado = empleado

class FulltimeEmployee(Employee):
    def __init__(self, empleado, salarioAnual):
        super().__init__(empleado)
        self.salarioAnual = salarioAnual

    def calculate_pay(self):
        return self.salarioAnual / 12


class PartTimeEmployee(Employee):
    def __init__(self, empleado, pagoPorHora, horasTrabajadas):
        super().__init__(empleado)
        self.pagoHora = pagoPorHora
        self.horasTrabajadas = horasTrabajadas

    def calculate_pay(self):
        return self.pagoHora * self.horasTrabajadas



empleado1 = FulltimeEmployee("Alice", 60000)
print(f'{empleado1.empleado} pago mensual {empleado1.calculate_pay()}')

empleado2 = PartTimeEmployee("Bob", 500, 20)
print(f'{empleado2.empleado} pago mensual {empleado2.calculate_pay()}')