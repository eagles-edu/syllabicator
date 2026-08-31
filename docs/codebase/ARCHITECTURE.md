# Architecture

## Core Sections (Required)

### 1) Architectural Style

- Primary style: layered / service-oriented Flask app
- Why this classification: Route handlers delegate to a dedicated service object and the app factory wires blueprints, which matches a thin-controller / rich-service split
- Primary constraints: no database layer, no authentication system, and a runtime dependency on NLTK CMU dictionary data for pronunciation lookups

### 2) System Flow

```text
run.py -> app.create_app() -> blueprint registration -> /api/analyze/<word> route -> WordAnalysisService.analyze() -> nltk cmudict lookup -> syllable/stress decoding -> JSON response
```

The flow is implemented as follows: [run.py](../../run.py) starts the app; [app/__init__.py](../../app/__init__.py) creates the Flask app and registers API and web blueprints; [app/routes/api.py](../../app/routes/api.py) handles HTTP requests and returns JSON responses; [app/services/word_service.py](../../app/services/word_service.py) normalizes the word, looks up the pronunciation from the CMU dictionary, splits phonemes into syllables, applies stress markers, and returns the structured result.

### 3) Layer/Module Responsibilities

| Layer or module | Owns | Must not own | Evidence |
|-----------------|------|--------------|----------|
| [app/routes/api.py](../../app/routes/api.py) | HTTP request handling, response codes, JSON serialization | Business logic or pronunciation heuristics | [app/routes/api.py](../../app/routes/api.py) |
| [app/services/word_service.py](../../app/services/word_service.py) | Word normalization, CMU dictionary lookup, stress decoding, CEFR estimate | Route/HTML concerns | [app/services/word_service.py](../../app/services/word_service.py) |
| [app/routes/web.py](../../app/routes/web.py) | Browser page rendering and web UI routing | Core analysis algorithm implementation | [app/routes/web.py](../../app/routes/web.py) |
| [app/config.py](../../app/config.py) | Runtime environment settings and defaults | Domain logic or request handling | [app/config.py](../../app/config.py) |

### 4) Reused Patterns

| Pattern | Where found | Why it exists |
|---------|-------------|---------------|
| App factory | [app/__init__.py](../../app/__init__.py) | Keeps app creation centralized and makes blueprint registration explicit |
| Blueprint registration | [app/__init__.py](../../app/__init__.py), [app/routes/api.py](../../app/routes/api.py), [app/routes/web.py](../../app/routes/web.py) | Separates API and web route concerns cleanly |
| Service object pattern | [app/services/word_service.py](../../app/services/word_service.py) | Keeps core analysis logic isolated from Flask request handling |
| Dataclass config | [app/config.py](../../app/config.py) | Provides typed defaults for environment-driven settings |

### 5) Known Architectural Risks

- Runtime dependency on the NLTK CMU dictionary makes first-run behavior dependent on corpus availability and network access if the data is absent
- The service layer is central to the app and could grow complex as more features are added, because it currently contains both dictionary access and pedagogical output logic
- The app has no persistence, auth, or multi-user model; it is intentionally a focused teaching prototype rather than a full production application

### 6) Evidence

- [run.py](../../run.py)
- [app/__init__.py](../../app/__init__.py)
- [app/routes/api.py](../../app/routes/api.py)
- [app/services/word_service.py](../../app/services/word_service.py)

## Extended Sections (Optional)

- No async/event-driven runtime, queue processing, or background worker topology was detected.
- No database or caching layer is present beyond the in-memory CMU dictionary cache used inside the service class.
