# Progress

Update this file at least twice a week. Keep it honest: never write progress that you cannot point to.

## Workspace setup (2026-10-30)

| Item | Result |
|---|---|
| Repository created | Yes: `ChristopherLS/trustml-chain`, **private** (confirmed in the GitHub response) |
| Did a repository with this name already exist? | No (lookup returned "not found" for the verified owner) |
| Planning documents and templates created | Yes (see the file list in the repo) |
| Collaborator invitations sent | **No.** Usernames have not been verified |
| Issues created | Yes: one per boss (issues #1 to #10), with owner, reviewer, checklist, and evidence; milestones and labels added |
| Project board created | Yes: https://github.com/users/ChristopherLS/projects/1 (columns: Not started, In progress, Blocked, Review, Done). Because the repo is private, teammates need repo access to see the items |
| Dataset columns and license verified | **No.** Not yet verified. Remington does this in Boss 2 |
| Exact tool versions verified | **No.** See [ENVIRONMENT.md](ENVIRONMENT.md) |
| Any model, contract, test, paper text, or result created | **No.** Implementation has not started |

## Project development status (the team updates this)

| Boss | Owner | Status | Evidence (link) |
|---|---|---|---|
| 1. Understand and set up | Chris | Ready for review | Workspace, issues #1 to #10 and project board created (see setup table above) |
| 2. Download and inspect data | Remington | Ready for review | `ml/TrustML_Basketball_Epoch1/data/data_report.json` |
| 3. Train and save one model | Remington | Ready for review | `ml/TrustML_Basketball_Epoch1/models/basketball_epoch_1.pt` and `training_report.json` |
| 4. Continue training, save three versions | Remington | In progress | Accuracy reported for epochs 1, 5, 10 in `training_report.json`; only the epoch 1 model file is in the repo |
| 5. Verify fingerprints locally | Shabach | In progress | Epoch 1 fingerprint verified (see presentation); code and log not yet committed |
| 6. Register on practice blockchain | Kaleb | Ready for review | [blockchain/README.md](../blockchain/README.md), `gas-report.md` |
| 7. Connect full workflow | Shabach | In progress | Epoch 1: 4 of 4 checks passed in Codespaces; epochs 5 and 10 waiting for model files; code and log not yet committed |
| 8. Tampering, permission, timing, gas tests | Shabach | In progress | Tamper and no-record checks done on epoch 1; permission and duplicate refusals in Kaleb's tests and smoke test; gas measured; timing not measured |
| 9. Research and paper | Chris | Not started | |
| 10. Rehearse and submit | Chris | In progress | Deck built in Google Slides; text copy in [presentation/SLIDES.md](../presentation/SLIDES.md) |

Allowed statuses: Not started, In progress, Blocked, Ready for review, Done.

_Statuses above were updated on 2026-11-16 from the files in this repository and the final presentation. Owners: please confirm or correct your own row. Boss 9 (research and paper) is unchanged because nothing about it is tracked in the repo._

**Completed tracked tasks:** __ of __ (count of checked boxes in `team/*.md`). This is a count, not a percentage of the work; tasks differ in effort.

## Open questions

| Question | Who asks / answers | Answer | Date |
|---|---|---|---|
| What date and time is the presentation? | Chris asks the professor | | |
| Who is the designated submitter, and what is the submission method? | Team | | |
| Which similarity checker will be used, and can we run it before submitting? | Chris asks the professor | | |
| What AI help (if any) is allowed for planning documents and code? | Chris asks the professor | | |
| Where is shared storage (link, not passwords)? | Chris | | |
| GitHub usernames for all four members | Each member tells Chris | | |

## Weekly goal setting (how each person plans their week)

Research on goal setting says goals work when they are **specific**, about **what you will do** (not just how it turns out), **short-term**, **chosen by you**, and **checked in on**. Each week every person writes goals in their own `team/` file.

| Weak goal | Strong goal |
|---|---|
| "Work on the model" | "By Wednesday I will download `games.csv`, list its columns, and commit `data/manifests/data_report.md` with row counts." |
| "Do the blockchain" | "By Thursday night I will have five Hardhat tests passing (register, retrieve, missing record, duplicate rejected, unauthorized rejected) and paste the output in my pull request." |
| "Do research" | "This week I will add four sources to `research/sources_template.csv`, each opened and confirmed to exist, with one sentence on why we might cite it." |

**Check-ins:** mid-week (2 minutes: did I do what I said? what is in my way?) and end of week (did I meet it? what will I change?). Post in the team chat using the progress-update format in your `team/` file.

## Weekly log

Add a dated entry each week. Do not edit old entries; add new ones.

### Week of Oct 30
- (nothing recorded yet)

## Issues and board

One issue per boss lives in the repository's Issues tab (#1 to #10), grouped by milestone. Labels: `owner:*`, `ws:*`, `status:*`. Owners are shown by label because teammates' GitHub usernames are not verified yet; assign people once they accept the invitation. The board is at https://github.com/users/ChristopherLS/projects/1. When you change a task's status, change the `status:*` label and the board column together.
