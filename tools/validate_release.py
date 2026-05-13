#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import pandas as pd

REQUIRED = [
    "README.md",
    "LICENSE",
    "CITATION.cff",
    ".zenodo.json",
    "DATA_AVAILABILITY.md",
    "CLAIM_POLICY.md",
    "data/benchmark/mismatch_bucket_coverage.tsv",
    "data/ranking/size_matched_topk_recovery_summary.tsv",
    "data/ranking/delta_vs_sequence_baseline_summary.tsv",
    "metadata/file_manifest.tsv",
    "metadata/checksums.tsv",
    "demo/run_minimal_demo.py",
]

def j(*parts: str) -> str:
    return "/".join(parts)

FORBIDDEN_DIRS = [
    "figures",
    j("data", "figure" + "_sources"),
    j("data", "reviewer" + "_defense"),
    j("data", "hard" + "_split"),
    j("data", "role" + "_gates"),
    j("data", "release" + "_metadata"),
]
HEAVY_SUFFIXES = (".fastq", ".fastq.gz", ".sra", ".bam", ".bai", ".sam")
STEP_PATTERN = re.compile(("s" + "tep") + r"[0-9]", re.IGNORECASE)

FORBIDDEN_TEXT = [
    "/home/" + "pjj",
    "data/" + "product/v0_",
    "github.com/" + "TBD",
    "zenodo" + "." + "TBD",
    "Prepare-" + "TopoEdit",
]

def skip(rel: str) -> bool:
    rel = rel.replace("\\", "/")
    return (
        rel.startswith(".git/")
        or rel.startswith("demo/output/")
        or "__pycache__/" in rel
        or rel.endswith(".pyc")
        or rel == "tools/validate_release.py"
    )

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    missing = [p for p in REQUIRED if not (root / p).exists()]
    if missing:
        print("[FAIL] missing required files")
        for p in missing:
            print(" -", p)
        return 1

    bad_dirs = [d for d in FORBIDDEN_DIRS if (root / d).exists()]
    if bad_dirs:
        print("[FAIL] forbidden public directories")
        for d in bad_dirs:
            print(" -", d)
        return 1

    try:
        json.loads((root / ".zenodo.json").read_text())
    except Exception as e:
        print(f"[FAIL] invalid .zenodo.json: {e}")
        return 1

    try:
        ranking = pd.read_csv(root / "data/ranking/size_matched_topk_recovery_summary.tsv", sep="\t")
        if set(ranking["k"]) != {10, 50, 100, 500, 1000}:
            print("[FAIL] unexpected K values in ranking table")
            return 1
        if set(ranking["method_key"]) != {"sequence_baseline", "integrated_heuristic", "supervised_atlas_model"}:
            print("[FAIL] unexpected ranking methods")
            return 1
    except Exception as e:
        print(f"[FAIL] ranking table parse/semantic error: {e}")
        return 1

    bad_text = []
    text_suffixes = {".md", ".txt", ".json", ".cff", ".tsv", ".py", ".sh", ".yml", ".yaml"}
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = str(p.relative_to(root)).replace("\\", "/")
        if skip(rel):
            continue
        if p.suffix.lower() not in text_suffixes:
            continue
        txt = p.read_text(errors="replace")
        for needle in FORBIDDEN_TEXT:
            if needle in txt:
                bad_text.append(f"{rel}: blocked_text")
        if STEP_PATTERN.search(txt):
            bad_text.append(f"{rel}: workflow_token")
    if bad_text:
        print("[FAIL] internal text remains")
        for p in sorted(set(bad_text)):
            print(" -", p)
        return 1

    heavy = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = str(p.relative_to(root)).replace("\\", "/")
        if skip(rel):
            continue
        if rel.endswith(HEAVY_SUFFIXES):
            heavy.append(rel)
    if heavy:
        print("[FAIL] raw/heavy files found")
        for p in heavy:
            print(" -", p)
        return 1

    print("[PASS] minimal TopoEdit-Off public release validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
