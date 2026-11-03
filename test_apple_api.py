from apple_api import AppleMusicApi
import pytest
import requests


def test_api_responds_ok():
    response = requests.get(
        AppleMusicApi.url,
        params={"term": "Get Lucky", "media": "music", "entity": "song"},
        timeout=10
    )
    assert response.status_code == 200

def test_search_song_returns_track_name():
    assert AppleMusicApi().search_song("Get Lucky") == "Get Lucky"

def test_search_song_not_found():
    with pytest.raises(ValueError):
        AppleMusicApi().search_song("xqzjwkvplmtrbn")
