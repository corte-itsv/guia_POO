class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()

d = Dog()

print("Is d an instance of Dog?", isinstance(d, Dog))
print("Is d an instance of Animal?", isinstance(d, Animal))
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
print("Is Animal a subclass of Dog?", issubclass(Animal, Dog))