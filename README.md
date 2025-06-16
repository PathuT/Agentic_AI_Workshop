#  AI Submission Validator

A smart AI-powered tool to validate academic or content-based submissions by checking for originality against a reference document using **LangChain**, **RAG (Retrieval-Augmented Generation)**, and **Agentic AI**.

---

##  Overview

This app evaluates the **authenticity** of submitted content (PDF, image, or text) by comparing it to a **trusted reference document**. It uses:

-  **LangChain** for agent-style logic and reasoning  
-  **FAISS** for semantic similarity via vector retrieval  
-  **RAG (Retrieval-Augmented Generation)** to enhance factual grounding  

---

##  Technologies Used

| Technology       | Purpose                                      |
|------------------|----------------------------------------------|
| **Python**        | Core programming language                    |
| **Streamlit**     | Frontend UI for file upload & display        |
| **LangChain**     | Agent framework for LLM-based reasoning      |
| **FAISS**         | Vector similarity search (for RAG)           |
| **PyMuPDF**       | PDF text extraction                          |
| **Pillow (PIL)**  | Image support and rendering                  |

---

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/username/ai-submission-validator.git
cd ai-submission-validator
```
### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 2. Install Required Packages

```bash
set API_KEY="gemini_key"  # Windows
```

### 4. Run the Application

```bash
streamlit run main.py
```





