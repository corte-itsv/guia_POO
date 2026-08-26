class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        return f"{self.name} seating capacity is: {capacity}"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


bus = Bus("School Bus", 120)

print(bus.seating_capacity())