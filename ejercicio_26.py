class Passenger:
    def __init__(self, name):
        self.name=name

class Flight:
    def __init__(self, code, capacity):
        self.code = code
        self.capacity = capacity
        self.passengers = []

    def reservar(self, passenger):
        if len(self.passengers) >= self.capacity:
            print(f"Sorry, flight {self.code} has full capacity")
        else:
            self.passengers.append(passenger)
            print(f"{passenger.name} booked on flight {self.code}")

vuelo1 = Flight("AI202", 2)
p1 = Passenger("Alice")
p2 = Passenger("Bob")
p3 = Passenger("Lucas")
pasageros = [p1, p2, p3]
for p in pasageros:
    vuelo1.reservar(p)