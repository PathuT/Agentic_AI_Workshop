from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os

def build_and_save_vectorstore(documents, save_path: str):
    """
    Build FAISS vector store from documents and save locally.
    """
    # Use OpenAIEmbeddings or switch to Gemini embeddings if available
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(documents, embeddings)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    vectorstore.save_local(save_path)
    print(f"Vector store saved at {save_path}")

def load_vectorstore(path: str) -> FAISS:
    """
    Load the FAISS vector store from disk.
    """
    return FAISS.load_local(path)
