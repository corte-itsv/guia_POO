class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        base_fare = 500
        
    def calculate_total_fare(self):
        maintenance_fee = self.base_fare * 0.10
        return self.base_fare + maintenance_fee

base_fare = 500

my_taxi = Taxi(base_fare)
total_fare = my_taxi.calculate_total_fare()

print(f"Total fare with maintenance fee: {total_fare}")