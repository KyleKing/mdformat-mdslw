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
    # Titles
    "Dr",
    "Prof",
    "Herr",
    "Hrn",
    "Fr",
    "Frau",
    "Frl",
    "Dr. med",
    # Latin/common abbreviations
    "z.B",
    "d.h",
    "u.a",
    "usw",
    "bzw",
    "evtl",
    "ggf",
    "inkl",
    "etc",
    "i.e",
    "e.g",
    # Business
    "GmbH",
    "AG",
    "Corp",
    "Inc",
    # Months
    "Jan",
    "Feb",
    "Mrz",
    "Apr",
    "Mai",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Okt",
    "Nov",
    "Dez",
    # Days
    "Mo",
    "Di",
    "Mi",
    "Do",
    "Fr",
    "Sa",
    "So",
    # Location
    "Str",
    "Hauptstr",
    # Misc
    "ca",
    "Uhr",
]

# Spanish (es) - Common Spanish abbreviations
_ES_SUPPRESSIONS = [
    # Titles
    "Dr",
    "Dra",
    "Sr",
    "Sra",
    "Srta",
    "D",
    "Dña",
    "Prof",
    # Latin abbreviations
    "p.ej",
    "es decir",
    "etc",
    "vs",
    "i.e",
    "e.g",
    # Business
    "S.A",
    "Ltda",
    "Cia",
    "Corp",
    "Inc",
    # Months
    "ene",
    "feb",
    "mar",
    "abr",
    "may",
    "jun",
    "jul",
    "ago",
    "sep",
    "oct",
    "nov",
    "dic",
    # Days
    "lun",
    "mar",
    "mié",
    "jue",
    "vie",
    "sáb",
    "dom",
    # Misc
    "aprox",
    "ca",
    "p.m",
    "a.m",
]

# French (fr) - Common French abbreviations
_FR_SUPPRESSIONS = [
    # Titles
    "Dr",
    "M",
    "Mme",
    "Mlle",
    "MM",
    "Prof",
    "Dr. med",
    # Latin/common abbreviations
    "p.ex",
    "c.-à-d",
    "etc",
    "vs",
    "i.e",
    "e.g",
    # Business
    "S.A",
    "S.A.R.L",
    "Cie",
    "Corp",
    "Inc",
    # Months
    "janv",
    "févr",
    "mars",
    "avr",
    "mai",
    "juin",
    "juil",
    "août",
    "sept",
    "oct",
    "nov",
    "déc",
    # Days
    "lun",
    "mar",
    "mer",
    "jeu",
    "ven",
    "sam",
    "dim",
    # Location
    "bd",
    "av",
    "rue",
    # Misc
    "env",
    "ca",
    "h",
]

# Italian (it) - Common Italian abbreviations
_IT_SUPPRESSIONS = [
    # Titles
    "Dr",
    "Dott",
    "Dr.ssa",
    "Sig",
    "Sig.ra",
    "Sig.na",
    "Sigg",
    "Prof",
    "Prof.ssa",
    # Latin/common abbreviations
    "es",
    "cioè",
    "ecc",
    "vs",
    "i.e",
    "e.g",
    # Business
    "S.p.A",
    "S.r.l",
    "Corp",
    "Inc",
    # Months
    "genn",
    "febbr",
    "mar",
    "apr",
    "magg",
    "giugno",
    "luglio",
    "ag",
    "sett",
    "ott",
    "nov",
    "dic",
    # Days
    "lun",
    "mar",
    "mer",
    "gio",
    "ven",
    "sab",
    "dom",
    # Location
    "via",
    "c.so",
    "p.za",
    # Misc
    "ca",
    "ore",
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
