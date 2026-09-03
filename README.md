# PlantDiseaseNet-Hybrid — clean manuscript workspace

This branch contains only the material retained for the current journal manuscript.

## Evidence policy
- No notebook is executed during this cleanup.
- Results are taken from saved repository artifacts (`metrics_summary.csv`, classification reports, training histories, ROC data, and saved figures).
- A result is not promoted into the manuscript merely because it appears in a notebook title or an earlier draft.
- NB6 and NB7 are excluded from the quantitative manuscript results because the repository does not contain a saved result set that can be independently verified for those runs.
- The soybean notebook is excluded from the quantitative results because its saved execution contains a failed data-download/extraction step and no complete validated test result.
- The original notebook files contain credential material and are therefore deliberately not copied into this clean publication branch.

## Verified quantitative experiments retained
1. `NB1_Wheat_Hybrid` — Wheat, 3 declared classes; the saved test report contains support for only Brown Rust and Yellow Rust, with zero support for Wheat Healthy.
2. `NB2_Cotton_Hybrid` — Cotton, 6 classes; complete test support is present.
3. `NB3_PlantVillage_Hybrid` — PlantVillage subset, 15 classes; complete test support is present.
4. `NB4_Combined_StandardInception` — 24 declared classes; the saved test report has zero support for Wheat Healthy, so only 23 classes are represented in the test report.
5. `NB5_Combined_ResNet` — same 24-class declaration and the same missing Wheat Healthy test support.

## Manuscript
- `paper/cas-dc-template.tex` — Elsevier CAS double-column manuscript.
- `paper/references.bib` — verified literature references.
- `paper/paper_figures/` — architecture and preprocessing figures.
- `paper/results/` — retained experimental evidence and consolidated metrics.

## Important interpretation
The repository evidence does **not** support the earlier draft claims of 99.12% accuracy or a 933K-parameter trained model for these saved NB1–NB5 runs. The verified saved outputs report approximately 59.8M parameters for NB1–NB3 and 270K/742K for the two combined baselines. The manuscript therefore uses the saved experimental evidence rather than the earlier draft numbers.

The combined experiments also contain a class-coverage problem (Wheat Healthy has zero test support). These results are retained for transparency and comparison, but the manuscript explicitly avoids treating them as a fully valid 24-class benchmark.

## Figure paths
The LaTeX manuscript uses:

```latex
\\graphicspath{{paper_figures/}{results/figures/}}
```

All manuscript image references therefore resolve relative to `paper/`.
