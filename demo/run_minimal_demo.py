#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

repo = Path(__file__).resolve().parents[1]
out = Path(__file__).resolve().parent / "output"
out.mkdir(parents=True, exist_ok=True)

mismatch = pd.read_csv(repo / "data/benchmark/mismatch_bucket_coverage.tsv", sep="\t")
panels = pd.read_csv(repo / "data/validation_panels/panel_tier_summary.tsv", sep="\t")
claims = pd.read_csv(repo / "data/role_gates/manuscript_claims.tsv", sep="\t")

focus = mismatch[
    mismatch["label"].isin(["TOPO_positive", "BE_positive", "CRISPRoffT_positive"])
    & mismatch["bucket"].isin(["mm_le4", "mm_eq5", "mm_eq6"])
].copy()

lines = []
lines.append("# TopoEdit-Off minimal demo summary")
lines.append("")
lines.append("## Mismatch-regime divergence")
for _, r in focus.iterrows():
    lines.append(
        f"- {r['label']} / {r['bucket']}: "
        f"observed={int(r['observed_label_rows'])}, "
        f"recall={float(r['recall_of_observed_label']):.6f}"
    )

lines.append("")
lines.append("## Validation panel tiers")
for _, r in panels.iterrows():
    unlabeled = int(r["unlabeled"]) if "unlabeled" in panels.columns else int(r.get("unlabeled_rows", 0))
    lines.append(
        f"- {r['panel_tier']}: rows={int(r['rows'])}, guides={int(r['guides'])}, "
        f"TOPO={int(r['topo_positive'])}, BE={int(r['be_positive'])}, "
        f"CRISPRoffT+={int(r['conventional_positive'])}, "
        f"CRISPRoffT-={int(r['conventional_negative'])}, unlabeled={unlabeled}"
    )

lines.append("")
lines.append("## Claim policy")
for _, r in claims.iterrows():
    lines.append(f"- {r['support_level']}: {r['claim']}")

(out / "minimal_demo_summary.md").write_text("\n".join(lines) + "\n")
focus.to_csv(out / "minimal_demo_mismatch_focus.tsv", sep="\t", index=False)
panels.to_csv(out / "minimal_demo_panel_tiers.tsv", sep="\t", index=False)
print("[DONE] demo outputs written to", out)
