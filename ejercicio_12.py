class Vehicle:
    color = "White"

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.model} - {self.color}, speed: {self.max_speed}"

v1 = Vehicle("Tesla", 250)   
v2 = Vehicle("BMW", 200)
print(v1)
print(v2)
Vehicle.color = "red"
print(v1)
print(v2)