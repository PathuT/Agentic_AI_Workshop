def compute_authenticity_score(ai_score, rag_distance, qr_status):
    # Extract numeric part of AI score if it's a string
    if isinstance(ai_score, str):
        try:
            ai_score = float(ai_score.split()[0])
        except (ValueError, IndexError):
            ai_score = 50.0  # fallback if conversion fails

    base = ai_score

    # Adjust score based on RAG match distance
    if rag_distance < 0.1:
        base += 20
    elif rag_distance < 0.3:
        base += 10

    # Penalize if QR is not present or invalid
    if "No QR" in qr_status or "Invalid" in qr_status:
        base -= 15

    # Clamp the score between 0 and 100, and round to 2 decimals
    return round(min(max(base, 0), 100), 2)
