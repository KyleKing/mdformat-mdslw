"""Debug test to understand table wrapping."""

import mdformat
from mdformat_slw import _sentence_wrapper

# Patch wrap_sentences to see when it's called
original_wrap = _sentence_wrapper.wrap_sentences

calls = []

def debug_wrap(text, node, context):
    parent_chain = []
    p = node.parent
    while p and not p.is_root:
        parent_chain.append(p.type)
        p = p.parent

    call_info = {
        "node_type": node.type,
        "parent_chain": parent_chain,
        "text_preview": text[:80],
    }
    calls.append(call_info)

    result = original_wrap(text, node, context)
    call_info["wrapped"] = result != text
    return result

_sentence_wrapper.wrap_sentences = debug_wrap

def test_table_debug():
    """Debug table wrapping behavior."""
    global calls
    calls = []

    # Use the FULL context like in pre-commit-test.md
    test_md = """## Tables

| Column 1 | Column 2 | Column 3 |
| --------------------------------- | ------------------------ | ---------------
| This cell has sentences. Multiple | Another cell. More text! | Final cell. End |
| Row two. More content! | Testing. Works! | Great. Done! |

## Custom Abbreviation Override
"""

    result = mdformat.text(test_md)

    print("\nAll wrap_sentences calls:")
    for i, call in enumerate(calls):
        print(f"\n[{i+1}] {call['node_type']}")
        print(f"    Parents: {' -> '.join(call['parent_chain'])}")
        print(f"    Text: {repr(call['text_preview'])}")
        print(f"    Wrapped: {call['wrapped']}")

    print("\nFinal result:")
    print(result)

    # Check if table content was wrapped (it shouldn't be)
    assert "This cell has sentences. Multiple" in result, f"Table should not be wrapped! Got:\n{result}"
