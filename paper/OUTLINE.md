# Paper Outline (outline only)

**This file contains structure and questions, not paper text.** The professor prohibits AI-generated text in the submitted paper. Every sentence in the submitted paper must be written by the team member who owns that section, in their own words.

## Assignment facts

- Due **Monday, November 16, 2026, 11:59 p.m.**
- 8 to 10 pages, IEEE conference format, Word file.
- At least 20 unique scholarly references.
- Similarity below 20 percent.
- One designated person submits the Word paper and the PowerPoint.

## Page budget (flexible)

About two pages per member is a guide. Title, abstract, and about one page of references must fit inside the 10-page limit, so sections may shrink or grow. Agree on actual lengths in a team meeting once figures and tables are drafted.

| Section | Owner | Approx. pages |
|---|---|---|
| Title, abstract (written last), index terms | Chris | front matter |
| I. Introduction and project purpose | Shabach | about 1 |
| II. Related work and background | Each author adds the part for their topic; Chris combines | shared |
| III. Overall design and integration | Shabach | about 1 |
| IV. Dataset, model training, checkpoints, accuracy | Remington | about 2 |
| V. Blockchain registration, verification, contract rules, blockchain results | Kaleb | about 2 |
| VI. Combined evaluation | Chris | about 1 |
| VII. Responsible use (ethics, privacy, transparency), limitations, future work | Chris | about 1 |
| VIII. Conclusion | Chris | short |
| References | Chris assembles | about 1 |

## Questions each section must answer (use your own words)

### I. Introduction (Shabach)
- What problem does file verification solve for AI models?
- What did we build, in one paragraph?
- What does the paper claim, and what does it deliberately not claim?

### III. Design and integration (Shabach)
- What are the components and how do they connect?
- Which design decisions did we make and why?
- How can someone repeat the demonstration?

### IV. Dataset and model (Remington)
- Where does the data come from and what are its usage terms?
- How was it cleaned, and how many games were removed and why?
- How was the 80/20 split made, and how do we know test games were never used for training?
- What does the model do, and how were the three checkpoints made?
- What accuracy did each stage have, and how does it compare with the baseline? (numbers from `results/accuracy.csv` only)
- Why is this classification of completed games, not forecasting?

### V. Blockchain (Kaleb)
- What does the contract store and what rules does it enforce?
- How does registration and retrieval work?
- What did permission, duplicate, and missing-record tests show?
- What gas units were used? (from `results/gas.csv`; no invented dollar costs)
- What are the limits of a local practice blockchain?

### VI. Combined evaluation (Chris)
- Did originals match, copies match, and modified copies fail? (from `results/verification.csv`)
- What were verification times? (from `results/timing.csv`)
- Did the workflow repeat from the documented instructions?

### VII. Responsible use, limitations, future work (Chris)
- What does a MATCH not prove?
- What privacy and ethics points apply to the data and to sharing models?
- What did we not test?
- What could extend the work?

### VIII. Conclusion (Chris)
- What was actually shown, supported by our own results?

## Writing rules

1. Write your own text. Do not paste AI-generated text, and do not paste from sources.
2. Every number must trace to a row in `results/`.
3. Every factual claim from the literature needs a reference you have opened and read.
4. Keep a note of who wrote what in `research/contribution_log.csv`.
5. Report negative or surprising results honestly.
