from pathlib import Path
import shutil

from git import Repo, GitCommandError
from rich.console import Console

from repomind.indexing.indexer import Indexer

console = Console()

class RepositoryManager:
    def __init__(self):
        self.repositories_dir = Path("repositories")
        self.repositories_dir.mkdir(exist_ok=True)
        self.indexer = Indexer()

    def get_repo_name(self, url: str) -> str:
        return url.rstrip("/").split("/")[-1].replace(".git", "")

    

    def clone(self, url: str):
        repo_name = self.get_repo_name(url)
        destination = self.repositories_dir / repo_name

        if destination.exists():
            console.print(f"[yellow]Repository '{repo_name}' already exists.[/yellow]")
            return

        try:
            Repo.clone_from(url, destination)

            stats = self.indexer.index(destination)

            console.print("[green]✓ Repository cloned[/green]")
            console.print("[green]✓ Repository cloned[/green]")
            console.print(
                f"[green]✓ Indexed {stats['chunks']} chunks from {stats['files']} files[/green]"
            )

        except GitCommandError as e:
            console.print("[red]Failed to clone repository.[/red]")
            print(e)



    def list_repositories(self) -> list[str]:
        repositories = Path("repositories")

        if not repositories.exists():
            return []

        return sorted(
            repo.name
            for repo in repositories.iterdir()
            if repo.is_dir()
        )
    
    


    def delete(self, repo: str):
        repo_path = Path("repositories") / repo

        if not repo_path.exists():
            raise FileNotFoundError(f"{repo} not found.")

        shutil.rmtree(repo_path)

        self.indexer.vector_store.collection.delete(
            where={"repo": repo}
        )

    def info(self, repo: str):
        repo_path = Path("repositories") / repo

        if not repo_path.exists():
            raise FileNotFoundError(f"{repo} not found.")

        files = sum(
            1
            for file in repo_path.rglob("*")
            if file.is_file()
        )

        return {
            "name": repo,
            "files": files,
        }