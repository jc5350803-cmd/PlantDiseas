# PlantDiseaseNet-Hybrid — Paper Evidence Branch

This branch is organised around the experiments actually used in the PlantDiseaseNet-Hybrid manuscript. It is intentionally separate from `main` so the working repository is not destroyed or rewritten.

## Important evidence policy

- Notebooks were **not executed** while preparing this branch.
- Existing notebook outputs/logs are treated as evidence only.
- A result is marked **verified** only when it is directly available in a repository metrics/classification file.
- Earlier manuscript numbers that cannot currently be matched to an exported result file are retained as **draft-reported** and are not silently presented as verified.
- `Soycultivar200` is excluded. `SoyDisease` is included using the India soyabean disease dataset.
- The potato augmentation notebook is excluded; it is a reference for how to report augmentation studies, not an experiment in this paper.

## Paper-aligned structure

```text
paper-organized-final/
├── README.md
├── paper/
│   ├── cas-dc-template.tex
│   └── results.csv
├── paper_figures/
│   ├── preprocessing_pipeline.png
│   ├── overall_architecture.png
│   ├── inception_block.jpg
│   └── skip_block.jpg
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
│   │   ├── nb2.ipynb
│   │   ├── nb3.ipynb
│   │   ├── nb4.ipynb
│   │   ├── nb5.ipynb
│   │   ├── nb6_pv+w.ipynb
│   │   ├── nb7_noaug_p1.ipynb
│   │   └── nb8_pv.ipynb
│   └── soydisease/
│       ├── soydisease1.ipynb
│       ├── soydisease2.ipynb
│       ├── soydisease3.ipynb
│       ├── soydisease4.ipynb
│       ├── soydisease5.ipynb
│       └── soydisease6.ipynb
└── evidence/
    └── DATA_SOURCES.md
```

## Primary experiments

The original paper naming is retained: NB1 Wheat Hybrid, NB2 Cotton Hybrid, and NB3 PlantVillage Hybrid. Repository metrics currently verify 97.8102%, 53.5466%, and 97.6744% accuracy respectively.

A critical audit finding is recorded for NB1: the stored classification report has zero test support for `Wheat_Healthy`. This means the reported overall accuracy should not be interpreted as balanced three-class performance until the split is reconciled.

## Architecture comparison

The paper distinguishes architectural ablation from dataset variation. NB4 and NB5 are verified combined-dataset baselines: Standard Inception and ResNet-style addition. NB6 and NB7 remain part of the original experimental design and are preserved, but their numerical results are not invented where an exported metrics file is absent.

## Augmentation study

Augmentation is a dedicated results section, not merely a bullet in preprocessing. The study should report the exact transformations, sample-count changes, representative examples, learning curves, class-wise metrics where available, and the measured change against the corresponding non-augmented setting.

The potato augmentation notebook is intentionally not included because it belongs to the reference methodology used to design the reporting style.

## SoyDisease

The manuscript uses the India soyabean disease dataset published by Kotwal, Kashyap, and Pathan (2024). The original Mendeley dataset contains 3363 images across six categories. The project evidence records a processed 1176-image subset: Healthy 288, Vein Necrosis 138, Dry Leaf 230, Septoria Brown Spot 284, Root Images 10, and Bacterial Leaf Blight 226.

Source: https://data.mendeley.com/datasets/bshkvgbzpt/1

## Current result status

See `paper/results.csv`. It deliberately separates repository-verified values from earlier draft-reported values. This prevents the manuscript from being made artificially consistent by copying an attractive number into multiple tables.
