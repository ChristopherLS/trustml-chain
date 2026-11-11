
import pandas as pd
import numpy as np
import json
from pathlib import Path

# Project folders
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "processed"
MANIFEST_DIR = ROOT / "data" / "manifests"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MANIFEST_DIR.mkdir(parents=True, exist_ok=True)

# Model features and answer
FEATURES = [
    "FG_PCT_home",
    "REB_home",
    "AST_home",
    "FG_PCT_away",
    "REB_away",
    "AST_away"
]

TARGET = "HOME_TEAM_WINS"

METADATA = ["GAME_DATE_EST", "GAME_ID"]

def main():
    input_file = RAW_DIR / "games.csv"

    print("Loading NBA dataset...")
    df = pd.read_csv(input_file)

    original_rows = len(df)

    # Convert dates and numeric columns
    df["GAME_DATE_EST"] = pd.to_datetime(
        df["GAME_DATE_EST"], errors="coerce"
    )

    required = METADATA + FEATURES + [TARGET]

    for column in FEATURES + [TARGET]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Keep completed games with all required values
    df = df.dropna(subset=required)
    missing_removed = original_rows - len(df)

    # Remove duplicate game IDs
    duplicate_count = int(df.duplicated("GAME_ID").sum())
    df = df.drop_duplicates("GAME_ID", keep="first")

    # Sort chronologically
    df = df.sort_values(
        ["GAME_DATE_EST", "GAME_ID"]
    ).reset_index(drop=True)

    # Chronological 80/20 split
    split_index = int(len(df) * 0.8)

    train = df.iloc[:split_index].copy()
    test = df.iloc[split_index:].copy()

    # Only keep permitted columns
    output_columns = METADATA + FEATURES + [TARGET]

    train[output_columns].to_csv(
        OUTPUT_DIR / "train.csv", index=False
    )

    test[output_columns].to_csv(
        OUTPUT_DIR / "test.csv", index=False
    )

    # Check for overlapping game IDs
    overlap = set(train["GAME_ID"]) & set(test["GAME_ID"])

    if overlap:
        raise RuntimeError("Game ID overlap detected!")

    # Baseline: always predict the majority training outcome
    majority_class = int(train[TARGET].mode().iloc[0])

    baseline_accuracy = float(
        (test[TARGET] == majority_class).mean()
    )

    # Save game IDs
    train["GAME_ID"].to_csv(
        MANIFEST_DIR / "train_game_ids.csv", index=False
    )

    test["GAME_ID"].to_csv(
        MANIFEST_DIR / "test_game_ids.csv", index=False
    )

    # Save preparation report
    report = {
        "original_rows": original_rows,
        "missing_required_rows_removed": missing_removed,
        "duplicate_game_ids_removed": duplicate_count,
        "clean_games": len(df),
        "training_games": len(train),
        "test_games": len(test),
        "training_start": str(train["GAME_DATE_EST"].min().date()),
        "training_end": str(train["GAME_DATE_EST"].max().date()),
        "test_start": str(test["GAME_DATE_EST"].min().date()),
        "test_end": str(test["GAME_DATE_EST"].max().date()),
        "overlapping_game_ids": len(overlap),
        "features": FEATURES,
        "target": TARGET,
        "baseline_class": majority_class,
        "baseline_test_accuracy": baseline_accuracy,
        "split_method": "Chronological 80/20"
    }

    with open(
        MANIFEST_DIR / "data_report.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(report, file, indent=4)

    print("\nDATA PREPARATION SUCCESSFUL")
    print("=" * 40)

    for key, value in report.items():
        print(f"{key}: {value}")

    print("\nFiles created:")
    print("data/processed/train.csv")
    print("data/processed/test.csv")
    print("data/manifests/train_game_ids.csv")
    print("data/manifests/test_game_ids.csv")
    print("data/manifests/data_report.json")


if __name__ == "__main__":
    main()
