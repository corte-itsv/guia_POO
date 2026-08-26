class Vehicle:
    color = "White"

    def __init__(self, marca, speed):
        self.marca = marca
        self.speed = speed

    def mostrar(self):
        print(f"{self.marca} - Color: {self.color}, Speed: {self.speed}")


v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

v1.mostrar()
v2.mostrar()

Vehicle.color = "Red"

v1.mostrar()
v2.mostrar()