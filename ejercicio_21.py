
class Vehicle:
    def __init__(self, max_speed):
        self.maxSpeed = max_speed
        self.nombre = 'Vehicle'

    def describe(self):
        return f'{self.nombre} max speed: {self.maxSpeed} km/h'


class Bike(Vehicle):
    def __init__(self):
        super().__init__(120)
        self.nombre = 'Bike'

class Truck(Vehicle):
    def __init__(self):
        super().__init__(90)
        self.nombre = 'trcuk'

class Bus(Vehicle):
    def __init__(self):
        super().__init__(100)
        self.nombre = 'bus'



bike = Bike()
print(bike.describe())
truck = Truck()
print(truck.describe())
bus = Bus()
print(bus.describe())