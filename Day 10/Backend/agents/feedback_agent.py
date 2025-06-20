from langchain.agents import Tool
from llm.gemini_llm import GeminiLLM
from llm.prompt_templates import feedback_prompt

llm = GeminiLLM()

def feedback_fn(feedback: str) -> str:
    prompt = feedback_prompt.format(feedback=feedback)
    return llm(prompt)

feedback_agent = Tool(
    name="Feedback Receiver",
    func=feedback_fn,
    description="Accept and log student feedback."
)
