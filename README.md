# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:
This project builds a simple content-based music recommender system that suggests songs based on a user’s personal taste profile. Songs are represented using features such as genre, mood, energy, tempo, valence, danceability, and acousticness, while the user is represented by preferred values for those same features. The system compares each song to the user’s preferences and assigns a weighted score based on how closely they match.

The recommender then ranks all songs from highest to lowest score and returns the top results as recommendations. Through this process, the project demonstrates how raw data can be transformed into personalized predictions using a clear and interpretable scoring system.

This simulation reflects how real-world AI recommenders work by showing how different features and design choices influence results, while also highlighting limitations such as bias, lack of diversity, and the need for human judgment in building effective recommendation systems.

---

## How The System Works

Explain your design in plain language.

This system recommends songs by comparing the features of each song to a user’s taste profile. Each Song in the dataset includes descriptive features such as genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. These features help represent both the style of the song and the overall listening experience it creates. For example, genre and mood describe the type of song, while energy and tempo help capture whether it feels intense, relaxed, upbeat, or calm.

The UserProfile stores the user’s preferences in a similar format. It includes the user’s favorite genre and mood, along with target values for numeric features such as energy, tempo, valence, danceability, and acousticness. This profile acts as a reference point for the recommender. Instead of asking whether a song is simply “good” or “bad,” the system asks how closely each song matches the user’s preferred sound and vibe.

To compute a score, the Recommender looks at one song at a time and compares it to the user profile. If the song matches the user’s preferred genre, it receives extra points. If it also matches the preferred mood, it earns additional points. For the numeric features, the system gives higher scores to songs whose values are closer to the user’s target values. This means a song with energy or tempo close to the user’s ideal will score higher than one that is very different. All of these points are combined into one total score for that song.

After every song has been scored, the recommender sorts the songs from highest score to lowest score. The songs with the highest scores are chosen as the recommendations because they are the closest overall match to the user’s taste profile.

A simple way to view the flow is:

<img width="533" height="1938" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/84a2e8d6-1a06-44ec-8ee4-43e3d69cd4c0" />


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---
## Output 
<img width="918" height="383" alt="Screenshot 2026-04-12 at 5 49 21 PM" src="https://github.com/user-attachments/assets/ba721ce1-fbd1-4af5-acae-2b4c8f4e3b6f" />

## Experiments You Tried

Several experiments were conducted to understand how different design choices affected the recommendations.

One experiment involved changing the weight of the genre feature. When the genre weight was reduced from 2.0 to 0.5, the recommendations became more flexible and included songs from different genres that still matched the user’s mood and energy. However, this also made the results feel less consistent with the user’s stated preferences. Increasing the genre weight again made the recommendations more focused, but less diverse.

Another experiment tested the impact of adding additional numeric features, such as tempo and valence. When only energy was used, the system sometimes recommended songs that matched intensity but not overall vibe. After adding tempo and valence, the recommendations improved because the system could better capture whether a song felt fast, slow, happy, or emotional. This made the results feel more realistic and aligned with how people experience music.

The system was also tested with different types of user profiles. For a high-energy, upbeat user, the recommender consistently returned pop and electronic songs with strong danceability. For a low-energy, calm user, the system shifted toward lofi, ambient, and acoustic tracks. This showed that the model could adapt to different preferences, although it sometimes overemphasized certain features and produced repetitive results.

Overall, these experiments showed that the recommender is highly sensitive to feature selection and weighting, and small changes can significantly impact both the accuracy and diversity of the recommendations.

---

## Limitations and Risks

Summarize some limitations of your recommender.

This recommender system has several limitations due to its simplicity and small scale. First, it only works on a small dataset of songs, which limits the variety and quality of recommendations. In a real-world system, a much larger catalog would be needed to provide meaningful and diverse suggestions.

The system also relies only on a fixed set of features, such as genre, mood, and numerical attributes like energy or tempo. It does not understand lyrics, language, cultural context, or artist relationships, which are important factors in how people actually choose music. This means it may miss songs that feel similar to the user in more subtle ways.

Another limitation is that it can over-favor certain features, such as genre or high-energy songs, depending on how the scoring weights are set. This can lead to repetitive recommendations and reduce diversity, especially if the system keeps selecting songs that are very similar to each other.

