from setuptools import setup, find_packages

setup(
    name="repomind",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "typer",
        "rich",
        "gitpython",
        "chromadb",
        "ollama",
        "pydantic",
        "arize-phoenix",
    ],
    entry_points={
        "console_scripts": [
            "repomind=repomind.main:app",
        ],
    },
)