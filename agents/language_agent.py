from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Language Agent")

# Initialize a text summarizer using HuggingFace's transformers
summarizer = pipeline("summarization")

class LanguageRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(request: LanguageRequest):
    # Using transformers to summarize the input text
    summary = summarizer(request.text, max_length=100, min_length=30, do_sample=False)
    
    return {"original_text": request.text, "summary": summary[0]["summary_text"]}
