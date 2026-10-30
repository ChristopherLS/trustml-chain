# blockchain/ : Smart Contract and Local Blockchain (Kaleb)

**Status: NOT STARTED. No contract or Hardhat project exists yet.**

## What belongs here

- The Hardhat project (config, contract, tests, deploy steps).
- `blockchain/abi/` : the exported contract interface that Python needs (this file **is** tracked in Git).
- A small Python helper using Web3.py with `register` and `get_record`.
- This README with tested start, deploy, and test commands.

## What does NOT belong here

- `node_modules`, build output, and local chain state (ignored by `.gitignore`).
- Private keys or `.env` files.

## Contract rules to implement (from `docs/SYSTEM_DESIGN.md`)

1. Records identified by training run and stage.
2. Store the model fingerprint and reported accuracy.
3. Record the submitting account.
4. Only the designated account may register.
5. Reject duplicate run-and-stage registration.
6. Clear response for a missing record.

If accuracy is stored as an integer, document the scale in this README and in `docs/SYSTEM_DESIGN.md`.

## Commands

_To be written by Kaleb after they work on a real setup. Do not paste commands you have not run._
