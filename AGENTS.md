# Agent Coding Guide

This document describes how AI coding agents should work in this repository.

## Project Overview

A terminal-based "Guess the Number" game written in Python (`guess_the_number.py`).

## Repository Layout

```
guess_the_number.py   # Main game module
tests/                # Pytest test suite
pyproject.toml        # Project metadata and tool configuration
AGENTS.md             # This file
```

## Environment Setup

```bash
pip install -e ".[dev]"
```

This installs the project in editable mode along with all development dependencies
(pytest, ruff, mypy).

## Commands

| Task | Command |
|------|---------|
| Run tests | `pytest` |
| Lint & format check | `ruff check .` |
| Auto-fix lint issues | `ruff check --fix .` |
| Format code | `ruff format .` |
| Type check | `mypy guess_the_number.py` |

Run all checks before opening or updating a pull request:

```bash
ruff check . && ruff format --check . && mypy guess_the_number.py && pytest
```

## Coding Conventions

- Python 3.10+.
- Follow [PEP 8](https://peps.python.org/pep-0008/) style (enforced by `ruff`).
- All public functions must have docstrings.
- Use type annotations on all new function signatures.
- Keep business logic testable: avoid mixing I/O directly with logic when possible.

## Testing Guidelines

- Tests live in `tests/`. Mirror the module name: `guess_the_number.py` → `tests/test_guess_the_number.py`.
- Use `pytest` and `unittest.mock` (or `pytest-mock`) to mock `input()` and `random.randint`.
- Aim for high coverage of the game logic functions.
- Each test function must have a descriptive name: `test_<what>_<expected_outcome>`.

## Pull Request Checklist

Before submitting a PR an agent must ensure:

- [ ] `ruff check .` passes with no errors.
- [ ] `ruff format --check .` passes (code is formatted).
- [ ] `mypy guess_the_number.py` passes with no errors.
- [ ] `pytest` passes with all tests green.
- [ ] New features include corresponding tests.
- [ ] Docstrings are present on all public functions.
