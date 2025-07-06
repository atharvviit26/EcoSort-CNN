

# 🌿 EcoSort-CNN: Waste Classification using Deep Learning

**EcoSort-CNN** is a deep learning project that classifies waste into two categories: **Organic (O)** and **Recyclable (R)**. The updated version uses **transfer learning and fine-tuning on a pre-trained VGG16 model**, originally trained on ImageNet, to enhance classification accuracy and robustness. This promotes intelligent waste segregation and contributes to sustainable waste management practices.

---

## 🧠 Project Summary

* Designed and trained a CNN-based deep learning model to classify waste as organic or recyclable, leveraging **data augmentation**, **batch normalization**, **early stopping**, and **fine-tuning of a pre-trained VGG16 model (trained on ImageNet)** to enhance accuracy.
* Built a **responsive Flask web app** for real-time image upload and prediction, and **containerized** the system using Docker for seamless deployment across platforms.
* Employed **TensorFlow, Keras, and Python** for model development; **Flask** for web integration; **Docker** for deployment; and **NumPy/SciPy** for efficient data preprocessing in a **Linux-based environment**.

---

## 🗂️ Project Overview

EcoSort-CNN is an end-to-end waste classification pipeline including:

* Dataset loading, labeling, and preprocessing
* Data augmentation for better generalization
* Fine-tuning with a pre-trained **VGG16** architecture
* Model evaluation and performance visualization
* Real-time deployment using Flask and Docker

---

## 📂 Dataset

* **Training/Validation Data**: Images stored in two folders – *Organic* and *Recyclable*
* **Test Data**: Used to evaluate performance on unseen images

![Dataset Image](https://github.com/user-attachments/assets/443f7109-d4e2-4e36-ab12-0d6a6c2f0402)

---

## 🔍 Features

* Transfer learning and **fine-tuning of VGG16** for improved feature extraction
* **ImageDataGenerator** for data augmentation (rotation, flipping, zoom, normalization)
* **BatchNormalization** and **Dropout layers** to prevent overfitting
* **Early Stopping** and **Model Checkpointing** for efficient and stable training
* Classification metrics: accuracy, loss, confusion matrix, and report

![Performance Graphs](https://github.com/user-attachments/assets/9ae0cb8c-a4fe-426e-bf02-d78a79466742)

---

## 🧱 Model Architecture

* **Base Model**: Pre-trained **VGG16** without the top layers
* **Custom Top Layers**:

  * `GlobalAveragePooling2D`
  * `Dense` layers with `ReLU` activation
  * `Dropout` for regularization
  * Final `Dense` layer with `sigmoid` for binary classification
* Fine-tuning enabled on selected deeper layers of VGG16 for better domain adaptation

---

## 📊 Performance

* **Training Accuracy**: \~87%
* **Validation Accuracy**: \~89%
* **Training Loss**: ↓ from 0.61 to 0.29
* **Validation Loss**: ↓ from 0.52 to 0.24

![Accuracy & Loss](https://github.com/user-attachments/assets/e6da9b9d-36eb-4c8a-bd1c-5c939315b9ee)

---

## 📈 Visualizations

* Accuracy/Loss curves for training and validation
* Confusion matrix & classification report for model evaluation

![Confusion Matrix](https://github.com/user-attachments/assets/cd167e84-eb80-4990-ae71-54b88f11970e)

---

## 🌐 Web Application

Real-time image upload and prediction interface:

![Website Output 1](https://github.com/user-attachments/assets/3ff6ad37-0d27-439c-8409-3d95a756be97)
![Website Output 2](https://github.com/user-attachments/assets/100502d7-d7d4-41c2-848d-14a931a3d497)

---

## 🚀 Installation & Setup

### ✅ Prerequisites

* Python 3.8+
* pip package manager
* Modern web browser (Chrome, Firefox)

---

### 💻 Manual Setup

1. **Clone the repository** and download:

   * `app.py` (Flask backend)
   * `frontend.html` (Web interface)
   * Trained `.h5` model file

👉 [Download Model (.h5)](https://drive.google.com/file/d/1S-_UoxyPb27F9n4jKAjSRQw2G8Zn0LBH/view?usp=drive_link)

2. **Install dependencies:**

```bash
pip install flask tensorflow pillow
```

3. **Run the Flask server:**

```bash
python app.py
```

4. **Open the app:**

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

### 🐳 Docker Setup (Optional)

1. **Pull Docker image:**

```bash
docker pull atharvviit/ecosort:03
```

2. **Run the container:**

```bash
docker run -p 5000:5000 atharvviit/ecosort:03
```

3. **Open the app:**

Visit [http://localhost:5000](http://localhost:5000)

---

## 📌 Key Insights

* Fine-tuning a pre-trained model (VGG16) significantly improved classification performance.
* Proper regularization (dropout, early stopping) helped prevent overfitting.
* Docker ensured consistent and portable deployment across systems.

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!
