import os
from dotenv import load_dotenv
import streamlit as st
from graph.langgraph_workflow import build_graph

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
VECTORSTORE_PATH = "./data/faiss_index"

def main():
    st.set_page_config(page_title="Multi-Agent Research Assistant", layout="centered")
    st.title("🤖 Multi-Agent Research & Summarization System")
    st.write("Ask any question — the system decides how to answer it!")

    query = st.text_input("Enter your query here:")

    if st.button("Get Answer"):
        if not query.strip():
            st.warning("Please enter a query.")
            return

        # Build LangGraph app
        graph = build_graph(GOOGLE_API_KEY, TAVILY_API_KEY, VECTORSTORE_PATH)
        app = graph.app

        try:
            result = app.invoke({"query": query})
            st.markdown("### Answer:")
            st.write(result.get("final_response", "No response returned."))

        except Exception as e:
            st.error(f"Error running agents: {str(e)}")

if __name__ == "__main__":
    main()
