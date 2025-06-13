import os
from src.ingest import build_vectorstore_from_multiple_pdfs

def ingest_all_pdfs():
    pdf_folder = "data"
    pdf_files = [f"{pdf_folder}/{file}" for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in 'data/' folder.")
        return

    print(f"📂 Found {len(pdf_files)} PDF(s): {pdf_files}")
    build_vectorstore_from_multiple_pdfs(pdf_files)

if __name__ == "__main__":
    ingest_all_pdfs()
