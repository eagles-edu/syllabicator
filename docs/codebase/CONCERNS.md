# Codebase Concerns

## Core Sections (Required)

### 1) Top Risks (Prioritized)

| Severity | Concern | Evidence | Impact | Suggested action |
|----------|---------|----------|--------|------------------|
| Medium | Runtime dependency on NLTK CMU dictionary availability and download behavior | [app/services/word_service.py](../../app/services/word_service.py) | First-run runtime may fail or stall if the corpus is unavailable or download access is restricted | Ensure corpus/download setup is documented and validated in deployment environments |
| Medium | Default secret key is hard-coded in config | [app/config.py](../../app/config.py) | Production environments may reuse a weak default if `SECRET_KEY` is not overridden | Require environment configuration for real deployments |
| Low | The analysis logic is concentrated in one service class | [app/services/word_service.py](../../app/services/word_service.py) | As feature scope grows, the class may become harder to extend safely | Split heuristics and formatting logic into clearer helper modules as the app grows |

### 2) Technical Debt

| Debt item | Why it exists | Where | Risk if ignored | Suggested fix |
|-----------|---------------|-------|-----------------|---------------|
| Single-service analysis implementation | The project is intentionally small and currently centralizes phoneme processing in one class | [app/services/word_service.py](../../app/services/word_service.py) | Future feature growth could make the class harder to reason about | Extract helper functions or supporting modules as complexity increases |
| Minimal operational guardrails | The repo does not include deployment, monitoring, or environment policies | [README.md](../../README.md), [app/config.py](../../app/config.py) | Runtime drift is more likely outside local development | Add explicit deployment configuration and environment checks before production rollout |

### 3) Security Concerns

| Risk | OWASP category (if applicable) | Evidence | Current mitigation | Gap |
|------|--------------------------------|----------|--------------------|-----|
| Default secret fallback | A05 Security Misconfiguration | [app/config.py](../../app/config.py) | Config reads environment variables first | No enforcement that a unique secret is supplied in production |
| No auth or session protection | N/A | [app/__init__.py](../../app/__init__.py), [app/routes/api.py](../../app/routes/api.py) | App is intentionally single-user and teaching-focused | If exposed broadly, API endpoints remain unauthenticated |

### 4) Performance and Scaling Concerns

| Concern | Evidence | Current symptom | Scaling risk | Suggested improvement |
|---------|----------|-----------------|-------------|-----------------------|
| CMU dictionary is loaded lazily and cached in memory | [app/services/word_service.py](../../app/services/word_service.py) | Single-process memory holds the corpus after first load | A multi-process deployment would duplicate the memory footprint | Keep the model in-memory only for a single worker or cache at a shared layer if scale grows |
| No async or queue-based processing | [app/routes/api.py](../../app/routes/api.py) | Request handling stays synchronous and simple | The app is fine for small traffic but not optimized for high concurrency | Add worker or cache layers only if usage increases |

### 5) Fragile/High-Churn Areas

| Area | Why fragile | Churn signal | Safe change strategy |
|------|-------------|-------------|----------------------|
| [app/services/word_service.py](../../app/services/word_service.py) | Core pronunciation logic and syllable parsing are highly coupled in one place | Central file for app functionality and likely extension point | Keep business logic in this service layer; add helper functions before broad refactors |
| [app/config.py](../../app/config.py) | Environment settings are simple but directly affect app runtime | Small file but high runtime impact | Treat config changes as deploy-time configuration rather than code changes |

### 6) `[ASK USER]` Questions

1. [ASK USER] Should this remain a lightweight, single-user Flask teaching app, or do you want it pushed toward a more production-ready architecture with stronger deployment and security controls?

### 7) Evidence

- [docs/codebase/.codebase-scan.txt](.codebase-scan.txt)
- [app/services/word_service.py](../../app/services/word_service.py)
- [app/config.py](../../app/config.py)
- [app/routes/api.py](../../app/routes/api.py)

## Extended Sections (Optional)

- No existing incident history or bug queue was found in the repo snapshot reviewed here.
- There are no explicit benchmark or profiling artifacts in the current codebase.
