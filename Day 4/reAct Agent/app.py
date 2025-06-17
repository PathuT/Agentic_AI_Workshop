import streamlit as st
from agent import WebResearchAgent
from report_generator import generate_research_report

st.set_page_config(page_title="ReAct Research Agent", page_icon="🔍", layout="centered")

st.markdown(
    """
    <style>
        .reportview-container {
            padding-top: 2rem;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #4CAF50;  /* Green base */
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-size: 1.1em;
            transition: background-color 0.3s ease;
        }

        /* Button Hover: Darker green, no red */
        .stButton>button:hover {
            background-color: #388E3C !important;  /* Darker green */
            color: white !important;
        }

        /* Text Input Styling */
        .stTextInput>div>div>input {
            font-size: 1.1em;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("AI-Powered Web Research Assistant")
st.markdown("Let an intelligent agent do your research using the **ReAct pattern** with LLM + real-time web search.")

# --- Input + Auto Button Display ---
topic = st.text_input("Enter your research topic here:")

if topic.strip():
    st.markdown("---")
    st.markdown("### Ready to generate your report?")

    if st.button("Generate Report Now"):
        with st.spinner("Thinking, researching, and writing..."):
            agent = WebResearchAgent(topic)
            questions = agent.formulate_questions()

            st.markdown("### Research Questions Generated")
            for i, q in enumerate(questions, 1):
                st.markdown(f"{i}. {q}")

            answers = agent.collect_web_data()
            report = generate_research_report(topic, questions, answers)

            st.markdown("---")
            st.markdown("### Full Research Report")
            st.markdown(report, unsafe_allow_html=True)

            st.download_button(
                label="Download Report as Markdown",
                data=report,
                file_name="research_report.md",
                mime="text/markdown"
            )
else:
    st.info("⏳ Please enter a topic to begin research.")
