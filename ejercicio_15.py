class Vehicle():
    def __init__(self, tarifa_base):
        self.tarifa_base = tarifa_base
        
class Taxi(Vehicle):
    def final_fare(self):
        tarifa_final = self.tarifa_base + (self.tarifa_base * 0.1)
        return tarifa_final


taxi = Taxi(500)
tarifa_final = taxi.final_fare()
print(f"Total fare with maintenance fee: {tarifa_final}")