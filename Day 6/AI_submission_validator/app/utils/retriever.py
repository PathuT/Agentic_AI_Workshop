import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os
from typing import List, Tuple

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def load_documents_from_folder(folder_path: str) -> List[str]:
    docs = []
    for fname in os.listdir(folder_path):
        with open(os.path.join(folder_path, fname), 'r', encoding='utf-8') as f:
            docs.append(f.read())
    return docs

def build_faiss_index(documents: List[str]) -> Tuple[faiss.IndexFlatIP, List[List[float]], List[str]]:
    embeddings = embedder.encode(documents, convert_to_tensor=False)
    dimension = len(embeddings[0])
    index = faiss.IndexFlatIP(dimension)
    index.add(np.array(embeddings).astype('float32'))
    return index, embeddings, documents

def retrieve_similar(query: str, index, embeddings, docs) -> Tuple[str, float]:
    query_emb = embedder.encode([query], convert_to_tensor=False)
    D, I = index.search(np.array(query_emb).astype('float32'), k=1)
    best_doc = docs[I[0][0]]
    similarity = D[0][0]
    return best_doc, similarity
