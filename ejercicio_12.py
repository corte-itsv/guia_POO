class Vehicle:
    color = "White"  

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def mostrar(self):
        print(f"{self.name} - Color: {self.color}, Speed: {self.speed}")

v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

v1.mostrar()
v2.mostrar()

Vehicle.color = "Red"
v1.mostrar()
v2.mostrar()         