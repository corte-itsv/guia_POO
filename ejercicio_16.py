class Animal:
    def speak(self):
        return "some sound"

class Dog(Animal):
    def speak(self):
        return "Guau!"

class Cat(Animal):
    def speak(self):
        return "Miau!"

Dog = Dog()
Cat = Cat()

print(f"Dog says: {Dog.speak()}")
print(f"Cat says: {Cat.speak()}")