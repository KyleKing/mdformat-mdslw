sentence wrapping with basic text (default behavior with min-line=40)
.
This is a test. It has multiple sentences! Does it work?
.
This is a test. It has multiple sentences!
Does it work?
.

sentence wrapping with short sentences (no wrap under 40 chars)
.
Short. Also short. And this.
.
Short. Also short. And this.
.

sentence wrapping with aggressive mode (min-line=0)
.
This is a test. It has multiple sentences! Does it work?
.
This is a test.
It has multiple sentences!
Does it work?
.
--slw-min-line=0

sentence wrapping disabled
.
This is a test. It has multiple sentences! Does it work?
.
This is a test. It has multiple sentences! Does it work?
.
--no-wrap-sentences

multiple paragraphs with default min-line
.
First paragraph with two sentences. Here is the second one.

Second paragraph also has sentences. This one too!
.
First paragraph with two sentences. Here is the second one.

Second paragraph also has sentences. This one too!
.

multiple paragraphs with aggressive mode
.
First paragraph with two sentences. Here is the second one.

Second paragraph also has sentences. This one too!
.
First paragraph with two sentences.
Here is the second one.

Second paragraph also has sentences.
This one too!
.
--slw-min-line=0

preserve formatting with default min-line
.
Some *markdown* text. **Bold** and _italic_!

- a list item
- another item
.
Some *markdown* text. **Bold** and _italic_!

- a list item
- another item
.

preserve formatting with aggressive mode
.
Some *markdown* text. **Bold** and _italic_!

- a list item
- another item
.
Some *markdown* text.
**Bold** and _italic_!

- a list item
- another item
.
--slw-min-line=0

sentence with quoted text
.
He said "Hello there." She replied "How are you?"
.
He said "Hello there." She replied "How are you?"
.

sentence with quoted text aggressive mode
.
He said "Hello there." She replied "How are you?"
.
He said "Hello there."
She replied "How are you?"
.
--slw-min-line=0

sentence with parentheses
.
This is a sentence (with a note). Another sentence follows!
.
This is a sentence (with a note). Another sentence follows!
.

sentence with parentheses aggressive mode
.
This is a sentence (with a note). Another sentence follows!
.
This is a sentence (with a note).
Another sentence follows!
.
--slw-min-line=0

sentence with brackets and braces
.
See the reference [1]. Also check {section 2}!
.
See the reference [1]. Also check {section 2}!
.

sentence with brackets and braces aggressive mode
.
See the reference [1]. Also check {section 2}!
.
See the reference [1].
Also check {section 2}!
.
--slw-min-line=0

colon no longer triggers wrapping by default
.
Consider this: It works well! Another point: Very good.
.
Consider this: It works well! Another point: Very good.
.

colon wrapping when explicitly enabled
.
Consider this: It works well! Another point: Very good.
.
Consider this:
It works well!
Another point:
Very good.
.
--slw-markers=.!?:
--slw-min-line=0

empty text
.

.

.

single sentence no ending punctuation
.
This is just one sentence
.
This is just one sentence
.

multiple spaces between sentences
.
First sentence.    Second sentence.     Third sentence.
.
First sentence. Second sentence. Third sentence.
.

multiple spaces with aggressive mode
.
First sentence.    Second sentence.     Third sentence.
.
First sentence.
Second sentence.
Third sentence.
.
--slw-min-line=0

sentence ending with multiple punctuation
.
What is this?! Really?!
.
What is this?! Really?!
.

sentence ending with multiple punctuation aggressive mode
.
What is this?! Really?!
.
What is this?!
Really?!
.
--slw-min-line=0

long sentence exceeding min-line threshold wraps
.
This is a longer sentence that exceeds forty characters. And another sentence here.
.
This is a longer sentence that exceeds forty characters.
And another sentence here.
.

very long paragraph tests wrap width at 88
.
This is a very long paragraph that needs to demonstrate how the wrap width works when lines get too long for comfortable reading in editors. The default is now 88 characters.
.
This is a very long paragraph that needs to demonstrate how the wrap width works when
lines get too long for comfortable reading in editors.
The default is now 88 characters.
.
