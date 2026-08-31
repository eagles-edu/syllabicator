# Technology Stack

## Core Sections (Required)

### 1) Runtime Summary

| Area | Value | Evidence |
|------|-------|----------|
| Primary language | Python | [README.md](../../README.md), [requirements.txt](../../requirements.txt) |
| Runtime + version | Python 3 ([TODO] exact minor version not pinned in repo) | [README.md](../../README.md), [requirements.txt](../../requirements.txt) |
| Package manager | pip via `requirements.txt` | [requirements.txt](../../requirements.txt) |
| Module/build system | Flask app factory with a Python entry script; no `pyproject.toml` or `setup.py` detected | [run.py](../../run.py), [app/__init__.py](../../app/__init__.py), [requirements.txt](../../requirements.txt) |

### 2) Production Frameworks and Dependencies

| Dependency | Version | Role in system | Evidence |
|------------|---------|----------------|----------|
| Flask | 3.1.0 | Web application framework and route registration layer | [requirements.txt](../../requirements.txt), [app/__init__.py](../../app/__init__.py) |
| nltk | 3.9.1 | Loads the CMU Pronouncing Dictionary (cmudict) for pronunciation analysis | [requirements.txt](../../requirements.txt), [app/services/word_service.py](../../app/services/word_service.py) |
| python-dotenv | 1.0.1 | Environment variable support for local configuration | [requirements.txt](../../requirements.txt) |
| gunicorn | 23.0.0 | WSGI server dependency for deployment/runtime hosting | [requirements.txt](../../requirements.txt) |

### 3) Development Toolchain

| Tool | Purpose | Evidence |
|------|---------|----------|
| pytest | Test runner for behavioral validation | [requirements.txt](../../requirements.txt), [tests/test_word_service.py](../../tests/test_word_service.py) |
| pylint | Static analysis/linting | [requirements.txt](../../requirements.txt) |
| Formatter | [TODO] No repository-level formatter config detected in the project root | [requirements.txt](../../requirements.txt) |

### 4) Key Commands

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
python -m pytest -q
```

### 5) Environment and Config

- Config sources: [app/config.py](../../app/config.py), [run.py](../../run.py)
- Required env vars: `SECRET_KEY`, `HOST`, `PORT`, `FLASK_ENV`
- Deployment/runtime constraints: The app is configured as a Flask app with a local dev server entry point; `gunicorn` is present but no production deployment manifest is checked into the repo. The app also expects the NLTK CMU dictionary corpus to be available at runtime.

### 6) Evidence

- [requirements.txt](../../requirements.txt)
- [app/config.py](../../app/config.py)
- [run.py](../../run.py)
- [README.md](../../README.md)

## Extended Sections (Optional)

- No monorepo workspaces or multi-package build system were detected.
- The repo uses a single service-oriented Python app with no separate native build step.
