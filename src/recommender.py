from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score_song_oop(self, user: UserProfile, song: Song) -> float:
        score = 0.0

        if song.genre == user.favorite_genre:
            score += 2.0

        if song.mood == user.favorite_mood:
            score += 1.0

        energy_similarity = 1 - abs(song.energy - user.target_energy)
        score += max(0.0, energy_similarity) * 2.0

        if user.likes_acoustic:
            score += song.acousticness * 1.0
        else:
            score += (1 - song.acousticness) * 1.0

        return round(score, 3)

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = sorted(
            self.songs,
            key=lambda song: self._score_song_oop(user, song),
            reverse=True
        )
        return scored_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("genre match (+2.0)")

        if song.mood == user.favorite_mood:
            reasons.append("mood match (+1.0)")

        energy_similarity = 1 - abs(song.energy - user.target_energy)
        energy_points = max(0.0, energy_similarity) * 2.0
        reasons.append(f"energy similarity (+{energy_points:.2f})")

        if user.likes_acoustic:
            acoustic_points = song.acousticness
            reasons.append(f"acoustic preference (+{acoustic_points:.2f})")
        else:
            acoustic_points = 1 - song.acousticness
            reasons.append(f"less acoustic preference (+{acoustic_points:.2f})")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = 1 - abs(song["energy"] - user_prefs["energy"])
    energy_points = max(0.0, energy_similarity) * 2.0
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic", False)
    if likes_acoustic:
        acoustic_points = song["acousticness"] * 1.0
        score += acoustic_points
        reasons.append(f"acoustic preference (+{acoustic_points:.2f})")
    else:
        acoustic_points = (1 - song["acousticness"]) * 1.0
        score += acoustic_points
        reasons.append(f"less acoustic preference (+{acoustic_points:.2f})")

    return round(score, 3), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_results.append((song, score, explanation))

    ranked_results = sorted(scored_results, key=lambda x: x[1], reverse=True)
    return ranked_results[:k]