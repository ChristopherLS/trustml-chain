# integration/ : Connecting Model Files to Verification (Shabach)

**Status: working.** The verification code lives in `blockchain/blockchain/blockchain/` next to the registry helper it uses: `demo_verify_all.py` runs all 12 checks (3 model files x 4 cases) and writes `results/raw/all-epochs-verification.txt` and `.csv`; `present_verification.py` replays or presents the results (add `--live` to rerun). Last run: **12 of 12 checks passed**.

## What belongs here

- The SHA-256 fingerprint code.
- The verification command (file + run + stage -> MATCH, CHANGED, or NO RECORD).
- The tamper-copy script and timing harness.
- **The start-to-finish instructions** for running the full demonstration. A teammate who did not write the code must be able to follow them.

## Interface agreed with Kaleb

_To be filled in during Boss 5/6: exact inputs and outputs of `register` and `get_record`, and how the contract address is passed._

## Full demonstration steps

_To be written after Boss 7. Write them as numbered steps with the exact commands that were tested, and note which terminal each runs in._
