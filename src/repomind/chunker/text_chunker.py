from repomind.models.chunk import Chunk
from repomind.models.document import Document


class TextChunker:

    def __init__(self, chunk_size=30, overlap=10):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: Document):
        lines = document.content.splitlines()

        chunks = []

        step = self.chunk_size - self.overlap

        for i in range(0, len(lines), step):

            chunk_lines = lines[i:i + self.chunk_size]

            if not chunk_lines:
                continue

            chunks.append(
                Chunk(
                    repo=document.metadata["repo"],
                    text="\n".join(chunk_lines),
                    path=document.path,
                    start_line=i + 1,
                    end_line=i + len(chunk_lines),
                )
            )

        return chunks
    
    def chunk_many(self, documents):
        chunks = []

        for document in documents:
            chunks.extend(self.chunk(document))

        return chunks