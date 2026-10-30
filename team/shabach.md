# Shabach: Engineering Lead

**Status of your work: Not started.** (Statuses: Not started, In progress, Blocked, Ready for review, Done.)
**GitHub username:** _(add after Chris verifies it)_

## Role and purpose

You make the pieces fit. Remington makes model files, Kaleb makes the blockchain registry, and you build the part that takes a file and says MATCH, CHANGED, or NO RECORD. You also make the whole demonstration repeatable by someone who did not build it.

## What you own

- Overall system design and integration (`docs/SYSTEM_DESIGN.md`, `integration/`).
- Shared code structure.
- Connecting model files to blockchain verification.
- Supporting technical troubleshooting (`docs/TROUBLESHOOTING.md`).
- Making the complete demonstration repeatable.
- Documenting the architecture and integration.

## What you need from others

| From | What | When |
|---|---|---|
| Remington | Real checkpoint files and the accuracy values (Boss 4); what is inside the checkpoint | Boss 4 |
| Kaleb | A working Python helper with `register` and `get_record`; contract address and ABI handoff | Boss 6 |
| Chris | Shared storage; a second person to run the workflow from your instructions | Boss 7 |

## Your first three actions

1. Read `docs/PROJECT_EXPLAINED.md` and `docs/SYSTEM_DESIGN.md`. Write down anything unclear or any change you want to propose.
2. Run `python --version` and `git --version` and add them to `docs/ENVIRONMENT.md`.
3. Make a small text file and calculate its SHA-256 with two different tools (see `docs/TROUBLESHOOTING.md`). Confirm they agree.

## Task list (in dependency order)

Each box is checked only when the file exists, the check passes, evidence is linked, and the reviewer has checked it.

- [ ] **1. Confirm the design decisions.** Meet Kaleb and Remington; turn each "proposed" item in `docs/SYSTEM_DESIGN.md` into "agreed" or change it. *Evidence:* merged PR editing that file. *Reviewer:* Remington.
- [ ] **2. Fingerprint function.** Write a SHA-256 function that reads a file in chunks (Python `hashlib`) plus a command that prints the 64-character result. *Evidence:* code in `integration/`, test log. *Reviewer:* Remington.
- [ ] **3. Independent check.** Confirm your function matches an independent tool on a test file. *Evidence:* both outputs saved in `results/raw/`. *Reviewer:* Remington.
- [ ] **4. Local comparison logic.** Build comparison returning MATCH, CHANGED, NO RECORD, tested with a clearly labeled temporary stand-in record. *Evidence:* test output for all three outcomes. *Reviewer:* Remington.
- [ ] **5. Fingerprint the three real checkpoints.** After Boss 4, record fingerprints and file sizes in `models/manifests/`. *Evidence:* manifest file. *Reviewer:* Remington.
- [ ] **6. Agree the interface with Kaleb.** Write the exact inputs and outputs of `register` and `get_record` in `integration/README.md`. *Evidence:* merged PR. *Reviewer:* Kaleb.
- [ ] **7. Verification command.** Connect your comparison logic to Kaleb's helper: file + run + stage in, one of the three results out. *Evidence:* output on the three originals. *Reviewer:* Kaleb (blockchain parts) and Remington.
- [ ] **8. Repeatable demonstration.** Write start-to-finish instructions in `integration/README.md`; run them twice. *Evidence:* two logs in `results/raw/`. *Reviewer:* Remington.
- [ ] **9. Tamper-copy script.** Create the three modified copies (T05 to T07) by changing bytes **in copies only**. Never load them as models. *Evidence:* script, list of copy names and sizes. *Reviewer:* Kaleb.
- [ ] **10. Verification tests T01 to T09, T12.** Run per `docs/TEST_PLAN.md`; fill `results/verification.csv`. *Evidence:* CSV rows and logs. *Reviewer:* Remington.
- [ ] **11. Timing harness and T14.** Time file reading, fingerprint, lookup, and comparison; 3 warm-up runs, then 10 measured per original. *Evidence:* `results/timing.csv` raw rows. *Reviewer:* Kaleb.
- [ ] **12. Architecture and integration documentation.** Update `docs/SYSTEM_DESIGN.md` to describe what was actually built. *Evidence:* merged PR. *Reviewer:* Kaleb and Remington.
- [ ] **13. Paper section drafted by you, in your own words** (see below). *Evidence:* draft in shared storage; contribution log entry. *Reviewer:* Chris (format and references) and Kaleb (technical accuracy).
- [ ] **14. Live demonstration plus backup recording.** *Evidence:* recording location; rehearsal notes. *Reviewer:* Chris.

## Paper section

Introduction, project purpose, overall design, and integration (about 2 pages, flexible). Outline: `paper/OUTLINE.md`.

## Presentation responsibility

"Why verify AI model files" (3 min), "Fingerprints" (3 min), and driving the live demonstration. See `presentation/OUTLINE.md`.

## Research questions and search terms

Questions: How can the integrity of AI model files be checked? What attacks change model files after they are saved? What does hash-based verification protect against, and what does it not?
Terms to try: model integrity verification, machine learning supply chain security, model provenance, trojaned or backdoored neural network, SHA-256 file integrity, software supply chain.
Add each source you verify to `research/sources.csv`.

## Your week's goals (write your own; keep them specific)

| Week | My goal (what I will do, by when, how I will know) | Mid-week check | End-of-week result |
|---|---|---|---|
| Oct 30 to Nov 5 | | | |
| Nov 6 to Nov 12 | | | |

## Example progress update

> **Shabach, Wed Nov 4.** Done: fingerprint function written and matches `sha256sum` on a test file (log: results/raw/fingerprint_check.txt). Next: comparison logic with the temporary record. Blocked: none. Need from Remington: checkpoint format by Friday.
