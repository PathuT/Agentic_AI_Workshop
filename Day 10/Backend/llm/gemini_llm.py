from typing import Any, List, Optional
from pydantic import PrivateAttr
from langchain.llms.base import LLM
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM(LLM):
    _model: Any = PrivateAttr()

    def __init__(self, model_name: str = "models/gemini-2.0-flash", **kwargs):
        super().__init__(**kwargs)
        self._model = genai.GenerativeModel(model_name=model_name)

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        try:
            response = self._model.generate_content(prompt)
            return response.text.strip() if response else "No response from Gemini."
        except Exception as e:
            return f"Error invoking Gemini: {e}"

    def predict(self, prompt: str) -> str:
        # Public method for agent/tools to use
        return self._call(prompt)

    @property
    def _identifying_params(self):
        return {"model_name": self._model.model_name}

    @property
    def _llm_type(self) -> str:
        return "gemini"
