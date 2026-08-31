from flask import Blueprint, jsonify

from app.services.word_service import WordAnalysisService

bp = Blueprint("api", __name__, url_prefix="/api")
service = WordAnalysisService()


@bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@bp.get("/analyze/<word>")
def analyze_word(word):
    try:
        result = service.analyze(word)
        return jsonify(result)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except LookupError as exc:
        return jsonify({"error": str(exc)}), 404
    except Exception as exc:  # pragma: no cover - defensive fallback
        return jsonify({"error": str(exc)}), 500
