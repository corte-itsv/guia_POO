class vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")
class bus(vehicle):
    pass

bus1 = bus("School Bus", 120)
bus1.display()