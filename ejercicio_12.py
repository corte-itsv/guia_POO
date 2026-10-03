class Vehicle:
    color = "White"
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def mostrar(self):
        return (self.name, self.speed)
        
auto1 = Vehicle("Tesla", 250)
auto2 = Vehicle("BMW", 200)
color1 = auto1.color
color2 = auto2.color

nombre, velocidad = auto1.mostrar()
nombre2, velocidad2 = auto2.mostrar()

print(f"{nombre} - Color: {color1}, Speed: {velocidad}")
print(f"{nombre2} - Color: {color2}, Speed: {velocidad2}")


auto1.color = "Red"
auto2.color = "Red"
color1 = auto1.color
color2 = auto2.color

print(f"{nombre} - Color: {color1}, Speed: {velocidad}")
print(f"{nombre2} - Color: {color2}, Speed: {velocidad2}")