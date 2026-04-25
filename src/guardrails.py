def validate_input(user_query):
    if not user_query or not user_query.strip():
        return False, "Input cannot be empty."

    if len(user_query.strip()) < 5:
        return False, "Please provide more detail, such as a mood, genre, artist, or activity."

    blocked_terms = ["hate music", "illegal"]
    for term in blocked_terms:
        if term in user_query.lower():
            return False, "Input was blocked by the safety guardrail."

    return True, "Input passed validation."