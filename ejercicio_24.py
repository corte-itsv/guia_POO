class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, otro):
        Xt = self.x + otro.x
        Yt = self.y + otro.y
        return (Xt, Yt)
        
v1 = Vector(2, 3)
v2 = Vector(4, 1)

Xt, Yt = v1 + v2
print(f"Vector({Xt}, {Yt})")