# Augmentation study protocol

The augmentation study is presented as a controlled training-distribution experiment, not as a preprocessing footnote. The retained combined-dataset runs are:

- No augmentation control: 96.03% accuracy.
- Strong augmentation: 96.31% accuracy, 99.84% specificity, macro AUC 0.9990.
- Light augmentation: 97.06% accuracy, 99.87% specificity, macro AUC 0.9992.

The light policy is therefore the best of the recorded policies, improving over the no-augmentation control by 1.03 percentage points. The stronger policy improves the control by only 0.28 points. The paper should describe this as evidence that augmentation strength must be tuned to the visual semantics of the task, not as evidence that augmentation universally improves performance.

The notebook `potato_Augumentation_L2_Earlystop.ipynb` is intentionally excluded from the paper branch because it was used as a reference/example rather than as one of the manuscript experiments.
