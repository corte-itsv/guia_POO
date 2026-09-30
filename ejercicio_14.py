class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        
    def display(self):
        return f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h"

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return capacity
        
    
class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)
        return self.capacity



bus = Bus("School Bus", 120)
capacidad = bus.seating_capacity()
print(f"{bus.name} seating capacity is: {capacidad}")

