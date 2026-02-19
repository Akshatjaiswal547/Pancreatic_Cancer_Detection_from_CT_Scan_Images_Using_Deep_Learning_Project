## 🧠 **Pancreatic Cancer Detection from CT Scan Images Using Deep Learning**

---

### 📌 **Overview**

This project is an AI-based diagnostic tool designed to detect **pancreatic cancer** from **CT scan images** using **deep learning**. By leveraging the power of Convolutional Neural Networks (CNNs), specifically the **ResNet50 architecture**, this system classifies CT images into cancerous or non-cancerous categories. It also predicts potential **future cancer risk** and provides **preventive health guidance** to users.

A user-friendly interface has been built using **Streamlit**, allowing medical professionals to upload CT images, input patient details, and view predictions along with visual and textual feedback. The goal is to assist doctors in early cancer detection, reduce diagnostic delays, and support decision-making in clinical workflows.

---

### 🎯 **Project Objectives**

* To detect pancreatic cancer from CT scan images using a deep learning model.
* To provide an interactive GUI for image upload, diagnosis, and result visualization.
* To estimate the future risk of cancer based on patient data.
* To suggest relevant precautions and health advice.
* To promote AI-driven medical diagnostics for faster and more accurate outcomes.

---

### 🔍 **Key Features**

* 🧪 **ResNet50-based CNN**: Pre-trained deep learning model fine-tuned on CT scan datasets.
* 📷 **Image Upload & Preview**: Upload CT images and see them before prediction.
* 🧾 **Patient Details Form**: Enter and track patient info (age, gender, history, etc.).
* 📊 **Cancer Prediction**: Model outputs binary classification (Cancer / No Cancer).
* 📈 **Future Risk Estimation**: Predicts probabilistic risk based on lifestyle/history.
* 🛡️ **Precautionary Advice**: Offers health tips based on results.
* 🌐 **Streamlit Web Interface**: Interactive, responsive and medically themed UI.
* 💾 **Model Save/Load**: Trained model stored in `.h5` format for future predictions.

---

### 🧰 **Tech Stack**

| Component            | Technology Used                          |
| -------------------- | ---------------------------------------- |
| 💻 Language          | Python                                   |
| 🤖 Model             | TensorFlow, Keras (ResNet50)             |
| 🖼️ Image Processing | OpenCV, NumPy                            |
| 📊 Data Handling     | Pandas, Scikit-learn                     |
| 🌐 GUI Framework     | Streamlit                                |
| 📁 File Types        | `.jpg`, `.png`, `.jpeg`, `.h5`, `.ipynb` |

---

### 🏗️ **Project Structure**

```
📁 Cancer_Project_8th_Sem/
├── app.py                           # Streamlit application
├── training.ipynb                  # Model training notebook
├── evaluation.ipynb                # Model evaluation notebook
├── models/
│   └── final_model.h5              # Trained CNN model
├── utils/
│   ├── data_loader.py              # Data loading & preprocessing functions
│   └── custom_model.py             # Model architecture (ResNet50 customization)
├── uploads/                        # Uploaded images (runtime)
├── data/
│   └── train/                      # CT scan image dataset
├── background.jpg                  # UI background
└── requirements.txt                # Python dependencies
```

---

### 📊 **Model Performance**

* **Model Type**: ResNet50 with custom top layers
* **Accuracy Achieved**: \~90% on validation data
* **Loss Function**: Binary Crossentropy
* **Optimizer**: Adam (learning rate: 0.0001)

---

### 🩺 **Use Case**

This tool is aimed at medical professionals, radiologists, and healthcare researchers. It provides a **decision-support system** that can enhance diagnostic workflows, especially in resource-constrained settings where expert radiologists may not be available.

---

### 📈 **Future Scope**

* Multi-class classification (e.g., Stage I, II, III cancer)
* Integration with other imaging modalities like MRI
* Use of larger and clinically annotated datasets
* Deploy as a web-based hospital-grade diagnostic tool
* Incorporate Electronic Health Record (EHR) systems

---

### 📚 **How to Run**

1. Clone the repository

2. Install dependencies using `requirements.txt`:

   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

4. Upload a CT scan image, fill in patient details, and get predictions instantly!

---

### 👨‍💻 **Team Members**

* Akshat Jaiswal
* Pratik Sao ![](https://github.com/ipratiksao)

> **Institution:** Lakhmi Chand Institute of Technology, Bilaspur
> **Department:** Computer Science & Engineering
> **Semester:** 8th
> **Project Type:** Major Project

---

### 📜 **License**

This project is developed for academic and research purposes only. It is **not intended** for real-world medical use unless clinically validated and approved.
