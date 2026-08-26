class Vehicle:
    def __init__(self, name, max_speed, milege,):
        self.max_speed = max_speed
        self.milege = milege
        self.name = name

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, {vehicle1.milege}")