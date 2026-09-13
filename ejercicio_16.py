class Animal:
    def speak(self):
        return "qsy"
    
class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Miau"
    
cat = Cat()
dog = Dog()
    
print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")
