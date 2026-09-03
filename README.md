# PlantDiseaseNet-Hybrid

Research repository for the manuscript **A Hybrid Deep Learning Framework for Multi-Crop Plant Disease Classification Using Strategic Data Augmentation**.

## Repository policy

This branch is organized around the experiments and evidence used in the paper. Notebook names alone are not treated as evidence: a notebook is retained for the manuscript only when its executed cells and recorded outputs support the corresponding experiment.

The repository is deliberately separated into primary experiments, augmentation studies, architectural ablations, results, figures, and manuscript material so that every reported table or figure can be traced to its source experiment.

## Paper experiment structure

```text
PlantDiseaseNet-Hybrid/
├── 01_Dataset_Description/
├── 02_Data_Preprocessing_and_Augmentation/
├── 03_Proposed_Methodology/
│   ├── Inception_Add/
│   └── SkipConnection_Concat/
├── 04_Experimental_Results/
│   ├── Primary_Dataset_Experiments/
│   ├── Combined_Dataset/
│   ├── Augmentation_Study/
│   └── Architectural_Ablation/
├── 05_Results_and_Analysis/
│   ├── metrics/
│   ├── confusion_matrices/
│   ├── roc_pr_curves/
│   ├── training_curves/
│   └── feature_visualizations/
├── 06_Manuscript/
├── 07_References_and_Data_Sources/
└── README.md
```

## Primary experiments retained

The primary dataset-specific experiments correspond to the executed Wheat, Cotton, and PlantVillage hybrid notebooks. The combined experiment and the architecture-comparison experiments are retained only where their recorded outputs are available and consistent with the manuscript.

## Architectural study

The original experimental comparison is preserved: Standard Inception, ResNet-style residual fusion, Inception with addition fusion, and SkipConnection with concatenation are treated as architectural comparison/ablation variants. No unrelated exploratory architecture is promoted into the paper merely because it exists in the repository.

## Augmentation study

Augmentation is reported as a dedicated experimental study rather than being buried inside preprocessing. The paper distinguishes ordinary preprocessing from controlled augmentation experiments and links augmentation claims to the corresponding executed notebooks and result files.

## Excluded material

`NB_SoyCultivar200_Proposed1.ipynb` is intentionally excluded from the manuscript organization and must not be used as evidence for reported results.

Dummy, incomplete, or unexecuted notebook copies are not treated as experimental evidence. The repository may retain historical material elsewhere when needed for provenance, but it is not part of the paper's evidence set.

## Reproducibility rule

Reported numerical values in the manuscript must be copied from the recorded result artifacts (metrics CSVs, classification reports, training histories, ROC/AUC files, and generated figures) rather than reconstructed from notebook names or assumed benchmark values.

## Important note

Some historical project files contain different experimental settings or draft metrics. These are not silently reconciled. The final manuscript should use only values that can be traced to the selected executed experiment and its result artifacts.
