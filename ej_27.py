class Animal:
    def __init__(self, nombre, comida):
        self.nombre = nombre
        self.comida = comida

    def eat(self):
        return f"{self.nombre} eats {self.comida}."

class Zoo:
    def __init__(self):
        self.animales = []

    def anadiranimal(self, animal):
        self.animales.append(animal)

    def feed_all(self):
        for i in self.animales:
            print(i.eat())

l = Animal("Lion", "meat")
e = Animal("Elephant", "grass")
p = Animal("Parrot", "seeds")

z = Zoo()

z.anadiranimal(l)
z.anadiranimal(e)
z.anadiranimal(p)

z.feed_all()