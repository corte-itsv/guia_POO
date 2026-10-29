class Animal:

    def __init__(self):
        pass
    def speak(self):
        return

class Dog(Animal):

    def __init__(self, ):
        super().__init__()
        
    def speak(self):
        return "Woof!"

class Cat(Animal):
  
    def __init__(self):
        super().__init__()

    def speak(self):
        return "Meow!"

perro = Dog()
gato = Cat()
print("Dog says:", perro.speak())
print("Cat says:", gato.speak())