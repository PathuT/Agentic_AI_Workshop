import streamlit as st
from PIL import Image
from app.utils.doc_utils import extract_text_from_pdf, extract_text_from_image
from app.ai.pipeline import run_agents

st.set_page_config(page_title="Agentic AI Validator", layout="centered")
st.title("🧠 Agentic AI-Submission Validator")

# Upload inputs
uploaded_submission = st.file_uploader("📄 Upload Submission (PDF/Image)", type=["pdf", "jpg", "jpeg", "png"])
uploaded_reference = st.file_uploader("📎 Upload Trusted Certificate or Reference (PDF)", type=["pdf"])
text_input = st.text_area("📝 Or Paste Submission Text Below", height=200)

submit_text = ""
img = None

# Handle file input
if uploaded_submission:
    if uploaded_submission.type == "application/pdf":
        submit_text = extract_text_from_pdf(uploaded_submission)
    else:
        img = Image.open(uploaded_submission)
        submit_text = extract_text_from_image(img)
elif text_input.strip():
    submit_text = text_input.strip()

# Validate button
if st.button("✅ Validate Submission"):
    if not submit_text:
        st.error("🚫 Please provide a submission via file or text.")
    else:
        with st.spinner("🔍 Running AI agents..."):
            result = run_agents(submit_text, uploaded_reference, img)

        # Display results
        if result['plagiarism']:
            st.error("🚫 Duplicate submission detected. Please submit original work.")
        else:
            st.success("✅ Submission validated and stored for future comparison.")

            st.subheader("🛠️ Submission Metadata")
            st.json(result['parsed'])

            st.subheader("🔍 Plagiarism Status")
            st.write("No plagiarism detected.")

            if result['credential']:
                cred = result['credential']
                st.subheader("📚 Credential Validation")
                st.write("🔹 Matched Snippet:")
                st.code(cred['matched'])
                st.write(f"🔹 Score Label: `{cred['label']}`")
                st.write("🔹 Gemini Output:")
                st.code(cred['gemini'])
