class Passanger:
    def __init__(self, name):
        self.name = name
        
class Fligth:
    def __init__(self, flight_name, capacity):
        self.flight_name = flight_name
        self.capacity = capacity
        
    def gestionar(self, pasajero):
        if self.capacity == 2 or self.capacity == 1:
            self.capacity -= 1
            return f"{pasajero.name} booked on Flight {self.flight_name}"
        else:
            return f"Sorry, Flight {self.flight_name} is fully booked."
        
p1 = Passanger("Alice")
p2 = Passanger("Bob")
p3 = Passanger("Gorge")

f1 = Fligth("AI202", 2)

print(f1.gestionar(p1))
print(f1.gestionar(p2))
print(f1.gestionar(p3))