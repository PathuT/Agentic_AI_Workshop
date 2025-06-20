# Agentic AI Submission Validator
A LangChain + RAG powered agentic AI app to **validate student submissions** by checking:
- :page_facing_up: Submission originality
- :mag: Plagiarism & outdated content
- :camera: QR code or certificate presence (OCR-based fallback)
- :books: Alignment with a trusted RAG corpus
- :brain: Authenticity scoring via multi-agent architecture
- :mag: All the 4 agents are functional and made using agent initiate
---
## :file_folder: Project Structure
```
AI_submission_validator/
├── app/
│   ├── ai/
│   │   ├── gemini_api.py           # Gemini API integration (optional)
│   │   ├── langchain_api.py        # LangChain agent handling
│   │   └── pipeline.py             # Full multi-agent pipeline
│   ├── tools/
│   └── utils/
│       ├── doc_utils.py            # PDF/image extraction, OCR, QR scan
│       ├── retriever.py            # RAG retriever with FAISS
│       └── score_utils.py          # Scoring logic
├── rag_corpus/                     # Trusted docs for dynamic RAG
│   └── Team Name/                  # Folder with .pdf/.txt/.docx files
├── main.py                         # Streamlit frontend
├── .env                            # API keys & environment variables
├── requirements.txt
└── README.md
```
---
## :rocket: Features
- :white_check_mark: Upload **PDF**, **image**, or **paste text**
- :white_check_mark: Extract submission content using `pytesseract` and `PyMuPDF`
- :white_check_mark: Dynamically build **RAG index** from `rag_corpus/`
- :white_check_mark: Evaluate content using **LangChain multi-agent pipeline**
- :white_check_mark: Score authenticity, reuse, and ghost authorship
---
## :gear: Setup Instructions
### 1. :white_check_mark: Clone the Repository
```bash
git clone https://github.com/username/AI_submission_validator.git
cd AI_submission_validator
```
### 2. :white_check_mark: Install Dependencies
```bash
pip install -r requirements.txt
```
Make sure you also have:
- **Tesseract OCR** installed and added to  system PATH
- **Python 3.10+**
### 3. :white_check_mark: Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=gemini_api_key
TAVILY_API_KEY=tavily_key  # optional for web search agent
```
---
### :arrow_forward: Run the App
```bash
streamlit run main.py
```
Then open browser at: [http://localhost:8501](http://localhost:8501)
---
## :brain: Agentic Flow (LangChain-based)
| Agent                        | Responsibility                                     |
|-----------------------------|-----------------------------------------------------|
| :receipt: Submission Parsing Agent | Extracts structure and QR metadata                  |
| :bar_chart: Plagiarism Detection Agent | Checks reuse via RAG + FAISS                      |
| :mortar_board: Credential Validation Agent | Verifies with uploaded certificates               |
| :heavy_division_sign: Authenticity Scoring Agent | Scores based on all checks                         |
---
## :books: How RAG Works
- Loads files from `rag_corpus/Team Name/`
- Converts documents into chunks
- Indexes chunks with **FAISS**
- Injects retrieved content into LangChain agents for accurate checking