class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        print(f"{self.name} seating capacity is: {capacity}")

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)

bus = Bus("School Bus", 120)
bus.seating_capacity()