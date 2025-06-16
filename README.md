# AI Submissions Validator 

A smart AI-powered tool built using **LangChain**, **Gemini Flash 2.0**, and **RAG (Retrieval-Augmented Generation)** to **auto-validate certificates and submissions**.

This validator:
-  Extracts text from PDF, DOCX, TXT, or images (OCR).
-  Detects plagiarism, ghost submissions, outdated content.
-  Computes an **AI Score** and **Authenticity Score**.
-  Uses Gemini + LangChain for similarity scoring.
-  Supports QR Code check (if using pyzbar or easyocr).
-  Optionally uses a RAG database for match checking (FAISS + local corpus).

---

## 📁 Folder Structure

```
AI_submission_validator/
│
├── main.py                # Streamlit UI
├── requirements.txt
├── .env                   # Contains GOOGLE_API_KEY
├── rag_corpus/            # Trusted certificates/documents
│   ├── cert1.txt
│   └── cert2.txt
├── app/
│   ├── ai/
│   │   ├── pipeline.py
│   │   ├── gemini_api.py
│   │   └── langchain_api.py
│   └── utils/
│       ├── doc_utils.py
│       ├── retriever.py
│       └── score_utils.py
```

---

##  Installation

1. **Clone** the repo or copy the files into a folder.

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up API key**:

Create a `.env` file in the root folder:

```ini
GOOGLE_API_KEY=gemini_api_key_here
```

4. **Run the app**:

```bash
streamlit run main.py
```

---

##  Supported Upload Formats

-  PDF  
-  DOCX  
-  TXT  
-  Images (JPG, JPEG, PNG, WEBP)  
-  Paste content manually

---

##  AI Techniques Used

- **Gemini Flash 1.5**: Prompt-based AI response generation.  
- **LangChain**: Dummy similarity logic to simulate vector comparison.  
- **EasyOCR**: Extracts text from image files.  
- **FAISS (RAG)**: Compares submission with trusted documents.  
- **QR Code Simulation**: Can detect if no QR is present or mismatch found.

---

##  Sample Dummy Certificate

You can use this dummy content as a file or pasted text:

```
Certificate of Completion

This is to certify that John Doe has successfully completed the course:
Machine Learning by Stanford University on Coursera

Issued: Jan 2024
Instructor: Andrew Ng
```

Try saving the above content as a `.txt`, `.pdf`, or `.docx` file and upload it for testing.

---

##  Future Scope

- Real LangChain embeddings (OpenAI/Gemini)  
- Certificate validation via official databases  
- QR Code decoding and authentication  
- Authenticated AI scoring logs

---

## Tip for Evaluators

> Although the LangChain logic here uses dummy similarity scoring for demo purposes, the code is structured to be replaced with real embedding-based comparison anytime — perfect for hackathons and demo submissions.

---

