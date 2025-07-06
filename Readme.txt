Pancreatic Cancer Detection from CT Scan Images Using Deep Learning

This project presents a deep learning-based application designed to detect Pancreatic Cancer from CT scan images using Convolutional Neural Networks (CNNs). The system is built with a user-friendly Streamlit interface, making advanced AI diagnostics accessible to medical professionals and researchers.

Key Features

	Deep Learning Model trained on annotated CT scan images
	Real-time Image Processing and prediction
	Patient Information Management (age, gender, history, etc.)
	Future Risk Prediction based on medical history
	Precaution Guidelines if cancer is detected
	Restart and Diagnosis History Options
	Clear visual results with probability scores
	Integrated with OpenCV, TensorFlow/Keras, and Streamlit

Technologies Used

	Python
	TensorFlow / Keras
	OpenCV
	Streamlit
	NumPy, Pandas
	Matplotlib & Seaborn (for visualization)

Folder Structure

	`models/` – Contains the trained CNN model (.h5)
	`uploads/` – For storing uploaded CT scan images
	`utils/` – Data loading and preprocessing scripts
	`app.py` – Main Streamlit web app file
	`training.ipynb` – Jupyter notebook used for training the model
	`data/` – Dataset used for training (organized in class folders)
	`README.md` – Project overview and instructions

Setup Instructions

	1. Clone the repo
	2. Install dependencies: `pip install -r requirements.txt`
	3. Run the app: `streamlit run app.py`
	4. Upload a CT scan and get predictions instantly!

Applications

	Early detection of Pancreatic Cancer
	Supporting diagnostic decisions in hospitals
	AI-based medical research and analysis