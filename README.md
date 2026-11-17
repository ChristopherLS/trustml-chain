# TrustML-Chain

**The question this project answers:** if someone hands you an AI model file, how can you tell whether it is the exact file the team originally saved?

We use a small basketball model as our example AI file. We save three versions of it, calculate a **fingerprint** (SHA-256) of each saved file, write each fingerprint to a **practice blockchain** that runs on our own computers, and then build a checker that says **MATCH**, **CHANGED**, or **NO RECORD** for any file you hand it.

> **New here? Open [START_HERE.md](START_HERE.md) first.**

## Where things stand

Status as of 2026-11-16, based on what is actually in this repository and on the final presentation.

| Area | Status |
|---|---|
| GitHub workspace (docs, checklists, templates) | Set up on 2026-10-30 |
| Basketball model (`ml/`) | All three model files (epochs 1, 5, 10), `training_report.json` and the training data copy are on `main` (`ml/TrustML_Basketball_Epoch1/`). Reported accuracy on 5,926 held-out games: 77.24%, 83.04%, 83.11%. The full prepare, train and predict scripts are on branch `rem/ml-training` and are **not merged yet** |
| Smart contract and local blockchain (`blockchain/`) | Built and tested on a local Hardhat chain. See [blockchain/README.md](blockchain/README.md) |
| Fingerprint + verification workflow | **Done for all three model files: 12 of 12 checks passed** (original and renamed copy MATCH, edited copy CHANGED, unknown run NO RECORD). Run with `blockchain/blockchain/blockchain/demo_verify_all.py`; replay or present the saved results with `present_verification.py` in the same folder |
| Tests and measurements (`results/`) | Evidence is in `results/raw/all-epochs-verification.txt` and `.csv`: registration gas (94,609 / 77,509 / 77,509) and median check time (13.8 / 11.3 / 15.7 ms) per checkpoint. The edited copy in this run adds bytes to a copy of each file. The CSV templates in `results/` are still templates |
| Research and paper (`research/`, `paper/`) | Only outlines and templates are committed |
| Presentation (`presentation/`) | Deck built in Google Slides. Text copy with speaker notes: [presentation/SLIDES.md](presentation/SLIDES.md) |

Nothing in the project is "done" because a document exists. See [docs/DEFINITION_OF_DONE.md](docs/DEFINITION_OF_DONE.md).

## Team

| Person | Role | Personal workspace |
|---|---|---|
| Shabach | Engineering Lead | [team/shabach.md](team/shabach.md) |
| Kaleb | Smart Contract and Blockchain Engineer | [team/kaleb.md](team/kaleb.md) |
| Remington | Machine Learning Lead | [team/remington.md](team/remington.md) |
| Chris | Technical Writing and Compliance Lead | [team/chris.md](team/chris.md) |

## Deadline

Paper (8-10 page IEEE Word paper) and presentation materials are due **Monday, November 16, 2026, at 11:59 p.m.** See [docs/SCHEDULE.md](docs/SCHEDULE.md).

## Map of the repository

| Folder or file | What belongs there |
|---|---|
| `START_HERE.md` | The first file everyone reads |
| `CONTRIBUTING.md` | How to use Git and GitHub as a team |
| `docs/` | Shared explanations, build order, design, test plan, schedule, troubleshooting, progress, environment record |
| `team/` | One personal instruction and task-tracker file per person |
| `ml/` | Basketball model code and notes (Remington) |
| `blockchain/` | Smart contract, local blockchain setup, contract tests (Kaleb) |
| `integration/` | Code that connects model files to blockchain verification (Shabach) |
| `tests/` | Shared test code and test instructions |
| `data/` | Dataset notes. Downloaded data is NOT stored in GitHub |
| `models/` | Model-file notes and fingerprint manifests. Large files are NOT stored in GitHub |
| `results/` | CSV templates and real measurements once collected |
| `research/` | Source tracker and contribution log |
| `paper/` | Paper outline and requirement checklist (outline only, no drafted paper text) |
| `presentation/` | Presentation outline and rehearsal checklist |
| `.github/` | Issue forms and the pull request template |

## Paper rule

The professor prohibits AI-generated text in the submitted paper. The `paper/` folder contains outlines, questions, and checklists only. **All text in the submitted paper must be written by the team members.** Record the professor's answer on what AI help is allowed for code in [docs/PROGRESS.md](docs/PROGRESS.md).

## Privacy and safety rules

- This repository is **private**. Do not make it public.
- Never commit passwords, private keys, `.env` files, or school-private information.
- Only add collaborators using usernames that have been verified by the person who owns the repository.
