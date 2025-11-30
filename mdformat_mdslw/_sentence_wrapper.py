"""Sentence wrapping logic inspired by mdslw."""

from __future__ import annotations

import functools
import logging
import re
from typing import TYPE_CHECKING

from ._helpers import get_conf
from ._language_data import DEFAULT_LANG, LANG_SUPPRESSIONS

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from collections.abc import Mapping
    from typing import Any

    from mdformat.renderer import RenderContext, RenderTreeNode

    ContextOptions = Mapping[str, Any]

# Default configuration constants
DEFAULT_SENTENCE_MARKERS = ".!?:"


class ConfigurationError(ValueError):
    """Raised when configuration values are invalid."""


def _validate_sentence_markers(markers: str) -> None:
    """Validate sentence markers string.

    Args:
        markers: String of sentence ending characters

    Raises (via _validate_sentence_markers):
        ConfigurationError: If markers is empty or invalid

    """
    if not markers:
        msg = "sentence_markers cannot be empty"
        raise ConfigurationError(msg)
    if len(markers) > 50:  # noqa: PLR2004
        msg = f"sentence_markers too long (max 50 chars): {len(markers)}"
        raise ConfigurationError(msg)


@functools.lru_cache(maxsize=128)
def _compile_sentence_pattern(sentence_markers: str) -> re.Pattern[str]:
    """Compile regex pattern for sentence ending detection.

    Compiles regex pattern with standard quantifiers for Python 3.10+ compatibility
    The pattern is cached to improve performance.

    Args:
        sentence_markers: String of characters that mark sentence endings

    Returns:
        Compiled regex pattern

    """
    _validate_sentence_markers(sentence_markers)
    marker_class = re.escape(sentence_markers)
    # Note: Using standard quantifiers (*) - possessive quantifiers not available in Python 3.10
    # Pattern: (marker)(optional closing chars)(whitespace)
    pattern = r"([" + marker_class + r"])(\s*[\"'\)\]\}]*)\s+"
    return re.compile(pattern)


def should_wrap_sentences(options: ContextOptions) -> bool:
    """Check if sentence wrapping is enabled via CLI or config.

    Sentence wrapping is ENABLED by default. Use --no-wrap-sentences to disable.

    Args:
        options: Configuration options from mdformat context

    Returns:
        True if sentence wrapping is enabled (default: True)

    """
    no_wrap = get_conf(options, "no_wrap_sentences")
    if no_wrap is not None:
        return not bool(no_wrap)
    return True  # Default: enabled


def get_sentence_markers(options: ContextOptions) -> str:
    """Get sentence ending markers from config.

    Args:
        options: Configuration options from mdformat context

    Returns:
        String of sentence ending characters (default: .!?:)

    Raises (via _validate_sentence_markers):
        ConfigurationError: If markers are invalid

    """
    markers = get_conf(options, "mdslw_markers")
    result = str(markers) if markers is not None else DEFAULT_SENTENCE_MARKERS
    _validate_sentence_markers(result)
    return result


def get_mdslw_wrap_width(options: ContextOptions) -> int:
    """Get line wrap width from mdslw's --mdslw-wrap setting.

    Args:
        options: Configuration options from mdformat context

    Returns:
        Maximum line width in characters, or 0 to disable wrapping (default: 0)

    """
    wrap_width = get_conf(options, "mdslw_wrap")
    return int(wrap_width) if wrap_width is not None else 0


def _get_suppression_words(options: ContextOptions) -> set[str]:
    """Build complete set of words that suppress sentence wrapping.

    Combines language-specific defaults with custom suppressions/ignores.
    Handles case sensitivity based on configuration.

    Args:
        options: Configuration options from mdformat context

    Returns:
        Set of words that should not trigger sentence breaks

    """
    mode = get_conf(options, "abbreviations_mode")
    if mode is None:
        mode = "default"
    mode = str(mode)

    # Mode: off - disable all abbreviation detection
    if mode == "off":
        return set()

    # Start with language-specific defaults
    words: set[str] = set()
    if mode in {"default", "extend"}:
        lang_str = get_conf(options, "lang")
        langs = str(lang_str).split() if lang_str else [DEFAULT_LANG]
        for lang in langs:
            words.update(LANG_SUPPRESSIONS.get(lang, []))

    # Handle custom abbreviations
    custom = get_conf(options, "abbreviations")
    if custom:
        # Parse custom abbreviations (comma-separated string)
        custom_words = str(custom).split(",")
        custom_words = [w.strip() for w in custom_words]

        if mode == "override":
            words = set(custom_words)
        else:  # extend or default mode
            words.update(custom_words)

    # Add extra suppressions
    suppressions = get_conf(options, "suppressions")
    if suppressions:
        supp_words = str(suppressions).split()
        words.update(supp_words)

    # Remove ignored words
    ignores = get_conf(options, "ignores")
    if ignores:
        ignore_words = str(ignores).split()
        words -= set(ignore_words)

    # Handle case sensitivity
    case_sensitive = get_conf(options, "case_sensitive")
    if not case_sensitive:
        # Convert to lowercase for case-insensitive matching
        words = {w.lower() for w in words}

    return words


