"""Integration tests for simplified configuration system."""

from __future__ import annotations

import mdformat

from mdformat_slw._sentence_wrapper import _get_suppression_words


def test_abbreviations_extend_is_default() -> None:
    """Test custom abbreviations extend language list by default."""
    text = "Dr. Smith works at NASA. Great!"
    result = mdformat.text(
        text,
        extensions={"slw"},
        options={
            "lang": "en",
            "abbreviations": "NASA",
            "slw_min_line": 0,
        },
    )
    # Both Dr (English) and NASA (custom) should be preserved
    assert "Dr. Smith works at NASA." in result
    assert "Great!" in result


def test_abbreviations_only_flag() -> None:
    """Test abbreviations-only flag ignores language lists."""
    text = "Dr. Smith works at NASA. Great!"
    result = mdformat.text(
        text,
        extensions={"slw"},
        options={
            "abbreviations_only": True,
            "abbreviations": "NASA",
            "slw_min_line": 0,
        },
    )
    # Dr should break (not in custom list), NASA should not
    assert "Dr.\n" in result
    assert "NASA." in result


def test_removed_options_do_not_affect_behavior() -> None:
    """Test that removed options don't break existing behavior."""
    # This should work without abbreviations_mode, suppressions, etc.
    text = "Dr. Smith arrived. He left."
    result = mdformat.text(
        text,
        extensions={"slw"},
        options={"slw_min_line": 0},
    )
    assert "Dr. Smith arrived.\nHe left." in result


def test_comma_separated_abbreviations() -> None:
    """Test comma-separated custom abbreviations work correctly."""
    text = "Visit NASA. headquarters or FBI. offices. Great tour!"
    result = mdformat.text(
        text,
        extensions={"slw"},
        options={
            "abbreviations": "NASA,FBI",
            "slw_min_line": 0,
        },
    )
    # Both NASA and FBI should be preserved
    assert "NASA. headquarters or FBI. offices." in result


def test_single_language_only() -> None:
    """Test only single language is supported."""
    options = {"mdformat": {"lang": "en"}}
    words = _get_suppression_words(options)
    # Should only contain English words
    assert "dr" in words  # English
    assert "mr" in words  # English
    # German-specific words should not be present
    assert "hrn" not in words  # German


def test_case_insensitive_always() -> None:
    """Test case-insensitive matching is always enabled."""
    # Lowercase abbreviation
    text1 = "dr. smith arrived. He left."
    result1 = mdformat.text(
        text1,
        extensions={"slw"},
        options={"slw_min_line": 0},
    )
    assert "dr. smith arrived.\nHe left." in result1

    # Uppercase abbreviation
    text2 = "DR. SMITH arrived. He left."
    result2 = mdformat.text(
        text2,
        extensions={"slw"},
        options={"slw_min_line": 0},
    )
    assert "DR. SMITH arrived.\nHe left." in result2

    # Mixed case abbreviation
    text3 = "Dr. Smith arrived. He left."
    result3 = mdformat.text(
        text3,
        extensions={"slw"},
        options={"slw_min_line": 0},
    )
    assert "Dr. Smith arrived.\nHe left." in result3
