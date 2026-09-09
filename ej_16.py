class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

Perro = Dog()
Gato = Cat()

print(f"Dog says: {Perro.speak()}")
print(f"Cat says: {Gato.speak()}")
