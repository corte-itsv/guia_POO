class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = vehicle("Tesla Model S", 250, 18)
print(f"vehicle model: {vehicle1.name}, speed: {vehicle1.max_speed}, mileage: {vehicle1.mileage}")