class Vehicle:
    
    color = "White"

    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
        color = "White"

v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

print(f"{v1.model} - Color: {v1.color}, Speed: {v1.speed}")
print(f"{v2.model} - Color: {v2.color}, Speed: {v2.speed}")

Vehicle.color = "Red"

print(f"{v1.model} - Color: {v1.color}, Speed: {v1.speed}")
print(f"{v2.model} - Color: {v2.color}, Speed: {v2.speed}")
        