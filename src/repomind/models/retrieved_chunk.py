from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    repo: str
    text: str
    path: str
    start_line: int
    end_line: int