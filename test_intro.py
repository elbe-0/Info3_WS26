from playlist import Playlist
import pytest


@pytest.fixture
def intro():
    print("Ich werde ausgeführt")

@pytest.fixture
def playlist():
    print("Playlist wird erstellt")
    p = Playlist()
    yield p
    print("Fixture beendet")

def beispiel():
    print("beispiel")

def test_beispiel(intro):
    print("Test")

def test_assert_intro():
    assert 5 > 3, "Dieser Text wird ausgegeben, wenn der Test rot ist"

def test_can_add_a_song(playlist):
    assert playlist.get_size() == 0
    playlist.add("Get Lucky")
    assert playlist.get_size() == 1

def test_can_add_a_song_expl():
    playlist1 = Playlist()
    assert "Get Lucky" not in playlist1.get_songs()
    playlist1.add("Get Lucky")
    assert "Get Lucky" in playlist1.get_songs()

def test_can_add_song_once():
    playlist1 = Playlist()
    playlist1.add("Get Lucky")
    with pytest.raises(ValueError):
        playlist1.add("Get Lucky")
    assert playlist1.get_size() == 1

def test_can_add_max_5():
    playlist1 = Playlist()
    for i in ["Song1", "Song2","Song3", "Song4", "Song5"]:
        playlist1.add(i)

    with pytest.raises(OverflowError):
        playlist1.add("Song6")
    