# PlantDiseaseNet-Hybrid — paper-organized research branch

This branch is a clean paper-facing organization of the experiments that are relevant to the manuscript. The existing `main` branch is not modified.

## Structure

- `01_Dataset_and_Preprocessing/` — preprocessing and augmentation figures.
- `02_Proposed_Architecture/` — overall architecture and block diagrams.
- `03_Primary_Experiments/` — Wheat, Cotton, and PlantVillage hybrid experiments plus saved result artifacts.
- `04_Augmentation_Study/` — controlled combined-dataset augmentation experiments. The potato augmentation reference notebook is excluded.
- `05_Architecture_Study/` — Standard Inception, ResNet-style residual, Inception(Add), and SkipConnection(Concat) studies.
- `06_Combined_Hybrid/` — complete hybrid architecture without augmentation.
- `07_Soybean_Study/` — soybean baseline and soybean-augmentation experiments retained as a separate study.
- `08_Results_and_Manuscript/` — consolidated results CSV, CAS manuscript, and bibliography.

## Evidence policy

Numerical claims in the manuscript are based on saved result files or outputs from executed notebooks. Unexecuted/dummy copies are not used as numerical evidence. The repository contains several historical duplicates; this branch intentionally keeps the paper-facing subset only.

The verified combined augmentation progression is 96.03% without augmentation, 96.31% with the stronger policy, and 97.06% with the lighter policy. The complete hybrid architecture without augmentation records 95.91% accuracy and 934,200 parameters. The crop-wise primary runs record 97.81% on Wheat, 53.55% on Cotton, and 97.67% on PlantVillage.

## Security

The source repository contains notebook history with credential-bearing cells. Do not publish API keys or credentials. Before making this branch public, sanitize/rotate any exposed credentials. This organization does not add new credentials.
