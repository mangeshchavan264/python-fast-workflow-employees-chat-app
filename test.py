from llm_client import LLMClient
llm=LLMClient(os.getenv("OPENROUTER_API_KEY"))
print(llm.ask("what is 3+3?"))