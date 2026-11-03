# data/ : Dataset Notes

**Status: NOT STARTED. No data has been downloaded.**

## Layout

| Path | Contents | In Git? |
|---|---|---|
| `data/raw/` | Downloaded files such as `games.csv` | No (ignored) |
| `data/processed/` | Cleaned files | No (ignored) |
| `data/manifests/` | Raw-file fingerprint, seed, training/test `GAME_ID` lists, data report | Yes |

## Source

- Starting point: https://huggingface.co/datasets/hamzas/nba-games/tree/main
- A mirror page describes it as an updated version of the Kaggle "NBA Games" dataset by Nathan Lauga, updated to 2025-02-13. **The Hugging Face page itself could not be opened when this was checked, so the columns and license below are unverified.**
- File we plan to use: `games.csv`, **only if inspection confirms it is suitable**.

## To fill in during Boss 2 (Remington, checked by Chris)

| Item | Value |
|---|---|
| Date downloaded | |
| Exact download link used | |
| SHA-256 of downloaded `games.csv` | |
| License / usage terms (copy the wording and where you found it) | |
| Attribution text to use in the paper | |
| Required columns present? (`GAME_ID`, `HOME_TEAM_WINS`, `FG_PCT_home`, `REB_home`, `AST_home`, `FG_PCT_away`, `REB_away`, `AST_away`) | |
| Rows before cleaning | |
| Duplicate `GAME_ID` rows removed | |
| Rows removed for missing needed values | |
| Rows after cleaning | |
| Training rows / test rows | |
| Split seed | |

If a required column is missing or the terms do not allow our use, stop and tell the team the same day.
