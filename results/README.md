# results/ : Measurements and Evidence

**Status: templates only. No results have been collected.**

## How to use the templates

1. Copy a template to a real file (for example `accuracy_template.csv` -> `accuracy.csv`). Keep the header row.
2. Add **one row per real measurement**. Do not invent or round values to look better.
3. Do not delete rows. If you made a mistake, add a corrected row and explain in `notes`.
4. Raw logs go in `results/raw/` as `.txt` files and are linked from the CSV `evidence_path` column.

| Template | For |
|---|---|
| `accuracy_template.csv` | Accuracy of each stage and the baseline |
| `verification_template.csv` | Expected versus actual for every test (T01 to T15) |
| `timing_template.csv` | Raw per-run timing (10 per original after warm-up) |
| `gas_template.csv` | Gas units from registration receipts |

## Units (write them in the column names or notes)

- Time: milliseconds.
- File size: bytes.
- Gas: gas units (never dollars).
- Accuracy: keep the exact fraction in the CSV. If you also store an integer on the blockchain, state the scale.
- Be careful to label what you are counting: tests vs devices vs environments vs people.
