import random 

class Song:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        print(self.name)
        
    def __repr__(self):
        print(self.name)
        
class Playlist:
    def __init__(self, name):
        self.name = name
        self.lista = []
        
    def add_song(self, cancion):
        self.lista.append(cancion)
    
    def show_playlist(self):
        nombres = []
        for i in self.lista:
            nombres.append(i.name)
        print(", ".join(nombres))
    
    def remove_song(self, song):
        for i in self.lista:
            if song == i.name:
                self.lista.remove(i)
                print(f"Removed: {i.name}")
                
    def shuffle(self):
        return random.shuffle(self.lista)
     
s1 = Song("Blinding Lights")
s2 = Song("Levitating")
s3 = Song("Peaches")

p1 = Playlist("Playlist")
p1.add_song(s1)
p1.add_song(s2)
p1.add_song(s3)

p1.show_playlist()
p1.remove_song("Levitating")
p1.show_playlist()
print(f"After shuflle: (order will vary)")
p1.shuffle()
p1.show_playlist()