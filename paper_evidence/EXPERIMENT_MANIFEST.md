# PlantDiseaseNet-Hybrid — Paper Evidence Manifest

This branch is a paper-evidence branch. It does not execute notebooks. Notebook execution status and numerical claims are judged from the recorded notebook outputs and committed result artifacts.

## Paper scope

The manuscript retains the original study structure: primary crop experiments, the combined multi-crop experiment, architectural comparisons, a dedicated augmentation study, and the SoyDisease study. `NB_SoyCultivar200_Proposed1.ipynb` is excluded.

## Primary experiments

| Paper role | Notebook | Verified result artifact | Status |
|---|---|---|---|
| Wheat primary | `Notebooks/Notebooks_initial_no aug/NB1_wheat-disease-hybrid-architecture.ipynb` | `Notebooks/Notebooks_initial_no aug/logs/NB1_logs/metrics_summary.csv` | Verified |
| Cotton primary | `Notebooks/Notebooks_initial_no aug/NB2_cotton-disease-hybrid-architecture.ipynb` | `Notebooks/Notebooks_initial_no aug/logs/NB2_logs/metrics_summary.csv` | Verified |
| PlantVillage primary | `Notebooks/Notebooks_initial_no aug/NB3_plantvillage-hybrid-architecture.ipynb` | `Notebooks/Notebooks_initial_no aug/logs/NB3_logs/metrics_summary.csv` | Verified |

## Architecture comparison

The original comparison design contains Standard Inception, ResNet-style residual fusion, Inception with Add fusion, and SkipConnection with Concat fusion. The repository contains the four named notebooks. Only experiments with recorded, executed outputs should receive numerical claims in the manuscript.

The currently verified log artifacts include:

- `NB4_Combined_StandardInception`: verified.
- `NB5_Combined_ResNet`: verified.
- `NB6_Combined_InceptionAdd`: notebook exists, but its recorded execution cells are not complete in the current main-branch copy; do not report a numeric result until a completed output artifact is identified.
- `NB7_Combined_SkipConcat`: notebook exists, but its recorded execution/result artifact must be verified before numerical reporting.

## Augmentation study

Augmentation is a separate experimental section in the paper. The notebooks under `Notebooks/Aug/` are treated as candidate augmentation experiments, not automatically as evidence. The Potato augmentation notebook is excluded from the paper's experimental evidence; it is retained only as a reference for how an augmentation study can be presented.

For the paper, the augmentation study should report, for each retained executed experiment:

1. the baseline condition;
2. the augmentation operations actually used;
3. class-count changes before and after augmentation;
4. performance changes on the same held-out test protocol;
5. training/convergence behaviour;
6. class-wise effects where recorded.

The reporting style is informed by Mhala et al. (2025), but the experiments and numbers in this paper must remain those of PlantDiseaseNet-Hybrid.

## SoyDisease

The intended soybean crop study is the `SoyDisease` material under `Notebooks/soydisease/`. The dataset recorded in the executed notebooks contains 1,176 images across six classes: Soybean Healthy (288), Soybean Vein Necrosis (138), Soybean Dry Leaf (230), Soybean Septoria Brown Spot (284), Soybean Root (10), and Soybean Bacterial Leaf Blight (226).

`soydisease1.ipynb` records the no-augmentation baseline configuration. The later improved notebook describes strategic per-class augmentation together with L2 regularisation and early stopping, but its current recorded execution includes an error during the data-download/extraction stage. Therefore, its numerical final performance must not be copied into the manuscript unless another complete executed SoyDisease augmentation result is identified.

`NB_SoyCultivar200_Proposed1.ipynb` is explicitly excluded.

## Important numerical discrepancy

The earlier manuscript draft quoted 99.12% accuracy and approximately 933K parameters. The currently committed primary log artifacts do **not** support those numbers: NB1 records 97.8102% accuracy with 59,775,267 parameters; NB2 records 53.5466% accuracy with 59,775,462 parameters; NB3 records 97.6744% accuracy with 59,776,047 parameters. These discrepancies must be resolved from the correct executed run before those older draft numbers are restored.

Likewise, the supplied Keras architecture summary for the later 24-class PlantDiseaseNet-Hybrid definition sums to 934,200 total parameters, not 933,426. This should be reported only if that exact architecture is the one used for the manuscript's final experiments.

## Rule

No favorable value is selected merely because it appears in an older draft. Every numerical table in the final manuscript must trace to a specific executed notebook/result artifact.
