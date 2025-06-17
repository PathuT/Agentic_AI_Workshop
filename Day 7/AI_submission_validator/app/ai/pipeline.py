import hashlib
import os
from app.ai.langchain_api import parse_submission, detect_plagiarism, validate_credential
from app.utils.retriever import load_corpus

RAG_FOLDER = "rag_corpus"

def save_unique_submission_to_rag(subm_text: str, title: str):
    # hash the content to avoid filename collisions
    hash_val = hashlib.md5(subm_text.encode()).hexdigest()
    filename = f"{title[:50]}_{hash_val}.txt"
    path = os.path.join(RAG_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(subm_text)

def run_agents(subm_text: str, reference_file=None, img=None):
    texts, _ = load_corpus(RAG_FOLDER)

    out = {}
    parsed = parse_submission(subm_text, img)
    out['parsed'] = parsed

    plag = detect_plagiarism(subm_text, texts)
    out['plagiarism'] = plag

    if not plag:
        save_unique_submission_to_rag(subm_text, parsed['title'] or "submission")

    if reference_file:
        out['credential'] = validate_credential(subm_text, reference_file)
    else:
        out['credential'] = None

    return out

