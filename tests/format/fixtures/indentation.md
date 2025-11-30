list item with multiple sentences
.
- First list item has one sentence. It also has another sentence! Does it work?
.
- First list item has one sentence.
  It also has another sentence!
  Does it work?
.

nested list multiple sentences
.
- Top level item starts here. It continues!
  - Nested item has text. More sentences follow?
.
- Top level item starts here.
  It continues!
  - Nested item has text.
    More sentences follow?
.

blockquote with sentences
.
> This is a quoted sentence. It has multiple parts! Does quote wrapping work?
.
> This is a quoted sentence.
> It has multiple parts!
> Does quote wrapping work?
.

no indentation baseline
.
This has no indentation. Normal wrapping applies!
.
This has no indentation.
Normal wrapping applies!
.

long line wrapping at 40 chars
.
This is a very long sentence that will exceed forty characters easily and should wrap!
.
This is a very long sentence that will
exceed forty characters easily and
should wrap!
.
--slw-wrap 40

long line wrapping with 80 chars default
.
This is an extraordinarily long sentence with many words that will certainly exceed the eighty character maximum line width when we enable wrapping!
.
This is an extraordinarily long sentence with many words that will certainly
exceed the eighty character maximum line width when we enable wrapping!
.
--slw-wrap 80

wrapping disabled with zero
.
This is a very long sentence. It won't wrap with zero! The setting disables wrapping?
.
This is a very long sentence.
It won't wrap with zero!
The setting disables wrapping?
.
--slw-wrap 0
