# Definition of Done

## Two different kinds of "done"

| Kind | What it means | Who did it |
|---|---|---|
| **Workspace setup** | The folders, instructions, templates, and checklists exist | Completed by the setup agent (Claude) on 2026-10-30 |
| **Project development** | The model is trained, the contract works, tests pass, the paper is written | **The team. None of this is done yet.** |

Creating a checklist is not completing the work the checklist describes.

## A box may be checked only when ALL four are true

1. **The promised file or output exists.**
2. **Its relevant check passes** (a test, a comparison, a re-run, a page count).
3. **Evidence is linked** (a file path in the repo, a log in `results/raw/`, or a pull request link).
4. **The assigned reviewer has checked it.**

If any of the four is missing, the box stays unchecked.

## Statuses

Use exactly these:

| Status | Meaning |
|---|---|
| Not started | Nobody has begun |
| In progress | Someone is actively working on it |
| Blocked | Cannot continue; the reason and who can unblock it is written down |
| Ready for review | The four conditions are met except reviewer sign-off |
| Done | All four conditions are met |

On GitHub issues these appear as labels: `status:not-started`, `status:in-progress`, `status:blocked`, `status:ready-for-review`, `status:done`.

## What counts as evidence

Good:
- A file in the repo at a stated path.
- A pasted command and its real output saved in `results/raw/`.
- A pull request link where the reviewer approved.
- A row in a `results/` CSV with raw values.

Not good:
- "It worked on my computer" with nothing saved.
- Numbers typed into a document with no raw record.
- Screenshots of results that cannot be reproduced by anyone else.

## What nobody may do

- Mark training, blockchain development, testing, research, or writing complete because a document about it exists.
- Invent results, sources, or progress percentages.
- Edit a test's expected result after seeing the actual result.

## Completed-task counting (optional)

You may report **completed tracked tasks**:

```
completed tracked tasks = number of checked task boxes in team/*.md
total tracked tasks     = number of task boxes in team/*.md
shown as: "X of Y completed tracked tasks"
```

This is a count, **not** a percentage of the project. Tasks differ a lot in effort (installing a tool is not the same as training a model), so "X of Y" must not be read as "X/Y of the work."

## Handling failures honestly

- A failed test is a **result**, not a mistake to hide. Record it in the CSV with the real output.
- Do not delete failed rows. Add the fix and the re-run as new rows.
- If a result is surprising (for example accuracy goes down in stage 2), report it and move on. There is no required minimum accuracy.
