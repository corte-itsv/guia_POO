class Animal:
    def speak(self):
        pass

class dog(Animal):
    def speak(self):
        return "Woof!"

class cat(Animal):
    def speak(self):
        return "Meow!"

perro = dog()
gato = cat()

print("Dog says: ",perro.speak())
print("Cat says: ",gato.speak())