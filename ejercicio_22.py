class Dog:
    pass

class Cat:
    pass

class Vehicle:
    pass

d = Dog()
c = Cat()
v = Vehicle()

objetos = {
"d": d,
"c": c,
"v": v}

for name, objeto in objetos.items():
    print(f"{name} is of type: {type(objeto).__name__}")