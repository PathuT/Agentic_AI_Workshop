# src/model_qa.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
from src.retriever import retrieve_relevant_chunks

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def answer_query_with_gemini(query):
    # Handle greetings directly
    greeting_phrases = ["hi", "hello", "hey", "good morning", "good evening", "good afternoon"]
    if query.lower().strip() in greeting_phrases:
        return {
            "answer": "How can I help you today?",
            "sources": []
        }

    # RAG flow
    retrieved = retrieve_relevant_chunks(query)
    context_chunks = [item["chunk"] for item in retrieved]
    sources = [f'{item["source"]} (Page {item["page"]})' for item in retrieved]

    context = "\n\n".join(context_chunks)

    prompt = f"""You are a helpful AI assistant answering questions from research papers.

Answer the following question clearly based on the context below. Be concise and accurate.

Context:
{context}

Question:
{query}
"""

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    return {
        "answer": response.text,
        "sources": sources
    }
