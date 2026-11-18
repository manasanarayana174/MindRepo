# RepoMind

RepoMind is a CLI-based Retrieval-Augmented Generation (RAG) application that allows you to chat with any GitHub repository using a local Large Language Model (LLM) running on Ollama.

The application clones a GitHub repository, indexes its source code, generates embeddings, stores them in a vector database, and answers natural language questions using semantic search and Retrieval-Augmented Generation (RAG).

Everything runs locally.

---

## Features

- Clone any public GitHub repository
- Parse and index source code
- Intelligent chunking of repository files
- Local embeddings using Ollama
- ChromaDB vector database
- Semantic search
- RAG-based question answering
- Rich CLI interface
- Repository filtering
- Phoenix observability
- Fully local (no cloud APIs required)

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Typer | CLI Framework |
| GitPython | Clone GitHub repositories |
| Ollama | Local LLM & Embeddings |
| ChromaDB | Vector Database |
| Pydantic | Data Models |
| Rich | Beautiful CLI Output |
| Arize Phoenix | AI Observability |

---

## Project Architecture

```text
                   +----------------------+
                   |       CLI (Typer)    |
                   +----------+-----------+
                              |
                              |
                    repomind clone / ask
                              |
                              |
              +---------------+---------------+
              |                               |
              |                               |
      Clone Repository                 Ask Question
              |                               |
              |                               |
      Repository Reader                Generate Embedding
              |                               |
              |                               |
        Document Parser                Similarity Search
              |                               |
              |                               |
         Text Chunker                Retrieve Top K Chunks
              |                               |
              |                               |
    Generate Embeddings                Prompt Builder
              |                               |
              |                               |
         Store in ChromaDB -----------> Ollama LLM
                                              |
                                              |
                                         Final Answer
                                              |
                                              |
                                       Rich CLI Output
                                              |
                                              |
                                   Phoenix Observability
```

---

## Project Structure

```text
repomind/
│
├── src/
│   └── repomind/
│       ├── chunker/
│       ├── cli/
│       ├── embeddings/
│       ├── git/
│       ├── indexing/
│       ├── llm/
│       ├── models/
│       ├── observability/
│       ├── parser/
│       ├── prompt/
│       ├── rag/
│       ├── reader/
│       ├── retrieval/
│       ├── vectorstore/
│       └── main.py
│
├── repositories/
├── database/
├── pyproject.toml
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/repomind.git

cd repomind
```

---

### Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install typer rich gitpython chromadb ollama pydantic arize-phoenix
```

---

## Install Ollama

Download Ollama

https://ollama.com

Pull the required models

Embedding model

```bash
ollama pull nomic-embed-text
```

Chat model

```bash
ollama pull qwen2.5-coder:7b
```

Verify

```bash
ollama list
```

---

## Run Phoenix

Start Phoenix in another terminal

```bash
phoenix serve
```

Phoenix UI

```
http://localhost:6006
```

---

## Running RepoMind

### Clone and Index a Repository

```bash
PYTHONPATH=src python -m repomind.main clone https://github.com/fastapi/typer
```

---

### Ask Questions

```bash
PYTHONPATH=src python -m repomind.main ask typer "How do I create a command?"
```

Example output

```text
Answer

To create a command, define a function using the
@app.command() decorator.

Sources

docs/tutorial/commands/arguments.md

docs_src/tutorial001.py
```

---

### List Indexed Repositories

```bash
PYTHONPATH=src python -m repomind.main list
```

---

### Repository Information

```bash
PYTHONPATH=src python -m repomind.main info typer
```

---

### Delete Repository

```bash
PYTHONPATH=src python -m repomind.main delete typer
```

---

## RAG Pipeline

```text
User Question
      │
      ▼
Generate Question Embedding
      │
      ▼
Vector Search (ChromaDB)
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Local LLM (Ollama)
      │
      ▼
Generate Answer
      │
      ▼
Display Sources
```

---

## Phoenix Observability

RepoMind integrates with Arize Phoenix for tracing and observability.

Each request records

- Retrieval stage
- Prompt generation
- LLM execution
- Latency
- Repository information
- Retrieved chunk count

This helps debug and evaluate the RAG pipeline.

---

## Supported File Types

- Python
- JavaScript
- TypeScript
- Java
- Go
- Rust
- Markdown
- JSON
- YAML
- TOML

Ignored folders

- `.git`
- `node_modules`
- `venv`
- `__pycache__`
- `dist`
- `build`

---

## Example Workflow

```text
Clone Repository
        │
        ▼
Read Files
        │
        ▼
Parse Documents
        │
        ▼
Chunk Source Code
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
Ask Question
        │
        ▼
Semantic Search
        │
        ▼
Retrieve Context
        │
        ▼
Generate Answer
```

---

## Future Improvements

- Function-level chunking
- AST-based parsing
- Hybrid Search (BM25 + Vector Search)
- Streaming responses
- Incremental indexing
- Multi-repository search
- Conversation memory
- Reranking
- Repository summarization
- Documentation generation

---

## Author

**Sathvik Tati**

Built as a learning project to understand how production-grade Retrieval-Augmented Generation (RAG) systems are designed and implemented using local LLMs.

---

## License

This project is licensed under the MIT License.# MindRepo
