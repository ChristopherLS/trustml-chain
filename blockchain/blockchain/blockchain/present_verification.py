#!/usr/bin/env python3
"""Present TrustML verification from a saved log, or run the verifier and present fresh output."""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ansi = sys.stdout.isatty() and 'NO_COLOR' not in __import__('os').environ
def color(value, code):
    return f"\033[{code}m{value}\033[0m" if ansi else str(value)

def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Run demo_verify_all.py against the local chain first")
    parser.add_argument("--interactive", action="store_true", help="Pause before revealing each epoch")
    parser.add_argument("--log", type=Path, default=here.parents[2] / "results/raw/all-epochs-verification.txt" if len(here.parents)>2 else Path("all-epochs-verification.txt"))
    args = parser.parse_args()
    folder = args.log.parent
    if args.live:
        folder.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        csv_path = folder / "all-epochs-verification.csv"
        if csv_path.exists():
            import shutil
            shutil.copy2(csv_path, folder / f"previous-verification-{stamp}.csv")
        print("Running the actual registry checks now…", flush=True)
        run = subprocess.run([sys.executable, "-u", str(here / "demo_verify_all.py")],
                             cwd=here, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = folder / f"live-verification-{stamp}.txt"
        log.write_text(run.stdout, encoding="utf-8")
        if run.returncode:
            print(run.stdout, end="")
            raise SystemExit(f"Live run failed. Output saved to {log}")
        raw = run.stdout
    else:
        try:
            raw = args.log.read_text(encoding="utf-8-sig")
        except OSError as exc:
            raise SystemExit(f"Could not open the saved log: {exc}")
        log = args.log
    groups = re.split(r"(?m)^Epoch (\d+) \| Stage (\d+)[^\n]*\n", raw)
    total = re.search(r"(?m)^Checks passed: (\d+)/(\d+)", raw)
    if len(groups) < 4 or not total:
        raise SystemExit(f"No complete verification run found in {log}. Open the log to see the original output.")
    items = []
    for i in range(1, len(groups), 3):
        epoch, stage, body = groups[i:i+3]
        receipt = re.search(r"Registration receipt:\s*(\{[^}]*\})", body)
        timing = re.search(r"Median verification time:\s*([\d.]+) ms over (\d+) checks", body)
        cases = re.findall(r"(?m)^(.+?): expected=(.+?), observed=([^\r\n]+)", body)
        readback = re.search(r"(?m)^Registry readback:\s*([^\r\n]+)", body)
        if not receipt or not timing or len(cases) != 4 or not readback:
            raise SystemExit(f"Incomplete evidence for epoch {epoch}; see {log}.")
        items.append((epoch, stage, json.loads(receipt[1]), timing.groups(), cases, readback[1]))
    print("\n" + color("TRUSTML-CHAIN  /  MODEL FILE VERIFICATION", "1;36"))
    print("LIVE RUN • just measured" if args.live else "REPLAY • recorded verification results")
    for line in groups[0].splitlines():
        if line.startswith(("Run ID:", "Contract:")):
            print(line)
    for epoch, stage, receipt, timing, cases, readback in items:
        print("\n" + color(f"EPOCH {epoch}  /  REGISTRY STAGE {stage}", "1;36"))
        print(f"Block {receipt['block_number']} | Registry readback: {readback}")
        print(f"Transaction: {receipt['tx_hash']}")
        if args.interactive and sys.stdin.isatty():
            try:
                input("Which files will match? Press Enter to reveal… ")
            except EOFError:
                pass
        print(f"{'FILE CHECK':<33} {'EXPECTED':<12} {'OBSERVED':<12} RESULT")
        print("-" * 68)
        for name, expected, observed in cases:
            ok = expected == observed
            print(f"{name:<33} {expected:<12} {observed:<12} " +
                  color("PASS" if ok else "FAIL", "1;32" if ok else "1;31"))
        print(f"Registration: {receipt['gas_used']:,} gas | Median check: {timing[0]} ms ({timing[1]} checks)")
    print("\n" + color(f"FINAL RESULT  /  {total[1]} of {total[2]} checks passed",
                       "1;32" if total[1] == total[2] else "1;31"))
    print("File integrity results only. Model accuracy is measured separately.")
    print(f"Evidence: {log}")
    return 0 if total[1] == total[2] else 1

if __name__ == "__main__":
    sys.exit(main())
