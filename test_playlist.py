from playlist import Playlist
import pytest


@pytest.fixture
def playlist():
    print("Playlist wird erstellt")
    p = Playlist()
    yield p

@pytest.fixture
def full_playlist(playlist):
    for i in ["Yesterday", "Imagine", "Smells Like Teen Spirit", "Hotel California", "Wonderwall"]:
        playlist.add(i)
    return playlist

def test_can_add_a_song(playlist):
    assert playlist.get_size() == 0
    playlist.add("Get Lucky")
    assert playlist.get_size() == 1

def test_can_add_a_song_expl():
    playlist1 = Playlist()
    assert "Get Lucky" not in playlist1.get_songs()
    playlist1.add("Get Lucky")
    assert "Get Lucky" in playlist1.get_songs()

@pytest.mark.parametrize("song", [
    "Bohemian Rhapsody",
    "Back In Black"
])


def test_add_different_songs(song):
    playlist = Playlist()
    playlist.add(song)

    assert song in playlist.get_songs()


def test_can_add_song_once():
    playlist1 = Playlist()
    playlist1.add("Get Lucky")
    with pytest.raises(ValueError):
        playlist1.add("Get Lucky")
    assert playlist1.get_size() == 1

def test_can_add_max_5(full_playlist):
    with pytest.raises(OverflowError):
        full_playlist.add("Get Lucky")
    assert full_playlist.get_size() == 5
