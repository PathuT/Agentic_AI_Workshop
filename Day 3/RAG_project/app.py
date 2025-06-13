import streamlit as st
from src.model_qa import answer_query_with_gemini
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Gemini RAG QA", layout="centered")

# --- Custom White-Based UI ---
st.markdown(
    """
    <style>
        body {
            background-color: #ffffff;
            color: #1f2937;
        }
        .title {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: bold;
            font-size: 2.2rem;
            color: #1f2937;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #4b5563;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }
        .answer-box {
            background-color: #f9fafb;
            border-radius: 10px;
            padding: 1.2rem 1.5rem;
            font-size: 1.1rem;
            color: #111827;
            border: 1px solid #e5e7eb;
            margin-top: 1.2rem;
            white-space: pre-wrap;
        }
        .stTextInput > div > div > input {
            height: 2.8rem;
            font-size: 1.1rem;
            padding-left: 0.75rem;
            border-radius: 8px;
            border: 1px solid #d1d5db;
        }
        .stSpinner > div > div {
            color: #2563eb;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- App Title & Description ---
st.markdown('<h1 class="title">RAG - Ask Questions from Research Papers</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask a question below. I will fetch answers using AI and your research PDFs.</p>', unsafe_allow_html=True)

# --- Query Input ---
query = st.text_input("Type your question:", placeholder="E.g., What is RAG architecture?", label_visibility="collapsed")

# --- Processing ---
if query:
    with st.spinner("🔎 Searching and thinking..."):
        result = answer_query_with_gemini(query)
        answer = result["answer"]
        sources = result["sources"]

    # --- Display Answer ---
    st.markdown("### 💡 Answer")
    st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)

    # --- Show Sources Only If Relevant ---
    excluded_phrases = [
        "this document does not contain an answer",
        "this query is too short",
        "no relevant information found",
        "i am sorry",
        "unable to answer"
    ]
    if not any(phrase in answer.lower() for phrase in excluded_phrases):
        st.markdown("### 📄 Sources")
        for src in sources:
            st.markdown(f"- {src}")
