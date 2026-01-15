# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

GABRIEL (Generalized Attribute Based Ratings Information Extraction Library) is an LLM-based social science analysis toolkit that turns qualitative data into analysis-ready datasets using GPT. It handles prompting, batching, retries, checkpointing, and audit trails.

## Development Commands

```bash
# Install for development
pip install -e .[dev]

# Run all tests (uses built-in dummy mode, no API key needed)
pytest

# Run specific test file
pytest tests/test_basic.py

# Run specific test
pytest tests/test_basic.py::test_prompt_template

# Run with coverage
pytest --cov=gabriel --cov-report=html

# Lint and format
ruff check src/ tests/
ruff format src/ tests/

# CLI commands
gabriel --list-tasks
gabriel --version
```

## Architecture

### Core Flow

```
User API (gabriel.rate, gabriel.classify, etc.)
    ↓
Task Classes (src/gabriel/tasks/)
    ↓
Core Infrastructure (src/gabriel/core/)
    ├── LLMClient/OpenAIClient
    ├── PromptTemplate (Jinja2)
    └── Pipeline
    ↓
Utils (src/gabriel/utils/openai_utils.py)
    - Rate limiting, batching, retries, checkpointing
    ↓
OpenAI API
```

### Key Components

- **`src/gabriel/api.py`** (2,200+ lines): Main public API exposing 19 async functions (`rate`, `classify`, `extract`, `rank`, `deduplicate`, `merge`, `filter`, etc.). Each wraps a corresponding Task class.

- **`src/gabriel/tasks/`**: 18 task implementations. Each task is a class with a `run()` async method that manages prompt rendering, LLM calls, response parsing, and checkpointing.

- **`src/gabriel/utils/openai_utils.py`**: Core operational module handling rate limiting (AsyncLimiter), batching, retry with exponential backoff, cost estimation, checkpointing, and web search integration.

- **`src/gabriel/prompts/`**: 16 Jinja2 templates for different task types. Templates use custom filters for prompt shuffling/variation.

### Patterns

**Async-first**: All main APIs are async. Use `asyncio.run()` in scripts or `await` in notebooks.

**Task configuration via dataclasses**: Each task uses a config dataclass (e.g., `RateConfig`, `ClassifyConfig`).

**Lazy loading**: Both `gabriel` module and `gabriel.tasks` use `__getattr__` for lazy imports.

**Dummy mode for testing**: Pass `use_dummy=True` or set `JSON_LLM_MODEL="dummy"` for offline testing without API calls. Tests use this by default in `conftest.py`.

**Checkpointing**: Tasks save intermediate results to `save_dir/responses/` for resumable runs. Pass `reset_files=True` to start fresh.

## Environment Variables

- `OPENAI_API_KEY`: Required for real API calls
- `OPENAI_BASE_URL`: Optional custom API endpoint
- `JSON_LLM_MODEL`: Override default model (set to "dummy" in tests)
