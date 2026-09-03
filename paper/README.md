# PlantDiseaseNet-Hybrid — Paper Workspace

This directory is a paper-oriented view of the project. It preserves the original repository and does not delete or overwrite the existing notebooks.

## Scope retained for the manuscript

- Dataset-specific Hybrid runs: Wheat, Cotton, PlantVillage.
- Combined-dataset comparison runs: Standard Inception and ResNet-style baselines, with the Inception(Add)-only and SkipConnection(Concat)-only variants retained only where their executed outputs can be verified.
- Soybean work is retained separately because it belongs to the current manuscript scope.
- Architecture figures and preprocessing figures are collected under `paper_figures/`.
- Experiment outputs are collected under `results/`.

## Important audit rule

Notebook files are **not executed as part of this organization**. Existing notebook outputs and saved CSV/PNG artifacts are treated as the evidence source. Where the repository does not contain a verifiable output for a claimed result, the value is not invented.

## Figure paths for LaTeX

The manuscript can use:

```latex
\\graphicspath{{paper_figures/}}
```

and then reference files by filename, for example:

```latex
\\includegraphics[width=0.95\\textwidth]{overall_architecture.png}
```

## Organization

- `core_experiments/` — dataset-specific Hybrid notebooks.
- `comparison_experiments/` — architecture comparison/ablation notebooks.
- `soybean/` — soybean notebook and supporting material.
- `paper_figures/` — manuscript-ready architecture and preprocessing figures.
- `results/` — verified experiment summaries and the experiment manifest.
- `supporting_literature/` — papers already present in the repository that support dataset/background discussion.

The original project files remain in their existing locations so that this organization is reversible and auditable.
