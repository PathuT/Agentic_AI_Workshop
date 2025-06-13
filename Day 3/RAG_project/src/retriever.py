# src/retriever.py
import faiss
import pickle
from sentence_transformers import SentenceTransformer

EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_relevant_chunks(query, persist_dir="vectorstore", k=4):
    index = faiss.read_index(f"{persist_dir}/index.faiss")
    with open(f"{persist_dir}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    with open(f"{persist_dir}/metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    query_vec = EMBED_MODEL.encode([query])
    D, I = index.search(query_vec, k)

    results = []
    for i in I[0]:
        results.append({
            "chunk": chunks[i],
            "source": metadata[i]["source"],
            "page": metadata[i]["page"]
        })
    return results
