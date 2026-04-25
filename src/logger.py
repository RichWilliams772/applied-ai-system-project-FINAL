import json
from datetime import datetime

def log_interaction(user_query, agent_output, evaluation):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_query": user_query,
        "agent_output": agent_output,
        "evaluation": evaluation
    }

    with open("recommendation_logs.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")