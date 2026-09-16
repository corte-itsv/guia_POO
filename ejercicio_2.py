
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle("Tesla Model S", 250, 18)

print(f"Nombre: {vehicle1.name}, Max_velocidad: {vehicle1.max_speed}, Kilometraje: {vehicle1.mileage}")