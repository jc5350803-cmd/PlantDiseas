# PlantDiseaseNet-Hybrid

Research repository for **A Hybrid Deep Learning Framework for Multi-Crop Plant Disease Classification Using Strategic Data Augmentation**.

## Paper-oriented structure

The `paper-evidence-organized` branch is the evidence-audit branch for the manuscript. It keeps the original research scope while separating routine preprocessing, the proposed methodology, primary crop experiments, augmentation, architectural comparisons, and SoyDisease.

```text
PlantDiseaseNet-Hybrid/
├── 01_Data_and_Preprocessing/
├── 02_Proposed_Methodology/
├── 03_Results/
│   └── Primary_Dataset_Experiments/
├── 04_Results/
│   └── Augmentation_Study/
├── 05_Results/
│   └── Architecture_Ablation/
├── 06_Results/
│   └── SoyDisease/
├── paper_evidence/
│   ├── verified_results.csv
│   ├── EXPERIMENT_MANIFEST.md
│   └── DATA_SOURCES.md
├── paper_figures/        # manuscript figures supplied separately
└── cas-dc-template.tex
```

## Primary experiments

The original primary experiment names are retained:

- NB1 Wheat Hybrid
- NB2 Cotton Hybrid
- NB3 PlantVillage Hybrid

## Architecture comparison

The original comparison inventory is retained:

- NB4 Combined Standard Inception
- NB5 Combined ResNet
- NB6 Combined InceptionAdd
- NB7 Combined SkipConcat

Only experiments with complete recorded evidence receive numerical claims in the manuscript.

## Augmentation

Augmentation is treated as a dedicated experimental study. The Potato augmentation notebook is not a paper experiment; it is a reporting reference inspired by Mhala et al. (2025).

## SoyDisease

SoyDisease is included as a crop. SoyCultivar200 is explicitly excluded. The six-class India soyabean dataset and its publication-level source are documented in `paper_evidence/DATA_SOURCES.md`.

## Evidence policy

The repository contains historical notebooks with inconsistent settings. Do not infer a result from a notebook name. Numerical values in the manuscript must trace to an executed notebook and its committed result artifact. The currently verified metrics are in `paper_evidence/verified_results.csv`.

## Important audit finding

An earlier draft reported 99.12% accuracy and approximately 933K parameters. The currently inspected committed primary metric files report different values and approximately 59.8M parameters for NB1--NB3. The supplied final Keras architecture summary independently sums to 934,200 parameters. These versions are not silently merged; the exact final experimental run must be identified before the older headline values are restored.
