import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def run_gemini_prompt(prompt, content=""):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(f"{prompt}\n\n{content}")
    return response.text
