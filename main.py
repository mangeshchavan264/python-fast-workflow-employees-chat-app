from fastapi import FastAPI
from pydantic import BaseModel
from llm_client import LLMClient
import os

app = FastAPI()

llm = LLMClient("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")

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: ChatRequest):

    answer = llm.ask(request.prompt)

    return {
        "prompt": request.prompt,
        "response": answer
    }