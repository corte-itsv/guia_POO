
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

print(f"{v1.name} - Color: {v1.color}, speed: {v1.max_speed}")
print(f"{v2.name} - Color: {v2.color}, speed: {v2.max_speed}")

Vehicle.color = "Red"

print(f"{v1.name} - Color: {v1.color}, speed: {v1.max_speed}")
print(f"{v2.name} - Color: {v2.color}, speed: {v2.max_speed}")