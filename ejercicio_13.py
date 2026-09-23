class Vehicle:
    def __init__(self , name , max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        return  "  Vehicle : " + self.name + " Max Speed: " + str(self.max_speed)

class Bus(Vehicle):
    pass


if __name__ ==  "__main__":
    bus1 = Bus("School Bus", 120)
    print(bus1.display())
