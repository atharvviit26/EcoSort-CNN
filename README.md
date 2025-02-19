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

![474041be-dcbb-400b-baf2-1c15da4eed22](https://github.com/user-attachments/assets/443f7109-d4e2-4e36-ab12-0d6a6c2f0402)



## Features

- Data augmentation with `ImageDataGenerator` (rotation, zoom, flipping, and normalization).
- Batch normalization and dropout layers to prevent overfitting.
- Early stopping and model checkpointing for efficient training.
- Visualization of accuracy, loss, and prediction results.
- Classification report and confusion matrix to assess performance per class.

![cd779e25-1ea3-4a56-bde6-1b824601e0df](https://github.com/user-attachments/assets/9ae0cb8c-a4fe-426e-bf02-d78a79466742)


## Model Architecture

The CNN model includes:
- **Conv2D layers:** For feature extraction.
- **MaxPooling2D:** For dimensionality reduction.
- **BatchNormalization:** For stable training.
- **Flatten and Dense layers:** To learn complex patterns.
- **Dropout (50%):** To reduce overfitting.

![download](https://github.com/user-attachments/assets/b724fc93-7698-4f05-94c5-85f410df2e1d)  


## Performance

- Achieved ~82% training accuracy and ~86% validation accuracy after 50 epochs.
- Reduced training loss from 0.63 to 0.34 and validation loss from 0.94 to 0.43.

![2a6bf65e-af90-4018-9956-20f6ffb3ec89](https://github.com/user-attachments/assets/e6da9b9d-36eb-4c8a-bd1c-5c939315b9ee)



## Visualization

- Accuracy and loss curves for both training and validation sets.
- Confusion matrix and classification report.

![583fdb4b-2165-4eca-92e2-6bb69128fa67](https://github.com/user-attachments/assets/cd167e84-eb80-4990-ae71-54b88f11970e)


## Key Findings

- Model achieved promising accuracy and generalization with early stopping and dropout layers.
- Variations in training times observed based on batch size and hardware efficiency.

![eec00dc9-6aaa-4f54-a8a1-e5c355849ca1](https://github.com/user-attachments/assets/bacafea2-5367-40e7-ba88-f6e65349894e)

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

