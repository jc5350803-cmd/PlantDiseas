# Paper Experiment Manifest

This manifest defines the evidence set for the manuscript. It is intentionally conservative: notebook names are not sufficient evidence; recorded execution and result artifacts are required.

## 1. Primary dataset experiments

| Paper role | Repository source | Status | Evidence used |
|---|---|---|---|
| Wheat primary experiment | `Notebooks/Notebooks_initial_no aug/NB1_wheat-disease-hybrid-architecture.ipynb` | Retain | Executed notebook; 3-class Wheat experiment |
| Cotton primary experiment | `Notebooks/Notebooks_initial_no aug/NB2_cotton-disease-hybrid-architecture.ipynb` | Retain | Executed notebook; dataset-specific hybrid experiment |
| PlantVillage primary experiment | `Notebooks/Notebooks_initial_no aug/NB3_plantvillage-hybrid-architecture.ipynb` | Retain | Executed notebook; dataset-specific hybrid experiment |

## 2. Combined and architectural comparison experiments

| Paper role | Repository source | Status |
|---|---|---|
| Standard Inception comparison | `Notebooks/Notebooks_initial_no aug/plant_disease_all_notebooks/NB4_Combined_StandardInception.ipynb` | Manuscript candidate; verify recorded result artifact before reporting numeric value |
| ResNet comparison | `Notebooks/Notebooks_initial_no aug/plant_disease_all_notebooks/NB5_Combined_ResNet.ipynb` | Manuscript candidate; verify recorded result artifact before reporting numeric value |
| Inception(Add) comparison | `Notebooks/Notebooks_initial_no aug/plant_disease_all_notebooks/NB6_Combined_InceptionAdd.ipynb` | Manuscript candidate; verify recorded result artifact before reporting numeric value |
| SkipConnection(Concat) comparison | `Notebooks/Notebooks_initial_no aug/plant_disease_all_notebooks/NB7_Combined_SkipConcat.ipynb` | Manuscript candidate; verify recorded result artifact before reporting numeric value |

The four variants above are retained because they correspond to the original architectural comparison design. A numeric result is not to be copied into the paper unless its executed output/log can be traced.

## 3. Augmentation study

Augmentation is a dedicated results study, not merely a preprocessing paragraph. The augmentation notebooks in `Notebooks/Aug/` are to be mapped to their actual strategy from their markdown/configuration and recorded outputs. The manuscript must distinguish:

1. preprocessing common to all experiments;
2. controlled augmentation strategies;
3. the resulting performance differences;
4. qualitative augmentation examples where available.

The potato augmentation example notebook is not part of the paper evidence set; it is a reference for presentation style only.

## 4. Soybean material

`NB_SoyCultivar200_Proposed1.ipynb` is explicitly excluded from the paper evidence set. No results from that notebook are to be reported.

Other soybean experiments are not automatically included merely because they contain the word `soy`. They must first be demonstrated to belong to the manuscript's intended soybean study and to contain recorded, complete outputs.

## 5. Excluded experiment classes

Do not promote exploratory architecture variants, incomplete notebooks, unexecuted notebook copies, dummy notebooks, or unrelated demonstrations into the manuscript.

In particular, the following are not paper evidence unless separately verified:

- notebooks with no executed output;
- duplicate copies of an experiment;
- incomplete exploratory architectures;
- notebooks created only for visualization/prototyping;
- the Potato augmentation demonstration used only as a reference for reporting style;
- `NB_SoyCultivar200_Proposed1.ipynb`.

## 6. Numerical reporting rule

The final results CSV and LaTeX tables must be generated from the experiment's recorded metrics artifacts. Values from an old draft, a summary paragraph, or an assumed benchmark must not override a directly recorded experiment result.

Where two historical artifacts disagree, the manuscript should flag the discrepancy and use the value traceable to the selected executed run rather than silently choosing the more favorable number.
