from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

def build_vectorstore(docs: list[Document]) -> FAISS:
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)
