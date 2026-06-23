from openai import OpenAI

class LLMClient:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    def ask(self, prompt):
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[
                 {
                    "role": "system",
                    "content": "You are a senior .NET architect and interview coach."
                 },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=10
        )

        return response.choices[0].message.content