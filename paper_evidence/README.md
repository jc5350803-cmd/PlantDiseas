# Paper Evidence

This directory records the evidence set used to build the PlantDiseaseNet-Hybrid manuscript.

## Scope

The paper keeps the original experimental naming and study logic:

- **Primary dataset experiments:** Wheat, Cotton, and PlantVillage.
- **Combined dataset:** 24-class multi-crop experiment.
- **Architecture comparison:** Standard Inception, ResNet-style, Inception(Add), and SkipConnection(Concat), only when complete executed evidence is available.
- **Augmentation study:** reported as a dedicated results section, separate from routine preprocessing.
- **SoyDisease:** included as the soybean crop study; SoyCultivar200 is excluded.

## Verified numerical evidence

`verified_results.csv` contains values copied from the committed `metrics_summary.csv` artifacts for NB1--NB5. These are the values currently supported by the repository evidence.

The older manuscript figures of 99.12% accuracy and approximately 933K parameters are not currently traceable to these primary logs. They should not be reintroduced without identifying the exact executed run that produced them.

## Notebook policy

Notebooks are not executed by this branch-building workflow. Existing execution counts, recorded outputs, logs, figures, and result files are inspected. A notebook with no meaningful recorded output is not promoted as evidence.

## Augmentation presentation

The structure of the augmentation analysis follows the scientific reporting principle illustrated by Mhala, Bilandani, and Sharma (2025): baseline condition → controlled augmentation/regularisation condition → class-balance effect → performance comparison → convergence/robustness interpretation. Their potato study is a methodological presentation reference only; it is not a source of results for this paper.
