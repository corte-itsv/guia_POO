class Vehicle:
    color="White"
    def __init__(self, nombre, max_velocidad):
        self.nombre=nombre
        self.max_velocidad=max_velocidad
    def mostrar_datos(self):
        print(f"{self.nombre} - Color: {self.color}, Speed: {self.max_velocidad}")
        
v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)
v1.mostrar_datos()
v2.mostrar_datos()