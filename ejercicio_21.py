class Vehicle:
    def __init__(self, name):
        self.name = name
        
    def describe(self):
        return f"{self.name} max speed: km/h"
    
class Bike(Vehicle):
    def describe_max_speed(self):
        super().describe()
        max_speed = 120
        return f"{self.name} max speed: {max_speed} km/h"
    
class Truck(Vehicle):
    def describe_max_speed(self):
        super().describe()
        max_speed = 90
        return f"{self.name} max speed: {max_speed} km/h"
    
class Bus(Vehicle):
    def describe_max_speed(self):
        super().describe()
        max_speed = 100
        return f"{self.name} max speed: {max_speed} km/h"
    
v1 = Bike("Bike")
v2 = Truck("Truck")
v3 = Bus("Bus")

bike_max_speed = v1.describe_max_speed()
truck_max_speed = v2.describe_max_speed()
bus_max_speed = v3.describe_max_speed()

print(bike_max_speed)
print(truck_max_speed)
print(bus_max_speed)