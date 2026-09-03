# 05 — Architecture Ablation and Comparison

Paper section: architectural comparison/ablation.

## Original variants
- `NB4_Combined_StandardInception.ipynb` — Standard Inception.
- `NB5_Combined_ResNet.ipynb` — ResNet-style residual fusion.
- `NB6_Combined_InceptionAdd.ipynb` — Inception(Add).
- `NB7_Combined_SkipConcat.ipynb` — SkipConnection(Concat).

Original notebook locations:
`Notebooks/Notebooks_initial_no aug/plant_disease_all_notebooks/`

Only NB4 and NB5 currently have directly verified metric CSVs in the inspected repository logs. NB6 and NB7 remain in the evidence inventory but should not receive numerical claims until their executed outputs/results are located and verified.

Changing crop datasets is not itself an ablation. The architectural comparison is the correct location for ablation language because the model component/fusion strategy is the experimental variable.
