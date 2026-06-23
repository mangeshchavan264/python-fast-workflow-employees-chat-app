from fastapi import FastAPI
from pydantic import BaseModel
from llm_client import LLMClient
import os

app = FastAPI()

llm = LLMClient("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")


class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message:": "AI is running"}

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: ChatRequest):

    answer=llm.ask(request.prompt)

    return {
        "prompt": request.prompt,
        "response": answer
    }

# @app.get("/chat")
# def chat(prm):
#     prompt="what is 3+3?"
#     return llm.ask("what is 3+3?")
    
