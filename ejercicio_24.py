class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)


v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2

print(f"Vector({v3.x}, {v3.y})")