# LLM Engineering — Practice

My code-along for Ed Donner's *Become an LLM Engineer in 8 weeks*.
Notes live in Notion; this repo is the code.

Reference repo (cloned next door, not forked): https://github.com/ed-donner/llm_engineering

## Setup

```bash
uv sync              # creates .venv, installs everything, installs llmx editable
cp .env.example .env # then fill in your keys
```

No `activate` step — `uv run` handles it.

```bash
uv run jupyter lab   # or just open a notebook in VS Code and pick the .venv kernel
uv add <package>     # instead of pip install
```

## Layout

```
src/llmx/            shared code — clients, scraper. Grows as weeks add reusable pieces.
week01_foundations/  one notebook per day
week02_frontier_apis/
projects/            things worth keeping, promoted out of a week folder
```

Notebooks import the shared code as a real package:

```python
from llmx import clients, MODELS, fetch_website_contents

response = clients["openai"].chat.completions.create(
    model=MODELS["openai"],
    messages=[{"role": "user", "content": "Tell me a fun fact"}],
)
```

## Rules I'm keeping

- `.env` never gets committed. Check `git status` before every push.
- Clear notebook outputs before committing (`nbstripout --install` does it automatically).
- When a function gets copy-pasted into a second notebook, it moves to `src/llmx/`.
- One commit per day of the course, message = what the day covered.

## Shape every project has:
1. CLIENTS    who am I calling            → src/llmx/config.py
2. SOURCES    what data goes in           → scraper, file read, DB query, API
3. PROMPTS    what am I asking            → system prompt + user prompt builder
4. PIPELINE   the orchestration           → one function that wires 1-3 together
5. SURFACE    how a human sees it         → print, Markdown, Gradio, CLI

## Progress

- [x] Week 1 — foundations, summarizer, Ollama, tokenization, brochure
- [ ] Week 2 — frontier APIs, Gradio, chatbots, tools, multi-modal
- [ ] Week 3 — open source with HuggingFace
- [ ] Week 4 — selecting the right LLM, code generation
- [ ] Week 5 — RAG
- [ ] Week 6 — fine-tuning frontier models
- [ ] Week 7 — fine-tuning open source
- [ ] Week 8 — autonomous agents
