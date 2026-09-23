
import random

class song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, Song):
        self.songs.append(Song)
        return f'Agregada con exito la cancion {Song.name}'

    def remove_song(self, title):
        for song in self.songs:
            if song.name == title:
                self.songs.remove(song)
                return f'Se ha movido con exito la cancion {title} de la playlist'
        return f'No existe la cancion {title}'

    def shuffle(self):
        random.shuffle(self.songs)
        return f'Mezclada con exito'



song1 = song('Sofia', 'Alvaro Solar')
song2 = song('ride', 'twenty one pilots')
song3 = song('stressed out', 'twenty one pilots')
playlist1 = Playlist('Favoritas')
print(playlist1.add_song(song1))
print(playlist1.add_song(song2))
print(playlist1.add_song(song3))
print(playlist1.remove_song('Sofia'))
print(playlist1.shuffle())