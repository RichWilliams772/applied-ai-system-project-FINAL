"""
Command line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs


def print_recommendations(profile_name, user_prefs, songs, k=5):
    print(f"\n{'=' * 60}")
    print(f"Profile: {profile_name}")
    print(f"Preferences: {user_prefs}")
    print(f"{'=' * 60}\n")

    recommendations = recommend_songs(user_prefs, songs, k=k)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "likes_acoustic": False,
        },
        "Edge Case: Sad but High Energy": {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.9,
            "likes_acoustic": False,
        },
    }

    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs, k=5)


if __name__ == "__main__":
    main()

