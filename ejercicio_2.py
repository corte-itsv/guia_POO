class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        pass

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print("Vehicle Name: ", vehicle1.name, ", Max Speed: ", vehicle1.max_speed, ", Mileage: ", vehicle1.mileage)
