"""Isolated test fixture: apply appends a receipt on every invocation."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--apply", action="store_true")
parser.add_argument("--attempt", required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parent
source = root / ".runtime/input.csv"
raw = source.read_bytes()
with source.open(newline="") as handle:
    rows = list(csv.DictReader(handle))
quantities = [int(row["quantity"]) for row in rows]
if any(value < 0 for value in quantities):
    raise ValueError("negative quantity")
result = {"attempt": args.attempt, "input_sha256": hashlib.sha256(raw).hexdigest(),
          "label": json.loads((root / "config.json").read_text())["label"],
          "rows": len(rows), "total": sum(quantities)}
if args.apply:
    with (root / ".runtime/executions.jsonl").open("a") as handle:
        handle.write(json.dumps(result, sort_keys=True) + "\n")
    (root / "result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, sort_keys=True))
