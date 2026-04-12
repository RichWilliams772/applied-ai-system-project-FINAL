from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """Represent a song and its audio/content features."""
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
    """Represent a user's music taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Provide object-oriented recommendation behavior for songs."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score_song_oop(self, user: UserProfile, song: Song) -> float:
        """Compute weighted score with energy emphasized."""
        score = 0.0

        # ↓ LOWER GENRE WEIGHT
        if song.genre == user.favorite_genre:
            score += 1.0

        # SAME MOOD WEIGHT
        if song.mood == user.favorite_mood:
            score += 1.0

        # ↑ HIGHER ENERGY IMPORTANCE
        energy_similarity = 1 - abs(song.energy - user.target_energy)
        score += max(0.0, energy_similarity) * 4.0

        # acoustic preference
        if user.likes_acoustic:
            score += song.acousticness
        else:
            score += (1 - song.acousticness)

        return round(score, 3)

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return top k recommended songs for a user."""
        scored_songs = sorted(
            self.songs,
            key=lambda song: self._score_song_oop(user, song),
            reverse=True
        )
        return scored_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate explanation for weight-shifted scoring."""
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("genre match (+1.0)")

        if song.mood == user.favorite_mood:
            reasons.append("mood match (+1.0)")

        energy_similarity = 1 - abs(song.energy - user.target_energy)
        energy_points = max(0.0, energy_similarity) * 4.0
        reasons.append(f"energy similarity (+{energy_points:.2f})")

        if user.likes_acoustic:
            acoustic_points = song.acousticness
            reasons.append(f"acoustic preference (+{acoustic_points:.2f})")
        else:
            acoustic_points = 1 - song.acousticness
            reasons.append(f"less acoustic preference (+{acoustic_points:.2f})")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV into dictionaries."""
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append({
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
            })

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score song with energy-heavy weighting."""
    score = 0.0
    reasons = []

    # ↓ LOWER GENRE WEIGHT
    if song["genre"] == user_prefs["genre"]:
        score += 1.0
        reasons.append("genre match (+1.0)")

    # SAME MOOD
    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # ↑ ENERGY DOMINATES
    energy_similarity = 1 - abs(song["energy"] - user_prefs["energy"])
    energy_points = max(0.0, energy_similarity) * 4.0
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # acoustic
    if user_prefs.get("likes_acoustic", False):
        acoustic_points = song["acousticness"]
        score += acoustic_points
        reasons.append(f"acoustic preference (+{acoustic_points:.2f})")
    else:
        acoustic_points = 1 - song["acousticness"]
        score += acoustic_points
        reasons.append(f"less acoustic preference (+{acoustic_points:.2f})")

    return round(score, 3), reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Return top k ranked songs using new weights."""
    scored_results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_results.append((song, score, explanation))

    ranked_results = sorted(scored_results, key=lambda x: x[1], reverse=True)
    return ranked_results[:k]