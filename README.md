# PlantDiseaseNet-Hybrid — Paper-Aligned Research Branch

This branch is the clean, paper-aligned research record for **PlantDiseaseNet-Hybrid**. The original `main` branch is left untouched. This branch keeps the notebooks and outputs that correspond to the manuscript's experimental programme and separates primary evaluation, architectural ablation, augmentation sensitivity, and SoyDisease evaluation.

## Evidence policy

- Notebooks were **not executed** during this organisation/audit pass.
- Saved notebook outputs and exported metrics are treated as the experimental record.
- Numerical values are reported only when they are present in the consolidated experiment record or an exported repository metric file.
- Where a result is known to be unstable or methodologically weak, the manuscript says so instead of replacing it with a more attractive number.
- `Soycultivar200` is excluded. **SoyDisease / Indian soybean** is included.
- The potato augmentation notebook is excluded from the evidence set; it is used only as a reporting reference for the dedicated augmentation section.

## Manuscript-to-repository map

```text
paper-organized-soydisease/
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
│   ├── primary/                 # Results: Primary Dataset-Specific Experiments
│   │   ├── NB1_Wheat_Hybrid.ipynb
│   │   ├── NB2_Cotton_Hybrid.ipynb
│   │   └── NB3_PlantVillage_Hybrid.ipynb
│   ├── architecture_ablation/  # Results: Architectural Ablation
│   │   ├── NB4_Combined_StandardInception.ipynb
│   │   ├── NB5_Combined_ResNet.ipynb
│   │   ├── NB6_Combined_InceptionAdd.ipynb
│   │   └── NB7_Combined_SkipConcat.ipynb
│   ├── augmentation/            # Results: Augmentation Sensitivity Study
│   │   ├── nb2.ipynb
│   │   ├── nb3.ipynb
│   │   ├── nb4.ipynb
│   │   ├── nb5.ipynb
│   │   ├── nb6_pv+w.ipynb
│   │   ├── nb7_noaug_p1.ipynb
│   │   └── nb8_pv.ipynb
│   └── soydisease/               # Results: Soybean Evaluation
│       ├── soydisease1.ipynb
│       ├── soydisease2.ipynb
│       ├── soydisease3.ipynb
│       ├── soydisease4.ipynb
│       ├── soydisease5.ipynb
│       └── soydisease6.ipynb
└── evidence/
    └── DATA_SOURCES.md
```

The folder names under `experiments/` correspond directly to the experimental families in the paper. The manuscript source is in `paper/`, and every figure path used by the LaTeX source points to `paper_figures/`.

## What the paper reports

### 1. Primary dataset-specific experiments

- **NB1 Wheat Hybrid:** 97.81% accuracy, 97.82% precision, 97.81% recall, 97.81% F1, 98.54% specificity.
- **NB2 Cotton Hybrid:** 53.55% accuracy, 53.01% precision, 53.55% recall, 51.66% F1, 90.71% specificity.
- **NB3 PlantVillage Hybrid:** 97.67% accuracy, 97.68% precision, 97.67% recall, 97.68% F1, 99.83% specificity.

NB1 has zero stored test support for the Wheat Healthy class, so its aggregate score is retained for traceability but is not used as proof of complete three-class generalisation.

### 2. 24-class combined benchmark

The complete PlantDiseaseNet-Hybrid records:

- Accuracy: **95.91%**
- Precision: **95.98%**
- Recall: **95.91%**
- F1-score: **95.91%**
- Specificity: **99.82%**
- Micro-AUC: **0.9996**
- Macro-AUC: **0.9990**
- Total parameters: **934,200**

### 3. Augmentation sensitivity

The dedicated augmentation study keeps the architecture and 24-class benchmark fixed while changing the training augmentation policy:

- Hybrid-NoAug: 96.03%
- Hybrid-CropColour: 96.31%
- Hybrid-LightAug: **97.06%**
- Hybrid-LightAug-v2: 96.43%
- Hybrid-FullAug: 95.91%

This is why augmentation is a separate results section rather than a short preprocessing bullet.

### 4. Architectural ablation

The controlled ablation compares five configurations on the same 24-class benchmark and LightAug condition:

| Configuration | Accuracy | F1 | Specificity | Parameters |
|---|---:|---:|---:|---:|
| Standard Inception + GAP | 95.33% | 95.32% | 99.80% | 270,656 |
| Residual CNN + GAP | **96.04%** | 96.02% | 99.83% | 741,720 |
| Inception(Add)-only + GAP | 95.84% | 95.82% | 99.82% | 949,112 |
| SkipConcat-only + GAP | 95.67% | 95.67% | 99.81% | 1,139,640 |
| PlantDiseaseNet-Hybrid | 95.91% | **95.91%** | 99.82% | **934,200** |

The residual baseline is slightly more accurate. The paper therefore makes an accuracy--capacity trade-off argument rather than claiming universal superiority.

### 5. SoyDisease

The soybean experiment uses the published **An India soyabean dataset**. The original source contains 3363 images in six categories. The project notebook uses a processed subset of 1176 images, including only 10 Root Images. Two single-split runs report 100%, but those are explicitly treated as unreliable because of the minority-class support. The principal soybean result is the five-fold configuration:

**99.57% ± 0.85% mean cross-validation accuracy**.

Source dataset: https://data.mendeley.com/datasets/bshkvgbzpt/1

## Dataset provenance

The paper cites the original scholarly/data sources rather than using Kaggle as the primary provenance:

- PlantVillage: Mohanty, Hughes and Salathé (2016), Frontiers in Plant Science, DOI 10.3389/fpls.2016.01419; official dataset repository: https://github.com/spMohanty/PlantVillage-Dataset
- Wheat: Fang, Zhen and Li (2023), Applied Sciences 13, 5801, DOI 10.3390/app13095801.
- Cotton: Bishshash et al. (2024), Data in Brief 57, 110913, DOI 10.1016/j.dib.2024.110913.
- Indian soybean: Kotwal, Kashyap and Pathan (2024), Data in Brief 53, 110216, DOI 10.1016/j.dib.2024.110216; original Mendeley record: https://data.mendeley.com/datasets/bshkvgbzpt/1

## Figures

The LaTeX manuscript uses only `paper_figures/` paths. Wide figures are constrained by both width and height with `keepaspectratio`; the two block diagrams use single-column figures. Optional training-curve, confusion-matrix and ROC figures are guarded with `\IfFileExists`, so their absence does not create a compilation failure.

## Important scope rule

Do not add a new notebook to the manuscript merely because its name sounds relevant. It must correspond to an experiment actually described in the paper and contain a saved output/result that can be traced to the reported value. Unexecuted/dummy notebooks remain in `main` and are not promoted into this paper-aligned branch.
