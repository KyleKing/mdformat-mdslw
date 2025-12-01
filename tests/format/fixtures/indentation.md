list item with multiple sentences aggressive mode
.
- First list item has one sentence. It also has another sentence! Does it work?
.
- First list item has one sentence.
  It also has another sentence!
  Does it work?
.
--slw-min-line=0

nested list multiple sentences aggressive mode
.
- Top level item starts here. It continues!
  - Nested item has text. More sentences follow?
.
- Top level item starts here.
  It continues!
  - Nested item has text.
    More sentences follow?
.
--slw-min-line=0

blockquote with sentences aggressive mode
.
> This is a quoted sentence. It has multiple parts! Does quote wrapping work?
.
> This is a quoted sentence.
> It has multiple parts!
> Does quote wrapping work?
.
--slw-min-line=0

no indentation baseline (under min-line)
.
This has no indentation. Normal wrapping applies!
.
This has no indentation. Normal wrapping applies!
.

no indentation baseline aggressive mode
.
This has no indentation. Normal wrapping applies!
.
This has no indentation.
Normal wrapping applies!
.
--slw-min-line=0

long line wrapping at 40 chars
.
This is a very long sentence that will exceed forty characters easily and should wrap!
.
This is a very long sentence that will
exceed forty characters easily and
should wrap!
.
--slw-wrap=40

long line wrapping with 88 chars default
.
This is an extraordinarily long sentence with many words that will certainly exceed the eighty-eight character maximum line width when we enable wrapping!
.
This is an extraordinarily long sentence with many words that will certainly exceed the
eighty-eight character maximum line width when we enable wrapping!
.

wrapping disabled with zero aggressive mode
.
This is a very long sentence. It won't wrap with zero! The setting disables wrapping?
.
This is a very long sentence.
It won't wrap with zero!
The setting disables wrapping?
.
--slw-wrap=0
--slw-min-line=0
