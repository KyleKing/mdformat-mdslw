"""Unit tests for language support."""

from __future__ import annotations

from mdformat_slw._language_data import DEFAULT_LANG, LANG_SUPPRESSIONS
from mdformat_slw._sentence_wrapper import _get_suppression_words


def test_all_documented_languages_exist() -> None:
    """Test all documented languages have suppression lists."""
    expected = {"ac", "en", "de", "es", "fr", "it"}
    assert set(LANG_SUPPRESSIONS.keys()) == expected


def test_default_language_is_ac() -> None:
    """Test default language is 'ac' (Author's Choice)."""
    assert DEFAULT_LANG == "ac"


def test_each_language_has_content() -> None:
    """Test each language list has at least one abbreviation."""
    for lang_code, words in LANG_SUPPRESSIONS.items():
        assert len(words) > 0, f"Language {lang_code} has empty list"


def test_english_contains_common_abbreviations() -> None:
    """Test English list contains expected abbreviations."""
    en_list = LANG_SUPPRESSIONS["en"]
    assert "Dr" in en_list
    assert "Mr" in en_list
    assert "Inc" in en_list


def test_german_contains_german_specific() -> None:
    """Test German list contains German-specific abbreviations."""
    de_list = LANG_SUPPRESSIONS["de"]
    assert "z.B" in de_list or any("z.b" in w.lower() for w in de_list)


def test_get_suppression_words_default() -> None:
    """Test default behavior uses AC language."""
    options = {"mdformat": {}}
    words = _get_suppression_words(options)
    assert len(words) > 0
    # AC list should contain common abbreviations (lowercase)
    assert "dr" in words
    assert "prof" in words


def test_get_suppression_words_english() -> None:
    """Test English language selection."""
    options = {"mdformat": {"lang": "en"}}
    words = _get_suppression_words(options)
    assert "dr" in words
    assert "mr" in words


def test_get_suppression_words_extend() -> None:
    """Test extending language list with custom abbreviations."""
    options = {
        "mdformat": {
            "lang": "en",
            "abbreviations": "CustomCorp,NASA",
        }
    }
    words = _get_suppression_words(options)
    assert "dr" in words  # From English list
    assert "customcorp" in words  # Custom (lowercased)
    assert "nasa" in words  # Custom (lowercased)


def test_get_suppression_words_only_mode() -> None:
    """Test abbreviations-only mode ignores language lists."""
    options = {
        "mdformat": {
            "lang": "en",
            "abbreviations_only": True,
            "abbreviations": "CustomCorp,NASA",
        }
    }
    words = _get_suppression_words(options)
    assert "dr" not in words  # English abbreviation excluded
    assert "customcorp" in words
    assert "nasa" in words


def test_get_suppression_words_always_lowercase() -> None:
    """Test all abbreviations are lowercased for case-insensitive matching."""
    options = {"mdformat": {"abbreviations": "NASA,Corp,Inc"}}
    words = _get_suppression_words(options)
    assert all(w.islower() or not w.isalpha() for w in words)


def test_single_language_only() -> None:
    """Test only single language is supported (not multi-language)."""
    # If multi-language was supported, this would parse as multiple languages
    # Now it should treat "en de" as a single (invalid) language code
    options = {"mdformat": {"lang": "en de"}}
    words = _get_suppression_words(options)
    # Should return empty set because "en de" is not a valid language code
    # (or it might return an empty list from LANG_SUPPRESSIONS.get())
    # Either way, it won't contain abbreviations from both English and German
    assert "hrn" not in words  # German-specific abbreviation should not be present
