# agents/parser_agent.py
from langchain.agents import Tool
from llm.gemini_llm import GeminiLLM
from llm.prompt_templates import parser_prompt

llm = GeminiLLM()

parser_agent = Tool(
    name="OKR Parser",
    func=lambda text: llm(parser_prompt.format(text=text)),
    description="Extract structured OKR from raw LinkedIn submission."
)
