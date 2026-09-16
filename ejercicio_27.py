class Animal:
    def eat(self):
        return "El animal come"
    
class Lion(Animal):
    def eat(self):
        return "Lion eats meat"
    
class Elephant(Animal):
    def eat(self):
        return "Elephant eats grass"    
    
class Parrot(Animal):
    def eat(self):
        return "Parrot eats seeds"
    
class Zoo:
    def __init__(self):
        self.animales = []
        
    def add_animal(self, animal):
        self.animales.append(animal)
            

        
    def feed_all(self):
        for animal in self.animales:
            print(animal.eat())
            
zoo = Zoo()
zoo.add_animal(Lion())
zoo.add_animal(Elephant())
zoo.add_animal(Parrot())

zoo.feed_all()