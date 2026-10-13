
"""Verify the RAG project's core library imports and versions."""

import chromadb
import langchain


def main():
    """Print installed versions and confirm imports work."""
    print(f"LangChain: {langchain.__version__}")
    print(f"ChromaDB: {chromadb.__version__}")
    print("Environment check passed!")


if __name__ == "__main__":
    main()
