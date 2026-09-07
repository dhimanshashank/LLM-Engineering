"""One place for API clients. Import from here instead of re-doing setup in every notebook."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

# Every one of these speaks the OpenAI Chat Completions shape,
# so one client class covers all of them - only base_url and key change.
_ENDPOINTS = {
    "openai":     (None,                                                    "OPENAI_API_KEY"),
    "anthropic":  ("https://api.anthropic.com/v1/",                         "ANTHROPIC_API_KEY"),
    "gemini":     ("https://generativelanguage.googleapis.com/v1beta/openai/", "GOOGLE_API_KEY"),
    "openrouter": ("https://openrouter.ai/api/v1",                          "OPENROUTER_API_KEY"),
    "groq":       ("https://api.groq.com/openai/v1",                        "GROQ_API_KEY"),
    "ollama":     ("http://localhost:11434/v1",                             None),
}

MODELS = {
    "openai": "gpt-4.1-mini",
    "anthropic": "claude-haiku-4-5",
    "gemini": "gemini-3.5-flash-lite",
    "ollama": "llama3.2",
}


def _build(base_url, key_name):
    api_key = os.getenv(key_name) if key_name else "ollama"
    if not api_key:
        return None
    return OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI()


clients = {name: _build(url, key) for name, (url, key) in _ENDPOINTS.items()}


def missing_keys():
    """Which providers aren't configured. Call this when something returns None."""
    return [name for name, client in clients.items() if client is None]
