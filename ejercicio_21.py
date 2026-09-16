class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def describe(self):
        print(f"{type(self).__name__} max speed: {self.max_speed} km/h")

class Bike(Vehicle):
    def __init__(self):
        super().__init__(120)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(90)

class Bus(Vehicle):
    def __init__(self):
        super().__init__(100)

lista = [Bike(), Truck(), Bus()]
for i in lista:
    i.describe()