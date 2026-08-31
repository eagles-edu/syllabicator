# External Integrations

## Core Sections (Required)

### 1) Integration Inventory

| System | Type (API/DB/Queue/etc) | Purpose | Auth model | Criticality | Evidence |
|--------|---------------------------|---------|------------|-------------|----------|
| CMU Pronouncing Dictionary (NLTK `cmudict`) | Local data corpus / library dependency | Supplies word pronunciations used to identify syllables and stress | None in-app; corpus is loaded from the local NLTK data set | High | [app/services/word_service.py](../../app/services/word_service.py), [requirements.txt](../../requirements.txt) |
| Flask web app | In-process web framework | Serves the browser UI and API endpoints | None beyond app-level config | High | [app/__init__.py](../../app/__init__.py), [app/routes/api.py](../../app/routes/api.py) |

### 2) Data Stores

| Store | Role | Access layer | Key risk | Evidence |
|-------|------|--------------|----------|----------|
| NLTK corpus cache | Local pronunciation dictionary cache | `nltk.data.find()` and `cmudict.dict()` in service logic | First-run availability depends on the corpus download and local environment readiness | [app/services/word_service.py](../../app/services/word_service.py) |
| No external DB | None | None | No persistence or transaction layer exists in the app | [README.md](../../README.md), [app/services/word_service.py](../../app/services/word_service.py) |

### 3) Secrets and Credentials Handling

- Credential sources: runtime environment variables via `os.getenv()` in [app/config.py](../../app/config.py)
- Hardcoding checks: a default fallback secret (`"dev-secret-key"`) is embedded in the config; no production secret provider is configured
- Rotation or lifecycle notes: [TODO] No secret-management workflow or rotation policy is defined in the repo

### 4) Reliability and Failure Behavior

- Retry/backoff behavior: none implemented for NLTK corpus lookup or pronunciation access
- Timeout policy: none configured in source code
- Circuit-breaker or fallback behavior: the route layer catches `LookupError` and returns a `404` when a pronunciation is unavailable; unexpected exceptions return `500`

### 5) Observability for Integrations

- Logging around external calls: no dedicated logging around the CMU dictionary access path
- Metrics/tracing coverage: none detected in source or config
- Missing visibility gaps: no request correlation, metrics, or external-call telemetry were found in the repo

### 6) Evidence

- [app/services/word_service.py](../../app/services/word_service.py)
- [app/config.py](../../app/config.py)
- [app/routes/api.py](../../app/routes/api.py)
- [requirements.txt](../../requirements.txt)

## Extended Sections (Optional)

- There are no external APIs, message queues, or persistence systems beyond the local NLTK corpus dependency.
- This repository is intentionally narrow and does not yet define contract monitoring, SLOs, or region-failover concerns.