def _wrap_long_line(line: str, max_width: int) -> list[str]:
    """Wrap a single long line into multiple lines.

    Args:
        line: The line to wrap
        max_width: Maximum width in characters

    Returns:
        List of wrapped lines

    """
    if len(line) <= max_width:
        return [line]

    words = line.split()
    wrapped_lines = []
    current_line: list[str] = []
    current_length = 0

    for word in words:
        word_len = len(word)
        # Calculate space needed: word length + 1 for space (if not first word)
        space_needed = word_len + (1 if current_line else 0)

        if current_length + space_needed > max_width and current_line:
            # Current line would exceed max_width, flush it
            wrapped_lines.append(" ".join(current_line))
            current_line = [word]
            current_length = word_len
        else:
            # Add word to current line
            current_line.append(word)
            current_length += space_needed

    if current_line:
        wrapped_lines.append(" ".join(current_line))

    return wrapped_lines


def wrap_sentences(  # noqa: C901
    text: str,
    _node: RenderTreeNode,
    context: RenderContext,
) -> str:
    """Wrap text by inserting line breaks after sentences.

    This is inspired by mdslw's sentence-wrapping behavior:
    - Insert line breaks after sentence-ending punctuation
    - Optionally wrap long lines using --mdslw-wrap setting
    - Preserve existing formatting for code blocks and special syntax
    - Respect abbreviations and suppression words

    Note: The _node parameter is required by mdformat's postprocessor
    interface but is not used in this implementation.

    Args:
        text: The rendered text to process
        _node: The syntax tree node being rendered (required by interface)
        context: The rendering context with configuration options

    Returns:
        The text with sentence breaks applied

    Raises (via _validate_sentence_markers):
        ConfigurationError: If configuration values are invalid

    """
    if not should_wrap_sentences(context.options):
        return text

    # Don't wrap if text is empty or just whitespace
    if not text or not text.strip():
        return text

    # Warn if mdformat's --wrap is set (potential conflict)
    mdformat_wrap = context.options.get("mdformat", {}).get("wrap")
    if mdformat_wrap is not None and mdformat_wrap not in {"keep", None}:
        logger.warning(
            "mdformat's --wrap is set to '%s'. "
            "Consider using --wrap=keep to avoid conflicts with mdslw sentence wrapping. "
            "Use --mdslw-wrap instead for line width control.",
            mdformat_wrap,
        )

    sentence_markers = get_sentence_markers(context.options)
    wrap_width = get_mdslw_wrap_width(context.options)
    suppression_words = _get_suppression_words(context.options)
    case_sensitive = get_conf(context.options, "case_sensitive")

    # Pattern to find potential sentence boundaries
    marker_class = re.escape(sentence_markers)
    # Match: marker + optional closing chars + whitespace
    boundary_pattern = re.compile(r"([" + marker_class + r"])(\s*[\"'\)\]\}]*)\s+")

    def _replace_with_newline(match: re.Match[str]) -> str:
        """Replace sentence ending with newline, checking suppressions."""
        marker = match.group(1)  # Sentence marker
        closing = match.group(2)  # Closing chars

        # Get text before this match to check for suppression words
        start_pos = match.start()
        text_before = text[:start_pos]

        # Check if any suppression word appears at the end of text_before
        if suppression_words:
            for supp_word in suppression_words:
                # Build pattern to check if suppression word appears before marker
                # Handle both "word." and "word" cases
                if case_sensitive:
                    check_pattern = re.escape(supp_word)
                else:
                    check_pattern = re.escape(supp_word)

                # Check if text_before ends with this suppression word
                # Allow for period-separated abbreviations like "p.m"
                pattern_to_check = r"\b" + check_pattern.replace(r"\.", r"\.") + r"$"
                if case_sensitive:
                    if re.search(pattern_to_check, text_before):
                        return match.group(0)
                elif re.search(pattern_to_check, text_before, re.IGNORECASE):
                    return match.group(0)

        # No suppression match - wrap with newline
        return f"{marker}{closing}\n"

    # Apply sentence breaks
    wrapped = boundary_pattern.sub(_replace_with_newline, text)

    # Optional: wrap long lines using --mdslw-wrap setting
    if wrap_width > 0:
        lines = wrapped.split("\n")
        wrapped_lines = []
        for line in lines:
            wrapped_lines.extend(_wrap_long_line(line, wrap_width))
        wrapped = "\n".join(wrapped_lines)

    return wrapped
