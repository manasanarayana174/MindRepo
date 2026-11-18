from pathlib import Path

from repomind.reader.repository_reader import RepositoryReader
from repomind.parser.document_parser import DocumentParser
from repomind.chunker.text_chunker import TextChunker
from repomind.embeddings.embedding_generator import EmbeddingGenerator
from repomind.vectorstore.chroma_store import ChromaStore


class Indexer:

    def __init__(self):
        self.reader = RepositoryReader()
        self.parser = DocumentParser()
        self.chunker = TextChunker()
        self.embedding_generator = EmbeddingGenerator()
        self.vector_store = ChromaStore()

    def index(self, repository: Path):

        files = self.reader.read(repository)

        documents = self.parser.parse_many(files)

        chunks = self.chunker.chunk_many(documents)

        embeddings = [
            self.embedding_generator.generate(chunk.text)
            for chunk in chunks
        ]

        self.vector_store.add_many(chunks, embeddings)

        return {
            "files": len(files),
            "documents": len(documents),
            "chunks": len(chunks),
        }