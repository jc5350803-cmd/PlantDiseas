# 02 — Proposed Methodology

Paper section: PlantDiseaseNet-Hybrid architecture.

## Architecture definition used in the manuscript
`256×256×3 → Inception(Add)-16 → MaxPool → Inception(Add)-32 → MaxPool → SkipConnection(Concat)-64 → MaxPool → SkipConnection(Concat)-128 → MaxPool → GAP → Dense(512) → Dropout → Dense(128) → Dropout → Softmax(24)`.

The supplied Keras summary totals 934,200 parameters. This architecture-level count must not be confused with the approximately 59.8M parameter counts recorded by older primary experiment logs.

## Figures
The manuscript expects the architecture figures under `paper_figures/`, including the overall architecture, Inception(Add) block, SkipConnection(Concat) block, and preprocessing/augmentation pipeline.
