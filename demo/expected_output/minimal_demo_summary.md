# TopoEdit-Off minimal demo summary

## Mismatch-regime divergence
- TOPO_positive / mm_le4: observed=833, recall=0.038543
- BE_positive / mm_le4: observed=360, recall=0.096205
- CRISPRoffT_positive / mm_le4: observed=78, recall=0.757282
- TOPO_positive / mm_eq5: observed=4301, recall=0.199010
- BE_positive / mm_eq5: observed=873, recall=0.233298
- CRISPRoffT_positive / mm_eq5: observed=13, recall=0.126214
- TOPO_positive / mm_eq6: observed=16478, recall=0.762447
- BE_positive / mm_eq6: observed=2509, recall=0.670497
- CRISPRoffT_positive / mm_eq6: observed=12, recall=0.116505

## Validation panel tiers
- core96: rows=96, guides=52, TOPO=20, BE=16, CRISPRoffT+=10, CRISPRoffT-=10, unlabeled=39
- expanded192: rows=192, guides=65, TOPO=40, BE=32, CRISPRoffT+=20, CRISPRoffT-=20, unlabeled=79
- backup384: rows=384, guides=80, TOPO=86, BE=66, CRISPRoffT+=32, CRISPRoffT-=40, unlabeled=159

## Claim policy
- SUPPORTED: Source-aware label harmonization is required for cross-assay off-target candidate benchmarking.
- SUPPORTED: TOPO and BE observed-positive spaces are high-mismatch dominated relative to conventional CRISPRoffT positives.
- SUPPORTED: Low-mismatch sequence-centric prioritization under-recovers TOPO/BE observed positives.
- SUPPORTED: Expanding candidate generation to mismatch 6 restores coverage but creates a large unranked tie-space.
- SUPPORTED: A strict validation panel can be constructed with balanced positive/control/unlabeled/QC/context strata.
- CONDITIONAL: AI all-PU provides modest expanded-panel enrichment.
- CONDITIONAL: TOPO-PU may be useful as a fold-balanced sampler.
- NOT_SUPPORTED: TopoEdit-Off is a calibrated off-target probability predictor.
- NOT_SUPPORTED: ATMP predicts off-target probability.
- NOT_SUPPORTED: Multi-atlas or AI rank replaces the default/sequence baseline.
- NOT_SUPPORTED: BE-specific AI head is successful.
