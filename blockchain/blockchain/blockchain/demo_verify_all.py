import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from tempfile import TemporaryDirectory
from time import perf_counter

import registry_client as registry

root = Path(__file__).resolve().parents[3]
models = root / "ml" / "TrustML_Basketball_Epoch1" / "models"
results = root / "results" / "raw"
results.mkdir(parents=True, exist_ok=True)

files = {e: models / f"basketball_epoch_{e}.pt" for e in (1, 5, 10)}
report_path = models / "training_report.json"
missing = [str(p) for p in [*files.values(), report_path] if not p.is_file()]
if missing:
    raise SystemExit("Missing files:\n" + "\n".join(missing))

report = json.loads(report_path.read_text(encoding="utf-8-sig"))
accuracies = {e: report["checkpoints"][str(e)]["test_accuracy"] for e in files}
run_id = datetime.now(timezone.utc).strftime("basketball-full-%Y%m%dT%H%M%S%fZ")
contract = registry.get_contract()
rows = []

def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def verify(path, lookup_id, stage):
    record = registry.get_record(lookup_id, stage, contract=contract)
    if record is None:
        return "NO RECORD"
    return "MATCH" if fingerprint(path) == record["fingerprint"] else "CHANGED"

print(f"Run ID: {run_id}")
print(f"Contract: {contract.address}")

with TemporaryDirectory() as temp:
    for stage, (epoch, original) in enumerate(files.items(), start=1):
        print(f"\nEpoch {epoch} | Stage {stage}")
        digest = fingerprint(original)
        receipt = registry.register(
            run_id, stage, digest, registry.accuracy_to_bps(accuracies[epoch]),
            contract=contract,
        )
        print("Registration receipt:", json.dumps(receipt))

        saved = registry.get_record(run_id, stage, contract=contract)
        if saved is None or saved["fingerprint"] != digest:
            raise RuntimeError(f"Registry readback failed for epoch {epoch}")
        print("Registry readback: MATCH")

        folder = Path(temp) / str(stage)
        (folder / "edited").mkdir(parents=True)
        original_bytes = original.read_bytes()
        renamed = folder / "renamed.pt"
        edited = folder / "edited" / original.name
        renamed.write_bytes(original_bytes)
        edited.write_bytes(original_bytes + b"\nDEMO COPY ONLY\n")

        cases = [
            ("Original", original, run_id, "MATCH"),
            ("Renamed exact copy", renamed, run_id, "MATCH"),
            ("Edited copy, same name", edited, run_id, "CHANGED"),
            ("Unknown run ID", original, run_id + "-missing", "NO RECORD"),
        ]
        for name, path, lookup_id, expected in cases:
            observed = verify(path, lookup_id, stage)
            print(f"{name}: expected={expected}, observed={observed}")
            rows.append({
                "run_id": run_id, "epoch": epoch, "stage": stage, "case": name,
                "expected": expected, "observed": observed,
                "registration_tx": receipt["tx_hash"],
                "registration_gas": receipt["gas_used"],
                "median_verification_ms": "",
            })

        verify(original, run_id, stage)  # warm-up
        times = []
        for _ in range(10):
            start = perf_counter()
            outcome = verify(original, run_id, stage)
            times.append((perf_counter() - start) * 1000)
            if outcome != "MATCH":
                raise RuntimeError(f"Repeated check failed for epoch {epoch}")
        rows[-4]["median_verification_ms"] = round(median(times), 3)
        print(f"Median verification time: {median(times):.3f} ms over 10 checks")

out = results / "all-epochs-verification.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

passed = sum(r["expected"] == r["observed"] for r in rows)
print(f"\nChecks passed: {passed}/{len(rows)}")
print(f"CSV saved to: {out}")
raise SystemExit(0 if passed == len(rows) else 1)
