from langchain.agents import Tool
from llm.gemini_llm import GeminiLLM
from llm.prompt_templates import scoring_prompt

llm = GeminiLLM()

def scoring_fn(parser_json):
    prompt = scoring_prompt.format(parser_json=parser_json)
    return llm(prompt)

scoring_agent = Tool(
    name="Semantic Scoring",
    func=scoring_fn,
    description="Score OKR (relevance, credibility, completeness)."
)
