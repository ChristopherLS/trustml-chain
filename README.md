# TrustML-Chain

**The question this project answers:** if someone hands you an AI model file, how can you tell whether it is the exact file the team originally saved?

We use a small basketball model as our example AI file. We save three versions of it, calculate a **fingerprint** (SHA-256) of each saved file, write each fingerprint to a **practice blockchain** that runs on our own computers, and then build a checker that says **MATCH**, **CHANGED**, or **NO RECORD** for any file you hand it.

> **New here? Open [START_HERE.md](START_HERE.md) first.**

## Where things stand

| Area | Status |
|---|---|
| GitHub workspace (docs, checklists, templates) | Set up by Claude on 2026-10-30 |
| Basketball model (`ml/`) | **Not started** |
| Smart contract and local blockchain (`blockchain/`) | **Not started** |
| Fingerprint + verification workflow (`integration/`) | **Not started** |
| Tests and measurements (`tests/`, `results/`) | **Not started** |
| Research and paper (`research/`, `paper/`) | **Not started** |
| Presentation (`presentation/`) | **Not started** |

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

## A note on AI use

Claude (an AI assistant) drafted the planning documents and templates in this workspace. The professor prohibits AI-generated text in the submitted paper. The `paper/` folder therefore contains outlines, questions, and checklists only. **All text in the submitted paper must be written by the team members.** Confirm with the professor what AI help (if any) is allowed for code, and record the answer in [docs/PROGRESS.md](docs/PROGRESS.md).

## Privacy and safety rules

- This repository is **private**. Do not make it public.
- Never commit passwords, private keys, `.env` files, or school-private information.
- Only add collaborators using usernames that have been verified by the person who owns the repository.
