from pathlib import Path
from pydantic import BaseModel, Field
from typing import Any


class Document(BaseModel):
    path: Path
    language: str
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)