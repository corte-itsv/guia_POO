class Passenger:
    def __init__(self, nombre):
        self.nombre = nombre

class Flight:
    cant_pasajeros = 0
    def __init__(self, nombre, capacidadvuelo):
        self.pasajeros = []
        self.nombre = nombre
        self.capacidadvuelo = capacidadvuelo

    def reserva(self, pasajero):
        self.pasajero = pasajero
        if len(self.pasajeros) >= self.capacidadvuelo:
            print(f"Sorry, Flight {self.nombre} is fully booked.")
        else:
            self.pasajeros.append(self.pasajero)
            print(f"{pasajero.nombre} booked on Flight {self.nombre}.")
        

a = Passenger("Alicia")
b = Passenger("Bob")
c = Passenger("Victor")

f = Flight("AI202", 2)

f.reserva(a)
f.reserva(b)
f.reserva(c)