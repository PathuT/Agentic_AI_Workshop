from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import numpy as np

# Initialize OpenAI embeddings (make sure OPENAI_API_KEY is set in your environment)
embeddings = OpenAIEmbeddings()

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def langchain_score_submission(trusted_doc: str, submitted_doc: str) -> str:
    # Split texts into chunks for embedding
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    trusted_chunks = text_splitter.split_text(trusted_doc)
    submitted_chunks = text_splitter.split_text(submitted_doc)

    # Embed the chunks
    trusted_embeds = [embeddings.embed_query(chunk) for chunk in trusted_chunks]
    submitted_embeds = [embeddings.embed_query(chunk) for chunk in submitted_chunks]

    # Compute average embeddings for both docs
    trusted_vec = np.mean(trusted_embeds, axis=0)
    submitted_vec = np.mean(submitted_embeds, axis=0)

    # Compute cosine similarity score (0 to 1)
    similarity = cosine_similarity(trusted_vec, submitted_vec)

    # Convert to percentage score
    score_pct = similarity * 100

    # Basic interpretation
    if score_pct > 90:
        return f"{score_pct:.2f} (identical or very similar content)"
    elif score_pct > 70:
        return f"{score_pct:.2f} (paraphrased or moderately similar)"
    else:
        return f"{score_pct:.2f} (low similarity or unique content)"
