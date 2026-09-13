class Vehicle:
    color = "White"
    def __init__(self, nombre, max_speed):
            self.nombre = nombre
            self.max_speed = max_speed
            
    def display(self):
        print(f"Vehicle: {self.nombre}, Max speed: {self.max_speed}km/h")
        
    
class Bus(Vehicle):
    pass

bus1 = Bus("School Bus", 120)

bus1.display()
        