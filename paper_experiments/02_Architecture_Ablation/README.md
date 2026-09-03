# Architecture Ablation

Required controlled comparisons:
- Standard Inception
- ResNet comparator
- Inception(Add)
- SkipConnection(Concat)
- Complete PlantDiseaseNet-Hybrid

All comparisons must use the same fixed combined dataset, split, preprocessing and training/evaluation protocol. The classifier head should use the final GAP formulation for the final comparable study. The historical Flatten-to-GAP evolution may be documented as model-development evidence, but it should not be mixed into the final ablation table unless explicitly designated as an experiment in the paper.
