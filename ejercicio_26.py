class Passenger:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
        

class Flight: 
    def __init__(self, flight_number, capacity, passengers):
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = passengers
        
    def book(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return f"{passenger} booked on Flight {self.flight_number}."
        else: return f"Sorry, Flight {self.flight_number} is fully booked."
        
f1 = Flight("AI202", 2, [])
p1 = Passenger("Alice")
p2 = Passenger("Bob")
p3 = Passenger("Juan")
print(f1.book(p1))
print(f1.book(p2))
print(f1.book(p3))