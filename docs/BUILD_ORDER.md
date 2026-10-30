# Build Order: The Ten Bosses

Do the bosses in order, except where a note says work can overlap. File names below marked *(suggested)* are suggestions. The owner decides the real names and documents them in their folder README. **Nothing here has been built yet.**

Every checkbox follows the [Definition of Done](DEFINITION_OF_DONE.md): file exists, check passes, evidence linked, reviewer signs off.

Reviewer rotation: Shabach's work is reviewed by Remington. Remington's work is reviewed by Kaleb. Kaleb's work is reviewed by Shabach. Chris's work is reviewed by Shabach, and the owner of any technical area Chris describes also checks that description.

---

## Boss 1: Understand the project and set up the workspace

**Plain English:** make sure everyone can open the project, understands it, and can make a safe change on GitHub.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Chris | Shabach | None | Boss 2 |

**Exact actions**
1. Everyone reads `START_HERE.md` and `docs/PROJECT_EXPLAINED.md`.
2. Each person sends Chris their GitHub username. Chris sends invitations only to usernames he has checked.
3. Each person accepts the invitation, clones the repo, and makes a branch.
4. Each person adds their GitHub username and one sentence ("I read START_HERE and understand the project") to their own `team/` file, then opens a pull request.
5. Chris asks the open questions listed in `docs/PROGRESS.md`.
6. Everyone fills in the versions they have in `docs/ENVIRONMENT.md`.
7. Chris sets up shared storage and records the link in `docs/ENVIRONMENT.md`.
8. Each person adds at least 3 verified candidate sources to `research/sources_template.csv` (copy it to `research/sources.csv` first).

**Expected output:** four merged pull requests (one per person); filled environment table; shared storage link.

**Checklist**
- [ ] Four collaborators can clone the private repo
- [ ] Four pull requests merged after review
- [ ] Open questions answered or assigned
- [ ] Environment table has at least Git and Python for every person
- [ ] Shared storage exists and its link is recorded
- [ ] Each person added 3+ verified sources

**How to verify:** the reviewer opens each pull request, confirms the file changed, and confirms the author can explain a branch and a pull request in one sentence each.

**Evidence:** pull request links; `docs/ENVIRONMENT.md`; `research/sources.csv`.

---

## Boss 2: Download and inspect basketball data

**Plain English:** get the spreadsheet, look at it carefully, clean it, and split it into a "study" part and a "quiz" part.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Remington | Chris (attribution and terms) | Boss 1: Python environment | Boss 3 |

**Exact actions**
1. Download `games.csv` from the dataset page (`hamzas/nba-games`) into `data/raw/` (ignored by Git).
2. Record the SHA-256 fingerprint of the downloaded file in `data/manifests/` so teammates can confirm they have the same file.
3. Inspect: column names, number of rows, whether `GAME_ID`, `HOME_TEAM_WINS`, `FG_PCT_home`, `REB_home`, `AST_home`, `FG_PCT_away`, `REB_away`, `AST_away` all exist, the date range, and how many games the home team won.
4. Count missing values in the seven needed columns. Count duplicate `GAME_ID` values.
5. Clean: keep one row per `GAME_ID` (state which duplicate you keep), and handle missing data in the simplest documented way (for example drop rows with missing needed values). Record every count removed.
6. Do **not** use the answer column, final scores, point difference, or any identifier as a model input.
7. Create a fixed 80/20 training/test split with a recorded seed. Each game appears in one split only.
8. Save the lists of training and test `GAME_ID`s and a short data report in `data/manifests/`.
9. Record the dataset license/usage terms and the source attribution in `data/README.md`.

**Expected output:** `data/manifests/` containing the raw-file fingerprint, the two ID lists, the seed, and a data report; completed attribution in `data/README.md`.

**Checklist**
- [ ] `games.csv` downloaded and its fingerprint recorded
- [ ] Required columns confirmed present (or the problem written up)
- [ ] Duplicate and missing-data counts recorded
- [ ] Cleaning rules documented
- [ ] 80/20 split created with recorded seed
- [ ] No game appears in both splits (check run and saved)
- [ ] Re-running the split gives identical ID lists
- [ ] License and attribution recorded

**How to verify:** reviewer runs the split script twice and compares the ID lists; checks that train and test ID lists share no IDs; checks counts add up.

**Evidence:** `data/manifests/*`, the script path, `data/README.md`, log in `results/raw/`.

---

## Boss 3: Train and save one working model

**Plain English:** prove the whole learning loop works once before doing it three times.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Remington | Shabach (checkpoint format) | Boss 2 | Boss 4 |

