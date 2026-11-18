from pathlib import Path

from repomind.models.document import Document


class DocumentParser:

    EXTENSIONS = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".java": "java",
        ".go": "go",
        ".rs": "rust",
        ".md": "markdown",
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".toml": "toml"
    }

    def get_language(self, path: Path):
        return self.EXTENSIONS.get(path.suffix, "text")
    
    def parse(self, path: Path) -> Document:
        content = path.read_text(encoding="utf-8", errors="ignore")

        return Document(
            path=path,
            language=self.get_language(path),
            content=content,
            metadata={
                "repo": path.parts[1],
                "extension": path.suffix,
                "filename": path.name,
                "size": path.stat().st_size,
            }
        )
    
    def parse_many(self, files: list[Path]) -> list[Document]:
        documents = []

        for file in files:
            documents.append(self.parse(file))

        return documents