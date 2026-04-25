from agent import generate_recommendations
from evaluator import evaluate_recommendations
from guardrails import validate_input
from logger import log_interaction


def main():
    print("AI Music Discovery & Insight System")
    print("----------------------------------")

    user_query = input("What kind of music are you looking for? ")

    is_valid, validation_message = validate_input(user_query)

    if not is_valid:
        print(f"Guardrail failed: {validation_message}")
        return

    print(f"Guardrail passed: {validation_message}")

    agent_output = generate_recommendations(user_query)
    evaluation = evaluate_recommendations(user_query, agent_output)

    log_interaction(user_query, agent_output, evaluation)

    print("\nRecommendations:")
    print(agent_output["message"])

    for i, song in enumerate(agent_output["recommendations"], start=1):
        print(f"\n{i}. {song['title']} by {song['artist']}")
        print(f"   Reason: {song['reason']}")
        print(f"   Explicit: {song['explicit']}")

    print(f"\nConfidence Score: {agent_output['confidence']}")

    print("\nReliability Check:")
    print(f"Passed: {evaluation['passed']}")
    print(f"Reliability Score: {evaluation['reliability_score']}")

    if evaluation["issues"]:
        print("Issues:")
        for issue in evaluation["issues"]:
            print(f"- {issue}")


if __name__ == "__main__":
    main()

