import os
from dotenv import load_dotenv
import google.generativeai as genai
from tavily import TavilyClient

# Load API keys from .env
load_dotenv()

# Configure APIs
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class WebResearchAgent:
    def __init__(self, subject):
        self.subject = subject
        self.research_questions = []
        self.research_summary = {}

    def formulate_questions(self):
        system_prompt = f"Devise 5–6 insightful, research-oriented questions about the topic: '{self.subject}' to guide a deep investigation."
        model = genai.GenerativeModel("gemini-2.0-flash")
        reply = model.generate_content(system_prompt)
        raw_text = reply.text
        self.research_questions = [
            q.strip("-•123456. ") for q in raw_text.strip().split("\n") if q.strip()
        ]
        return self.research_questions

    def collect_web_data(self):
        for query in self.research_questions:
            try:
                web_results = tavily_client.search(
                    query=query[:400],
                    search_depth="advanced",
                    include_answer=True
                )
                top_3 = web_results.get("results", [])[:3]
                summary_points = "\n".join([
                    f"- **{res.get('title')}**: {res.get('content')[:200].strip()}..."
                    for res in top_3
                ])
                self.research_summary[query] = summary_points
            except Exception as error:
                self.research_summary[query] = f" Could not retrieve data: {error}"
        return self.research_summary
