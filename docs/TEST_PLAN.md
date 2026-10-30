# Test Plan

No test has been run. Every "Actual" column starts empty. Fill in real results only.

## Rules for every test

- Write the **expected** result **before** running.
- Record the **actual** result exactly as observed. Mark Pass or Fail.
- Save the command output in `results/raw/` and link it.
- Record file sizes (bytes) and the environment versions from `docs/ENVIRONMENT.md`.
- **Never load deliberately damaged model files. Only hash their bytes.**
- If a test fails: keep the failed row, write what you think went wrong, fix, and add a **new** row for the re-run. Never change the expected value after seeing the actual one.

## Tests

| ID | What we do | Expected | Owner | Evidence goes in |
|---|---|---|---|---|
| T01 | Verify original stage 1 against its registered record | MATCH | Shabach | `results/verification.csv` |
| T02 | Verify original stage 2 | MATCH | Shabach | same |
| T03 | Verify original stage 3 | MATCH | Shabach | same |
| T04 | Verify an exact copy of an original (copy with a file manager or `cp`, not by loading and re-saving) | MATCH | Shabach | same |
| T05 | Modified copy A: change one byte of a copy of stage 1 | CHANGED | Shabach | same |
| T06 | Modified copy B: append extra bytes to a copy of stage 2 | CHANGED | Shabach | same |
| T07 | Modified copy C: remove bytes from the end of a copy of stage 3 | CHANGED | Shabach | same |
| T08 | Ask for a run that was never registered | NO RECORD | Shabach | same |
| T09 | Ask for a stage that was never registered for a real run | NO RECORD | Shabach | same |
| T10 | Try to register from an account that is not the designated one | Rejected, no record created | Kaleb | same |
| T11 | Try to register the same run and stage again | Rejected, original record unchanged | Kaleb | same |
| T12 | Run the complete workflow twice from the documented instructions (second run by a different person or on a fresh clone) | Same outcomes both times | Shabach, Chris | logs in `results/raw/` |
| T13 | Check accuracy used only test games: no test ID appears in the training list; counts match | Pass | Remington | `results/accuracy.csv` and manifests |
| T14 | Timing: 10 measurements per original (30 total) after warm-up | All 30 collected | Shabach | `results/timing.csv` |
| T15 | Gas: read `gasUsed` from each registration transaction receipt | One value per successful registration | Kaleb | `results/gas.csv` |

## Timing method (T14)

- Time **the same four operations every time**: file reading, fingerprint calculation, record lookup, comparison.
- **Exclude** model training and blockchain startup. The local chain is already running and the contract already deployed.
- **Warm-up:** run the whole check 3 times and discard those runs, then record 10 measured runs per original.
- Use one clock consistently (for example Python `time.perf_counter_ns`), record in milliseconds, and keep the raw per-run values.
- Close heavy programs. Record the computer and software versions once. Do not delete slow runs.

## Gas method (T15)

- Report **gas units** from transaction receipts only.
- Do **not** report or estimate dollar costs.
- Record the transaction hash so anyone can check the receipt.
- Rejected transactions are not registrations; note them separately in the verification CSV.

## Failure examples (what honest looks like)

- "T06 expected CHANGED, got MATCH. Cause: script read the original instead of the copy. Fixed script; re-run is row T06b, passed."
- "T14 run 7 was slow because a backup started. Kept in data and noted."
