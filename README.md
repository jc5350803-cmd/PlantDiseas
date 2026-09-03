# PlantDiseaseNet-Hybrid — Paper-Aligned Research Branch

This branch is the **paper-aligned research record** for PlantDiseaseNet-Hybrid. The original `main` branch is not modified by this organisation pass. The branch is organised around the experimental families intended for the manuscript.

## Paper scope

The manuscript retains:

1. **Primary Dataset-Specific Evaluation** — Wheat, Cotton and the selected PlantVillage subset.
2. **Architectural Ablation** — controlled 24-class comparison of Standard Inception, Residual CNN, Inception(Add)-only, SkipConcat-only and the complete PlantDiseaseNet-Hybrid.
3. **Dedicated Augmentation Study** — the same 24-class benchmark and hybrid architecture under different augmentation policies.
4. **SoyDisease Evaluation** — the published Indian soybean dataset, kept separate from the 24-class benchmark.

`SoyCultivar200` is excluded. The potato augmentation notebook is not a paper experiment; it is used only as a literature/reporting reference, following Mhala et al. (2025).

## Repository structure

```text
paper-organized-soydisease/
├── README.md
├── evidence/
│   ├── DATA_SOURCES.md
│   └── NOTEBOOK_AUDIT.md
├── experiments/
│   ├── primary/
│   │   ├── NB1_Wheat_Hybrid.ipynb
│   │   ├── NB2_Cotton_Hybrid.ipynb
│   │   └── NB3_PlantVillage_Hybrid.ipynb
│   ├── architecture_ablation/
│   │   ├── NB4_Combined_StandardInception.ipynb
│   │   ├── NB5_Combined_ResNet.ipynb
│   │   ├── NB6_Combined_InceptionAdd.ipynb
│   │   └── NB7_Combined_SkipConcat.ipynb
│   ├── augmentation/
│   │   └── selected augmentation-study notebooks
│   └── soydisease/
│       ├── soydisease1.ipynb
│       ├── soydisease2.ipynb
│       ├── soydisease3.ipynb
│       ├── soydisease4.ipynb
│       ├── soydisease5.ipynb
│       └── soydisease6.ipynb
├── paper/
│   ├── cas-dc-template-final.tex
│   ├── references.bib
│   └── results.csv
└── paper_figures/
    ├── preprocessing_pipeline.png
    ├── overall_architecture.png
    ├── inception_block.jpg
    └── skip_block.jpg
```

## Experimental results currently recorded

### Primary dataset-specific evaluation

| Experiment | Dataset | Classes | Accuracy | Precision | Recall | F1 | Specificity |
|---|---|---:|---:|---:|---:|---:|---:|
| NB1 Wheat Hybrid | Wheat | 3 | 97.81% | 97.82% | 97.81% | 97.81% | 98.54% |
| NB2 Cotton Hybrid | Cotton | 6 | 53.55% | 53.01% | 53.55% | 51.66% | 90.71% |
| NB3 PlantVillage Hybrid | PlantVillage subset | 15 | 97.67% | 97.68% | 97.67% | 97.68% | 99.83% |

The stored Wheat result has zero test support for the Healthy class. It is retained for traceability but must be qualified in the manuscript.

### Complete 24-class benchmark

PlantDiseaseNet-Hybrid records 95.91% accuracy, 95.98% precision, 95.91% recall, 95.91% F1-score, 99.82% specificity, 0.9996 micro-AUC and 0.9990 macro-AUC. The saved architecture has 934,200 total parameters, of which 933,720 are trainable and 480 are non-trainable.

### Augmentation study

| Condition | Main policy | Accuracy |
|---|---|---:|
| Hybrid-NoAug | None | 96.03% |
| Hybrid-CropColour | Crop + colour | 96.31% |
| Hybrid-LightAug | Flip + brightness | **97.06%** |
| Hybrid-LightAug-v2 | Flip + brightness | 96.43% |
| Hybrid-FullAug | All recorded transforms | 95.91% |

The 97.06% value is reported as the best recorded augmentation-policy run, not as a universal claim. The independent LightAug repeat records 96.43%.

### Architectural ablation

| Configuration | Accuracy | Precision | Recall | F1 | Specificity |
|---|---:|---:|---:|---:|---:|
| Standard Inception + GAP | 95.33% | 95.34% | 95.33% | 95.32% | 99.80% |
| Residual CNN + GAP | **96.04%** | 96.03% | 96.04% | 96.02% | 99.83% |
| Inception(Add)-only + GAP | 95.84% | 95.84% | 95.84% | 95.82% | 99.82% |
| SkipConcat-only + GAP | 95.67% | 95.70% | 95.67% | 95.67% | 99.81% |
| PlantDiseaseNet-Hybrid | 95.91% | **95.98%** | 95.91% | **95.91%** | 99.82% |

The residual comparator is slightly more accurate. The paper therefore does not claim universal accuracy superiority for the proposed model.

### SoyDisease

The published Indian soybean dataset contains 3363 source images in six categories. The project experiments use a processed 1176-image subset. Recorded single-split experiments include two 100% results, but these are treated cautiously because the Root Images class contains only ten images. The preferred generalisation estimate is the recorded five-fold result of **99.57% ± 0.85%**.

## Data provenance

The paper cites scholarly/original sources rather than treating Kaggle as the primary scientific source:

- PlantVillage: Mohanty, Hughes and Salathé (2016), *Frontiers in Plant Science*, DOI `10.3389/fpls.2016.01419`.
- Wheat: Fang, Zhen and Li (2023), *Applied Sciences*, 13(9), 5801, DOI `10.3390/app13095801`.
- Cotton: Bishshash et al. (2024), *Data in Brief*, DOI `10.1016/j.dib.2024.110913`.
- Indian soybean: Kotwal, Kashyap and Pathan (2024), *Data in Brief*, 53, 110216, DOI `10.1016/j.dib.2024.110216`; dataset DOI `10.17632/bshkvgbzpt.1`.
- Augmentation-reporting reference: Mhala, Bilandani and Sharma (2025), *Expert Systems with Applications*, 267, 126066, DOI `10.1016/j.eswa.2024.126066`.

## Evidence and reproducibility policy

No notebook is executed as part of the repository-organisation or paper-writing process. Saved outputs are inspected statically. Metrics enter `paper/results.csv` only when they can be traced to project evidence.

A static audit has identified that at least one GitHub copy of a selected primary notebook currently contains `execution_count: null` and empty outputs in its inspected cells. Therefore the exact provenance of the corresponding saved result must be reconciled with the original executed notebook/log before final submission. The paper does not treat the GitHub copy itself as proof of execution.

The audit also identified a hard-coded Kaggle credential in an inspected notebook. That credential must be revoked/rotated and removed before any public release. Credentials are never part of the manuscript evidence.

## Figures

The current paper figure directory contains the preprocessing pipeline, overall architecture, Inception(Add) block and SkipConnection(Concat) block. Training curves, confusion matrices, ROC/PR curves and augmentation examples must be added only from saved notebook outputs. They must not be recreated from aggregate numbers.