Finally, the system uses a static user profile, meaning it does not adapt over time based on user feedback like likes or skips. As a result, it cannot learn or adjust if the user’s preferences change, which limits its effectiveness compared to real-world recommendation systems.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

Building this recommender showed how systems turn data into predictions by translating both songs and user preferences into comparable features, then using a scoring rule to measure similarity. Instead of “understanding” music the way humans do, the model reduces everything to numbers and categories—like energy, tempo, and mood—and combines them into a single score. I learned that predictions are not random; they are the result of carefully designed rules and weights. Small changes in those rules can significantly impact the output, which highlights how important feature selection and weighting are in shaping recommendations.

This project also made it clear how bias and unfairness can appear even in simple systems. For example, if certain features like genre or energy are weighted more heavily, the system may consistently favor specific types of music while ignoring others. This can lead to filter bubbles, where users are only exposed to a narrow range of content. Additionally, since the model uses a fixed user profile, it assumes all preferences are stable and does not account for changing moods or diverse tastes. In real-world systems, these kinds of biases could limit discovery, disadvantage certain artists or genres, and create an experience that feels less inclusive or personalized.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

RhythmIQ 1.0

---

## 2. Intended Use

This system is designed to recommend songs to a user based on their personal music preferences. It analyzes features such as genre, mood, energy, tempo, and other audio characteristics to identify songs that closely match what the user is likely to enjoy. The goal is to simulate how a basic music recommendation system can transform song data and user preferences into personalized suggestions.

The system is intended for students and learners who are exploring how recommendation systems work, as well as for developers building simple, interpretable models. It is not meant to replace real-world platforms like Spotify, but rather to serve as an educational tool that demonstrates the core ideas behind content-based filtering and scoring algorithms.

---

## 3. How It Works (Short Explanation)

The recommender system decides which songs to suggest by comparing each song’s characteristics to what the user prefers. It looks at several features of each song, including the genre, mood, energy level, tempo (speed), valence (how happy or positive the song feels), danceability, and acousticness (how natural vs. electronic the song sounds).

The system also uses information about the user’s taste profile, such as their favorite genre and mood, along with their preferred levels for energy, tempo, positivity, and other musical qualities. This profile acts as a “target” that the system tries to match.

To score a song, the system first checks for exact matches in category-based features like genre and mood. If a song matches the user’s favorite genre or mood, it earns extra points. Then, for the numerical features like energy or tempo, the system looks at how close the song is to the user’s preferred values. Songs that are closer to the user’s ideal levels receive higher scores, while songs that are very different receive lower scores.

All of these points are combined into a single number that represents how well the song matches the user’s taste. After scoring every song, the system ranks them from highest to lowest score and recommends the top matches to the user.

---

## 4. Data
The dataset in data/songs.csv contains a total of 18 songs. The original file started with 10 songs, and 8 additional songs were added to expand the diversity of the dataset. No songs were removed.

The dataset includes a wide range of genres, such as pop, lofi, rock, ambient, jazz, synthwave, hip-hop, indie, folk, and metal. It also represents a variety of moods, including happy, chill, intense, relaxed, moody, excited, peaceful, confident, calm, and focused. This variety allows the recommender system to distinguish between different musical “vibes,” such as high-energy songs versus calm or relaxing tracks.

Overall, the dataset reflects a broad and balanced range of musical tastes, but it slightly leans toward modern and popular styles like pop, lofi, and electronic music. This means the data somewhat reflects the taste of a listener who enjoys contemporary, mood-based music (such as study playlists, workout songs, and upbeat pop), rather than someone focused on a single niche genre.
---

## 5. Strengths

This recommender works well when the user has clear and consistent preferences, such as a specific genre and mood combination. In these situations, the top recommendations tend to “feel right” because the system directly rewards songs that match those preferences. For example, a user who prefers upbeat pop music with high energy will consistently receive songs that match that vibe.

The system is especially effective for mood-based listening, such as finding songs for studying, working out, or relaxing. Because it uses features like energy, tempo, and valence, it can capture the overall “feel” of a song and recommend tracks that align closely with the user’s desired atmosphere.

Another strength is its simplicity and transparency. The scoring system is easy to understand because each feature contributes a clear number of points. This makes it easy to explain why a song was recommended, which is an advantage compared to more complex systems that act like a “black box.” Users and developers can easily adjust the weights to fine-tune the recommendations.

