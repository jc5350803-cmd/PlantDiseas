# PlantDiseaseNet-Hybrid — Paper-Aligned Research Branch

This branch is the **paper-aligned research record** for PlantDiseaseNet-Hybrid. The original `main` branch is not modified by this organisation pass. This branch keeps the notebooks, figures, and result tables that are actually used by the manuscript and groups them by the corresponding paper section.

## Evidence policy

- Notebooks were **not executed** during this organisation/audit pass.
- Saved notebook outputs, exported CSV files, and the manuscript's existing experiment record are treated as the evidence base.
- Numerical values are reported only when they can be traced to saved experiment output or the consolidated result record.
- A failed final cell does not invalidate earlier saved outputs; however, a notebook with no usable executed result is not promoted into the paper's evidence set.
- `SoyCultivar200` is excluded. **SoyDisease / Indian soybean** is included.
- The potato augmentation notebook is **not** part of the evidence set. It is used only as a literature/reporting example for how a dedicated augmentation study can be presented.

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

The directory names mirror the manuscript's experimental sections: **Primary Dataset-Specific Experiments**, **Augmentation Study**, **Architectural Ablation**, and **SoyDisease Evaluation**.

## Experimental record used by the paper

### Primary dataset-specific experiments

| Experiment | Dataset | Classes | Accuracy | Precision | Recall | F1 | Specificity |
|---|---|---:|---:|---:|---:|---:|---:|
| NB1 Wheat Hybrid | Wheat | 3 | 97.81% | 97.82% | 97.81% | 97.81% | 98.54% |
| NB2 Cotton Hybrid | Cotton | 6 | 53.55% | 53.01% | 53.55% | 51.66% | 90.71% |
| NB3 PlantVillage Hybrid | PlantVillage subset | 15 | 97.67% | 97.68% | 97.67% | 97.68% | 99.83% |

The Wheat run has zero stored test support for the Wheat Healthy class. Its aggregate metrics are retained for traceability, but they should not be interpreted as complete three-class evidence.

### 24-class combined benchmark

The recorded complete PlantDiseaseNet-Hybrid benchmark reports **95.91% accuracy**, **95.98% precision**, **95.91% recall**, **95.91% F1-score**, **99.82% specificity**, **0.9996 micro-AUC**, and **0.9990 macro-AUC**, with **934,200 total parameters** in that saved configuration.

### Dedicated augmentation study

The augmentation study holds the architecture and 24-class benchmark fixed and varies the training augmentation policy. The recorded accuracy values are:

- Hybrid-NoAug: 96.03%
- Hybrid-CropColour: 96.31%
- Hybrid-LightAug: **97.06%**
- Hybrid-LightAug-v2: 96.43%
- Hybrid-FullAug: 95.91%

The 97.06% value is therefore reported as the **best recorded augmentation-policy run**, not as evidence that every augmentation strategy improves performance.

### Architectural ablation

The controlled ablation compares configurations on the same 24-class benchmark and LightAug condition:

| Configuration | Accuracy | F1 | Specificity | Parameters |
|---|---:|---:|---:|---:|
| Standard Inception + GAP | 95.33% | 95.32% | 99.80% | 270,656 |
| Residual CNN + GAP | **96.04%** | 96.02% | 99.83% | 741,720 |
| Inception(Add)-only + GAP | 95.84% | 95.82% | 99.82% | 949,112 |
| SkipConcat-only + GAP | 95.67% | 95.67% | 99.81% | 1,139,640 |
| PlantDiseaseNet-Hybrid | 95.91% | **95.91%** | 99.82% | **934,200** |

The residual baseline is slightly more accurate. Accordingly, the manuscript does **not** claim universal accuracy superiority; it discusses the proposed design as a hybrid trade-off between multi-scale fusion, feature reuse, and model capacity.

### SoyDisease evaluation

The soybean experiments use the published **An India soyabean dataset**. The source dataset contains 3363 images in six disease/condition categories. The project notebooks use a processed 1176-image subset with the following class counts: Healthy 288, Septoria Brown Spot 284, Dry Leaf 230, Bacterial Leaf Blight 226, Vein Necrosis 138, and Root Images 10.

Two single-split runs report 100% accuracy, but the Root Images class has extremely small support, so those runs are treated as **unstable exploratory results**, not as the principal soybean claim. The principal generalisation estimate is the recorded five-fold result of **99.57% ± 0.85% mean accuracy**.

## Dataset provenance

The manuscript uses scholarly/original data records rather than citing Kaggle as the primary source:

- **PlantVillage:** Mohanty, Hughes and Salathé (2016), *Frontiers in Plant Science*, DOI `10.3389/fpls.2016.01419`; public dataset repository: `spMohanty/PlantVillage-Dataset`.
- **Wheat:** Fang, Zhen and Li (2023), *Applied Sciences*, 13(9), 5801, DOI `10.3390/app13095801`.
- **Cotton:** Bishshash et al. (2024), *Data in Brief*, DOI `10.1016/j.dib.2024.110913`.
- **Indian soybean:** Kotwal, Kashyap and Pathan (2024), *Data in Brief*, 53, 110216, DOI `10.1016/j.dib.2024.110216`; original Mendeley Data DOI `10.17632/bshkvgbzpt.1`.

## Figures and LaTeX

All manuscript figures are kept under `paper_figures/`. The LaTeX source references that directory explicitly. Wide architecture/pipeline figures should use `width` together with `height` and `keepaspectratio`; block diagrams should be constrained to the text width rather than allowed to float at arbitrary dimensions. This keeps figures from being clipped or pushed partly off the page in the Elsevier CAS two-column layout.

The repository currently contains the four architecture/preprocessing figures. Training curves, confusion matrices, ROC/PR plots, and augmentation examples should be added to `paper_figures/` only after the corresponding saved notebook outputs have been extracted and checked; they should not be invented from summary numbers.

## Scope rule

Do not promote a notebook simply because its filename sounds relevant. A notebook belongs in this branch when it is part of the manuscript's named experimental programme and contains a saved, traceable result. Unexecuted/dummy notebooks remain outside this paper-aligned evidence set.
