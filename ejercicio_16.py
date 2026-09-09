class Animal:
    def speak(self):
        return "sonido"

class Dog(Animal):
     def speak(self):
            return "Woof!"

class Cat(Animal):
     def speak(self):
            return "Meow!"

gato = Cat()
perro = Dog()

print(f"Dog says: {perro.speak()}")
print(f"Cat says: {gato.speak()}")


