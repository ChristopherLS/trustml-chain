# Schedule (Recovery Plan)

**Written:** Friday, October 30, 2026 (evening).
**Final deadline:** Monday, November 16, 2026, 11:59 p.m. That is 17 days away, so the deadline has not passed.
**Assumption:** implementation has not started. Nothing in the repo shows otherwise.

All dates below are **proposed targets**, not progress. Adjust them in a team meeting and edit this file in a PR.

## Strategy

Build the **smallest complete demonstration** first: one model, three saved versions, three registered records, one checker that prints MATCH / CHANGED / NO RECORD. Reserve the last five days for writing and rehearsal. **Research and drafting the non-results paper sections start this week**, not at the end.

## Target dates

| Target date | Boss / activity | Who |
|---|---|---|
| Sat Oct 31 - Sun Nov 1 | **Boss 1** workspace set up; invitations accepted; environment table started; each person adds 3+ research sources | All; Chris coordinates |
| Mon Nov 2 - Tue Nov 3 | **Boss 2** data downloaded, inspected, cleaned, split. Kaleb: Hardhat running, contract drafted | Remington; Kaleb |
| Wed Nov 4 | **Boss 3** one model trained and saved. **Check-in 1: is the model training?** | Remington |
| Thu Nov 5 - Fri Nov 6 | **Boss 4** three checkpoints saved. **Boss 5** fingerprints verified locally. Contract tests passing | Remington; Shabach; Kaleb |
| Sat Nov 7 - Sun Nov 8 | **Boss 6** three real records registered. **Check-in 2: are three records on the practice chain?** | Kaleb; Shabach |
| Mon Nov 9 - Tue Nov 10 | **Boss 7** full workflow connected; first complete run | Shabach |
| Wed Nov 11 | **Boss 8** tests finished. **CODE FREEZE** (only fixes for failing tests after this) | Shabach; Kaleb; Chris |
| Wed Nov 11 - Fri Nov 13 | Paper sections drafted by their owners in their own words; results sections written from real CSVs; slides drafted | All |
| Sat Nov 14 | Paper assembled; IEEE formatting check; reference check; similarity check; abstract finalized | Chris (assembly); all review |
| Sun Nov 15 | Two timed rehearsals; backup demo recorded; final review | All |
| **Mon Nov 16** | **Target: submit by 12:00 noon.** Hard deadline 11:59 p.m. | Designated submitter |

## Decision points

- **Wed Nov 4 evening:** if no model has trained, Remington and Shabach pair up that night. Reduce model size or features, not scope elsewhere.
- **Sun Nov 8:** if records are not registered, drop all optional polish and finish the verification path only.
- **Wed Nov 11:** code freeze. New features are not allowed.

## If we fall behind: what to cut (in this order)

1. Extra charts and plots.
2. Convenience scripts beyond the required path.
3. Extra metrics beyond accuracy and the baseline.

**Never cut:** the three originals, three tampered copies, NO RECORD, unauthorized and duplicate tests, timing (10 per original after warm-up), gas from receipts, or the two-run repeatability test.

## Unknowns to settle this week (see PROGRESS.md)

- Presentation date and time.
- Who submits, and how.
- Which similarity checker is used.
- What AI help is allowed for code and planning.
