class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        
    def display(self):
        return f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h"

class Bus(Vehicle):
    pass
    
bus1 = Bus("School Bus", 120)
confirmacion = bus1.display()

print(confirmacion)