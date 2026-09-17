class Animal:
    def __init__(self):
        pass
    def eat(self):
        pass

class Leon(Animal):
    def __init__(self):
        pass
    def eat(self):
        print("El leon come carne")

class Elefante(Animal):
    def __init__(self):
        pass
    def eat(self):
        print("El elefante come mani")

class Loro(Animal):
    def __init__(self):
        pass
    def eat(self):
        print("El loro come papa")

class Zoo:
    def __init__(self):
        self.lista_animales=[]
    def agregar_animal(self, animal):
        self.lista_animales.append(animal)

    def alimentar_todos(self):
        for a in self.lista_animales:
            a.eat()

zoo = Zoo()
le = Leon()
e = Elefante()
lo= Loro()
animales = [le, e, lo]
for a in animales:
    zoo.agregar_animal(a)

zoo.alimentar_todos()