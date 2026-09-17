class Dog:
    pass

class Cat:
    pass

class Vehicle:
    pass

d=Dog()
c=Cat()
v=Vehicle()
dict_obj={"d":d, "c":c, "v": v}
for nombre, obj in dict_obj.items():
    print(f"{nombre} is of type:{type(obj).__name__}")