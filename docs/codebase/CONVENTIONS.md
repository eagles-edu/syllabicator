# Coding Conventions

## Core Sections (Required)

### 1) Naming Rules

| Item | Rule | Example | Evidence |
|------|------|---------|----------|
| Files | Python modules use snake_case | `word_service.py`, `api.py`, `web.py` | [app/services/word_service.py](../../app/services/word_service.py), [app/routes/api.py](../../app/routes/api.py) |
| Functions/methods | Methods and helpers use snake_case | `_normalize_word`, `_load_cmu_dict`, `analyze` | [app/services/word_service.py](../../app/services/word_service.py) |
| Types/interfaces | Classes use PascalCase | `WordAnalysisService`, `Config` | [app/services/word_service.py](../../app/services/word_service.py), [app/config.py](../../app/config.py) |
| Constants/env vars | Environment-backed values use uppercase names | `SECRET_KEY`, `HOST`, `PORT`, `FLASK_ENV` | [app/config.py](../../app/config.py) |

### 2) Formatting and Linting

- Formatter: [TODO] No repository-level formatter configuration detected in the project root
- Linter: `pylint` is declared in [requirements.txt](../../requirements.txt)
- Most relevant enforced rules: naming checks, unused imports, and basic code quality warnings are consistent with Pylint usage; no custom repo-specific formatting policy is present
- Run commands: `python -m pytest -q` (tests), `pylint ...` (if used locally)

### 3) Import and Module Conventions

- Import grouping/order: standard library imports come first (`re`, `typing`), then third-party imports (`nltk`), and app modules follow afterwards
- Alias vs relative import policy: app-level imports use package-qualified paths such as `from app.config import settings` and `from app.services.word_service import WordAnalysisService`; no complex aliasing pattern is in place
- Public exports/barrel policy: the repo does not use a `__init__.py` export layer beyond package registration; the app factory registers blueprints explicitly

### 4) Error and Logging Conventions

- Error strategy by layer: request handlers translate `ValueError` to `400` and `LookupError` to `404`; unexpected errors fall back to `500` in [app/routes/api.py](../../app/routes/api.py)
- Logging style and required context fields: no structured logger or request-id context is present in the repo; route errors are returned as JSON payloads
- Sensitive-data redaction rules: not applicable in this repo; there are no credential logs or external API traces present in source

### 5) Testing Conventions

- Test file naming/location rule: tests live under [tests/](../../tests/) and use the `test_*.py` naming pattern
- Mocking strategy norm: tests use direct service instantiation and real dictionary-backed behavior rather than mocking external dependencies
- Coverage expectation: [TODO] There is no configured coverage threshold or coverage report in the repository

### 6) Evidence

- [app/config.py](../../app/config.py)
- [app/services/word_service.py](../../app/services/word_service.py)
- [app/routes/api.py](../../app/routes/api.py)
- [tests/test_word_service.py](../../tests/test_word_service.py)

## Extended Sections (Optional)

- The codebase does not define a strong commit or branch policy in source; that is not part of the repository contents.
- There are no custom TypeScript or frontend lint conventions because the project is Python-first.
