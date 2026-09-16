class Animal:
    def eat(self):
        pass

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
        self.animales = []

    def agrega(self, animal):
        self.animales.append(animal)

    def alimentar(self):
        for animal in self.animales:
            print(animal.eat())


zoo = Zoo()
zoo.agrega(Lion())
zoo.agrega(Elephant())
zoo.agrega(Parrot())

zoo.alimentar()