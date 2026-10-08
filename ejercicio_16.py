class Animal:
    def speak(self):
        sound = "Hola!"
        return sound
    
class Dog(Animal):
    def speak(self):
        sound = "Woof!"
        return sound
    
class Cat(Animal):
    def speak(self):
        sound = "Meow!"
        return sound

perro = Dog()
gato = Cat()

sonido_de_perro = perro.speak()
sonido_de_gato = gato.speak()

print(f"Dog says: {sonido_de_perro}")
print(f"Cat says: {sonido_de_gato}")

