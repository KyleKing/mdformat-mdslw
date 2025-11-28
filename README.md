# mdformat-mdslw

[![Build Status][ci-badge]][ci-link] [![PyPI version][pypi-badge]][pypi-link]

An [mdformat](https://github.com/executablebooks/mdformat) plugin for [mdslw](https://github.com/razziel89/mdslw)-style sentence wrapping.

This plugin wraps markdown text by inserting line breaks after sentence-ending punctuation, making diffs cleaner and easier to review.

## Features

- Wrap sentences at configurable punctuation marks (default: `.!?:`)
- Optional maximum line width enforcement
- Preserves markdown formatting (bold, italic, links, etc.)
- Handles edge cases: quoted text, parentheses, brackets

## `mdformat` Usage

Add this package wherever you use `mdformat` and the plugin will be auto-recognized. No additional configuration necessary. See [additional information on `mdformat` plugins here](https://mdformat.readthedocs.io/en/stable/users/plugins.html)

### CLI

```sh
mdformat --wrap-sentences document.md
```

#### Options

- `--wrap-sentences`: Enable sentence wrapping (required to activate the plugin)
- `--sentence-markers TEXT`: Characters that mark sentence endings (default: `.!?:`)
- `--max-line-width INTEGER`: Maximum line width for wrapping (default: 80, 0 to disable)

### Configuration File

Create a `.mdformat.toml` file in your project root:

```toml
[plugin.mdslw]
wrap_sentences = true
sentence_markers = ".!?:"
max_line_width = 80
```

### pre-commit / prek

```yaml
repos:
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.19
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-mdslw
        args: [--wrap-sentences]
```

### uvx

```sh
uvx --with mdformat-mdslw mdformat --wrap-sentences document.md
```

Or with pipx:

```sh
pipx install mdformat
pipx inject mdformat mdformat-mdslw
mdformat --wrap-sentences document.md
```

### Python API

```python
import mdformat

text = """
This is a test. It has multiple sentences! Does it work?
"""

# Enable sentence wrapping
result = mdformat.text(text, extensions={"mdslw"}, options={"wrap_sentences": True})

print(result)
# Output:
# This is a test.
# It has multiple sentences!
# Does it work?
```

## Example

**Input:**

```markdown
This is a long sentence. It contains multiple clauses! Does it work? Yes it does.
```

**Output (with `--wrap-sentences`):**

```markdown
This is a long sentence.
It contains multiple clauses!
Does it work?
Yes it does.
```

## Contributing

See [CONTRIBUTING.md](https://github.com/kyleking/mdformat-mdslw/blob/main/CONTRIBUTING.md)

[ci-badge]: https://github.com/kyleking/mdformat-mdslw/actions/workflows/tests.yml/badge.svg?branch=main
[ci-link]: https://github.com/kyleking/mdformat-mdslw/actions?query=workflow%3ACI+branch%3Amain+event%3Apush
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-mdslw.svg
[pypi-link]: https://pypi.org/project/mdformat-mdslw
