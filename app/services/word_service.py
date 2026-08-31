import re
from typing import Dict, List

import nltk
from nltk.corpus import cmudict


class WordAnalysisService:
    _cmudict: dict | None = None

    @classmethod
    def _load_cmu_dict(cls) -> dict:
        if cls._cmudict is None:
            try:
                nltk.data.find('corpora/cmudict')
            except LookupError:
                nltk.download('cmudict', quiet=True)
            cls._cmudict = cmudict.dict()
        return cls._cmudict

    @staticmethod
    def _normalize_word(word: str) -> str:
        cleaned = re.sub(r"[^a-zA-Z'-]", "", word).strip().lower()
        if not cleaned:
            raise ValueError("Word input is required.")
        return cleaned

    @classmethod
    def _get_stress_index(cls, phonemes: List[str]) -> int:
        for idx, phone in enumerate(phonemes):
            if phone.endswith("1"):
                return idx
        return 0

    @classmethod
    def _phoneme_to_syllable_points(cls, phonemes: List[str]) -> List[str]:
        syllables: List[str] = []
        current: List[str] = []
        prev_was_vowel = False

        for phone in phonemes:
            base = re.sub(r"\d$", "", phone)
            vowels = {
                'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY',
                'OW', 'OY', 'UH', 'UW'
            }
            is_vowel = base in vowels

            if is_vowel:
                current.append(phone)
                prev_was_vowel = True
            else:
                if prev_was_vowel and current:
                    syllables.append("".join(current))
                    current = []
                current.append(phone)
                prev_was_vowel = False

        if current:
            syllables.append("".join(current))

        return [re.sub(r"\d", "", s) for s in syllables if s]

    @classmethod
    def _get_stressed_syllable_index(cls, phonemes: List[str], syllables: List[str]) -> int:
        vowels = {
            'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY',
            'OW', 'OY', 'UH', 'UW'
        }
        stressed_phone_index = next(
            (idx for idx, phone in enumerate(phonemes) if phone.endswith("1")),
            0,
        )
        vowel_positions = [
            idx for idx, phone in enumerate(phonemes)
            if re.sub(r"\d$", "", phone) in vowels
        ]
        if not vowel_positions:
            return 0

        stressed_vowel_index = 0
        for idx, vowel_position in enumerate(vowel_positions):
            if vowel_position >= stressed_phone_index:
                stressed_vowel_index = idx
                break
        if stressed_phone_index == 0:
            stressed_vowel_index = 0

        return min(stressed_vowel_index, max(len(syllables) - 1, 0))

    @classmethod
    def _add_stress_marker(cls, syllables: List[str], stressed_index: int) -> str:
        if not syllables:
            return ""
        if stressed_index < 0 or stressed_index >= len(syllables):
            stressed_index = 0

        target = list(syllables[stressed_index])
        vowels = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "y": "ý"}
        for idx, char in enumerate(target):
            if char.lower() in vowels:
                target[idx] = vowels[char.lower()]
                break

        syllables = list(syllables)
        syllables[stressed_index] = "".join(target)
        return " · ".join(syllables)

    @classmethod
    def _calculate_cefr(cls, word: str) -> str:
        # Simple frequency-based approximation for teaching use.
        length = len(word)
        if length <= 3:
            return "A1"
        if length <= 5:
            return "A2"
        if length <= 8:
            return "B1"
        if length <= 10:
            return "B2"
        if length <= 12:
            return "C1"
        return "C2"

    def analyze(self, word: str) -> Dict[str, object]:
        cleaned = self._normalize_word(word)
        cmu = self._load_cmu_dict()

        # pylint: disable=unsupported-membership-test,unsubscriptable-object
        if cleaned not in cmu:
            raise LookupError(f"No pronunciation data found for '{cleaned}'.")

        pronunciation = cmu[cleaned]
        phonemes = pronunciation[0]
        syllables = self._phoneme_to_syllable_points(phonemes)
        stressed_index = self._get_stressed_syllable_index(phonemes, syllables)

        if not syllables:
            syllables = [cleaned]
            stressed_index = 0

        decoding = self._add_stress_marker(syllables, min(stressed_index, len(syllables) - 1))
        return {
            "word": cleaned,
            "syllables": syllables,
            "stressed_syllable_index": min(stressed_index, len(syllables) - 1),
            "decoding": decoding,
            "cefr": self._calculate_cefr(cleaned),
        }
