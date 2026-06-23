from fastapi import FastAPI
from pydantic import BaseModel
from llm_client import LLMClient
import os

app = FastAPI()

llm = LLMClient("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")


class InterviewRequest(BaseModel):
    question: str


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


@app.post("/interview") 
def interview(request:InterviewRequest):
    question=request.question

    prompt=f"""
    You are a senior Python developer and interview coach. You will be given a question from a candidate. You will provide a detailed answer to the question, explaning the reasoning behind your answer. You will also provide a list of follow-up questions that the candidate can ask to further explore the topic. The follow-up questions should be open-ended and encourage critical thinking.

    Input:
    Question: {question}
    Answer: you will give the answer.

    Output:
        Provide:
        1. Answer
        2. Conceptual Diagram realted to the concept asked in the question
        3. Difficuly level
        4. Follow-up questions
    """

    answer=llm.ask(prompt)

    return {
        "question": request.question,
        "response": answer
    }