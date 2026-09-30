class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(f"Is d instance of Dog: {isinstance(d, Dog)}")
print(f"Is d instance of Aniaml: {isinstance(d, Animal)}")
print(f"Is Dog a subclass of Animal: {issubclass(Dog, Animal)}")
print(f"Is Animal a subclass of Dog: {issubclass(Animal, Dog)}")