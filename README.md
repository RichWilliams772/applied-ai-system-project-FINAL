# 🎵 AI Music Discovery & Insight System
## Loom Demo

Watch the full system walkthrough here:  

https://www.loom.com/share/19458ac3aef345a2bf3bd5d4d3075de1

## Project Summary

This project extends my original Music Recommender Simulation into a full applied AI system.

The original project built a simple content-based recommender that suggested songs based on a user’s taste profile using features like genre, mood, energy, tempo, and valence. It compared each song to the user profile, assigned a score, and returned the highest-ranking songs.

This upgraded system transforms that basic recommender into a more advanced AI pipeline by adding retrieval (RAG), agent-based reasoning, reliability checks, and guardrails. Instead of only scoring songs, the system now interprets user requests, retrieves relevant data, applies constraints (like clean music), and evaluates how reliable the recommendations are.

## How The System Works

This system recommends music by combining retrieval, reasoning, and evaluation into a structured pipeline.

When a user enters a request, such as wanting upbeat or calm music, the system first validates the input using guardrails to ensure it is clear and safe to process. It then uses a retrieval step (RAG) to search a dataset of songs stored in music_data.json. This dataset includes attributes such as genre, mood, and whether a song is explicit.

After retrieving relevant songs, the system acts like an “agent” by applying decision logic. It interprets the user’s intent and filters results based on constraints. For example, if the user requests clean music, the system removes any explicit songs before generating recommendations. It also generates explanations for why each song was selected, based on how well it matches the requested mood and genre.

Once recommendations are generated, a reliability evaluator checks the results. It verifies that:

recommendations were produced
constraints (like clean music) were respected
explanations are included

If the system cannot find valid results, it does not fail silently. Instead, it returns a fallback message and lowers its confidence score to reflect uncertainty.

## A simple view of the system flow is:

User Input
   ↓
Input Validation Guardrails
   ↓
Retriever (RAG - music_data.json)
   ↓
Recommendation Agent
   ↓
Reliability Evaluator
   ↓
Final Output + Confidence Score
   ↓
Logger (records results)

## architecture diagram 
<img width="536" height="1382" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/e13d2d1d-d934-41fc-b7b3-e0b15bd5a6fa" />



## 🚀 Getting Started

### Setup

1. Create a virtual environment (optional):

```bash
python3 -m venv .venv
source .venv/bin/activate

2. Install dependencies:

pip3 install -r requirements.txt

3. Run the system:
python3 src/main.py

### Sample Outputs

Example 1: Clean upbeat request

Input:

I want upbeat pop music for studying, clean and not explicit

Output:

Blinding Lights by The Weeknd
Levitating by Dua Lipa
Confidence Score: 0.8
Reliability: Passed
Example 2: Calm ambient request

Example 2: Calm music request 
Input:

Give me calm ambient music

Output:

Weightless by Marconi Union
Confidence Score: 0.65
Reliability: Passed
Example 3: Constraint conflict (advanced case)

Example 3: Invalid reccomendation

Input:

I want hype rap music, but clean only

Output:

No valid recommendations
System explains why
Confidence Score: 0.3
Reliability: Failed (no valid results)
Design Decisions

The system was designed as a modular pipeline so each part has a clear role.

The retriever handles data lookup
The agent handles reasoning and filtering
The evaluator checks reliability
The guardrails validate input
The logger records system behavior

One key design decision was to use simple keyword-based retrieval instead of embeddings. This keeps the system easy to run and understand, but limits flexibility. A more advanced version would use semantic search.

Another important decision was to include a reliability layer. Instead of always returning results, the system can detect when it fails and communicate that clearly, which makes it more trustworthy.

## Reliability and Evaluation

The system includes multiple reliability features:

Input validation (guardrails)
Explicit-content filtering
Confidence scoring
Reliability evaluator
Logging of all interactions

Testing showed that:

The system works well when the user provides clear mood or genre
It correctly filters explicit songs when requested
It handles failure cases by lowering confidence and explaining the issue

## Example summary:

3 out of 3 test scenarios behaved as expected.
The system correctly retrieved songs, applied constraints, and flagged invalid outputs.
Limitations and Risks

## This system has several limitations.

It relies on a small dataset, which limits the variety of recommendations. It also uses keyword matching, which means it may miss relevant songs if the user’s wording is different. Additionally, the system does not understand deeper context such as lyrics, culture, or artist similarity.

There is also potential bias in the dataset. If certain genres or moods are overrepresented, the system will favor those in its recommendations.

## Reflection

This project showed that building an AI system is not just about generating outputs, but about designing a full pipeline that includes retrieval, reasoning, validation, and evaluation.

One important insight was how valuable failure cases are. When the system could not find clean hype rap songs, it correctly returned no results and lowered its confidence. This made the system feel more reliable instead of forcing incorrect recommendations.

Working with AI tools was helpful for structuring the system and debugging code. One helpful suggestion was adding a reliability evaluator to check constraint violations. One flawed suggestion was initially treating a simple recommender as sufficient, which did not meet the requirements for a full AI system.

Overall, this project improved my understanding of how real-world AI systems balance accuracy, reliability, and user trust.
