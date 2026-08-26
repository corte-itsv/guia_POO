"""Escribe un programa en Python para crear una clase padre `Vehicle` con atributos `name` y `max_speed` 
y un método `display()`. Luego crea una clase hija `Bus` que herede todo de `Vehicle` 
sin agregar nada nuevo, y confirma que una instancia de `Bus` puede acceder al método 
del padre.bus1 = Bus("School Bus", 120)"""

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

class Bus(Vehicle):
    pass
    
bus1 = Bus("School Bus", 120)

bus1.display()

# Salida -> Vehicle: School Bus, Max Speed: 120 km/h