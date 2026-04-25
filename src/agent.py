from retriever import retrieve_songs


def generate_recommendations(user_query):
    retrieved_songs = retrieve_songs(user_query)

    clean_requested = (
        "not explicit" in user_query.lower()
        or "clean" in user_query.lower()
        or "family friendly" in user_query.lower()
    )

    if not retrieved_songs:
        return {
            "recommendations": [],
            "message": (
                "I couldn't find strong matches in the music database. "
                "Try adding a genre, mood, artist, or activity."
            ),
            "confidence": 0.2
        }

    recommendations = []

    for song in retrieved_songs:
        if clean_requested and song["explicit"]:
            continue

        reason = (
            f"{song['title']} by {song['artist']} fits because it matches "
            f"the {song['mood']} mood and {song['genre']} genre."
        )

        recommendations.append({
            "title": song["title"],
            "artist": song["artist"],
            "reason": reason,
            "explicit": song["explicit"]
        })

    if not recommendations:
        return {
            "recommendations": [],
            "message": (
                "I couldn't find clean matches for your request. "
                "Try broadening your search, such as using a different genre or mood, "
                "or allow explicit songs for more options."
            ),
            "confidence": 0.3
        }

    confidence = min(0.95, 0.5 + (0.15 * len(recommendations)))

    return {
        "recommendations": recommendations,
        "message": (
            "Here are AI-assisted music recommendations based on retrieved song data "
            "and your constraints."
        ),
        "confidence": round(confidence, 2)
    }