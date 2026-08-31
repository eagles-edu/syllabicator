# Testing Patterns

## Core Sections (Required)

### 1) Test Stack and Commands

- Primary test framework: `pytest` 8.3.2
- Assertion/mocking tools: direct assertions with `pytest.raises` and fixture-based service instantiation; no dedicated mocking library detected
- Commands:

```bash
python -m pytest -q
```

### 2) Test Layout

- Test file placement pattern: tests live under the repository-level [tests/](../../tests/) directory
- Naming convention: files are named `test_*.py` and functions use descriptive names like `test_word_service_handles_common_word`
- Setup files and where they run: no dedicated `conftest.py` or shared test bootstrap file was found

### 3) Test Scope Matrix

| Scope | Covered? | Typical target | Notes |
|-------|----------|----------------|-------|
| Unit | Yes | `WordAnalysisService` behavior | Covered in [tests/test_word_service.py](../../tests/test_word_service.py) |
| Integration | No | API/data boundaries | No API integration tests were found |
| E2E | No | Browser and end-to-end app flows | No browser or full-stack E2E suite was detected |

### 4) Mocking and Isolation Strategy

- Main mocking approach: no external-call mocking; the tests rely on the real `cmudict` data set and direct object instantiation
- Isolation guarantees: each test instantiates `WordAnalysisService` via a fixture, and the test cases focus on deterministic word-analysis behavior rather than shared state
- Common failure mode in tests: missing CMU dictionary data at runtime would cause the service to download it or fail; no mock fallback is present in tests

### 5) Coverage and Quality Signals

- Coverage tool + threshold: [TODO] no coverage configuration is present in the repo
- Current reported coverage: [TODO] not reported in repo files
- Known gaps/flaky areas: the suite validates a few representative words and input handling but does not cover API error responses, web routes, or edge-case pronunciation failures comprehensively

### 6) Evidence

- [requirements.txt](../../requirements.txt)
- [tests/test_word_service.py](../../tests/test_word_service.py)
- [README.md](../../README.md)

## Extended Sections (Optional)

- There is no CI workflow or coverage gate defined in the repository snapshot reviewed here.
- This project currently uses a compact unit-test approach rather than a formal suite of integration or end-to-end tests.