Overall, the recommender performs best when matching songs with similar characteristics to the user’s preferences, providing consistent and interpretable results.

---

## 6. Limitations and Bias

Where does your recommender struggle

This recommender system has several limitations due to its simple, content-based design. One major issue is that it can over-prioritize certain features, such as genre and energy, depending on how the weights are set. For example, if genre is heavily weighted, the system may ignore songs from other genres that still match the user’s mood or vibe, reducing diversity in recommendations.

The system also assumes that all users have a fixed and consistent taste profile, which is not always realistic. In real life, users often have varied preferences depending on context, such as wanting high-energy music for workouts but calm music for studying. Because this system uses a single static profile, it cannot adapt to different listening situations.

Another limitation is that it may create a filter bubble, repeatedly recommending songs with very similar characteristics. This can prevent users from discovering new genres or styles and may make the recommendations feel repetitive over time.

Additionally, the system may be biased toward certain types of songs, such as high-energy or highly danceable tracks, if those features are weighted more heavily. This could unintentionally disadvantage slower, acoustic, or niche genres, even if they are high-quality or enjoyable.

If used in a real product, these limitations could be unfair because they might limit exposure to diverse music and reinforce narrow listening habits. Users with more complex or evolving tastes may not receive accurate recommendations, and lesser-known artists or genres could be underrepresented in the results.

---

## 7. Evaluation

How did you check your system

The system was evaluated by testing it with multiple different user profiles and observing whether the recommended songs matched the expected “vibe.” For example, profiles with high energy and upbeat moods were expected to return songs with similar characteristics, while profiles focused on calm or relaxed preferences should return lower-energy, slower songs. In most cases, the top-ranked results aligned well with these expectations, indicating that the scoring logic was working as intended.

The results were also compared conceptually to how real platforms like Spotify or YouTube recommend music. Similar to those systems, this recommender prioritized songs that closely matched the user’s preferences in genre, mood, and overall feel. While the simulation is much simpler, it produced recommendations that felt realistic for a content-based approach.

In addition, the scoring logic was checked by reviewing individual song scores to ensure that songs with features closer to the user’s preferences consistently received higher scores than those that were further away. This helped confirm that the similarity calculations were functioning correctly.

Although no formal numeric metric was required, the system effectively measured relevance by assigning higher scores to songs that more closely matched the user profile. This score acts as a proxy for how likely a user is to enjoy a song, allowing the system to rank recommendations accordingly.

---

## 8. Future Work

If you had more time, how would you improve this recommender

If more time were available, this recommender system could be improved in several ways to make it more realistic and effective. One major improvement would be to support multiple user profiles and group recommendations, allowing the system to suggest songs that satisfy more than one person’s preferences at the same time. This would better reflect real-world use cases like shared playlists or social listening.

Another important enhancement would be to increase diversity in recommendations. Currently, the system focuses on finding the closest matches, which can lead to repetitive results. Adding a diversity mechanism would allow the recommender to include songs that are slightly different from the user’s preferences, helping users discover new genres or styles while still maintaining relevance.

The system could also be improved by incorporating additional features, such as lyrical themes, artist similarity, or listening context (e.g., time of day or activity). This would allow for more nuanced recommendations that better reflect how people actually choose music.

Finally, a more advanced version could include learning from user feedback, such as likes, skips, or repeated plays. This would allow the system to update the user profile dynamically over time, rather than relying on a fixed set of preferences, making the recommendations more personalized and adaptive.

---

## 9. Personal Reflection

A few sentences about what you learned:

One thing that surprised me was how much the recommendations depended on the weights and feature choices. Small changes in how much importance was given to genre or energy could completely change the top results. This showed that even a simple system can behave very differently depending on how it is designed.

Building this system changed how I think about real music recommenders by making me realize that they are not just “guessing” what users like, but are carefully combining many signals and tradeoffs. Even though my model is simple, it helped me understand how real platforms might balance factors like similarity, diversity, and user behavior at a much larger scale.

I also realized that human judgment still matters in deciding what features to use, how to weight them, and how to define a “good” recommendation. Even if a model seems smart, it can still miss context, such as when a user’s mood changes or when they want to explore something new. Humans are still needed to design systems that feel intuitive, fair, and enjoyable to use.

