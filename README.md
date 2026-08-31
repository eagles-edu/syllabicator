# Syllabicator

A teaching-first English word analysis app that decodes syllables and stress patterns for ESL learners.

## Features

- Word syllable and stress analysis
- CEFR estimation for learner guidance
- Clean web interface
- REST API for programmatic usage
- Ready for extension with classroom analytics, saved vocabulary, and pronunciation features

## Startup

1. Create and activate a virtual environment using Python 3.10 or newer:
   python3 -m venv .venv
   source .venv/bin/activate
2. Install dependencies:
   pip install -r requirements.txt
3. Start the app:
   python run.py
4. Open http://localhost:5000 in your browser.

Optional environment variables:
- `SECRET_KEY` — Flask secret key (default: `dev-secret-key`)
- `HOST` — server host (default: `0.0.0.0`)
- `PORT` — server port (default: `5000`)
- `FLASK_ENV` — set to `production` to disable Flask debug mode

The first time the app runs, it may automatically download the NLTK CMU Pronouncing Dictionary if it is not already available locally.

When starting locally with `python run.py`, the app will attempt to open your browser automatically unless `OPEN_BROWSER` is set to `0`, `false`, or `no`.

## Docker Compose

Build and run the app with Docker Compose:

  docker compose up --build

Then open http://localhost:5000.

Stop the app and remove containers with:

  docker compose down

## Operation

Use the web UI at `/` for interactive syllable and stress analysis.

Programmatic API endpoints:
- `GET /api/health` — service health check
- `GET /api/analyze/<word>` — return syllable, stress, and CEFR analysis for `<word>`

Example API request:

curl http://localhost:5000/api/analyze/beautiful

## Project structure

- app/
  - routes/
  - services/
  - static/
  - templates/
- tests/
- run.py

## Notes

This project intentionally keeps the core logic isolated in a service layer so it can be expanded later with additional features such as CSV vocabulary import, classroom dashboards, and pronunciation audio support.
