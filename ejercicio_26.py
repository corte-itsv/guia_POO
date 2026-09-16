class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, vuelo, capacidad):
        self.vuelo = vuelo
        self.capacidad = capacidad
        self.pasajeros = []

    def book(self, pasajeros):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajeros)
            print(f"{pasajeros.name} booked on Flight {self.vuelo}.")
        else:
            print(f"Sorry, Flight {self.vuelo} is fully booked.")


vuelo = Flight("AI202", 2)
vuelo.book(Passenger("Alice"))
vuelo.book(Passenger("Bob"))
vuelo.book(Passenger("Charlie"))