## Ejercicio 2: Clase Vehicle con atributos de instancia

##**Pista:**
##- Define un método `__init__` que acepte `self`, `name`, `max_speed` y `mileage` como parámetros.
##- Dentro de `__init__`, asigna cada parámetro a `self` para almacenarlos como atributos de instancia.
##- Crea una instancia llamando a `Vehicle(...)` con los argumentos requeridos, y luego accede a los atributos usando notación de punto.

class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")