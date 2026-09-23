class Vehicle:
    def __init__(self , name , max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self ,capacity = None):
        return self.name + "seating capacity is: " + str(capacity)

class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return super().seating_capacity(50)

if __name__ == "__main__":
    bus = Bus("School Bus", 120)
    print(bus.seating_capacity(1))