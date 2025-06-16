import json
import os

SUBMISSION_STORE = "submitted_texts.json"

def load_submissions():
    if not os.path.exists(SUBMISSION_STORE):
        return []
    with open(SUBMISSION_STORE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_submission(text):
    submissions = load_submissions()
    submissions.append(text)
    with open(SUBMISSION_STORE, "w", encoding="utf-8") as f:
        json.dump(submissions, f, indent=2)
