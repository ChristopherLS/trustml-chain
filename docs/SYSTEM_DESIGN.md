# System Design (PROPOSED, not built)

Everything here is a **proposal** for the team to confirm or change. When the team agrees on a detail, replace "proposed" with "agreed (date, who)". No component below exists yet.

## Components and owners

| Component | Folder | Owner | Plain job |
|---|---|---|---|
| Data preparation | `ml/` | Remington | Clean data, split 80/20 |
| Model training | `ml/` | Remington | Train in 3 stages, save 3 checkpoints, measure accuracy |
| Fingerprint calculator | `integration/` | Shabach | SHA-256 of a file |
| Registry contract | `blockchain/` | Kaleb | Store and enforce records |
| Python registry helper | `blockchain/` | Kaleb | `register` and `get_record` using Web3.py |
| Verification workflow | `integration/` | Shabach | File + run + stage in, MATCH / CHANGED / NO RECORD out |

## Flow

```
Remington: checkpoint file (stage N)
   |
Shabach: fingerprint = SHA-256(file bytes)
   |
Kaleb's helper: register(run, stage, fingerprint, accuracy)   -> local practice blockchain
   ...
Later, someone hands us a file:
Shabach: fingerprint = SHA-256(file bytes)
Kaleb's helper: get_record(run, stage)                         <- local practice blockchain
Shabach: compare -> MATCH / CHANGED / NO RECORD
```

## Verification outcomes

| Situation | Result |
|---|---|
| No record exists for that run and stage | **NO RECORD** |
| Record exists and fingerprints are identical | **MATCH** |
| Record exists and fingerprints differ | **CHANGED** |

## Contract rules (proposed)

1. A record is identified by **training run** and **stage**.
2. A record stores: the **model fingerprint**, the **reported accuracy**, and the **submitting account**.
3. **Only the designated account** (the account that deployed the contract) may register.
4. Registering the same run and stage twice is **rejected**. Records are never overwritten.
5. Retrieval returns a clear "exists or not" answer, so a missing record is a normal result, not a crash.

## Proposed data conventions (team confirms during Boss 1 to Boss 3)

| Item | Proposal | Why |
|---|---|---|
| Training run identifier | Whole number (1, 2, 3...) | Simple to type and test |
| Stage | Whole number 1, 2, or 3 | Matches the three saved checkpoints |
| Fingerprint | 64 hex characters in Python; stored in the contract as 32 bytes | SHA-256 is 32 bytes |
| Accuracy scale | Whole number in **basis points**: accuracy times 10,000, rounded to nearest (example of the format only: 8,123 would mean 81.23%) | Contracts do not handle decimals |
| Accuracy source | `results/accuracy.csv` stores the exact fraction; the on-chain integer is derived from it by one documented rule | One consistent scale everywhere |
| Checkpoint file names | `run-001_stage-1.pt` style names (extension depends on the save method) | Run and stage visible in the name |
| Contract address handoff | Kaleb writes address and ABI to a file Shabach reads; address changes when the local chain restarts | Avoids copy-paste mistakes |

## Decisions still open

| Decision | Owner | Needed by |
|---|---|---|
| Hardhat 2 or Hardhat 3 | Kaleb with Shabach | Boss 6 start |
| Exact checkpoint contents (settings and preprocessing info) | Remington with Shabach | Boss 3 |
| How the registry helper is imported by the verification code | Kaleb with Shabach | Boss 6 |
| Shared storage location | Chris | Boss 1 |

## What this system does NOT protect against

- A dishonest person who controls the designated account registering a false record.
- Bad or biased training data.
- A model that is inaccurate or unfair.
- Anything on a real network. The practice chain runs on one computer and shows the idea only.

Document these limits plainly in the paper.
