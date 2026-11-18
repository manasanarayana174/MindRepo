from pprint import pprint

from repomind.retrieval.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    repo="typer",
    question="How do I create a command?"
)

pprint(results)