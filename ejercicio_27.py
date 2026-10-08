class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        return f"{self.name} eats ."

class Lion(Animal):
    def eat(self):
        return f"{self.name} eats meat."

class Elephant(Animal):
    def eat(self):
        return f"{self.name} eats grass."

class Parrot(Animal):
    def eat(self):
        return f"{self.name} eats seeds."

class Zoo:
    def __init__(self):
        self.lista = []
        
    def add_animal(self, animal):
        self.lista.append(animal)
        
    def feed_all(self):
        for i in self.lista:
            print(i.eat())


a1 = Lion("Lion")
a2 = Elephant("Elephant")
a3 = Parrot("Parrot")

z1 = Zoo()

z1.add_animal(a1)
z1.add_animal(a2)
z1.add_animal(a3)

z1. feed_all()