import pytest

from app.services.word_service import WordAnalysisService


@pytest.fixture
def word_service_fixture():
    return WordAnalysisService()


def test_word_service_handles_common_word(word_service_fixture):
    result = word_service_fixture.analyze("beautiful")
    assert result["word"] == "beautiful"
    assert len(result["syllables"]) >= 2
    assert result["stressed_syllable_index"] >= 0
    assert "decoding" in result
    assert result["decoding"]


def test_word_service_stresses_primary_syllable(word_service_fixture):
    result = word_service_fixture.analyze("hello")
    assert result["syllables"] == ["he", "llo"] or len(result["syllables"]) == 2
    assert result["decoding"]
    assert "á" in result["decoding"] or "é" in result["decoding"] or "ó" in result["decoding"]


def test_word_service_rejects_empty_input(word_service_fixture):
    with pytest.raises(ValueError):
        word_service_fixture.analyze("   ")


def test_word_service_provides_cefr_value(word_service_fixture):
    result = word_service_fixture.analyze("calendar")
    assert result["cefr"] in {"A1", "A2", "B1", "B2", "C1", "C2"}


def test_word_service_maps_primary_stress_to_the_correct_syllable(word_service_fixture):
    for word, expected_index in {
        "hello": 1,
        "beautiful": 0,
        "calendar": 0,
    }.items():
        result = word_service_fixture.analyze(word)
        assert result["stressed_syllable_index"] == expected_index
        assert result["decoding"]
        assert any(vowel in result["decoding"] for vowel in "áéíóúý")
