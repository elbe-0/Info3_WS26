import requests

url = "https://itunes.apple.com/search"

response = requests.get(
    url,
    params={
        "term": "Queen",
        "media": "music",
        "entity": "song",
        "country": "de",
        "limit": 1
    },
    timeout=10
)
print(response)

daten = response.json()

print(daten)

print(daten["results"][0]["trackName"])

