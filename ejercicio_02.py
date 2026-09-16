class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Vehicle1 = Vehicle("Tesla Model S", 200, 18)
print(f"Vehicle Name: {Vehicle1.name}, Max Speed: {Vehicle1.max_speed}, Mileage: {Vehicle1.mileage}")