class Animal:
    def eat(self):
        pass


class Lion(Animal):
    def eat(self):
        print("Lion eats meat.")


class Elephant(Animal):
    def eat(self):
        print("Elephant eats grass.")


class Parrot(Animal):
    def eat(self):
        print("Parrot eats seeds.")


class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def feed_all(self):
        for animal in self.animals:
            animal.eat()


lion = Lion()
elephant = Elephant()
parrot = Parrot()

zoo = Zoo([lion, elephant, parrot])

zoo.feed_all()