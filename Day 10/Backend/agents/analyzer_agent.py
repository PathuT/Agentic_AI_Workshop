from langchain.agents import Tool   # <- Add this import
from llm.gemini_llm import GeminiLLM
from llm.prompt_templates import analyzer_prompt

llm = GeminiLLM()

analyzer_agent = Tool(
    name="Analyzer",
    func=lambda text: llm.predict(analyzer_prompt.format(text=text)),
    description="Analyze OKR data for inconsistencies and discrepancies."
)
