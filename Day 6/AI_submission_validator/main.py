import streamlit as st
from PIL import Image
import numpy as np
import easyocr
import fitz  # PyMuPDF
import docx2txt
from app.ai.pipeline import process_submission

st.set_page_config(page_title="AI Submission Validator", layout="centered")
st.title("📄 AI Submission Validator")
st.markdown("Upload any type of file or paste your content.")

uploaded_file = st.file_uploader("Upload File (Image, PDF, DOCX, TXT)", type=["jpg", "jpeg", "png", "webp", "pdf", "docx", "txt"])
pasted_text = st.text_area("Or Paste Certificate Content")

reader = easyocr.Reader(['en'])

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.lower()

    if file_type.endswith((".jpg", ".jpeg", ".png", ".webp")):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        image_np = np.array(image)
        text_list = reader.readtext(image_np, detail=0)
        return "\n".join(text_list)

    elif file_type.endswith(".pdf"):
        pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        full_text = ""
        for page in pdf_doc:
            full_text += page.get_text()
        return full_text

    elif file_type.endswith(".docx"):
        return docx2txt.process(uploaded_file)

    elif file_type.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    else:
        return None

if st.button("✅ Validate Submission"):
    with st.spinner("🔄 Validating your submission... Please wait"):
        try:
            if uploaded_file:
                extracted_text = extract_text_from_file(uploaded_file)
                result = process_submission(extracted_text, uploaded_file)
            elif pasted_text:
                result = process_submission(pasted_text, None)
            else:
                st.warning("⚠️ Please upload a file or paste some text.")
                st.stop()

            # Safely extract and clamp scores
            ai_score = float(str(result['ai_score']).split()[0])
            ai_score = round(min(max(ai_score, 15), 100), 2)

            rag_distance = round(result["rag_distance"], 2)
            qr_status = result["qr_status"]
            authenticity_score = round(min(max(result["authenticity_score"], 15), 100), 2)

            # ✅ Show results
            st.success("✅ Validation Complete")
            st.metric("🤖 AI Score", f"{ai_score:.2f}")
            st.metric("📌 RAG Match Distance", f"{rag_distance:.2f}")
            st.metric("🔍 QR Status", qr_status)
            st.metric("🧠 Authenticity Score", f"{authenticity_score:.2f}")

            st.subheader("📄 Closest Match from RAG:")
            st.code(result["match_found"], language="text")

        except Exception as e:
            st.error(f"❌ Error during processing: {e}")
