import random


class Song:
    def __init__(self, title):
        self.title = title


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                print(f"Removed: {title}")
                return

    def shuffle(self):
        random.shuffle(self.songs)

    def display(self):
        titles = [song.title for song in self.songs]
        print(f"Playlist: {', '.join(titles)}")


playlist = Playlist()

playlist.add_song(Song("Blinding Lights"))
playlist.add_song(Song("Levitating"))
playlist.add_song(Song("Peaches"))

playlist.display()

playlist.remove_song("Levitating")

playlist.shuffle()

print("After shuffle:", end=" ")
playlist.display()