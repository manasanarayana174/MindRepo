from repomind.llm.ollama_client import OllamaClient
from repomind.prompt.prompt_builder import PromptBuilder
from repomind.retrieval.retriever import Retriever
from repomind.observability.phoenix import tracer


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = OllamaClient()

    def ask(self, repo: str, question: str):

        with tracer.start_as_current_span("RAG Pipeline"):

            with tracer.start_as_current_span("Retrieve") as span:

                chunks = self.retriever.retrieve(repo, question)

                span.set_attribute("repo", repo)
                span.set_attribute("question", question)
                span.set_attribute("chunks_retrieved", len(chunks))
                span.set_attribute(
                    "retrieved_characters",
                    sum(len(chunk.text) for chunk in chunks),
                )
                span.set_attribute(
                    "retrieved_files",
                    [chunk.path for chunk in chunks],
                )

                for i, chunk in enumerate(chunks, start=1):
                    span.add_event(
                        f"Chunk {i}",
                        {
                            "repository": chunk.repo,
                            "file": chunk.path,
                            "lines": f"{chunk.start_line}-{chunk.end_line}",
                            "preview": chunk.text[:300],
                        },
                    )

            with tracer.start_as_current_span("Build Prompt") as span:

                prompt = self.prompt_builder.build(
                    question,
                    chunks,
                )

                span.set_attribute("prompt_length", len(prompt))
                span.set_attribute("prompt", prompt)

            with tracer.start_as_current_span("LLM") as span:

                response = self.llm.ask(prompt)

                answer = response.message.content

                span.set_attribute("model", response.model)
                span.set_attribute("prompt_tokens", response.prompt_eval_count)
                span.set_attribute("completion_tokens", response.eval_count)
                span.set_attribute(
                    "total_tokens",
                    response.prompt_eval_count + response.eval_count,
                )
                span.set_attribute(
                    "total_duration_ms",
                    response.total_duration / 1_000_000,
                )
                span.set_attribute(
                    "generation_duration_ms",
                    response.eval_duration / 1_000_000,
                )

            return {
                "answer": answer,
                "sources": chunks,
            }