"""Edge case tests for mdformat-mdslw plugin."""

from __future__ import annotations

import pytest

from mdformat_mdslw._sentence_wrapper import (
    DEFAULT_MAX_LINE_WIDTH,
    DEFAULT_SENTENCE_MARKERS,
    MAX_LINE_WIDTH,
    ConfigurationError,
    get_max_line_width,
    get_sentence_markers,
)


def test_empty_sentence_markers_raises_error() -> None:
    """Test that empty sentence markers raises ConfigurationError."""
    options = {"mdformat": {"plugin": {"mdslw": {"sentence_markers": ""}}}}
    with pytest.raises(ConfigurationError, match="sentence_markers cannot be empty"):
        get_sentence_markers(options)


def test_too_long_sentence_markers_raises_error() -> None:
    """Test that excessively long sentence markers raises ConfigurationError."""
    options = {"mdformat": {"sentence_markers": "x" * 51}}
    with pytest.raises(ConfigurationError, match="sentence_markers too long"):
        get_sentence_markers(options)


def test_max_line_width_below_minimum_raises_error() -> None:
    """Test that max_line_width below minimum raises ConfigurationError."""
    options = {"mdformat": {"max_line_width": -1}}
    with pytest.raises(
        ConfigurationError, match="max_line_width must be 0-10000, got -1"
    ):
        get_max_line_width(options)


def test_max_line_width_above_maximum_raises_error() -> None:
    """Test that max_line_width above maximum raises ConfigurationError."""
    options = {"mdformat": {"max_line_width": MAX_LINE_WIDTH + 1}}
    with pytest.raises(
        ConfigurationError, match="max_line_width must be 0-10000, got 10001"
    ):
        get_max_line_width(options)


def test_max_line_width_at_boundary_minimum() -> None:
    """Test that max_line_width at minimum boundary (0) is valid."""
    options = {"mdformat": {"plugin": {"mdslw": {"max_line_width": 0}}}}
    result = get_max_line_width(options)
    assert result == 0


def test_max_line_width_at_boundary_maximum() -> None:
    """Test that max_line_width at maximum boundary is valid."""
    options = {"mdformat": {"max_line_width": MAX_LINE_WIDTH}}
    result = get_max_line_width(options)
    assert result == MAX_LINE_WIDTH


def test_default_sentence_markers() -> None:
    """Test default sentence markers when none specified."""
    options = {"mdformat": {}}
    result = get_sentence_markers(options)
    assert result == DEFAULT_SENTENCE_MARKERS


def test_default_max_line_width() -> None:
    """Test default max_line_width when none specified."""
    options = {"mdformat": {}}
    result = get_max_line_width(options)
    assert result == DEFAULT_MAX_LINE_WIDTH


def test_custom_sentence_markers() -> None:
    """Test custom sentence markers."""
    options = {"mdformat": {"sentence_markers": ".!?"}}
    result = get_sentence_markers(options)
    assert result == ".!?"


def test_custom_max_line_width() -> None:
    """Test custom max_line_width."""
    custom_width = 100
    options = {"mdformat": {"max_line_width": custom_width}}
    result = get_max_line_width(options)
    assert result == custom_width


def test_special_characters_in_sentence_markers() -> None:
    """Test sentence markers with special regex characters."""
    options = {"mdformat": {"sentence_markers": ".!?*+[]"}}
    result = get_sentence_markers(options)
    assert result == ".!?*+[]"
