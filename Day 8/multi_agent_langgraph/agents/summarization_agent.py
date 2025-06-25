from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class SummarizationAgent:
    def __init__(self, google_api_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=google_api_key
        )
        self.prompt = PromptTemplate(
            input_variables=["text"],
            template="Please summarize the following information in a clear and concise manner:\n\n{text}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def run(self, texts: list[str]) -> str:
        combined_text = "\n\n".join(texts)
        return self.chain.run(text=combined_text)
