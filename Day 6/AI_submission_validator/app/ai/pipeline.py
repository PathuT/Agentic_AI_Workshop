from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import numpy as np

embeddings = OpenAIEmbeddings()

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def langchain_score_submission(trusted_doc: str, submitted_doc: str) -> str:
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    trusted_chunks = text_splitter.split_text(trusted_doc)
    submitted_chunks = text_splitter.split_text(submitted_doc)

    trusted_embeds = [embeddings.embed_query(chunk) for chunk in trusted_chunks]
    submitted_embeds = [embeddings.embed_query(chunk) for chunk in submitted_chunks]

    trusted_vec = np.mean(trusted_embeds, axis=0)
    submitted_vec = np.mean(submitted_embeds, axis=0)

    similarity = cosine_similarity(trusted_vec, submitted_vec)
    score_pct = similarity * 100

    if score_pct > 90:
        return f"{score_pct:.2f} (identical or very similar content)"
    elif score_pct > 70:
        return f"{score_pct:.2f} (paraphrased or moderately similar)"
    else:
        return f"{score_pct:.2f} (low similarity or unique content)"

def process_submission_with_storage(trusted_doc, submitted_doc, qr_found=False):
    analysis_result = langchain_score_submission(trusted_doc, submitted_doc)
    flags = []

    if "identical" in analysis_result.lower():
        flags.append("Content appears identical to trusted document")
    elif "paraphrased" in analysis_result.lower():
        flags.append("Paraphrased content detected")
    else:
        flags.append("Unique or low similarity content detected")

    return {
        "authenticity_score": analysis_result,
        "flags": flags,
        "matched_reference": trusted_doc[:500],  # first 500 chars
        "qr_found": qr_found
    }
