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

## Website Output
![image](https://github.com/user-attachments/assets/3ff6ad37-0d27-439c-8409-3d95a756be97)
![image](https://github.com/user-attachments/assets/100502d7-d7d4-41c2-848d-14a931a3d497)


---

## 🚀 Installation & Setup

### 🔧 Prerequisites

- Python 3.8 or higher  
- `pip` package manager  
- A modern web browser (for running the frontend)  

### 🧠 Model Download

Download the trained CNN model from the link below and save it in the root project directory (where `app.py` is located):

👉 [Download Waste Classification Model (.h5)](https://drive.google.com/file/d/1S-_UoxyPb27F9n4jKAjSRQw2G8Zn0LBH/view?usp=drive_link)

---

### 🖥️ Manual Setup

1. **Clone the repository (or download the required files):**
   - `app.py` (Flask backend)
   - `frontend.html` (Web interface)
   - `.h5` model file (from the above drive link)

2. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

   > If `requirements.txt` is not available, install dependencies manually:
   ```bash
   pip install flask tensorflow pillow
   ```

3. **Start the Flask server:**

   ```bash
   python app.py
   ```

4. **Access the website:**

   Open your browser and visit [http://localhost:5000](http://localhost:5000)

---

### 🐳 Docker Setup (Optional)

If you'd prefer running the project via Docker:

1. **Pull the Docker image:**

   ```bash
   docker pull atharvviit/ecosort:03
   ```

2. **Run the container:**

   ```bash
   docker run -p 5000:5000 atharvviit/ecosort:03
   ```

3. **Access the web app:**

   Open your browser and navigate to [http://localhost:5000](http://localhost:5000)




---

⭐ **Star this repo if you found it helpful!** ⭐

