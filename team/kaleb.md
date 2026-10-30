# Kaleb: Smart Contract and Blockchain Engineer

**Status of your work: Not started.**
**GitHub username:** _(add after Chris verifies it)_

## Role and purpose

You build the official record book: a smart contract on a local practice blockchain that stores one record per model version and refuses cheating (wrong account, duplicates, overwriting). Your records are what everyone else compares against.

## What you own

- Local Hardhat blockchain setup.
- Solidity contract.
- Authorized registration and record retrieval.
- Protection against duplicate registration and overwriting.
- Blockchain permission tests.
- Registration gas measurements.
- Blockchain implementation documentation (`blockchain/README.md`).

## What you need from others

| From | What | When |
|---|---|---|
| Shabach | Agreement on `register` and `get_record` inputs and outputs; agreement on how the contract address is shared | Before Boss 6 coding |
| Remington | The three accuracy values and the accuracy scale agreed | Boss 4 |
| Shabach | The three real fingerprints | Boss 5 |

## Your first three actions

1. Check `node --version` against the current Hardhat documentation and install a supported version if needed.
2. Read the current Hardhat "Getting started" page and tell Shabach which Hardhat version you plan to use (Hardhat 2 or 3).
3. Record all your tool versions in `docs/ENVIRONMENT.md`.

## Task list (in dependency order)

- [ ] **1. Tools installed and versions recorded.** *Evidence:* `docs/ENVIRONMENT.md`. *Reviewer:* Shabach.
- [ ] **2. Hardhat project created in `blockchain/`** and the local blockchain starts. *Evidence:* the start command and what it prints, saved in `results/raw/`; documented in `blockchain/README.md`. *Reviewer:* Shabach.
- [ ] **3. Agree the interface with Shabach.** Function names, inputs, outputs, the accuracy scale, and how a missing record is reported. *Evidence:* `docs/SYSTEM_DESIGN.md` edited (merged PR). *Reviewer:* Shabach.
- [ ] **4. Contract written.** Records keyed by training run and stage; stores fingerprint, reported accuracy, submitter; only the designated account may register; duplicates rejected. *Evidence:* contract file; compiles. *Reviewer:* Shabach.
- [ ] **5. Contract tests.** Register succeeds; retrieve returns the same values; missing record reports "no record"; duplicate rejected and original unchanged; unauthorized account rejected. *Evidence:* test output in `results/raw/`. *Reviewer:* Shabach.
- [ ] **6. Deployment.** Deploy to the local chain; export the ABI to `blockchain/abi/`; document how the address reaches the Python code. *Evidence:* README steps; ABI file. *Reviewer:* Shabach.
- [ ] **7. Python helper.** `register` and `get_record` using Web3.py, with clear errors (never crashes on a missing record). *Evidence:* code and a run log. *Reviewer:* Shabach.
- [ ] **8. Register the three real records** after Boss 4 and Boss 5, using the real fingerprints and accuracy values. *Evidence:* three retrieved records matching the CSV; transaction hashes. *Reviewer:* Shabach.
- [ ] **9. Permission and duplicate tests T10, T11 through Python** (not only Hardhat tests). *Evidence:* `results/verification.csv` rows and logs. *Reviewer:* Shabach.
- [ ] **10. Gas T15.** Read `gasUsed` from each registration receipt. Gas units only, no dollar costs. *Evidence:* `results/gas.csv` with transaction hashes. *Reviewer:* Shabach.
- [ ] **11. Blockchain documentation.** `blockchain/README.md` states how to start, deploy, test, and what the contract guarantees and does not. *Evidence:* merged PR. *Reviewer:* Shabach, followed by a read-through by Chris.
- [ ] **12. Paper section drafted by you, in your own words.** *Evidence:* draft in shared storage; contribution log entry. *Reviewer:* Chris (format and references), Shabach (technical accuracy).
- [ ] **13. Presentation section and demo narration.** *Evidence:* slides; rehearsal notes. *Reviewer:* Chris.

## Paper section

Blockchain registration, verification, contract rules, and blockchain results (about 2 pages, flexible). Outline: `paper/OUTLINE.md`.

## Presentation responsibility

"The blockchain record" (5 min) and narrating the registration part of the demonstration. See `presentation/OUTLINE.md`.

## Research questions and search terms

Questions: How is blockchain used to record the origin or integrity of data or AI models? What are the limits of a local or permissioned chain compared with a public one? What do smart-contract access controls protect against? What are known smart-contract mistakes?
Terms to try: blockchain provenance machine learning, blockchain data integrity, smart contract access control, Ethereum gas cost, permissioned blockchain, smart contract vulnerabilities.
Add each verified source to `research/sources.csv`.

## Your week's goals (write your own; keep them specific)

| Week | My goal (what I will do, by when, how I will know) | Mid-week check | End-of-week result |
|---|---|---|---|
| Oct 30 to Nov 5 | | | |
| Nov 6 to Nov 12 | | | |

## Example progress update

> **Kaleb, Thu Nov 5.** Done: contract compiles; 4 of 5 Hardhat tests pass (output: results/raw/contract_tests_nov5.txt). Next: fix the duplicate-registration test. Blocked: none. Need from Shabach: confirm the accuracy scale by Friday.
