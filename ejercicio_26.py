class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = []

    def book(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} booked on Flight {self.flight_number}.")
        else:
            print(f"Sorry, Flight {self.flight_number} is fully booked.")


flight = Flight("AI202", 2)

alice = Passenger("Alice")
bob = Passenger("Bob")
charlie = Passenger("Charlie")

flight.book(alice)
flight.book(bob)
flight.book(charlie)