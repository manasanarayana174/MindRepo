import chromadb

from repomind.models.chunk import Chunk


class ChromaStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="database")

        self.collection = self.client.get_or_create_collection(
            name="repomind"
        )

    def add(self, chunk: Chunk, embedding: list[float]):
        self.collection.add(
            ids=[f"{chunk.path}:{chunk.start_line}"],
            documents=[chunk.text],
            embeddings=[embedding],
            metadatas=[
                {
                    "repo": chunk.repo,
                    "path": str(chunk.path),
                    "start_line": chunk.start_line,
                    "end_line": chunk.end_line,
                }
            ],
        )

    def add_many(self, chunks, embeddings):
        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:
            ids.append(f"{chunk.path}:{chunk.start_line}")
            documents.append(chunk.text)
            metadatas.append(
                {
                    "repo": chunk.repo,
                    "path": str(chunk.path),
                    "start_line": chunk.start_line,
                    "end_line": chunk.end_line,
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def search(
        self,
        repo: str,
        embedding: list[float],
        k: int = 5,
    ):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=k,
            where={
                "repo": repo
            },
        )