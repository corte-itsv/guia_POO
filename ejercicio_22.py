class dog:
    pass
class cat:
    pass
class Vehicle:
    pass

d = dog()
c = cat()
v = Vehicle()

lista = {"d": d, "c": c, "v": v}

for nombre, obj in lista.items():
    print(f"{nombre} is of type: {type(obj).__name__}")