class Dog:
    def __init__(self):
        pass

class Cat:
    def __init__(self):
        pass

class Vehicle:
    def __init__(self):
        pass

d = Dog()
c = Cat()
v = Vehicle()

l = {"d": d, "c": c, "v": v}

for i, j in l.items():
    print(f"{i} is of type: {type(j).__name__}")