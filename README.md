

# 🌿 Plant-Disease-Detection

### Multi-Class Plant Disease Diagnostic System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![License](https://img.shields.io/badge/License-Educational-green)

---

## 📌 Project Overview

**Plant-Disease-Detection** is an end-to-end deep learning application designed to detect plant diseases from leaf images with high accuracy. The system leverages a Convolutional Neural Network (CNN) trained on the **PlantVillage dataset** to classify images into **38 different plant-disease categories**.

It provides **instant diagnosis, confidence scores, and treatment suggestions** through an intuitive web interface, making it highly useful for farmers, researchers, and agricultural experts.

---

## 👨‍💻 Contributors
- Shikhar Shukla
- Teammate 1 - Gargi Verma
- Teammate 2 - Prachi Gupta 
- Teammate 3 - Mayank Agarwal 
- Teammate 4 - Harsh Raj
- Teammate 5 - Chemate Shubham Sharad 
## 🎯 Objective

The primary goal of this project is to bridge the gap between **advanced computer vision techniques** and **real-world agricultural needs** by building a fast, reliable, and user-friendly plant disease detection system.

---

## 🚀 Key Features

* ⚡ **Instant Diagnosis**
  Predict plant diseases in under 2 seconds.

* 🌾 **Wide Coverage**
  Supports **38 plant-disease classes** across multiple crops.

* 🖥️ **Interactive Web Interface**
  Built using **Streamlit** for simplicity and usability.

* 📊 **Confidence Visualization**
  Displays prediction probabilities using progress bars.

* 💡 **Treatment Suggestions**
  Provides actionable insights for disease management.

* 🚀 **Optimized Performance**
  Uses `@st.cache_resource` for efficient model loading.

---

## 🏗️ Technical Architecture

### 🔹 Data Acquisition

* Dataset: **PlantVillage Dataset**
* Total Images: **54,000+**
* Source: Kaggle

---

### 🔹 Data Preprocessing

* Image Resizing: **224 × 224**
* Normalization: **1/255 scaling**
* Data Augmentation:

  * Rotation
  * Flipping
  * Zooming

---

### 🔹 Model Architecture

A **Sequential CNN model** consisting of:

* Convolution Layer 1 – 32 filters
* Convolution Layer 2 – 64 filters
* Convolution Layer 3 – 128 filters
* MaxPooling Layers
* Dropout Layer (0.5)
* Dense Layer (256 neurons)
* Output Layer – Softmax (38 classes)

---

## 📊 Dataset Information

The model is trained on the **PlantVillage Dataset**, containing labeled images of healthy and diseased leaves.

### 🌱 Plants Covered

* **Apple** – Scab, Black Rot, Cedar Apple Rust, Healthy
* **Tomato** – Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Mosaic Virus, Healthy
* **Potato** – Early Blight, Late Blight, Healthy
* **Grape** – Black Rot, Esca, Leaf Blight, Healthy
* **And many more…**

---

## 📷 Example Workflow

1️⃣ Upload a leaf image
2️⃣ Image is preprocessed
3️⃣ CNN model predicts disease class
4️⃣ System displays:

* ✅ Predicted Disease
* 📊 Confidence Score
* 💡 Suggested Treatment

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gargi42828/plant-disease-detection.git
cd plant-disease-detection
```

### 2️⃣ Install Dependencies

Ensure Python **3.9+** is installed.

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 💻 Tech Stack

* **Programming Language:** Python
* **Deep Learning:** TensorFlow / Keras
* **Web Framework:** Streamlit
* **Libraries:** NumPy, OpenCV, Matplotlib

---

## 📈 Future Enhancements

* 📱 Mobile-friendly UI
* 📸 Real-time camera detection
* 🌐 Multi-language support for farmers
* ☁️ Cloud deployment
* 📡 Integration with agricultural advisory systems

---

## 👨‍💻 Author

**Gargi Verma**
Aspiring Machine Learning Engineer

---

## 📜 License

This project is intended for **educational and research purposes only**.

---

## ⭐ Show Your Support

If you found this project useful, consider:

* ⭐ Starring the repository
* 🍴 Forking the project
* 🛠️ Contributing

---

