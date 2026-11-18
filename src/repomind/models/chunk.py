from pathlib import Path

from pydantic import BaseModel


class Chunk(BaseModel):
    repo: str
    text: str
    path: Path
    start_line: int
    end_line: int