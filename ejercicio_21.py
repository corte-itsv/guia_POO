class Vehicle:
    def describe(self):
        print(f"{self.__class__.__name__} max speed: {self.max_speed} km/h")
class Bike(Vehicle):
    max_speed = 120
class Truck(Vehicle):
    max_speed = 90
class Bus(Vehicle):
    max_speed = 100
bike = Bike()
truck = Truck()
bus = Bus()
bike.describe()
truck.describe()
bus.describe()