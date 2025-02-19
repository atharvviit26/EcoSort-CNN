# EcoSort-CNN

EcoSort-CNN is a deep learning project designed to classify waste into two categories: **Organic (O)** and **Recyclable (R)**. Built with TensorFlow and Keras, this Convolutional Neural Network (CNN) model aims to promote efficient waste segregation, contributing to sustainable waste management practices.

## Project Overview

EcoSort-CNN focuses on automating waste classification using computer vision. The model processes images of waste and accurately predicts whether an item is organic or recyclable. The end-to-end pipeline includes:
- Dataset loading and preprocessing.
- Data augmentation for better generalization.
- Model architecture definition and training.
- Performance evaluation on validation and test sets.
- Visualization of model performance and predictions.

## Dataset

- **Training and Validation Data:** Images sorted into two folders: Organic (O) and Recyclable (R).
- **Test Data:** Separate dataset for evaluating model performance on unseen images.

## Features

- Data augmentation with `ImageDataGenerator` (rotation, zoom, flipping, and normalization).
- Batch normalization and dropout layers to prevent overfitting.
- Early stopping and model checkpointing for efficient training.
- Visualization of accuracy, loss, and prediction results.
- Classification report and confusion matrix to assess performance per class.

## Model Architecture

The CNN model includes:
- **Conv2D layers:** For feature extraction.
- **MaxPooling2D:** For dimensionality reduction.
- **BatchNormalization:** For stable training.
- **Flatten and Dense layers:** To learn complex patterns.
- **Dropout (50%):** To reduce overfitting.

## Performance

- Achieved ~82% training accuracy and ~86% validation accuracy after 50 epochs.
- Reduced training loss from 0.63 to 0.34 and validation loss from 0.94 to 0.43.

## Installation

```bash
# Clone the repository
git clone https://github.com/atharvviit26/EcoSort-CNN/


# Navigate to the project folder
cd ecosort-cnn

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. **Verify TensorFlow and GPU availability:**
```python
import tensorflow as tf
print(tf.__version__)
print("GPU Available:", tf.test.is_gpu_available())
```

2. **Train the model:**
```python
python train.py
```

3. **Evaluate the model:**
```python
evaluate_model.py
```

4. **Make predictions:**
```python
predict.py
```

## Visualization

- Accuracy and loss curves for both training and validation sets.
- Confusion matrix and classification report.

## Key Findings

- Model achieved promising accuracy and generalization with early stopping and dropout layers.
- Variations in training times observed based on batch size and hardware efficiency.

## Next Steps

- Fine-tune hyperparameters (learning rate, batch size, and dropout rates).
- Experiment with model architecture (add/reduce layers or neurons).
- Optimize training speed and resource usage.


## Acknowledgements

- TensorFlow and Keras for deep learning.
- OpenCV and Matplotlib for image processing and visualization.
- The dataset providers for enabling this project.

---

⭐ **Star this repo if you found it helpful!** ⭐

