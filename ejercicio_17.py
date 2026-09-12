class Employee:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def calcular_pago(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, nombre, pago_anual):
        super().__init__(nombre)
        self.pago_anual = pago_anual
    
    def calcular_pago(self):
        pago = self.pago_anual / 12
        return pago

class PartTimeEmployee(Employee):
    def __init__(self, nombre, pago_por_hora, horas_semanales):
        super().__init__(nombre)
        self.pago_por_hora = pago_por_hora
        self.horas_semanales = horas_semanales
        
    def calcular_pago(self):
        pago = self.pago_por_hora * self.horas_semanales
        return pago
    
    

p1 = FullTimeEmployee("Alice", 60000)
p2 = PartTimeEmployee("Bob", 500, 20)

print(f"{p1.nombre}'s monthly pay: {p1.calcular_pago()}")
print(f"{p2.nombre}'s monthly pay: {p2.calcular_pago()}")


