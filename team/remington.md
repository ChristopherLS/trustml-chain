# Remington: Machine Learning Lead

**Status of your work: Not started.**
**GitHub username:** _(add after Chris verifies it)_

## Role and purpose

You create the example AI files. You prepare basketball data, train a small PyTorch model in three stages, save three checkpoints, and measure how accurate each one is on games it never studied.

## What you own

- Basketball dataset preparation.
- A small PyTorch model.
- Training and test separation.
- Continued training with three saved checkpoints.
- Accuracy measurements and baseline comparison.
- Machine learning documentation (`ml/README.md`).

**Use PyTorch throughout.** Do not mix in scikit-learn checkpoint instructions. If the team deliberately switches, write down why in `ml/README.md` first.

## What you need from others

| From | What | When |
|---|---|---|
| Chris | Dataset usage-terms and attribution check; shared storage for big files | Boss 2 |
| Shabach | What the verification code needs to know about your checkpoint files; fingerprints of your three files | Boss 3 to 5 |
| Kaleb | Confirmation of the accuracy scale (see `docs/SYSTEM_DESIGN.md`) | Before Boss 6 |

## Your first three actions

1. Install a Python version PyTorch supports (check the official PyTorch "Get Started" page) and create a virtual environment. Record versions in `docs/ENVIRONMENT.md`.
2. Download `games.csv` from the dataset page, open it, and write down the column names and number of rows.
3. Read the dataset page for usage terms and attribution and record them in `data/README.md`.

## Task list (in dependency order)

- [ ] **1. Environment ready.** Python, pandas, NumPy, PyTorch (CPU) installed; versions recorded. *Evidence:* `docs/ENVIRONMENT.md`. *Reviewer:* Kaleb.
- [ ] **2. Data downloaded and inspected.** Columns, row count, date range, home-win count, missing values, duplicate `GAME_ID`s. *Evidence:* `data/manifests/` data report. *Reviewer:* Kaleb.
- [ ] **3. License and attribution recorded.** *Evidence:* `data/README.md`. *Reviewer:* Chris.
- [ ] **4. Cleaning documented and done.** One row per `GAME_ID`; documented missing-data rule; counts removed recorded. *Evidence:* data report; script. *Reviewer:* Kaleb.
- [ ] **5. Fixed 80/20 split.** Seed recorded; training and test `GAME_ID` lists saved; no overlap. Re-running gives identical lists. *Evidence:* `data/manifests/`; log of two runs. *Reviewer:* Kaleb.
- [ ] **6. Inputs and answer chosen.** Inputs are exactly `FG_PCT_home`, `REB_home`, `AST_home`, `FG_PCT_away`, `REB_away`, `AST_away`; the answer is `HOME_TEAM_WINS`. The answer, final scores, point difference, and identifiers are never inputs. Preprocessing fit on training data only. *Evidence:* `ml/README.md` and code. *Reviewer:* Kaleb.
- [ ] **7. Baseline.** Compute a simple baseline accuracy (for example always predict the more common training outcome). *Evidence:* row in `results/accuracy.csv`. *Reviewer:* Kaleb.
- [ ] **8. First model trained and saved (Boss 3).** One small PyTorch model; checkpoint includes model settings and the preprocessing information needed to reproduce predictions; reload gives identical predictions. *Evidence:* log; run instructions. *Reviewer:* Kaleb.
- [ ] **9. Three-stage training (Boss 4).** One model and one optimizer continue across three stages; stage plan written before testing; same test set each time; a separate checkpoint each stage; never overwrite. *Evidence:* three checkpoints in shared storage; three accuracy rows with file sizes. *Reviewer:* Kaleb, with Shabach confirming the checkpoint interface.
- [ ] **10. Honest reporting.** Accuracy may rise, fall, or stay the same. Record what happened with no tuning against the test set. *Evidence:* `results/accuracy.csv`. *Reviewer:* Kaleb.
- [ ] **11. T13 check.** Show accuracy used only test games (no overlap; counts match). *Evidence:* check output. *Reviewer:* Kaleb.
- [ ] **12. Handoff to Shabach.** Final checkpoint names, sizes, and locations; never edit or re-save them after fingerprinting. *Evidence:* `models/manifests/`. *Reviewer:* Shabach.
- [ ] **13. Machine learning documentation.** `ml/README.md` explains how to run each step from a clean setup. *Evidence:* a teammate runs it successfully. *Reviewer:* Kaleb.
- [ ] **14. Paper section drafted by you, in your own words.** *Evidence:* draft in shared storage; contribution log entry. *Reviewer:* Chris (format and references), Shabach (technical accuracy).
- [ ] **15. Presentation section.** *Evidence:* slides; rehearsal notes. *Reviewer:* Chris.

## Safety note for model files

Only open model files you made yourself. When loading a PyTorch checkpoint, follow the current PyTorch documentation on safe loading, and never load deliberately damaged files.

## Paper section

Dataset, model training, checkpoints, and accuracy (about 2 pages, flexible). Outline: `paper/OUTLINE.md`.

## Presentation responsibility

"The basketball model" (5 min) and narrating the model part of the demonstration. See `presentation/OUTLINE.md`.

## Research questions and search terms

Questions: How have basketball game outcomes been classified or predicted with machine learning? Why must training and test data be kept separate? What is feature leakage, and could our inputs cause it? How do baselines help interpret accuracy?
Terms to try: NBA game outcome prediction machine learning, sports analytics classification, train test split generalization, data leakage machine learning, model checkpointing, logistic regression baseline.
Add each verified source to `research/sources.csv`.

## Your week's goals (write your own; keep them specific)

| Week | My goal (what I will do, by when, how I will know) | Mid-week check | End-of-week result |
|---|---|---|---|
| Oct 30 to Nov 5 | | | |
| Nov 6 to Nov 12 | | | |

## Example progress update

> **Remington, Tue Nov 3.** Done: games.csv downloaded and inspected; data report committed (data/manifests/). Next: cleaning rules and the 80/20 split. Blocked: none. Need from Chris: dataset usage terms confirmed.
