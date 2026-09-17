class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self, otro):
        return Vector(x=self.x+otro.x, y=self.y+otro.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3=v1+v2
print(v3)