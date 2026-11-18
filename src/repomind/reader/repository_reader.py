from pathlib import Path


class RepositoryReader:

    def __init__(self):

        self.ignored_dirs = {
            ".git",
            "node_modules",
            "__pycache__",
            "venv",
            ".venv",
            "dist",
            "build",
        }

        self.ignored_files = {
            "package-lock.json",
            "yarn.lock",
            "pnpm-lock.yaml",
            "poetry.lock",
            "Cargo.lock",
            "composer.lock",
            ".DS_Store",
        }

        self.supported_extensions = {
            ".py",
            ".js",
            ".ts",
            ".java",
            ".go",
            ".rs",
            ".md",
            ".json",
            ".yaml",
            ".yml",
            ".toml",
        }

    def read(self, repository_path: Path):

        files = []

        for file in repository_path.rglob("*"):

            if any(part in self.ignored_dirs for part in file.parts):
                continue

            if file.name in self.ignored_files:
                continue

            if file.is_file() and file.suffix in self.supported_extensions:
                files.append(file)

        return files