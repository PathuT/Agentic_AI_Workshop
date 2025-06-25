# data/build_vectorstore.py

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from document_loader import load_documents
import os
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

def build_and_save_vectorstore():
    docs = load_documents("./data/docs", file_types=["*.txt", "*.pdf"])
    print(f"Loaded {len(docs)} documents")  # debug

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=google_api_key
    )

    vectorstore = FAISS.from_documents(docs, embedding=embeddings)

    vectorstore.save_local("./data/faiss_index")
    print("✅ Vectorstore created and saved.")

if __name__ == "__main__":
    build_and_save_vectorstore()
