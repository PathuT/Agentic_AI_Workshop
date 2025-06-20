from langchain.agents import Tool
from llm.gemini_llm import GeminiLLM
from llm.prompt_templates import compiler_prompt

llm = GeminiLLM()

def compile_fn(all_data: str) -> str:
    prompt = compiler_prompt.format(all_data=all_data)
    return llm(prompt)

compiler_agent = Tool(
    name="Results Compiler",
    func=compile_fn,
    description="Compile final results summary."
)
