class Vehicle:
    color = "white"
    def __init__(self, marca, max_speed):
        self.marca = marca
        self.max_speed = max_speed
    
v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

print(f"{v1.marca} - Color: {v1.color}, Speed: {v1.max_speed}")
print(f"{v2.marca} - Color: {v2.color}, Speed: {v2.max_speed}")

Vehicle.color = "Red"

print(f"{v1.marca} - Color: {v1.color}, Speed: {v1.max_speed}")
print(f"{v2.marca} - Color: {v2.color}, Speed: {v2.max_speed}")