**Exact actions**
1. Fit any preprocessing (such as scaling) on the **training** games only; apply the same settings to test games.
2. Build one small PyTorch model (see `ml/README.md`).
3. Train it on the training games. Do not look at the test set while choosing settings.
4. Measure accuracy on the test games, and compute a baseline.
5. Save one checkpoint containing the model settings and the preprocessing information needed to reproduce predictions.
6. Reload the checkpoint in a fresh program run and confirm it makes the same predictions.

**Expected output:** one checkpoint file (stored in shared storage, not GitHub), a row in the accuracy CSV, and a log.

**Checklist**
- [ ] Preprocessing fit on training data only
- [ ] Model trains without errors
- [ ] Accuracy measured on the held-out test games
- [ ] Baseline accuracy measured
- [ ] Checkpoint saved and reloaded with identical predictions
- [ ] Row added to `results/accuracy.csv`

**How to verify:** reviewer follows `ml/README.md` on their own computer and reproduces predictions from the saved checkpoint.

**Evidence:** log in `results/raw/`; accuracy row; `ml/README.md` run instructions.

---

## Boss 4: Continue training and save three versions

**Plain English:** keep teaching the same model in three rounds and save a separate file after each round.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Remington | Shabach | Boss 3 | Boss 5 and Boss 6 |

**Exact actions**
1. Use **one** model and **one** optimizer that continue learning across three stages.
2. Decide the length of each stage **before** looking at test results, and write it down.
3. After each stage: evaluate on the **same** held-out test set; save a **separate** checkpoint (never overwrite).
4. Record accuracy after each stage. It may improve, drop, or stay the same. There is no minimum.
5. If you want to tune settings, carve a validation set out of the **training** 80%. Never tune on the test set.
6. Reload each checkpoint and confirm the reproduced accuracy matches what you recorded.
7. Record file names and sizes. Never edit or re-save a checkpoint after it has been fingerprinted.

**Expected output:** three checkpoint files (stage 1, 2, 3), three accuracy rows, three file sizes.

**Checklist**
- [ ] Stage plan written down before testing
- [ ] Same optimizer continued across stages
- [ ] Three separate checkpoints saved
- [ ] Each evaluated on the same test games
- [ ] Each reloaded and accuracy reproduced
- [ ] Three rows in `results/accuracy.csv` with sizes

**How to verify:** reviewer reloads each checkpoint and checks the accuracy matches the CSV.

**Evidence:** accuracy CSV, logs, `models/manifests/` entry (name and size only until fingerprinted).

---

## Boss 5: Verify file fingerprints locally

**Plain English:** before involving a blockchain, prove we can calculate fingerprints correctly and spot a changed file.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Shabach | Remington | Dummy file now; real checkpoints from Boss 4 | Boss 6 |

**Exact actions**
1. Write a fingerprint function using Python `hashlib` SHA-256 that reads the file in chunks.
2. Test it against a tiny text file and compare with an independent tool (see `docs/TROUBLESHOOTING.md`). They must agree.
3. Run it on the three real checkpoints. Record the fingerprints in `models/manifests/`.
4. Write comparison logic that returns MATCH, CHANGED, or NO RECORD, tested against a temporary stand-in record (clearly labeled temporary, not the blockchain).
5. Test an exact copy (same fingerprint) and a copy with one changed byte (different fingerprint). **Only hash damaged files. Never load them as models.**

**Expected output:** a fingerprint function and command, plus three recorded fingerprints.

**Checklist**
- [ ] Function matches an independent tool on a test file
- [ ] Fingerprints recorded for all three checkpoints
- [ ] Exact copy gives the same fingerprint
- [ ] One-byte change gives a different fingerprint
- [ ] Stand-in comparison returns all three outcomes

**How to verify:** reviewer runs the command on a file and checks it with an independent tool.

**Evidence:** log, `models/manifests/`, first rows in `results/verification.csv`.

---

## Boss 6: Register model versions on the practice blockchain

**Plain English:** put an official record of each model file on our local blockchain, with rules that stop cheating.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Kaleb | Shabach | Node/Hardhat running (can start early); real fingerprints and accuracies from Boss 4 and 5 | Boss 7 |

**Exact actions**
1. Set up the Hardhat project in `blockchain/`; record versions in `docs/ENVIRONMENT.md`.
2. Write the contract following `docs/SYSTEM_DESIGN.md`: records identified by training run and stage; stores fingerprint and reported accuracy; records the submitting account; only the designated account may register; duplicates rejected; retrieval with a clear missing-record response.
3. Write Hardhat tests for each rule (success, retrieval, missing record, duplicate, unauthorized).
4. Deploy to the local node; export the ABI to `blockchain/abi/`.
5. Provide a small Python module (Web3.py) with `register` and `get_record` for Shabach.
6. Register the three real records. Save each transaction hash and gas used.

