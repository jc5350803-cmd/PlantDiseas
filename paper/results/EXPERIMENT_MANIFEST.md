# Manuscript experiment manifest

This manifest defines what is retained for the paper workspace. Classification is based on the manuscript scope and repository evidence, not filename alone.

| Artifact | Manuscript role | Evidence/notes |
|---|---|---|
| `Notebooks/Notebooks_initial_no aug/NB1_wheat-disease-hybrid-architecture.ipynb` | Core experiment | Wheat Hybrid notebook. Existing metrics output is retained under its log directory. |
| `Notebooks/Notebooks_initial_no aug/NB2_cotton-disease-hybrid-architecture.ipynb` | Core experiment | Cotton Hybrid notebook. Existing metrics output is retained under its log directory. |
| `Notebooks/Notebooks_initial_no aug/NB3_plantvillage-hybrid-architecture.ipynb` | Core experiment | PlantVillage Hybrid notebook. Existing metrics output is retained under its log directory. |
| `Notebooks/Notebooks_initial_no aug/NB4_combined-dataset-standard-inceptionnet.ipynb` | Architecture comparison | Combined 24-class Standard Inception run. |
| `Notebooks/Notebooks_initial_no aug/NB5_combined-dataset-resnet-style.ipynb` | Architecture comparison | Combined 24-class ResNet-style run. |
| `Notebooks/Notebooks_initial_no aug/NB6_combined-dataset-inception-add.ipynb` | Architecture comparison | Retained as a candidate comparison artifact; numeric result is not copied into the verified CSV until its output is directly located. |
| `Notebooks/Notebooks_initial_no aug/NB7_combined-dataset-skip-concat.ipynb` | Architecture comparison | Retained as a candidate comparison artifact; numeric result is not copied into the verified CSV until its output is directly located. |
| `Notebooks/NB_SoyCultivar200_Proposed1.ipynb` | Soybean experiment | Retained separately for the manuscript; numeric claims require direct inspection of its executed outputs. |
| `docs/overall_architecture.png` | Main architecture figure | Copied into `paper_figures/overall_architecture.png`. |
| `docs/inception_block.jpg` | Inception(Add) figure | Copied into `paper_figures/inception_block.jpg`. |
| `docs/skip_block.jpg` | SkipConnection(Concat) figure | Copied into `paper_figures/skip_block.jpg`. |
| `docs/preprocessing_pipeline.png` | Preprocessing/augmentation figure | Copied into `paper_figures/preprocessing_pipeline.png`. |
| `docs/cnn_graph.png` | Supporting architecture visualization | Copied into `paper_figures/cnn_graph.png`. |
| `Notebooks/Notebooks_initial_no aug/logs/NB1_logs/*` | Wheat results | Existing classification report, confusion matrix, training curves, ROC data/curves, per-class metrics and arrays. |
| `Notebooks/Notebooks_initial_no aug/logs/NB2_logs/*` | Cotton results | Existing classification report, confusion matrix, training curves, ROC data/curves, per-class metrics and arrays. |
| `Notebooks/Notebooks_initial_no aug/logs/NB3_logs/*` | PlantVillage results | Existing classification report, confusion matrix, training curves, ROC data/curves, per-class metrics and arrays. |
| `Notebooks/Notebooks_initial_no aug/logs/NB4_logs/*` | Standard Inception comparison results | Existing comparison outputs. |
| `Notebooks/Notebooks_initial_no aug/logs/NB5_logs/*` | ResNet comparison results | Existing comparison outputs. |

## Explicit exclusions from the paper workspace

Legacy/redundant notebooks, augmentation prototypes not explicitly part of the manuscript, duplicate comparison notebooks, and unrelated supporting documents are not promoted into the paper workspace. They remain in the original repository for traceability.

## Important correction

An earlier executive-summary-style audit contained numerical claims that do not agree with the currently stored `metrics_summary.csv` files. For example, the stored Wheat file reports 0.978102 accuracy and 59,775,267 parameters, while an earlier summary stated 99.12% and about 934k parameters. The repository must follow the actual stored outputs. Therefore the paper workspace deliberately records the verified CSV values and leaves unverified values blank rather than silently adopting the earlier claims.
