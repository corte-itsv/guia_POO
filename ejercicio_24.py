class Vector:
    def __init__(self, f, s):
        self.f = f
        self.s = s
        
    def __str__(self):
        return f"Vector({self.f},{self.s})"
        
    def __add__(self, other):
        return Vector(self.f + other.f, self.s + other.s)
    

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2

print(v3)