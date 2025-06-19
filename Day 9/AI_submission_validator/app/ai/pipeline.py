import hashlib
import os
from app.ai.langchain_api import parse_submission, detect_plagiarism, validate_credential
from app.utils.retriever import load_corpus
from app.tools.web_search_tool import get_web_search_tool

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

RAG_FOLDER = "rag_corpus"

def save_unique_submission_to_rag(subm_text: str, title: str):
    # hash the content to avoid filename collisions
    hash_val = hashlib.md5(subm_text.encode()).hexdigest()
    filename = f"{title[:50]}_{hash_val}.txt"
    path = os.path.join(RAG_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(subm_text)

def run_agents(subm_text: str, reference_file=None, img=None):
    texts, _ = load_corpus(RAG_FOLDER)

    out = {}
    parsed = parse_submission(subm_text, img)
    out['parsed'] = parsed

    # Plagiarism check (offline with RAG)
    plag = detect_plagiarism(subm_text, texts)
    out['plagiarism'] = plag

    # Save to RAG if new
    if not plag:
        save_unique_submission_to_rag(subm_text, parsed['title'] or "submission")

    # Credential validation (if certificate provided)
    if reference_file:
        out['credential'] = validate_credential(subm_text, reference_file)
    else:
        out['credential'] = None

    # Web Validation (ghost authorship, outdated info)
    try:
        search_tool = get_web_search_tool()
        tools = [search_tool]
        llm = ChatOpenAI(temperature=0, model="gpt-4")  # or your Gemini wrapper here

        agent = initialize_agent(
            tools,
            llm,
            agent="zero-shot-react-description",
            verbose=False
        )

        query = (
            f"Check if this submission appears to be ghostwritten or copied "
            f"from online sources. Is it outdated or suspicious? Content:\n{subm_text}"
        )
        web_validation = agent.run(query)
        out['web_validation'] = web_validation
    except Exception as e:
        out['web_validation'] = f"Web validation failed: {str(e)}"

    return out
