class Vehicle:
    def __init__(self, nombre, max_speed, mileage):
        self.nombre = nombre
        self.max_speed = max_speed
        self.mileage = mileage
        

vehicle1 = Vehicle("Tesla Model S", 250, 18)

print(f"Vehicle Name: {vehicle1.nombre}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage} ")