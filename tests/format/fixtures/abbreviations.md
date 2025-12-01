common title abbreviations
.
Dr. Smith arrived at the hospital. He met with Prof. Johnson.
.
Dr. Smith arrived at the hospital. He met with Prof. Johnson.
.

common title abbreviations aggressive mode
.
Dr. Smith arrived at the hospital. He met with Prof. Johnson.
.
Dr. Smith arrived at the hospital.
He met with Prof. Johnson.
.
--slw-min-line=0

time abbreviations
.
The meeting is at 3 p.m. today. It starts promptly at 3:00 p.m. sharp!
.
The meeting is at 3 p.m. today. It starts promptly at 3:00 p.m. sharp!
.

time abbreviations aggressive mode
.
The meeting is at 3 p.m. today. It starts promptly at 3:00 p.m. sharp!
.
The meeting is at 3 p.m. today.
It starts promptly at 3:00 p.m. sharp!
.
--slw-min-line=0

latin abbreviations
.
This is an example, e.g. like this one. It works well, i.e. correctly! Use it etc. for more cases.
.
This is an example, e.g. like this one. It works well, i.e. correctly!
Use it etc. for more cases.
.

latin abbreviations aggressive mode
.
This is an example, e.g. like this one. It works well, i.e. correctly! Use it etc. for more cases.
.
This is an example, e.g. like this one.
It works well, i.e. correctly!
Use it etc. for more cases.
.
--slw-min-line=0

mixed abbreviations in sentence
.
Dr. Smith said hello at 3 p.m. yesterday. The study included multiple items, e.g. samples and data! Prof. Johnson agreed etc. with the findings.
.
Dr. Smith said hello at 3 p.m. yesterday.
The study included multiple items, e.g. samples and data!
Prof. Johnson agreed etc. with the findings.
.

abbreviations mode off aggressive
.
Dr. Smith arrived. Prof. Johnson was there.
.
Dr.
Smith arrived.
Prof.
Johnson was there.
.
--slw-abbreviations-mode=off
--slw-min-line=0

custom abbreviations extend (line exceeds min-line so wraps)
.
The company XYZ Corp. announced new products. The CEO Mr. Anderson attended!
.
The company XYZ Corp. announced new products.
The CEO Mr. Anderson attended!
.
--slw-abbreviations-mode=extend
--slw-abbreviations=Corp,XYZ

custom abbreviations extend aggressive mode
.
The company XYZ Corp. announced new products. The CEO Mr. Anderson attended!
.
The company XYZ Corp. announced new products.
The CEO Mr. Anderson attended!
.
--slw-abbreviations-mode=extend
--slw-abbreviations=Corp,XYZ
--slw-min-line=0

custom abbreviations override aggressive mode
.
Dr. Smith arrived. But CustomAbbr. was preserved!
.
Dr.
Smith arrived.
But CustomAbbr. was preserved!
.
--slw-abbreviations-mode=override
--slw-abbreviations=CustomAbbr
--slw-min-line=0

case sensitivity default
.
dr. smith and DR. SMITH both work. Same with prof. johnson!
.
dr. smith and DR. SMITH both work. Same with prof. johnson!
.

case sensitivity default aggressive mode
.
dr. smith and DR. SMITH both work. Same with prof. johnson!
.
dr. smith and DR. SMITH both work.
Same with prof. johnson!
.
--slw-min-line=0

business abbreviations
.
The company Inc. filed papers. The firm Ltd. responded. Apple Corp. announced earnings!
.
The company Inc. filed papers. The firm Ltd. responded.
Apple Corp. announced earnings!
.

business abbreviations aggressive mode
.
The company Inc. filed papers. The firm Ltd. responded. Apple Corp. announced earnings!
.
The company Inc. filed papers.
The firm Ltd. responded.
Apple Corp. announced earnings!
.
--slw-min-line=0

academic titles
.
She has a Ph.D. in biology. He earned his M.D. last year. The B.S. degree took four years!
.
She has a Ph.D. in biology. He earned his M.D. last year.
The B.S. degree took four years!
.

academic titles aggressive mode
.
She has a Ph.D. in biology. He earned his M.D. last year. The B.S. degree took four years!
.
She has a Ph.D. in biology.
He earned his M.D. last year.
The B.S. degree took four years!
.
--slw-min-line=0

geography abbreviations
.
They live on Main St. near Oak Ave. downtown. The building is on Park Blvd. by the river!
.
They live on Main St. near Oak Ave. downtown.
The building is on Park Blvd. by the river!
.

geography abbreviations aggressive mode
.
They live on Main St. near Oak Ave. downtown. The building is on Park Blvd. by the river!
.
They live on Main St. near Oak Ave. downtown.
The building is on Park Blvd. by the river!
.
--slw-min-line=0

months abbreviations
.
The event is in Jan. or Feb. next year. It might be Mar. or Apr. instead!
.
The event is in Jan. or Feb. next year. It might be Mar. or Apr. instead!
.

months abbreviations aggressive mode
.
The event is in Jan. or Feb. next year. It might be Mar. or Apr. instead!
.
The event is in Jan. or Feb. next year.
It might be Mar. or Apr. instead!
.
--slw-min-line=0

suppressions option (line exceeds min-line so wraps)
.
Custom word CustomWord. should not wrap. But normal sentence ends here!
.
Custom word CustomWord. should not wrap.
But normal sentence ends here!
.
--slw-suppressions=CustomWord

suppressions option aggressive mode
.
Custom word CustomWord. should not wrap. But normal sentence ends here!
.
Custom word CustomWord. should not wrap.
But normal sentence ends here!
.
--slw-suppressions=CustomWord
--slw-min-line=0

ignores option aggressive mode
.
Dr. should wrap now. But Mr. should still be preserved!
.
Dr.
should wrap now.
But Mr. should still be preserved!
.
--slw-ignores=Dr
--slw-min-line=0
