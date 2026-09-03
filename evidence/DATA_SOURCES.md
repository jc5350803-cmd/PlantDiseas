# Dataset sources used in the manuscript

The manuscript distinguishes **original/public dataset provenance** from later papers that merely reuse or document a dataset. Kaggle pages are not used as the sole scholarly citation.

## PlantVillage

Primary scholarly dataset paper: Hughes, D. P., and Salathé, M., *An open access repository of images on plant health to enable the development of mobile disease diagnostics through machine learning and crowdsourcing* (2015). The peer-reviewed benchmark paper is Mohanty, Hughes and Salathé (2016), *Using deep learning for image-based plant disease detection*, Frontiers in Plant Science 7, 1419, DOI 10.3389/fpls.2016.01419.

Official dataset repository: https://github.com/spMohanty/PlantVillage-Dataset

The present study uses selected PlantVillage classes in the crop-specific and combined experiments; it does not claim that every experiment uses the full PlantVillage collection.

## Wheat Disease Detection Dataset

The three-class wheat experiment uses Brown Rust, Healthy and Yellow Rust. The dataset is attributed in later peer-reviewed work to Safarijalal et al. (2022), whose original study *Automated Wheat Disease Detection using a ROS-based Autonomous Guided UAV* describes the construction of a custom wheat-disease dataset. The dataset is publicly referenced through the Safarijalal Kaggle record, while the scholarly source should be cited for provenance.

Original study: Safarijalal, B., Alborzi, Y., Najafi, E. (2022), *Automated Wheat Disease Detection using a ROS-based Autonomous Guided UAV*, arXiv:2206.15042.

Dataset reference used by later literature: https://www.kaggle.com/sinadunk23/behzad-safari-jalal

A later peer-reviewed study also documents the three-class Brown Rust/Healthy/Yellow Rust configuration and reports 3,679 images (1128 Brown Rust, 1395 Healthy, 1156 Yellow Rust). The manuscript does not assume that this published total equals the exact subset loaded by every project notebook.

## Cotton Plant Disease Dataset

The project cotton experiment uses six classes: Aphids, Army Worm, Bacterial Blight, Healthy, Powdery Mildew and Target Spot. The public dataset is attributed to Dhamodharan and is hosted on Kaggle. A peer-reviewed Frontiers in Plant Science paper explicitly documents use of the same Cotton Plant Disease database and the same six disease/healthy categories.

Peer-reviewed documenting source: Johri, P., Kim, S., Dixit, K., et al. (2024), *Advanced deep transfer learning techniques for efficient detection of cotton plant diseases*, Frontiers in Plant Science, 15, 1441117, DOI 10.3389/fpls.2024.1441117.

Dataset page: https://www.kaggle.com/datasets/dhamur/cotton-plant-disease

This source hierarchy is reported transparently because the public dataset itself is hosted on Kaggle rather than in a journal repository.

## Indian Soybean Disease Dataset

The SoyDisease study uses the published six-class Indian soybean dataset: Healthy, Vein Necrosis, Dry Leaf, Septoria Brown Spot, Root Images and Bacterial Leaf Blight. The original Mendeley record contains 3363 images in seven folders and is licensed under CC BY 4.0.

Original dataset: Kotwal, J., Kashyap, R., Pathan, M. S. (2024), *An India soyabean dataset for identification and classification of diseases using computer-vision algorithms*, Data in Brief, 53, 110216, DOI 10.1016/j.dib.2024.110216.

Mendeley Data: https://data.mendeley.com/datasets/bshkvgbzpt/1

The project notebook uses a processed 1176-image subset with class counts: Healthy 288, Vein Necrosis 138, Dry Leaf 230, Septoria Brown Spot 284, Root Images 10, Bacterial Leaf Blight 226. The paper reports both numbers so that the source dataset is not confused with the experimental subset.

## Augmentation reporting reference

Mhala, P., Bilandani, A., Sharma, S. (2025), *Enhancing crop productivity with fined-tuned deep convolution neural network for Potato leaf disease detection*, Expert Systems with Applications, 267, 126066, DOI 10.1016/j.eswa.2024.126066.

This paper is used only as a methodological/reporting reference for presenting a dedicated augmentation study. Its potato experiment is not included as a PlantDiseaseNet-Hybrid result.
