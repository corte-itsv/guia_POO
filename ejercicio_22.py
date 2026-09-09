class Dog:
    pass

class Cat:
    pass

class Vehicle:
    pass

d = Dog()
c = Cat()
v = Vehicle()
objects = {"d": d, "c": c, "v": v}



for name, obj in objects.items():
    print(f"{name} is of type: {type(obj).__name__}")