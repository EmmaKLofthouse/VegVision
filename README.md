# VegVision

VegVision is a repository dedicated to identifying different vegetables using neural networks. This project utilizes deep learning techniques to classify various types of vegetables from images.

# Dataset

The dataset used in this project is collected from Google Images, consisting of images of various vegetables. Currently, the model is trained on 8 classes: bell peppers, carrots, mushrooms, peas, broccoli, tomatoes, onion, and lettuce. More classes will be added soon to enhance the model's versatility and applicability.

## Scripts

**sort_raw_files.py**: This Python script is used to sort and clean raw images collected from Google Images. It helps organize and preprocess the dataset before feeding it into the neural network models.
    
## Notebooks

**basic_CNN.ipynb**: This notebook demonstrates the development of a neural network from scratch for vegetable classification. It covers data loading, model construction, training, and evaluation.

**transfer_inception.ipynb**: This notebook showcases the use of transfer learning with the InceptionV3 model for vegetable classification. Transfer learning allows leveraging pre-trained models to achieve better performance with less training data.

**VegVision.ipynb**: Tutorial on how to use the trained models to classify your own images.

# Example

Below are example results showing images of vegetables along with their true and predicted categories:

![Untitled](https://github.com/EmmaKLofthouse/VegVision/assets/18194748/525f986a-4a4c-497c-813a-ee6d32bd3b4b)

# Usage

To utilize the code in this repository, follow these steps:

Clone the repository:

    git clone https://github.com/EmmaKLofthouse/VegVision.git

Explore the notebooks and scripts to understand the training and implementation of the neural networks or use the trained models to predict your own images. 

# Contributing

Contributions to VegVision are welcome! If you have any ideas, bug fixes, or enhancements, feel free to open an issue or submit a pull request.
