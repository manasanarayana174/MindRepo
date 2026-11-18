from repomind.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

answer = rag.ask(
    "How do I create a command?"
)

print(answer)