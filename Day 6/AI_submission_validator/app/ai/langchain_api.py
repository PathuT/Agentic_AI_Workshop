import numpy as np
from langchain.text_splitter import CharacterTextSplitter

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def langchain_score_submission(trusted_doc: str, submitted_doc: str) -> str:
    """
    Dummy version of LangChain similarity checker using word overlap.
    """
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    trusted_chunks = text_splitter.split_text(trusted_doc)
    submitted_chunks = text_splitter.split_text(submitted_doc)

    trusted_words = set(trusted_doc.lower().split())
    submitted_words = set(submitted_doc.lower().split())

    common_words = trusted_words.intersection(submitted_words)
    similarity_ratio = len(common_words) / max(len(trusted_words), 1)

    # Simulated similarity score with noise
    score_pct = min(100, max(30, similarity_ratio * 100 + np.random.normal(5, 3)))

    if score_pct > 90:
        return f"{score_pct:.2f} (identical or very similar content)"
    elif score_pct > 70:
        return f"{score_pct:.2f} (paraphrased or moderately similar)"
    else:
        return f"{score_pct:.2f} (low similarity or unique content)"