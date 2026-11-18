from repomind.embeddings.embedding_generator import EmbeddingGenerator
from repomind.vectorstore.chroma_store import ChromaStore
from repomind.models.retrieved_chunk import RetrievedChunk


class Retriever:

    def __init__(self):
        self.embedding_generator = EmbeddingGenerator()
        self.vector_store = ChromaStore()

    def retrieve(
        self,
        repo: str,
        question: str,
        k: int = 15,
    ) -> list[RetrievedChunk]:
        embedding = self.embedding_generator.generate(question)

        results = self.vector_store.search(
            repo=repo,
            embedding=embedding,
            k=k,
        )

        retrieved_chunks = []

        for document, metadata in zip(
            results["documents"][0],
            results["metadatas"][0]
        ):
            retrieved_chunks.append(
                RetrievedChunk(
                    repo=metadata["repo"],
                    text=document,
                    path=metadata["path"],
                    start_line=metadata["start_line"],
                    end_line=metadata["end_line"],
                )
            )

        return retrieved_chunks