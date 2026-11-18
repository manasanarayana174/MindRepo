from pathlib import Path

from repomind.indexing.indexer import Indexer

indexer = Indexer()

indexer.index(
    Path("repositories/typer")
)