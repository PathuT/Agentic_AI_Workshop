# RAG QA App

This is a Research Assistant app using **RAG (Retrieval-Augmented Generation)** with **Google Gemini API**, allowing users to ask questions based on the content of uploaded research PDFs.

---

## ✨ Features

- 🔍 Extracts and chunks text from PDFs  
- 📌 Embeds chunks using SentenceTransformer  
- ⚡ Retrieves relevant chunks using FAISS  
- 💬 Generates accurate, source-grounded answers using Gemini  
- 🖥️ Clean UI with Streamlit  
- 🧠 Tracks source of each answer (PDF file name)

---

## 🗂️ Project Structure

```
RAG_project/
├── app.py                       # Streamlit UI
├── ingest_all.py               # Script to process PDFs into vectorstore
├── vectorstore/                # Saved FAISS index + chunk + metadata
├── data/                       # Research PDFs go here
├── .env                        # Environment variable for Gemini API key
└── src/
    ├── __init__.py
    ├── ingest.py               # PDF loading, chunking, embedding
    ├── retriever.py            # FAISS retrieval logic
    └── model_qa.py             # Prompting and response generation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/username/gemini-rag-qa.git
cd gemini-rag-qa
```

### 2. Install Dependencies

Use a virtual environment (recommended):

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not created yet, generate it with:
> `pip freeze > requirements.txt`

### 3. Set Up Environment Variables

Create a `.env` file in the root with  [Gemini API Key](https://makersuite.google.com/app/apikey):

```env
GEMINI_API_KEY=google_gemini_api_key_here
```

### 4. Add PDFs

Place all research PDFs inside the `data/` folder:

```
RAG_project/
└── data/
    ├── paper1.pdf
    ├── paper2.pdf
    └── ...
```

---

## 🏗️ Build the Vectorstore

Run the ingestion script to process all PDFs:

```bash
python ingest_all.py
```

It will:
- Extract and chunk text from all PDFs
- Embed each chunk
- Save vectors, chunks, and sources into `vectorstore/`

---

## 💬 Run the QA App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in browser.

---

## ✅ Example Workflow

1. Drop PDFs in `data/`
2. Run: `python ingest_all.py`
3. Start app: `streamlit run app.py`
4. Ask questions like:
   - *"What is the main methodology used in the paper?"*
   - *"Summarize the results section."*

---

## 📄 Sample Answer

> **Q:** What is the primary dataset used in the paper?  
> **A:** The primary dataset used is the MNIST dataset for handwritten digit recognition.  
> **Sources:** `data/paper1.pdf`

---

## 📦 Dependencies

- `streamlit`  
- `faiss-cpu`  
- `PyPDF2`  
- `sentence-transformers`  
- `google-generativeai`  
- `python-dotenv`

---

## 🔐 Notes

- Answers only come from uploaded PDFs.
- If no answer is found, the model says:
  > `"This question cannot be answered from the given source."`

---

## 🛠️ To Do

- [ ] Add PDF upload via UI  
- [ ] Add chunk threshold filtering  
- [ ] Use Gemini Pro or Gemini 1.5 (when available)
