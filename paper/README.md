# PlantDiseaseNet-Hybrid — Journal Manuscript

This folder contains the journal-oriented manuscript and the verified result table.

## Main manuscript

`PlantDiseaseNet-Hybrid_CAS.tex` is written for Elsevier CAS double-column (`cas-dc`). It uses the figures in `../paper_figures/` and keeps the original paper title and experiment naming.

## Evidence rule

Numerical claims in the manuscript are restricted to committed executed result artifacts. The final architecture specification and historical experiment logs are kept conceptually separate because the repository contains more than one architectural/configuration generation.

## Verified numerical experiments

- NB1_Wheat_Hybrid
- NB2_Cotton_Hybrid
- NB3_PlantVillage_Hybrid
- NB4_Combined_StandardInception
- NB5_Combined_ResNet

NB6_Combined_InceptionAdd and NB7_Combined_SkipConcat remain in the research inventory but are not assigned numerical values until complete executed result artifacts are recovered.

## Dedicated studies

The manuscript keeps separate sections for:

1. data and preprocessing;
2. PlantDiseaseNet-Hybrid architecture;
3. primary crop experiments;
4. combined architecture comparison;
5. strategic augmentation study; and
6. SoyDisease.

The Potato augmentation notebook is not used as evidence; it is only a methodological/reporting reference to Mhala et al. (2025). SoyCultivar200 is excluded.

## Figures

The manuscript expects:

- `paper_figures/preprocessing_pipeline.png`
- `paper_figures/overall_architecture.png`
- `paper_figures/inception_block.jpg`
- `paper_figures/skip_block.jpg`

The LaTeX uses `\IfFileExists` fallbacks so a missing figure does not cause a cryptic compilation failure. For the submitted version, all four actual figures should be present and checked visually.

## Build

Compile from this directory with a normal Elsevier CAS LaTeX environment. Do not use Markdown links inside author `\ead{}` fields; use plain email addresses.

## Important unresolved issue

The earliest draft contained 99.12% accuracy and approximately 933K parameters. Those values are not supported by the currently verified primary metric artifacts, so they are intentionally absent from the final numerical results. The supplied final Keras summary sums to 934,200 parameters. Resolve the exact final executed run before restoring any older headline value.
