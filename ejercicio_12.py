class Vehicle:
    color = "White"

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def show_info(self):
        print(f"{self.name} - Color: {Vehicle.color}, Speed: {self.max_speed}")



v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

v1.show_info()
v2.show_info()

Vehicle.color = "Red"

v1.show_info()
v2.show_info()
