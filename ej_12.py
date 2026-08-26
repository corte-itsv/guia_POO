class Vehicle:
    color = 'White'

    def __init__(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad

    def mostrardatos(self):
        print(f"{self.modelo} - Color: {self.color}, Speed: {self.velocidad}")

v1 = Vehicle("Tesla", 250)
v1.mostrardatos()

v2 = Vehicle("BMW", 200)
v2.mostrardatos()