# agents/validator_agent.py

from langchain.agents import Tool
from llm.gemini_llm import GeminiLLM
from llm.prompt_templates import validator_prompt
from tools.retriever_tool import retriever_tool  # This should be a Tool instance

rt = retriever_tool  # assign Tool instance, not calling it
llm = GeminiLLM()

def validate_fn(okr_json: str) -> str:
    snippet = rt.invoke(okr_json)  # invoke() with input text
    prompt = validator_prompt.format(okr_json=okr_json, evidence_snippet=snippet)
    return llm.predict(prompt=prompt)

validator_agent = Tool(
    name="Evidence Validator",
    func=validate_fn,
    description="Verify LinkedIn evidence using RAG + Gemini."
)