**Expected output:** passing contract tests; three retrievable records; gas rows.

**Checklist**
- [ ] Contract compiles
- [ ] Tests pass for register, retrieve, missing, duplicate, unauthorized
- [ ] ABI exported
- [ ] Python helper can register and retrieve
- [ ] Three real records registered
- [ ] Gas used recorded from transaction receipts
- [ ] Accuracy scale documented

**How to verify:** reviewer reruns the contract tests and retrieves all three records.

**Evidence:** test output in `results/raw/`; `results/gas.csv`; `blockchain/README.md`.

---

## Boss 7: Connect the full verification workflow

**Plain English:** one clear path from "here is a file" to "MATCH, CHANGED, or NO RECORD".

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Shabach | Kaleb, Remington | Boss 5 and 6 | Boss 8 |

**Exact actions**
1. Build a verification command that takes a file, a run, and a stage; computes the fingerprint; fetches the record; compares; prints one of MATCH, CHANGED, NO RECORD.
2. Write `integration/README.md` with the exact start-to-finish order (start chain, deploy, register, verify).
3. Run the whole workflow once, then a second time following only the written instructions.
4. Ask a teammate who did not write it to run it from the instructions.

**Expected output:** repeatable workflow documented step by step.

**Checklist**
- [ ] Verification command works on all three originals
- [ ] Written instructions are complete
- [ ] Run twice from documented instructions
- [ ] Run by a teammate who did not build it

**How to verify:** Chris (not an author) follows the instructions and reports exactly where he got stuck.

**Evidence:** two run logs; teammate's notes; `integration/README.md`.

---

## Boss 8: Run tampering, permission, timing, and gas tests

**Plain English:** try to break it, and measure honestly what happens.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Shabach | Kaleb (permission, gas), Chris (evidence collection) | Boss 7 | Boss 9 results writing |

**Exact actions:** follow `docs/TEST_PLAN.md` test by test (T01 to T15). Record expected versus actual, pass or fail, file sizes, environment versions, raw measurements and evidence paths in the `results/` CSVs.

**Checklist**
- [ ] T01-T03 originals MATCH
- [ ] T04 exact copy MATCH
- [ ] T05-T07 three modified copies flagged CHANGED
- [ ] T08-T09 unknown run and unknown stage give NO RECORD
- [ ] T10 unauthorized registration rejected
- [ ] T11 duplicate registration rejected
- [ ] T12 workflow run twice from documented instructions
- [ ] T13 accuracy uses separate test games
- [ ] T14 timing: 10 measurements per original after warm-up
- [ ] T15 gas collected from receipts for all registrations

**How to verify:** reviewer spot-checks at least three raw rows against logs and reruns one test.

**Evidence:** `results/verification.csv`, `results/timing.csv`, `results/gas.csv`, logs.

---

## Boss 9: Finish research and the paper

**Plain English:** research never stopped; now the team writes up what was actually built and measured, in their own words.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Chris (assembly) | Everyone writes their own section | Research from Boss 1 on; results from Boss 8 | Boss 10 |

**Exact actions**
1. Keep adding sources weekly. Reach at least 20 unique scholarly references, each opened and confirmed to exist.
2. Each author drafts their section **themselves** following `paper/OUTLINE.md`.
3. Results sections use only numbers from the `results/` CSVs.
4. Chris assembles the paper in the IEEE conference Word template, finalizes the abstract last, checks formatting and references, and runs the similarity check.
5. Everyone reads the whole paper once for accuracy of their own technical claims.

**Checklist:** see `paper/REQUIREMENTS_CHECKLIST.md`.

**Evidence:** reference tracker, paper draft in shared storage, similarity report, `research/contribution_log.csv`.

---

## Boss 10: Rehearse and submit

**Plain English:** practice until the demo and the talk are boring, then submit early.

| Owner | Supporting | Prerequisites | Next |
|---|---|---|---|
| Chris | All | Boss 8 and 9 | Done |

**Exact actions:** follow `presentation/OUTLINE.md` and `presentation/REHEARSAL_CHECKLIST.md`; record a backup demo; submit the Word paper and PowerPoint through the designated person; keep proof of submission.

**Checklist**
- [ ] Slides complete and speaker owners assigned
- [ ] Two timed rehearsals within 25 to 30 minutes
- [ ] Backup demo recorded and tested offline
- [ ] Paper and slides final-checked by someone other than the author
- [ ] Submitted by the designated person before the deadline
- [ ] Proof of submission saved

**Evidence:** rehearsal notes, backup demo location, submission confirmation.
