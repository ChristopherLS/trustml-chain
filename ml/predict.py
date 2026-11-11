

from pathlib import Path

import torch
from torch import nn


ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT = ROOT / "models" / "checkpoints" / "basketball_epoch_10.pt"

FEATURES = [
    "FG_PCT_home",
    "REB_home",
    "AST_home",
    "FG_PCT_away",
    "REB_away",
    "AST_away",
]


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
    if not CHECKPOINT.exists():
        raise FileNotFoundError(
            f"Checkpoint not found: {CHECKPOINT}"
        )

    checkpoint = torch.load(
        CHECKPOINT,
        map_location="cpu",
        weights_only=True,
    )

    model = BasketballModel()
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    print("\n===================================")
    print("     TRUSTML BASKETBALL PREDICTOR")
    print("===================================")
    print(f"Model checkpoint: Epoch {checkpoint['epoch']}")
    print("\nEnter the game statistics below.")
    print("Use completed-game statistics.\n")

    values = {}

    for feature in FEATURES:
        while True:
            try:
                values[feature] = float(input(f"{feature}: "))
                break
            except ValueError:
                print("Please enter a valid number.")

    normalized = [
        (values[feature] - checkpoint["mean"][feature])
        / checkpoint["std"][feature]
        for feature in FEATURES
    ]

    inputs = torch.tensor([normalized], dtype=torch.float32)

    with torch.no_grad():
        logits = model(inputs)
        probability = torch.sigmoid(logits).item()

    print("\n===================================")
    print("           PREDICTION")
    print("===================================")
    print(f"Home team win probability: {probability:.2%}")
    print(f"Away team win probability: {(1 - probability):.2%}")

    if probability >= 0.5:
        print("\nPREDICTION: HOME TEAM WINS")
    else:
        print("\nPREDICTION: AWAY TEAM WINS")

    print("===================================")


if __name__ == "__main__":
    main()
