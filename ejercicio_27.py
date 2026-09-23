
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def eat(self):
        return f'{self.nombre} esta comiendo'


class carnivoros(Animal):
    def eat(self):
        return f'{self.nombre} esta comiendo carne'

class Herbivoros(Animal):
    def eat(self):
        return f'{self.nombre} esta comiendo hojas'

class Omnivoros(Animal):
    def eat(self):
        return f'{self.nombre} esta comiendo lo que encontro'


class zoo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def add_animal(self, animal):
        self.lista.append(animal)

    def feed_all(self):
        for elemento in self.lista:
            print(elemento.eat())


leon = carnivoros('leon')
elefante = Herbivoros('Elefante')
pajaro = Omnivoros('Pajaro')

zoo1 = zoo('Jeres zoo')
zoo1.add_animal(leon)
zoo1.add_animal(elefante)
zoo1.add_animal(pajaro)
zoo1.feed_all()
