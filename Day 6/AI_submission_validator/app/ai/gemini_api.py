# app/ai/gemini_api.py

def gemini_score_submission(trusted_doc: str, submitted_doc: str) -> str:
    """
    Dummy Gemini scoring simulation.
    For demo, it returns a mock score based on simple checks.
    """

    # Very simple logic: 
    if submitted_doc.strip() == trusted_doc.strip() and trusted_doc != "":
        return "Identical content detected — Score: 0.1"
    elif len(submitted_doc) > 100:
        return "Unique content detected — Score: 0.9"
    else:
        return "Paraphrased content detected — Score: 0.5"
