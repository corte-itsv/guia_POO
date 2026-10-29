import random

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, title):
        original_count = len(self.songs)
        self.songs = [s for s in self.songs if s.title != title]
        if len(self.songs) < original_count:
            print(f"Removed: {title}")
        else:
            print(f"Song '{title}' not found in playlist.")

    def shuffle(self):
        random.shuffle(self.songs)

    def display(self):
        titles = [s.title for s in self.songs]
        print(f"Playlist: {', '.join(titles)}")


playlist = Playlist("My Mix")
playlist.add_song(Song("Blinding Lights", "The Weeknd"))
playlist.add_song(Song("Levitating", "Dua Lipa"))
playlist.add_song(Song("Peaches", "Justin Bieber"))

playlist.display()
playlist.remove_song("Levitating")
playlist.shuffle()
print("After shuffle:", end=" ")
playlist.display()