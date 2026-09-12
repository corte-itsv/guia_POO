class Vehicle:
    color = "White"
    def __init__(self, nombre, max_speed):
            self.nombre = nombre
            self.max_speed = max_speed
            
    def mostrarDatos(self):
        print(f"{self.nombre} - Color: {self.color}, Speed: {self.max_speed}")


v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

v1.mostrarDatos()
v2.mostrarDatos()

Vehicle.color = "Green"

v1.mostrarDatos()
v2.mostrarDatos()
