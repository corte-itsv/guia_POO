class Dog:
    pass

class Cat:
    pass

class Vehicle:
    pass


d = Dog()
c = Cat()
v = Vehicle()

object = {"d": d, "c": c, "v": v}

for nombre, object in object.items():
    print(f"{nombre} is of type: {type(object).__name__}")