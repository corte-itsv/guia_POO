class Passenger:
    def __init__(self, name):
        self.name = name

class flight:

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


flight = flight("AI202", 2)
flight.book(Passenger("Alice"))
flight.book(Passenger("Bob"))
flight.book(Passenger("Charlie"))