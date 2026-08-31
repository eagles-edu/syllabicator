# Codebase Structure

## Core Sections (Required)

### 1) Top-Level Map

| Path | Purpose | Evidence |
|------|---------|----------|
| [app/](../../app/) | Primary application package containing config, routes, and service logic | [app/__init__.py](../../app/__init__.py), [app/config.py](../../app/config.py), [app/routes/api.py](../../app/routes/api.py), [app/services/word_service.py](../../app/services/word_service.py) |
| [app/routes/](../../app/routes/) | HTTP blueprints for API and web endpoints | [app/routes/api.py](../../app/routes/api.py), [app/routes/web.py](../../app/routes/web.py) |
| [app/services/](../../app/services/) | Business logic, pronunciation analysis, stress decoding | [app/services/word_service.py](../../app/services/word_service.py) |
| [app/static/](../../app/static/) | Frontend assets used by the web UI | [app/static/app.js](../../app/static/app.js) |
| [app/templates/](../../app/templates/) | Jinja templates for the web interface | [app/templates/index.html](../../app/templates/index.html) |
| [tests/](../../tests/) | Test suite for core service behavior | [tests/test_word_service.py](../../tests/test_word_service.py) |
| [run.py](../../run.py) | Script that builds the app and starts the server | [run.py](../../run.py) |
| [README.md](../../README.md) | Project intent and quick-start instructions | [README.md](../../README.md) |
| [requirements.txt](../../requirements.txt) | Dependency manifest | [requirements.txt](../../requirements.txt) |

### 2) Entry Points

- Main runtime entry: [run.py](../../run.py)
- Secondary entry points: none detected beyond the Flask app factory created in [app/__init__.py](../../app/__init__.py)
- How entry is selected: `run.py` calls `create_app()` and runs the Flask app with config-derived host/port values; [app/__init__.py](../../app/__init__.py) registers the API and web blueprints

### 3) Module Boundaries

| Boundary | What belongs here | What must not be here |
|----------|-------------------|------------------------|
| [app/routes/](../../app/routes/) | HTTP request handling, argument validation, and JSON responses | Business logic, pronunciation decoding, or persistence |
| [app/services/](../../app/services/) | Core word processing and phoneme-to-syllable interpretation | Route-specific response formatting or UI rendering |
| [app/templates/](../../app/templates/) | HTML rendering for the browser UI | Analysis logic or API behavior |
| [app/static/](../../app/static/) | Frontend JavaScript and static client assets | Server-defined business rules |
| [tests/](../../tests/) | Behavior validation for service-layer contracts | Production logic or deployment configuration |

### 4) Naming and Organization Rules

- File naming pattern: Python modules use snake_case (for example, `word_service.py`, `api.py`, `web.py`)
- Directory organization pattern: layered structure by concern (`routes`, `services`, `static`, `templates`)
- Import aliasing or path conventions: the app uses package imports such as `from app.config import settings` and `from app.routes import api, web`; no alias-heavy import conventions were detected

### 5) Evidence

- [app/__init__.py](../../app/__init__.py)
- [app/routes/api.py](../../app/routes/api.py)
- [app/services/word_service.py](../../app/services/word_service.py)
- [run.py](../../run.py)

## Extended Sections (Optional)

- No feature-based modularization was detected; the codebase is deliberately compact and service-oriented.
- The app does not contain generated output directories or compiled artifacts under source control.
