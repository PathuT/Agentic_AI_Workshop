from app.utils.doc_utils import extract_text_from_image, scan_qr_from_image
from app.utils.score_utils import interpret_score
from app.utils.retriever import load_corpus, build_faiss, retrieve
from app.ai.gemini_api import query_gemini
import os

RAG_FOLDER = "rag_corpus"
os.makedirs(RAG_FOLDER, exist_ok=True)

# 1. Submission Parsing Agent
def parse_submission(subm_text: str, img=None):
    metadata = {}
    if img:
        metadata['qr_data'] = scan_qr_from_image(img)
    else:
        metadata['qr_data'] = "No QR found"
    lines = subm_text.splitlines()
    metadata['title'] = lines[0].strip() if lines else "Untitled Submission"
    return metadata

# 2. Plagiarism Agent
def detect_plagiarism(submission_text: str, corpus_texts: list) -> dict:
    """
    Detects exact duplicate submission from existing RAG corpus.
    """
    for corpus_text in corpus_texts:
        if submission_text.strip() == corpus_text.strip():
            return {
                "status": "duplicate",
                "message": "🚫 Duplicate submission detected. Please submit original work."
            }
    return {
        "status": "original",
        "message": "✅ No plagiarism detected."
    }


# 3. Credential Validation Agent (RAG + Gemini)
def validate_credential(subm_text: str, reference_file):
    # Save reference file dynamically for RAG corpus update
    dest = os.path.join(RAG_FOLDER, os.path.basename(reference_file.name))
    reference_file.seek(0)
    with open(dest, "wb") as w:
        w.write(reference_file.read())

    # Load updated corpus and build FAISS index
    texts, names = load_corpus(RAG_FOLDER)
    index, embeds = build_faiss(texts)
    retrieved = retrieve(subm_text, index, texts, k=1)

    if not retrieved:
        return {
            "matched": "No relevant matches found.",
            "similarity": 0.0,
            "label": "No Match",
            "gemini": "N/A"
        }

    top, score = retrieved[0]

    label = interpret_score(score)
    gemini_resp = query_gemini(top, subm_text)

    return {
        "matched": top[:500],  # snippet preview
        "similarity": score,
        "label": label,
        "gemini": gemini_resp
    }

# 4. Authenticity Scoring Agent
def compute_authenticity_score(plagiarism_detected: bool, rag_similarity: float, qr_status: str) -> float:
    """
    Calculate overall authenticity score between 0 and 100.

    Args:
        plagiarism_detected (bool): True if plagiarism detected.
        rag_similarity (float): Similarity score from RAG (0.0 to 1.0).
        qr_status (str): QR code scan result string.

    Returns:
        float: Authenticity score between 0 and 100.
    """

    if plagiarism_detected:
        base_score = 10  # Penalize heavily for plagiarism
    else:
        base_score = 50  # Base score without plagiarism

    # Boost score based on RAG similarity thresholds
    if rag_similarity > 0.9:
        base_score += 30
    elif rag_similarity > 0.7:
        base_score += 20
    elif rag_similarity > 0.4:
        base_score += 10

    # Penalize missing QR code
    if qr_status == "No QR found":
        base_score -= 15

    # Clamp score between 0 and 100
    final_score = max(0, min(100, base_score))
    return final_score
