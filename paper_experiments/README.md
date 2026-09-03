# PlantDiseaseNet-Hybrid — Paper Experiments

This branch is the paper-oriented organization layer. The original `main` branch is preserved.

## Experiment groups

1. `01_Primary_Evaluation/` — Wheat, Cotton, and the PlantVillage subset used in the paper.
2. `02_Architecture_Ablation/` — Standard Inception, ResNet comparator, Inception(Add), SkipConnection(Concat), and the complete proposed hybrid.
3. `03_Augmentation_Study/` — No augmentation, Light augmentation, and Heavy augmentation on the fixed combined dataset.
4. `04_SoyDisease/` — SoyDisease as a separate crop-level evaluation/augmentation study. SoyCultivar200 is intentionally excluded.
5. `05_Shared/` — uniform result-writing/evaluation helpers and paper tables.

## Re-execution rule

These experiments must be executed from the repository's verified source notebooks. No notebook is to be executed merely to inspect it. Existing executed outputs are evidence; dummy/unexecuted notebooks are not treated as evidence.

## Security

Kaggle credentials must be supplied through Kaggle Secrets or environment variables. API keys/tokens must never be committed to Git. Any credential previously committed to a public repository should be revoked/rotated.

## Result contract

Every final experiment should write one result directory containing: dataset counts, split counts, complete training history, scalar test metrics, per-class metrics, confusion matrix, ROC/AUC data, predictions, model summary, FLOPs/parameter count, inference timing, training time, RAM where measured, and all paper figures. Augmentation experiments additionally write the controlled augmentation examples and comparison figures.
