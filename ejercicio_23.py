class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(f"Is d an instance of Dog? {isinstance(d, Dog)}")
print(f"Is d an instance of Animal? {isinstance(d, Animal)}")
print(f"Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")
print(f"Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")