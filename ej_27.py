class Animal:

    def eat(self):
        return "eating."

class Lion(Animal):

    def eat(self):
        return "Lion eats meat."

class Elephant(Animal):

    def eat(self):
        return "Elephant eats grass."

class Parrot(Animal):

    def eat(self):
        return "Parrot eats seeds."

class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self):
        for animal in self.animals:
            print(animal.eat())


zoo = Zoo()
zoo.add_animal(Lion())
zoo.add_animal(Elephant())
zoo.add_animal(Parrot())
zoo.feed_all()