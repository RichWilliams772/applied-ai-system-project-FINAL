import json

def load_data():
    with open("data/music_data.json", "r") as f:
        return json.load(f)

def retrieve_songs(query):
    data = load_data()
    query = query.lower()

    results = []

    for song in data:
        if (
            song["genre"] in query
            or song["mood"] in query
            or song["artist"].lower() in query
        ):
            results.append(song)

    return results