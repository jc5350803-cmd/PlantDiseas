# Experiment evidence audit

## Inclusion rule
A run is retained only when a saved result set exists in the repository and contains an evaluation report/metrics artifact. Notebooks are not executed during this audit.

## Retained runs
- NB1_Wheat_Hybrid: saved classification report, metrics summary, per-class metrics, ROC data, training history, confusion matrix, ROC curve, training curve, and distribution figure.
- NB2_Cotton_Hybrid: same evidence set.
- NB3_PlantVillage_Hybrid: same evidence set.
- NB4_Combined_StandardInception: same evidence set.
- NB5_Combined_ResNet: same evidence set.

## Excluded runs
- NB6_Combined_InceptionAdd: notebook file exists, but no saved result directory with independently verifiable metrics was found in the repository.
- NB7_Combined_SkipConcat: notebook file exists, but no saved result directory with independently verifiable metrics was found in the repository.
- Soybean notebook: execution is incomplete; the recorded run contains a `BadZipFile` failure during data acquisition/extraction and does not provide a complete validated test result.

## Important findings
1. NB1 declares three wheat classes, but its saved test report has zero support for Wheat Healthy. Only Brown Rust and Yellow Rust contribute to the reported test accuracy.
2. NB4 and NB5 declare 24 classes, but their saved test reports also have zero support for Wheat Healthy. Their test reports therefore cover 23 classes.
3. NB2 has complete support for all six declared cotton classes, but performance varies substantially by class.
4. NB3 has complete support for all 15 declared PlantVillage-subset classes and is the strongest complete-coverage experiment in the retained set.
5. The saved metrics report approximately 59.8M parameters for NB1--NB3. Earlier manuscript drafts quoted approximately 933K parameters; that number is not used here.
6. Earlier draft headline accuracies of 99.12% and 97.06% are not present in the retained NB1--NB5 evidence and are not used here.

## Metric policy
The consolidated CSV contains both macro and weighted metrics. Weighted metrics reproduce the aggregate values in the saved `metrics_summary.csv` files, while macro metrics are taken from the saved classification reports. The manuscript emphasizes macro scores when discussing class balance and always reports class-support limitations.
