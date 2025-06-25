
# Multi-Agent Research & Summarization System

This project is a multi-agent AI system built using **LangChain**, **LangGraph**, and **Google Gemini API** to perform research, retrieval-augmented generation (RAG), web search, and summarization tasks. It integrates several AI agents orchestrated through a state graph to answer user queries efficiently and accurately.

---

## Project Structure

```

multi\_agent\_langgraph/
├── app.py                        # Streamlit frontend application entrypoint
├── agents/
│   ├── **init**.py               # Makes 'agents' a Python package
│   ├── rag\_agent.py              # Retrieval-Augmented Generation agent using FAISS and Gemini
│   ├── router\_agent.py           # Router agent to decide routing logic based on user query
│   ├── summarizer\_agent.py       # Summarization agent using Google Gemini API
│   └── web\_research\_agent.py     # Web search agent using Tavily Search API
├── graph/
│   ├── **init**.py
│   └── langgraph\_workflow\.py     # LangGraph setup defining agent workflow and routing logic
├── data/
│   ├── build\_vectorstore.py      # Script to load documents and build FAISS vectorstore index
│   ├── document\_loader.py        # Utilities to load documents from disk for vectorstore
│   └── faiss\_index/              # Folder containing saved FAISS vectorstore files
├── .env                          # API keys & environment variables
├── requirements.txt              # Python dependencies file
└── README.md                     # Documentation file

```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <repository_url>
cd multi_agent_langgraph
````

### 2. Create and Activate Virtual Environment (Recommended)

```bash
# For Linux/Mac
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## 📚 Build Vectorstore

Before running the app, build the FAISS vectorstore:

```bash
python data/build_vectorstore.py
```

Ensure you place your documents in the folder:

```
./data/docs/
```

(Supported formats: `.txt`, `.pdf`)

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Open the browser and access the Streamlit interface to input your queries.

---

## 🧠 Agents Overview

| Agent Name         | Functionality                                                              |
| ------------------ | -------------------------------------------------------------------------- |
| `RouterAgent`      | Routes the query to the appropriate agent (RAG, Web Search, or Summarizer) |
| `RAGAgent`         | Uses FAISS vectorstore + Gemini API for context-based answers              |
| `WebResearchAgent` | Uses Tavily API to perform live web searches                               |
| `SummarizerAgent`  | Uses Gemini API to summarize large text content                            |

---

## 📝 Notes

* Vectorstore files are stored in `./data/faiss_index/`.
* Ensure your `.env` file is valid and contains working keys.
* Make sure to build the FAISS index **before** running the Streamlit app.

---

## 🧰 Troubleshooting

* `ModuleNotFoundError`: Ensure you run scripts from the project root and that `PYTHONPATH` includes root.
* `FileNotFoundError`: Make sure `./data/docs/` exists with valid documents.
* `FAISS index loading errors`: Re-run `build_vectorstore.py`.
* `.env not loading`: Install `python-dotenv` if not already installed.

---

## 📌 Requirements

Ensure the following libraries are included in `requirements.txt`:

```txt
langchain>=0.1.0
langgraph>=0.0.30
google-generativeai
tavily-python
streamlit
faiss-cpu
python-dotenv
```

