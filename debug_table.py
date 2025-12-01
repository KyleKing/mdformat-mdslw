"""Debug table rendering to understand where wrapping happens."""

from markdown_it import MarkdownIt
from mdformat.renderer import MDRenderer, RenderContext, RenderTreeNode

# Import our plugin
from mdformat_slw import plugin

test_md = """| Column 1 |
| -------- |
| Cell. More |
"""

# Build markdown-it with table support
mdit = MarkdownIt("commonmark").enable("table")

# Apply plugin
plugin.update_mdit(mdit)

# Parse
tokens = mdit.parse(test_md)
tree = RenderTreeNode(tokens)

# Render with our postprocessors
context = RenderContext(
    renderer=MDRenderer(),
    options={},
    env={},
    postprocessors={"paragraph": [plugin.wrap_sentences]},
)

def render_debug(node: RenderTreeNode, ctx: RenderContext, indent: int = 0) -> str:
    """Render and show debug info."""
    prefix = "  " * indent

    # Get renderer function
    renderer = ctx.renderer.get_renderer(node.type)
    text = renderer(node, ctx) if renderer else ""

    # Apply postprocessors
    for pp in ctx.postprocessors.get(node.type, []):
        print(f"{prefix}Postprocessing {node.type}: {repr(text[:50])}")
        text = pp(text, node, ctx)
        print(f"{prefix}  -> Result: {repr(text[:50])}")

    print(f"{prefix}{node.type}: {repr(text[:50])}")
    return text

# Recursively show tree and rendering
def show_render(node: RenderTreeNode, ctx: RenderContext, indent: int = 0):
    """Show rendering of tree."""
    render_debug(node, ctx, indent)
    for child in node.children:
        show_render(child, ctx, indent + 1)

show_render(tree, context)

# Do full render
result = context.renderer.render(tree, context)
print("\nFinal result:")
print(result)
