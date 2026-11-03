# Environment Record

Record **versions that actually work on your computer**. Do not copy a version from a web page unless you have run it. Fill in the table when you first install each tool, and update it if you change anything.

## What the documentation said when checked (2026-10-30)

These are notes from reading documentation pages, **not tested here**. Re-check the official pages before installing.

| Tool | What the documentation said | Source |
|---|---|---|
| PyTorch | Recommends Python 3.10 to 3.14. Generate the install command from the "Get Started" selector (choose CPU, since no GPU is needed) | pytorch.org "Get Started" |
| Hardhat 3 | Described as production ready. Requires Node.js v22.13.0 or later. Supports even-numbered Node.js releases that are still maintained. Project start command: `npx hardhat --init` | hardhat.org getting-started docs |
| Web3.py | Install with `pip install web3`. The extra `web3[tester]` is only needed for the built-in test provider. We plan to talk to a Hardhat node over HTTP instead | web3py.readthedocs.io quickstart |
| Dataset | `hamzas/nba-games` on Hugging Face is described on a mirror page as an updated version of the Kaggle "NBA Games" dataset by Nathan Lauga, updated to 2025-02-13, containing `games.csv`, `games_details.csv`, `players.csv`, `ranking.csv`, `teams.csv` | Mirror page (the Hugging Face page itself could not be opened when this was checked) |

**Not verified:** the latest Web3.py version, the Solidity compiler version Hardhat will use, the dataset license, and the dataset columns. A decision on Hardhat 2 versus Hardhat 3 belongs to Kaleb and Shabach; record it below.

## Version table (team fills in)

| Item | Version / value | Recorded by | Date |
|---|---|---|---|
| Operating system | | | |
| Git (`git --version`) | | | |
| Python (`python --version`) | | | |
| pandas and NumPy (`pip show pandas numpy`) | | | |
| PyTorch (`pip show torch`) | | | |
| Web3.py (`pip show web3`) | | | |
| Node.js (`node --version`) | | | |
| npm (`npm --version`) | | | |
| Hardhat (`npx hardhat --version`) | | | |
| Solidity compiler version (from the Hardhat config file) | | | |
| Random seed used for the data split | | | |
| Random seed used for training | | | |

## Shared storage

| Item | Value |
|---|---|
| Where large files live (service + folder link, no passwords) | |
| Who can access it | |
| Last time the folder was checked | |

Rule: large artifacts (dataset, model checkpoints, Word and PowerPoint drafts) live in shared storage. The repo tracks **fingerprints and retrieval instructions**, not the big files.
