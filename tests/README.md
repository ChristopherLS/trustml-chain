# tests/ : Shared Tests

**Status: NOT STARTED.**

## What belongs here

- Shared Python tests that are not specific to one folder.
- Notes on how to run them.

Contract tests live with the contract in `blockchain/`. Measured results go in `results/`. The full list of required tests is in `docs/TEST_PLAN.md`.

Rule: never load deliberately damaged model files in any test. Only hash their bytes.
