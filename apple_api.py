import requests


class AppleMusicApi:
    url = "https://itunes.apple.com/search"

    def search_song(self, term: str) -> str:
        response = requests.get(
            self.url,
            params={
                "term": term,
                "media": "music",
                "entity": "song",
                "country": "de",
                "limit": 1
            },
            timeout=10
        )
        results = response.json()["results"]
        if not results:
            raise ValueError("Song nicht gefunden")
        return results[0]["trackName"]
