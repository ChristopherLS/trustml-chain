# integration/ : Connecting Model Files to Verification (Shabach)

**Status: workflow run, code not committed yet.** The epoch 1 verification (4 of 4 checks: MATCH, MATCH, CHANGED, NO RECORD) was run in GitHub Codespaces against the local registry. The verification code and the saved terminal log (`results/raw/epoch1-verification.txt`) still need to be committed to this folder. Epochs 5 and 10 are waiting for their model files.

## What belongs here

- The SHA-256 fingerprint code.
- The verification command (file + run + stage -> MATCH, CHANGED, or NO RECORD).
- The tamper-copy script and timing harness.
- **The start-to-finish instructions** for running the full demonstration. A teammate who did not write the code must be able to follow them.

## Interface agreed with Kaleb

_To be filled in during Boss 5/6: exact inputs and outputs of `register` and `get_record`, and how the contract address is passed._

## Full demonstration steps

_To be written after Boss 7. Write them as numbered steps with the exact commands that were tested, and note which terminal each runs in._
