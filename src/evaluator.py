def evaluate_recommendations(user_query, agent_output):
    issues = []

    recommendations = agent_output.get("recommendations", [])

    if not recommendations:
        issues.append("No recommendations were generated.")

    if "not explicit" in user_query.lower() or "clean" in user_query.lower():
        for song in recommendations:
            if song.get("explicit") is True:
                issues.append(f"Explicit song included despite clean music request: {song['title']}")

    for song in recommendations:
        if not song.get("reason"):
            issues.append(f"Missing explanation for: {song['title']}")

    passed = len(issues) == 0

    return {
        "passed": passed,
        "issues": issues,
        "reliability_score": 1.0 if passed else 0.5
    }