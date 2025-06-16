import streamlit as st
from PIL import Image
import fitz  # PyMuPDF
from app.utils.doc_utils import extract_text_from_image, scan_qr_from_image
from app.ai.pipeline import process_submission_with_storage

st.set_page_config(page_title="AI Submission Validator", layout="centered")
st.title("📄 AI Submission Validator")

st.markdown("Upload the **submitted** file and a **trusted reference document** to validate authenticity.")

uploaded_pdf = st.file_uploader("Upload Submission PDF", type=["pdf"])
trusted_pdf = st.file_uploader("Upload Trusted Reference PDF", type=["pdf"])

uploaded_image = st.file_uploader("Or upload Submission as Image", type=["jpg", "jpeg", "png"])
text_input = st.text_area("Or paste Submission Text (optional)", height=200)

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

submitted_text = ""
qr_data = ""
trusted_text = ""

# Extract submitted content
if uploaded_pdf:
    submitted_text = extract_text_from_pdf(uploaded_pdf)
    st.text_area("Extracted Submission Text (from PDF)", value=submitted_text, height=300)

elif uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Submission Image", use_column_width=True)
    submitted_text = extract_text_from_image(img)
    qr_data = scan_qr_from_image(img)
    st.markdown(f"**QR Code Result:** `{qr_data}`")
    st.markdown("**Extracted Text:**")
    st.code(submitted_text)

elif text_input.strip():
    submitted_text = text_input.strip()

# Extract trusted content
if trusted_pdf:
    trusted_text = extract_text_from_pdf(trusted_pdf)
    st.text_area("Extracted Trusted Reference Text", value=trusted_text, height=300)

# Validation button
if st.button("✅ Validate Submission"):
    if not submitted_text.strip():
        st.error("❗ Please upload or paste a submission.")
    elif not trusted_text.strip():
        st.error("❗ Please upload a trusted reference document.")
    else:
        qr_found = (qr_data != "No QR found")
        result = process_submission_with_storage(trusted_text, submitted_text, qr_found=qr_found)

        st.markdown(f"### 🔍 Authenticity Score: **{result['authenticity_score']}**")
        st.markdown("---")

        if result.get("flags"):
            st.warning("⚠️ Issues Detected:")
            for flag in result["flags"]:
                st.markdown(f"- **{flag}**")

        st.markdown("**Top Matched Reference:**")
        st.code(result.get("matched_reference", "No matched reference available."))
