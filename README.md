# Interview Questions & Answers API

A FastAPI-powered backend that uses an LLM (via OpenRouter) to generate detailed interview answers, conceptual diagrams, difficulty levels, and follow-up questions.

## Features

- `/interview` — Submit an interview question and get a structured answer with follow-ups
- `/chat` — Free-form prompt to the LLM
- Powered by OpenRouter (GPT-class models)

## Setup

### Prerequisites
- Python 3.10+
- [OpenRouter API key](https://openrouter.ai/)

### Install dependencies

```bash
pip install fastapi uvicorn openai python-dotenv pydantic
```

### Configure environment

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### Run the server

```bash
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`.

## API Reference

### `POST /interview`

Returns a detailed answer to an interview question.

**Request:**
```json
{
  "question": "What is the difference between a class and an object?"
}
```

**Response:**
```json
{
  "question": "...",
  "response": "1. Answer\n2. Conceptual Diagram\n3. Difficulty Level\n4. Follow-up questions"
}
```

### `POST /chat`

Send any prompt to the LLM.

**Request:**
```json
{
  "prompt": "Explain dependency injection"
}
```

### `GET /`

Health check — returns `{ "message": "AI is running" }`.

## Project Structure

```
.
├── main.py          # FastAPI routes
├── llm_client.py    # OpenRouter LLM wrapper
├── .env             # API key (not committed)
└── .gitignore
```
