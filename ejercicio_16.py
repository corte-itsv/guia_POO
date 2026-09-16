class animal:
    def speak(self):
        return "Some sound"

class dog(animal):
    def speak(self):
        return "Woof!"

class cat(animal):
    def speak(self):
        return "Meow!"

dog = dog()
cat = cat()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())
