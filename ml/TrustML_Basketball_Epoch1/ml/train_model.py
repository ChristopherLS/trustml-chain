
import json
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

# Reproducibility
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

# Project paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
MODEL_DIR = ROOT / "models" / "checkpoints"
MANIFEST_DIR = ROOT / "models" / "manifests"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
MANIFEST_DIR.mkdir(parents=True, exist_ok=True)

FEATURES = [
    "FG_PCT_home",
    "REB_home",
    "AST_home",
    "FG_PCT_away",
    "REB_away",
    "AST_away",
]

TARGET = "HOME_TEAM_WINS"


class BasketballModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(6, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
        )

    def forward(self, x):
        return self.network(x).squeeze(1)


def main():
    print("Loading training and testing data...")

    train = pd.read_csv(DATA_DIR / "train.csv")
    test = pd.read_csv(DATA_DIR / "test.csv")

    # Fit normalization using training data only
    mean = train[FEATURES].mean()
    std = train[FEATURES].std().replace(0, 1)

    X_train = ((train[FEATURES] - mean) / std).to_numpy(
        dtype=np.float32
    )
    X_test = ((test[FEATURES] - mean) / std).to_numpy(
        dtype=np.float32
    )

    y_train = train[TARGET].to_numpy(dtype=np.float32)
    y_test = test[TARGET].to_numpy(dtype=np.float32)

    train_dataset = TensorDataset(
        torch.tensor(X_train),
        torch.tensor(y_train),
    )

    loader = DataLoader(
        train_dataset,
        batch_size=128,
        shuffle=True,
    )

    X_test_tensor = torch.tensor(X_test)
    y_test_tensor = torch.tensor(y_test)

    model = BasketballModel()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_function = nn.BCEWithLogitsLoss()

    results = {
        "training_games": len(train),
        "test_games": len(test),
        "seed": SEED,
        "baseline_accuracy": 0.5568680391495107,
        "checkpoints": {},
    }

    print("Starting training...")

    for epoch in range(1, 11):
        model.train()
        total_loss = 0

        for features, labels in loader:
            optimizer.zero_grad()

            predictions = model(features)
            loss = loss_function(predictions, labels)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        if epoch in [1, 5, 10]:
            model.eval()

            with torch.no_grad():
                logits = model(X_test_tensor)
                predictions = (torch.sigmoid(logits) >= 0.5).float()
                accuracy = (
                    predictions == y_test_tensor
                ).float().mean().item()

            checkpoint_path = (
                MODEL_DIR / f"basketball_epoch_{epoch}.pt"
            )

            torch.save(
                {
                    "epoch": epoch,
                    "model_state_dict": model.state_dict(),
                    "optimizer_state_dict": optimizer.state_dict(),
                    "features": FEATURES,
                    "mean": mean.to_dict(),
                    "std": std.to_dict(),
                    "seed": SEED,
                },
                checkpoint_path,
            )

            results["checkpoints"][str(epoch)] = {
                "test_accuracy": accuracy,
                "average_training_loss": total_loss / len(loader),
                "checkpoint": str(checkpoint_path),
            }

            print(
                f"Epoch {epoch}: "
                f"Test accuracy = {accuracy:.4f}"
            )

    with open(MANIFEST_DIR / "training_report.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\nTRAINING COMPLETE")
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
