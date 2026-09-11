class Vehicle:
    def __init__(self, name, base_fare):
        self.name=name
        self.base_fare=base_fare

class Taxi(Vehicle):
    def __init__(self, name, base_fare):
        super().__init__(name, base_fare)
        self.maintenance_fee = base_fare * 0.10
    def tarifa(self):
        tarifa=self.base_fare+self.maintenance_fee
        print(f"Total fare with maintenance fee {tarifa}")

taxi=Taxi("Taxi", 500)
taxi.tarifa()