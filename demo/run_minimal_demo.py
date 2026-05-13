#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
out = Path(__file__).resolve().parent / "output"
out.mkdir(exist_ok=True)

ranking = pd.read_csv(root / "data/ranking/size_matched_topk_recovery_summary.tsv", sep="\t")
delta = pd.read_csv(root / "data/ranking/delta_vs_sequence_baseline_summary.tsv", sep="\t")
labels = pd.read_csv(root / "data/benchmark/source_aware_label_inventory.tsv", sep="\t")

top1000 = ranking[ranking["k"].eq(1000)].copy()
top1000.to_csv(out / "top1000_recovery_summary.tsv", sep="\t", index=False)

lines = [
    "# TopoEdit-Off minimal demo",
    "",
    f"Ranking rows: {len(ranking)}",
    f"Delta rows: {len(delta)}",
    f"Label-inventory rows: {len(labels)}",
    "",
    "Top-1000 size-matched recovery summary written to `top1000_recovery_summary.tsv`.",
]
(out / "minimal_demo_summary.md").write_text("\n".join(lines) + "\n")
print(f"[DONE] demo outputs written to {out}")
