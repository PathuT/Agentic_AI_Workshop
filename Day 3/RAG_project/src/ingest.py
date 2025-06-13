from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

CHUNK_SIZE = 500
EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def chunk_text(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# ✅ For single PDF
def build_vectorstore(pdf_path, persist_dir="vectorstore"):
    raw_text = load_pdf(pdf_path)
    print(f"🔍 Extracted text length: {len(raw_text)}")

    chunks = chunk_text(raw_text)
    print(f"🧱 Total chunks: {len(chunks)}")

    if not chunks:
        raise ValueError("⚠️ No chunks found. PDF might be empty or not parseable.")

    embeddings = EMBED_MODEL.encode(chunks)
    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(embeddings)

    if not os.path.exists(persist_dir):
        os.makedirs(persist_dir)

    faiss.write_index(index, f"{persist_dir}/index.faiss")
    with open(f"{persist_dir}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("✅ Vectorstore created successfully.")

def build_vectorstore_from_multiple_pdfs(pdf_paths, persist_dir="vectorstore"):
    all_chunks = []
    metadata = []

    for path in pdf_paths:
        print(f"🔍 Processing: {path}")
        reader = PdfReader(path)
        for page_number, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            page_chunks = chunk_text(page_text)

            for chunk in page_chunks:
                all_chunks.append(chunk)
                metadata.append({
                    "source": os.path.basename(path),
                    "page": page_number + 1
                })

    print(f"🧱 Total combined chunks: {len(all_chunks)}")

    if not all_chunks:
        raise ValueError("⚠️ No chunks found across PDFs.")

    embeddings = EMBED_MODEL.encode(all_chunks)
    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(embeddings)

    if not os.path.exists(persist_dir):
        os.makedirs(persist_dir)

    faiss.write_index(index, f"{persist_dir}/index.faiss")
    with open(f"{persist_dir}/chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)
    with open(f"{persist_dir}/metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("✅ Vectorstore created from multiple PDFs successfully.")
