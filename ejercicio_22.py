class Vehicle:
    pass

class Cat:
    pass

class Dog:
    pass



d = Dog()
c = Cat()
v = Vehicle()

objects = {"d": d, "c": c, "v": v}

for c, v in objects.items():
    print(f"{c} is of type: {type(v).__name__}")
