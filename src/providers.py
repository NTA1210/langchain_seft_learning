"""Provider factory shared by notebooks.

Keep model selection outside business logic. Free tiers and model IDs change,
so notebooks read their defaults from environment variables.
"""
from __future__ import annotations

import os
from dotenv import load_dotenv

load_dotenv()


def get_chat_model(provider: str | None = None, *, temperature: float = 0):
    provider = (provider or os.getenv("LLM_PROVIDER", "gemini")).lower()

    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=os.getenv("GEMINI_MODEL", "gemini-3.7-flash"),
            temperature=temperature,
        )

    if provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "openai/gpt-oss-20b"),
            temperature=temperature,
            max_retries=2,
        )

    if provider == "openrouter":
        from langchain_openrouter import ChatOpenRouter
        return ChatOpenRouter(
            model=os.getenv("OPENROUTER_MODEL", "openrouter/free"),
            temperature=temperature,
        )

    if provider == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "qwen3:8b"),
            temperature=temperature,
        )

    raise ValueError(
        f"Unsupported provider={provider!r}. "
        "Choose gemini, groq, openrouter, or ollama."
    )


def get_embeddings():
    """Primary course embedding model.

    Gemini embeddings keep the RAG modules easy to run without provisioning a
    separate vector-embedding provider. Swap this factory when benchmarking
    other embedding families.
    """
    from langchain_google_genai import GoogleGenerativeAIEmbeddings

    return GoogleGenerativeAIEmbeddings(
        model=os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-001")
    )
