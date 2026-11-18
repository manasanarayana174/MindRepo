from ollama import embed
from repomind.models.chunk import Chunk

class EmbeddingGenerator:

    def generate(self, text: str):
        response = embed(
            model="nomic-embed-text",
            input=text,
        )

        return response.embeddings[0]
    
    