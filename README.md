# PlantDiseaseNet-Hybrid — Organized Research Branch

This branch is the paper-oriented research record for **PlantDiseaseNet-Hybrid**. It is intentionally separate from `main` and keeps only material that is directly relevant to the manuscript structure or to experimental provenance.

## Paper-aligned structure

- `01_Primary_Results/` — NB1 Wheat, NB2 Cotton, NB3 PlantVillage, and the executed combined `original-custom-hybrid` notebook.
- `02_Augmentation_Study/` — the repository's augmentation-study notebooks except the potato augmentation example used as a reference for methodology presentation.
- `03_Architecture_Ablation/` — NB4 Standard Inception, NB5 ResNet-style, NB6 Inception+Add, and NB7 Skip+Concat.
- `04_Soybean_Study/` — soybean notebooks retained as a separate evaluation stream.
- `05_Results_Evidence/` — stored classification reports, metric CSVs, training histories, confusion matrices, ROC curves, and per-class plots from the logged experiments.
- `paper_figures/` — architecture and manuscript figures used by the CAS manuscript.
- `paper/` — Elsevier CAS manuscript source.
- `results/` — verified numerical result register.

## Verified result policy

The manuscript is deliberately conservative. A number is included in the result register only when it can be traced to an executed notebook output or a stored repository result log. Earlier draft values that conflict with the stored experiment evidence are not silently reused.

Current verified headline accuracies are:

| Experiment | Dataset | Accuracy |
|---|---|---:|
| NB1 | Wheat Disease | 97.81% |
| NB2 | Cotton Disease | 53.55% |
| NB3 | PlantVillage | 97.67% |
| Primary combined | Combined multi-crop | 95.91% |
| NB4 | Standard Inception | 95.33% |
| NB5 | ResNet-style | 96.04% |
| NB6 | Inception + Add | 95.84% |
| NB7 | Skip + Concat | 95.67% |

Two soybean notebooks currently expose a 100% final accuracy in their executed outputs; other soybean notebooks are retained for provenance but are not assigned unsupported final metrics.

## Augmentation study

The augmentation notebooks are retained as a separate study because augmentation changes the training distribution and therefore should not be presented as an architectural ablation. The potato augmentation notebook is intentionally excluded from this branch because it is the reference-work example used to guide presentation of an augmentation study, not an experiment belonging to this project.

## Important reproducibility note

Do not execute notebooks merely to regenerate numbers. The paper should use the outputs already recorded in the notebooks/logs unless a new experiment is explicitly planned and documented as a new run.

## Dataset-source policy

For publication, cite the original scholarly/archival source of each dataset where available, rather than citing a Kaggle mirror as the primary scientific source. PlantVillage is cited through Mohanty et al.; the soybean ASDID dataset is cited through Bevers et al. and its Dryad archive.

## Security note

The historical repository contains notebook material associated with external API credentials. Credentials must never be committed to this research branch or to a public repository. Any exposed credential should be revoked/rotated at the provider before publication of the repository.
