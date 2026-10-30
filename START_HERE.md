# START HERE

Read this whole page (about 5 minutes). Then open your personal file in `team/`.

## 1. What are we building? (60 seconds)

1. A **small basketball AI model** reads a spreadsheet of finished games and learns which statistics go with a home-team win.
2. We **save the model three times** while it keeps learning (stage 1, stage 2, stage 3).
3. For each saved file we calculate a **fingerprint** (a long code made from the file's exact contents).
4. We **register** each fingerprint on a **practice blockchain** on our own computers. That registered record is our official reference.
5. A **checker** takes any file, calculates its fingerprint, looks up the official record, and shows **MATCH**, **CHANGED**, or **NO RECORD**.

An exact copy should say MATCH. A copy with even one changed byte should say CHANGED.

Details and plain-English definitions: [docs/PROJECT_EXPLAINED.md](docs/PROJECT_EXPLAINED.md).

## 2. Two things to remember

- The basketball model is just a **stand-in AI file**. Our main subject is **file verification**.
- A MATCH means "this is the same file we registered." It does **not** prove the AI is accurate, fair, explainable, or trained on good data.

## 3. Find your file and do your first three actions

| Person | Role | Your file |
|---|---|---|
| Shabach | Engineering Lead | [team/shabach.md](team/shabach.md) |
| Kaleb | Smart Contract and Blockchain Engineer | [team/kaleb.md](team/kaleb.md) |
| Remington | Machine Learning Lead | [team/remington.md](team/remington.md) |
| Chris | Technical Writing and Compliance Lead | [team/chris.md](team/chris.md) |

**Chris (first three):**
1. Collect each teammate's GitHub username and send repository invitations (only to usernames you have checked).
2. Ask the professor the open questions in [docs/PROGRESS.md](docs/PROGRESS.md) (presentation date, submission method, similarity tool, AI-help rules).
3. Create the team's shared storage folder and put its link in [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md).

**Shabach (first three):**
1. Read [docs/PROJECT_EXPLAINED.md](docs/PROJECT_EXPLAINED.md) and [docs/SYSTEM_DESIGN.md](docs/SYSTEM_DESIGN.md); write down questions or proposed changes.
2. Run `python --version` and `git --version`; add the results to [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md).
3. Make a tiny text file, calculate its SHA-256 with two different tools (see [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)), and confirm both give the same answer.

**Kaleb (first three):**
1. Check your Node.js version (`node --version`) against the current Hardhat documentation and install a supported one.
2. Read the current Hardhat "Getting started" page and tell Shabach which Hardhat version you plan to use.
3. Record your versions in [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md).

**Remington (first three):**
1. Install a PyTorch-supported Python version and create a virtual environment (see [ml/README.md](ml/README.md)).
2. Download `games.csv` from the dataset page, open it, and write down the column names and number of rows.
3. Read the dataset page for usage terms and attribution and record them in [data/README.md](data/README.md).

## 4. How work gets checked off

A box in a checklist is checked **only when**:
1. The promised file or output exists.
2. Its check passes.
3. Evidence is linked (file path, log, or pull request).
4. The assigned reviewer has checked it.

Full rules: [docs/DEFINITION_OF_DONE.md](docs/DEFINITION_OF_DONE.md). Git steps: [CONTRIBUTING.md](CONTRIBUTING.md).

## 5. The big picture: ten "bosses"

1. Understand the project and set up the workspace
2. Download and inspect basketball data
3. Train and save one working model
4. Continue training and save three versions
5. Verify file fingerprints locally
6. Register model versions on the practice blockchain
7. Connect the full verification workflow
8. Run tampering, permission, timing, and gas tests
9. Finish research and the paper
10. Rehearse and submit

Each boss has exact steps in [docs/BUILD_ORDER.md](docs/BUILD_ORDER.md). **Research starts now, not at Boss 9.**

## 6. Dates

Final deadline: **Monday, November 16, 2026, 11:59 p.m.** Target dates are in [docs/SCHEDULE.md](docs/SCHEDULE.md).

## 7. Stuck?

1. Check [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).
2. Open a "Help request" issue (GitHub: Issues, New issue). Say what you tried and paste the exact error.
3. Ask in your team chat the same day. Being stuck for more than a day without telling anyone is the main way this project fails.
