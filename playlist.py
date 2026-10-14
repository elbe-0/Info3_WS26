from typing import List


class Playlist:
    def __init__(self) -> None:
        self.songs: List[str] = []

    def add(self, song: str):
        if song in self.get_songs():
            raise ValueError("Song ist bereits in der Playlist")
        elif self.get_size() >= 5:
            raise OverflowError("Die Playliste ist voll")
        else: 
            self.songs.append(song)


    def get_size(self) -> int:
        return len(self.songs)

    def get_songs(self) -> List[str]:
        return self.songs
