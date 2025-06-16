from sentence_transformers import SentenceTransformer
import faiss
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_corpus(folder):
    docs = []
    paths = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            text = f.read()
            docs.append(text)
            paths.append(file)
    return docs, paths

def build_faiss_index(docs):
    embeddings = model.encode(docs)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index, embeddings

def query_faiss(index, docs, query):
    q_vec = model.encode([query])
    D, I = index.search(q_vec, k=1)
    return docs[I[0][0]], D[0][0]
