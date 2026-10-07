import random

class Song:
    def __init__(self, nombre):
        self.nombre = nombre

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregarcancion(self, cancion):
        self.canciones.append(cancion)

    def eliminarcancion(self, titulo):
        for cancion in self.canciones:
            if cancion.nombre == titulo:
                self.canciones.remove(cancion)
        print(f"Removed: {titulo}")

    def mezclar(self):
        random.shuffle(self.canciones)

    def mostrar(self):
        nombres = []
        for cancion in self.canciones:
            nombres.append(cancion.nombre)       
        print(', '.join(nombres))
            

p = Playlist("Playlist")

c1 = Song("Blinding Lights")
c2 = Song("Levitating")
c3 = Song("Peaches")

p.agregarcancion(c1)
p.agregarcancion(c2)
p.agregarcancion(c3)

p.mostrar()
p.eliminarcancion("Levitating")
p.mezclar()
p.mostrar()