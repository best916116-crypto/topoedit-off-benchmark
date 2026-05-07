# TopoEdit-Off

**TopoEdit-Off** is a source-aware benchmark and validation-priority framework for high-mismatch genome-editing off-target candidates.

## Repository scope

This repository contains the public GitHub release package for `topoedit-off-benchmark`.

The repository intentionally contains only small, publication-facing resource tables, metadata, and a minimal demo. Candidate-level large derived tables are listed for Zenodo Data deposition and are not committed to GitHub.

## Repository structure

```text
data/benchmark/          Source-aware benchmark summaries
data/figure_sources/     TSV source tables for manuscript figures
data/validation_panels/  Core96, expanded192, backup384 validation-panel resources
data/hard_split/         Guide-heldout split summaries
data/role_gates/         Claim, role, ATMP, atlas, and AI policy summaries
demo/                    Minimal reproducibility demo
metadata/                File manifest, checksums, data dictionary, large-table manifest
```

## Quick demo

```bash
cd demo
python run_minimal_demo.py
cat output/minimal_demo_summary.md
```

## Data policy

Raw public SRA/genome/accessibility resources are not rehosted.

Large derived tables should be deposited in a separate Zenodo Dataset record. See `metadata/large_derived_tables_for_zenodo.tsv`.

## DOI placeholders

Code DOI: pending Zenodo code DOI  
Data DOI: pending Zenodo data DOI

## Version

v0.67E
