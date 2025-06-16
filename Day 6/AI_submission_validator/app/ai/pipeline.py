from app.ai.gemini_api import run_gemini_prompt
from app.utils.doc_utils import extract_qr_code
from app.utils.retriever import load_corpus, build_faiss_index, query_faiss
from app.utils.score_utils import compute_authenticity_score
from app.ai.prompts import doc_validation_prompt

def process_submission(file_text, image_path):
    # Extract QR (fallback if pyzbar removed)
    qr_result = extract_qr_code(image_path)

    # Run Gemini to get AI feedback score
    ai_response = run_gemini_prompt(doc_validation_prompt.format(input=file_text))
    score_line = [line for line in ai_response.split('\n') if 'score' in line.lower()]

    # Safely extract integer score
    try:
        ai_score = int(''.join(filter(str.isdigit, score_line[0]))) if score_line else 50
    except ValueError:
        ai_score = 50  # fallback if no digits in line

    # Run RAG similarity
    docs, _ = load_corpus("rag_corpus")
    index, _ = build_faiss_index(docs)
    match_text, distance = query_faiss(index, docs, file_text)

    # Compute authenticity
    final_score = compute_authenticity_score(ai_score, distance, qr_result)

    return {
        "ai_score": ai_score,
        "qr_status": qr_result,
        "rag_distance": distance,
        "authenticity_score": final_score,
        "match_found": match_text[:300]  # preview match text
    }
