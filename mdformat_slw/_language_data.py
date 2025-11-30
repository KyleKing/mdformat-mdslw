"""Language-specific word lists for abbreviation detection.

This module provides suppression word lists for different languages.
Words in these lists won't trigger sentence wrapping when followed by
sentence-ending punctuation.

Based on slw's approach with Unicode CLDR-inspired lists.
"""

from __future__ import annotations

# Author's Choice (ac) - Curated English list (default)
# These are common abbreviations that should not trigger sentence breaks
_AC_SUPPRESSIONS = [
    # Titles
    "Dr",
    "Mr",
    "Mrs",
    "Ms",
    "Prof",
    "Sr",
    "Jr",
    # Time
    "a.m",
    "p.m",
    "A.M",
    "P.M",
    # Latin abbreviations
    "e.g",
    "i.e",
    "etc",
    "et al",
    "vs",
    "viz",
    "cf",
    "ca",
    # Academic/Professional
    "Ph.D",
    "M.D",
    "B.A",
    "M.A",
    "B.S",
    "M.S",
    "D.D.S",
    "Esq",
    # Business
    "Inc",
    "Ltd",
    "Corp",
    "Co",
    "LLC",
    # Geography
    "St",
    "Ave",
    "Blvd",
    "Rd",
    "Mt",
    "Ft",
    # Misc
    "No",
    "Nos",
    "Vol",
    "pp",
    "Fig",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Sept",
    "Oct",
    "Nov",
    "Dec",
]

# English (en) - Standard Unicode-based list
_EN_SUPPRESSIONS = [
    "Dr",
    "Mr",
    "Mrs",
    "Ms",
    "Prof",
    "Sr",
    "Jr",
    "e.g",
    "i.e",
    "etc",
    "vs",
    "Inc",
    "Ltd",
    "Corp",
    "St",
    "Ave",
]

# German (de) - Common German abbreviations
_DE_SUPPRESSIONS = [
    "Dr",
    "Prof",
    "Hrn",
    "Fr",
    "Frau",
    "z.B",
    "d.h",
    "u.a",
    "usw",
    "bzw",
    "evtl",
    "ggf",
    "inkl",
    "etc",
]

# Spanish (es) - Common Spanish abbreviations
_ES_SUPPRESSIONS = [
    "Dr",
    "Sr",
    "Sra",
    "Srta",
    "D",
    "Dña",
    "p.ej",
    "es decir",
    "etc",
    "vs",
    "S.A",
    "Ltda",
]

# French (fr) - Common French abbreviations
_FR_SUPPRESSIONS = [
    "Dr",
    "M",
    "Mme",
    "Mlle",
    "Prof",
    "p.ex",
    "c.-à-d",
    "etc",
    "vs",
    "S.A",
    "Cie",
]

# Italian (it) - Common Italian abbreviations
_IT_SUPPRESSIONS = [
    "Dr",
    "Sig",
    "Sig.ra",
    "Prof",
    "es",
    "cioè",
    "ecc",
    "vs",
    "S.p.A",
]

# Main mapping of language codes to suppression lists
LANG_SUPPRESSIONS: dict[str, list[str]] = {
    "ac": _AC_SUPPRESSIONS,
    "en": _EN_SUPPRESSIONS,
    "de": _DE_SUPPRESSIONS,
    "es": _ES_SUPPRESSIONS,
    "fr": _FR_SUPPRESSIONS,
    "it": _IT_SUPPRESSIONS,
}

# Default language
DEFAULT_LANG = "ac"
