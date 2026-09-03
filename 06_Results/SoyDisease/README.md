# 06 — SoyDisease

SoyDisease is included as a crop-level study. `SoyCultivar200` is excluded.

## Dataset
The executed baseline notebook records 1,176 images across six classes:

- Healthy — 288
- Vein Necrosis — 138
- Dry Leaf — 230
- Septoria Brown Spot — 284
- Root Images — 10
- Bacterial Leaf Blight — 226

Scholarly dataset citation: Kotwal, Kashyap, and Pathan (2024), Data in Brief 53, 110216, DOI 10.1016/j.dib.2024.110216.

## Experiments
- Baseline/no augmentation: `Notebooks/soydisease/soydisease1.ipynb` (executed evidence present).
- Improved augmentation + L2 + early stopping: `Notebooks/soydisease/soydisease4.ipynb` (current copy records a data-extraction error, so its final performance must not be reported without another complete executed artifact).

The SoyDisease section should be reported separately from SoyCultivar200 and should not be used to inflate the 24-class combined experiment unless the exact combined experiment includes it.
