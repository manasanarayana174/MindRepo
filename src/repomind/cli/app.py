import typer
from repomind.git.repository_manager import RepositoryManager
from repomind.rag.rag_pipeline import RAGPipeline
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
app = typer.Typer()
manager = RepositoryManager()
rag = RAGPipeline()



@app.command()
def clone(url: str):
    manager.clone(url)


@app.command()
def ask(repo: str, question: str):

    result = rag.ask(repo, question)

    console.print(
        Panel(
            result["answer"],
            title="Answer",
            border_style="green",
        )
    )

    table = Table(title="Sources")

    table.add_column("File", style="cyan")
    table.add_column("Lines", style="yellow")

    for source in result["sources"]:
        table.add_row(
            source.path,
            f"{source.start_line}-{source.end_line}",
        )

    console.print(table)

@app.command()
def list():
    repositories = manager.list_repositories()

    if not repositories:
        console.print("[yellow]No repositories indexed.[/yellow]")
        return

    table = Table(title="Indexed Repositories")

    table.add_column("Repository", style="cyan")

    for repo in repositories:
        table.add_row(repo)

    console.print(table)


@app.command()
def delete(repo: str):
    manager.delete(repo)

    console.print(
        f"✅ Deleted repository '{repo}'",
        style="green",
    )

@app.command()
def info(repo: str):

    data = manager.info(repo)

    table = Table(title=f"Repository: {repo}")

    table.add_column("Property")
    table.add_column("Value")

    table.add_row("Repository", data["name"])
    table.add_row("Files", str(data["files"]))

    console.print(table)