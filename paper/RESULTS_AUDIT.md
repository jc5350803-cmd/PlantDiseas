# Results Audit

This file records how numerical claims in the manuscript were selected.

## Authoritative values used in the paper

The consolidated experiment record is the source for the values in `results.csv`. The paper uses:

- NB1 Wheat Hybrid: 97.81% accuracy.
- NB2 Cotton Hybrid: 53.55% accuracy.
- NB3 PlantVillage Hybrid: 97.67% accuracy.
- Standard Inception + GAP: 95.33%.
- Residual CNN + GAP: 96.04%.
- Inception(Add)-only + GAP: 95.84%.
- SkipConcat-only + GAP: 95.67%.
- PlantDiseaseNet-Hybrid: 95.91%.
- Hybrid-NoAug: 96.03%.
- Hybrid-CropColour: 96.31%.
- Hybrid-LightAug: 97.06%.
- Hybrid-LightAug-v2: 96.43%.
- Hybrid-FullAug: 95.91%.
- PlantVillage + Wheat, 18 classes, LightAug: 99.46%.
- PlantVillage + Wheat, 18 classes, NoAug: 99.12%.
- PlantVillage-38: 99.56%.
- Soybean five-fold estimate: 99.57% ± 0.85%.

## Important reconciliation

The early draft contained a 99.12% value in a context that was easy to interpret as the primary Wheat/PlantVillage result. The consolidated record shows that 99.12% belongs to the separate 18-class PlantVillage+wheat NoAug benchmark. It is therefore not used as the headline result for NB1 Wheat Hybrid.

Likewise, the 97.06% value is used for the recorded Hybrid-LightAug augmentation configuration, not as the standalone cotton result.

## Soybean interpretation

Two single-split soybean experiments report 100% accuracy. The experiment record marks these runs unreliable because the processed dataset contains only 10 Root Images. The paper therefore reports the five-fold result, 99.57% ± 0.85%, as the principal soybean generalisation estimate.

## Architecture interpretation

The residual comparator is slightly more accurate than the complete hybrid (96.04% versus 95.91%). The manuscript therefore does not claim universal accuracy superiority. The proposed contribution is an asymmetric dual-mode fusion design and its accuracy--capacity trade-off.

## Scope exclusions

- SoyCultivar200 is excluded.
- The potato augmentation notebook is not an experiment in this paper.
- SE-enhanced variants are not part of the strict NB4--NB7 ablation reported in the first-draft experimental scope.
- Unexecuted/dummy notebooks are not promoted from `main` into this paper-aligned branch.
