from fastapi import FastAPI, Request
from pydantic import BaseModel
from pipeline import run_okr_pipeline, run_okr_pipeline_from_url

app = FastAPI()

class TextInput(BaseModel):
    text: str

class URLInput(BaseModel):
    url: str

@app.post("/okr/process-text")
async def process_text(input: TextInput):
    result = run_okr_pipeline(input.text)
    return result

@app.post("/okr/process-url")
async def process_url(input: URLInput):
    result = run_okr_pipeline_from_url(input.url)
    return result
