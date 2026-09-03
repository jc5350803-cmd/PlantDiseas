# PlantDiseaseNet-Hybrid

Paper-aligned research branch for the manuscript **A Hybrid Deep Learning Framework for Multi-Crop Plant Disease Classification Using Strategic Data Augmentation**.

## Evidence policy

- Notebooks were **not executed** during this audit.
- Saved notebook code, saved outputs, committed metric files, the original draft, the executive summary, and the retained research documents were used as evidence.
- Values are not silently reconciled when sources disagree. The manuscript identifies the source/status of results.
- `SoyCultivar200` is excluded. The included soybean study is **Indian SoyDisease**.
- The potato augmentation notebook is excluded from the paper experiments; Mhala et al. is used only as a reporting precedent for separating augmentation analysis from preprocessing.

## Paper-aligned repository

```text
paper-organized-final/
├── README.md
├── evidence/
│   └── DATA_SOURCES.md
├── experiments/
│   ├── primary/
│   │   ├── NB1_Wheat_Hybrid.ipynb
│   │   ├── NB2_Cotton_Hybrid.ipynb
│   │   └── NB3_PlantVillage_Hybrid.ipynb
│   ├── final_model/
│   │   └── PlantDiseaseNet-Hybrid_Combined.ipynb
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
├── paper/
│   ├── cas-dc-template.tex
│   ├── references.bib
│   └── results.csv
└── paper_figures/
    ├── preprocessing_pipeline.png
    ├── overall_architecture.png
    ├── inception_block.jpg
    └── skip_block.jpg
```

The augmentation filenames are preserved because the repository evidence does not establish a trustworthy one-to-one filename-to-policy mapping. They are therefore documented by role rather than renamed speculatively.

## Experimental families

### Primary crop experiments

NB1, NB2 and NB3 retain the original paper naming: Wheat Hybrid, Cotton Hybrid and PlantVillage Hybrid. These are **dataset-specific evaluations**, not architectural ablations.

Repository metric files report:

| Experiment | Classes | Accuracy | Precision | Recall | F1 | Specificity | Parameters |
|---|---:|---:|---:|---:|---:|---:|---:|
| NB1 Wheat Hybrid | 3 | 97.8102% | 97.8202% | 97.8102% | 97.8100% | 98.5365% | 59.78 M |
| NB2 Cotton Hybrid | 6 | 53.5466% | 53.0072% | 53.5466% | 51.6565% | 90.7079% | 59.78 M |
| NB3 PlantVillage Hybrid | 15 | 97.6744% | 97.6824% | 97.6744% | 97.6761% | 99.8332% | 59.78 M |

NB1 has a documented class-support problem in the stored test report: `Wheat_Healthy` has zero test support. The value is retained for provenance but should not be used as strong evidence of three-class generalisation.

### Final combined hybrid

The final complete hybrid is the architecture used for the main 24-class discussion. Its saved model evidence gives **934,200 total parameters**, comprising **933,720 trainable** and **480 non-trainable** parameters. The recorded complete-hybrid run reports 95.91% accuracy, 95.98% weighted precision, 95.91% weighted recall, 95.91% weighted F1, 99.82% specificity, micro AUC 0.9996 and macro AUC 0.9990.

### Architectural ablation

NB4--NB7 are controlled architecture comparisons on the 24-class combined benchmark. The term *ablation* is reserved for these structural comparisons; changing datasets is not called an ablation.

| Architecture | Parameters | Accuracy | F1 | Specificity | Train time |
|---|---:|---:|---:|---:|---:|
| Standard Inception + GAP | 270,656 | 95.33% | 95.32% | 99.80% | 59.1 min |
| Residual CNN + GAP | 741,720 | **96.04%** | 96.02% | 99.83% | **27.9 min** |
| Inception(Add)-only + GAP | 949,112 | 95.84% | 95.82% | 99.82% | 82.0 min |
| SkipConcat-only + GAP | 1,139,640 | 95.67% | 95.67% | 99.81% | 63.9 min |
| PlantDiseaseNet-Hybrid | **934,200** | 95.91% | 95.91% | 99.82% | 93.3 min |

This comparison does **not** show the proposed hybrid as the highest-accuracy architecture. ResNet is 0.13 percentage points higher. The paper therefore claims a specific fusion design and parameter-compactness trade-off, not universal architectural superiority.

### Strategic augmentation

Augmentation is a separate experimental section. The recorded 24-class sensitivity study contains five configurations:

- Hybrid-NoAug: no additional augmentation.
- Hybrid-LightAug: flip + brightness.
- Hybrid-LightAug-v2: independent repeat of LightAug.
- Hybrid-CropColour: crop + colour transformations.
- Hybrid-FullAug: broad recorded transform set.

Recorded results are 96.03%, 97.06%, 96.43%, 96.31% and 95.91%, respectively. The 97.06% result is the best recorded augmentation-policy result. The independent LightAug repeat at 96.43% demonstrates run-to-run variation. These values are marked in `paper/results.csv` with their evidence status because the augmentation notebooks are large and their exported metric artifacts are not all present as small committed CSV files.

### Indian SoyDisease

The published source dataset contains 3363 images across six categories. The project uses a documented 1176-image processed subset:

- Healthy: 288
- Vein Necrosis: 138
- Dry Leaf: 230
- Septoria Brown Spot: 284
- Root Images: 10
- Bacterial Leaf Blight: 226

Four recorded configurations are reported. EXP-1 and EXP-2 produce 100% single-split accuracy but are treated as statistically fragile because the Root class has only ten original images. EXP-3 records 85.88%. EXP-4 records 99.44% on the held-out evaluation and **99.57% ± 0.85%** across five-fold validation. The five-fold estimate is the preferred generalisation result.

## Dataset provenance

The paper cites the scientific/publication source for PlantVillage, the original wheat dataset paper/preprint and dataset record, the cotton dataset record and peer-reviewed papers documenting its use, and the published India SoyDisease dataset. Kaggle is not used as the sole scientific citation for PlantVillage or SoyDisease.

See `evidence/DATA_SOURCES.md` and `paper/references.bib`.

## Reproducibility note

The repository contains executed notebooks with their saved outputs. They are retained as research records and are **not executed automatically**. Raw datasets and credentials are not part of the paper branch. Any API key previously present in an original notebook must be revoked/rotated before public release; credentials must never be committed.
