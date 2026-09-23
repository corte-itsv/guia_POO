class Vehicle:
    def __init__(self ,base_fare):
        self.base_fare = base_fare

    def tarifa(self):
        return " Total fare with maintenance fee: " + str(self.base_fare)

class Taxi(Vehicle):
    def tarifa(self):
       self.base_fare = self.base_fare * 1.10
       return super().tarifa()

if __name__ == "__main__":
    tax = Taxi(base_fare = 500)
    print(tax.tarifa())