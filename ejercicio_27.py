class animal:
    def eat(self):
        return "eating"

class lion(animal): 
    def eat(self):
        return "Lion eats meat"

class elephant(animal):
    def eat(self):
        return "Elephant eats grass"

class parrot(animal):
    def eat(self):
        return "Parrot eats seeds"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self):
        for animal in self.animals:
            print(animal.eat())

zoo = Zoo()
zoo.add_animal(lion())
zoo.add_animal(elephant())
zoo.add_animal(parrot())

zoo.feed_all()