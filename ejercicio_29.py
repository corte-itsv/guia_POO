import random

class Song:
    def __init__(self, name, artist):
        self.artist = artist
        self.name = name

class Playlist:
    def __init__(self, name):
        self.name = name
        self.lista_canciones = []

    def agregar_cancion(self, cancion):
        self.lista_canciones.append(cancion)

    def eliminar_cancion(self, nombre_cancion):
        cancion_a_eliminar = None
        for s in self.lista_canciones:
            if s.name == nombre_cancion:
                cancion_a_eliminar = s
                break
        
        if cancion_a_eliminar:
            self.lista_canciones.remove(cancion_a_eliminar)
            print(f"Removed: {nombre_cancion}")
        else:
            print(f"{nombre_cancion} not found at {self.name}")

    def shuffle(self):
        random.shuffle(self.lista_canciones)

    def display(self):
        canciones = [s.name for s in self.lista_canciones]
        print(f"Playlist: {', '.join(canciones)}")

playlist = Playlist("My Mix")
playlist.agregar_cancion(Song("Blinding Lights", "The Weeknd"))
playlist.agregar_cancion(Song("Levitating", "Dua Lipa"))
playlist.agregar_cancion(Song("Peaches", "Justin Bieber"))

playlist.display()
playlist.eliminar_cancion("Levitating")
playlist.shuffle()
print("After shuffle:", end=" ")
playlist.display()