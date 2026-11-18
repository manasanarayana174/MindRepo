from ollama import chat

class OllamaClient:

    def ask(self, prompt: str):

        response = chat(
            model="qwen2.5-coder:7b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response