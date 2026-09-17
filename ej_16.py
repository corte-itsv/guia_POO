class Animal:
    def speak(self):
        return "algun sonido"

class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")