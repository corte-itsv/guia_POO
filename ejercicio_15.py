class Vehicle:
    def __init__(self, tarifa_base):
        self.tarifa_base = tarifa_base

class Taxi(Vehicle):
    def __init__(self, tarifa_base):
        super().__init__(tarifa_base)
        self.tarifa_mantenimiento = tarifa_base * 0.10

    def tarifa_total(self):
        return self.tarifa_base + self.tarifa_mantenimiento

taxi = Taxi(500)
print("Total fare with maintenance fee:", taxi.tarifa_total())