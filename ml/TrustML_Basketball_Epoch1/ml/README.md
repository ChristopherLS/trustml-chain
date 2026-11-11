# ml/ : Basketball Model (Remington)

**Status: NOT STARTED. No code exists in this folder yet.**

## What belongs here

- Data preparation code (clean, split).
- Model, training, and evaluation code (PyTorch).
- This README, kept up to date with the **real** commands once they work.

## What does NOT belong here

- Downloaded data (goes in `data/raw/`, which Git ignores).
- Model checkpoint files (go in shared storage; fingerprints go in `models/manifests/`).

## Planned design (a plan, not a fact)

- **Language and tools:** Python, pandas, NumPy, PyTorch (CPU is enough). Use PyTorch consistently. Do not mix in scikit-learn checkpoints without writing down a deliberate reason here first.
- **Inputs:** `FG_PCT_home`, `REB_home`, `AST_home`, `FG_PCT_away`, `REB_away`, `AST_away`.
- **Answer:** `HOME_TEAM_WINS`.
- **Never an input:** the answer column, final scores, point difference, any identifier.
- **Cleaning:** one row per `GAME_ID`; document missing-data handling and counts.
- **Split:** fixed 80/20, recorded seed, saved ID lists, each game in one split only.
- **Preprocessing:** fit on training data only; save what is needed to reproduce predictions.
- **Model:** one small model (for example a single layer or one small hidden layer). Keep it small and simple.
- **Training:** one model and one optimizer continue through three stages; separate checkpoint after each stage; evaluate each on the same test set; do not tune on the test set (use a validation split from the training portion if you need to tune).
- **Baseline:** compare with a simple guess such as always predicting the more common training outcome.

## Setup (works today)

```bash
python -m venv .venv
# activate it:
#   macOS/Linux:  source .venv/bin/activate
#   Windows:      .venv\Scripts\activate
```

Then install packages using the **current** official PyTorch "Get Started" command (choose CPU) plus pandas and NumPy, and record the versions in `docs/ENVIRONMENT.md`.

## Run instructions

_To be written by Remington once the scripts exist. Replace this line with exact commands that were tested._
