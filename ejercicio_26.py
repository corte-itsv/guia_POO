
class Pasenger:
    def __init__(self, nombre):
        self.nombre = nombre

class flight:
    # count = 0

    def __init__(self, flight, capacidad_avion):
        self.flight = flight
        self.capacidad_avion = capacidad_avion
        self.passengers = []

    def reservar(self, pasajero):
     if len(self.passengers) >= self.capacidad_avion:
        return f'lo siento, el vuelo {self.flight} esta lleno'
     else:
        self.passengers.append(pasajero)
        return f'{pasajero.nombre} se registro en el vuelo {self.flight}'


vuelo1 = flight('AAIOI', 2)
pasajero1 = Pasenger('Jere')
pasajero2 = Pasenger('Pedro')
pasajero3 = Pasenger('Lorenzo')
print(vuelo1.reservar(pasajero1))
print(vuelo1.reservar(pasajero2))
print(vuelo1.reservar(pasajero3))
        




