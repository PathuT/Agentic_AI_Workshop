import streamlit as st
from PIL import Image
from app.utils.doc_utils import extract_text_from_pdf, extract_text_from_image
from app.ai.pipeline import run_agents

st.set_page_config(page_title="Agentic AI Validator", layout="centered")
st.title("🧠 Agent-based AI Submission Validator")

uploaded_submission = st.file_uploader("Upload Submission (PDF/Image)", type=["pdf","jpg","jpeg","png"])
uploaded_reference = st.file_uploader("Upload Trusted Reference (PDF)", type=["pdf"])
text_input = st.text_area("Or Paste Submission Text", height=200)

submit_text = ""
img = None
if uploaded_submission and uploaded_submission.type == "application/pdf":
    submit_text = extract_text_from_pdf(uploaded_submission)
elif uploaded_submission:
    img = Image.open(uploaded_submission)
    submit_text = extract_text_from_image(img)
elif text_input.strip():
    submit_text = text_input.strip()

if st.button("✅ Validate"):
    if not submit_text:
        st.error("Please provide submission.")
    else:
        result = run_agents(submit_text, uploaded_reference, img)

        # 💥 Reject duplicate
        if result['plagiarism']:
            st.error("🚫 Duplicate submission detected. Please submit original work.")
        else:
            st.success("✅ Submission validated and stored for future comparison.")
            st.write("### 🛠️ Submission Metadata:", result['parsed'])
            st.write("### 🔍 Plagiarism Detected:", result['plagiarism'])
            if result['credential']:
                cred = result['credential']
                st.write("### 📚 Credential Validation:")
                st.write("Matched Snippet:", cred['matched'])
                st.write("Score Label:", cred['label'])
                st.code(cred['gemini'])
