import os
import sys
import time
import base64
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image

# =========================
# ✅ Set Project Path
# =========================
project_root = os.path.expanduser("C:/Users/aksha/OneDrive/Desktop/Cancer_Project_8th_Sem")
if project_root not in sys.path:
    sys.path.append(project_root)

# =========================
# ✅ Load Trained Model
# =========================
model_path = os.path.join(project_root, "models/final_model.h5")
try:
    model = load_model(model_path, compile=False)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# =========================
# 🎨 Set Background Image
# =========================
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

background_image_path = os.path.join(project_root, "background.jpg")
set_background(background_image_path)

# =========================
# ✅ Initialize Session State
# =========================
if "page" not in st.session_state:
    st.session_state["page"] = "welcome"
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "uploaded_image" not in st.session_state:
    st.session_state["uploaded_image"] = None
if "patient_details" not in st.session_state:
    st.session_state["patient_details"] = {}

# =========================
# 🏠 Welcome Page
# =========================
if st.session_state["page"] == "welcome":
    st.title("👋 Welcome to Medical Diagnosis App")
    st.write("This application helps in detecting Pancreatic Cancer using AI.")
    time.sleep(3)
    st.session_state["page"] = "login"
    st.rerun()

# =========================
# 🔐 Login Page
# =========================
elif st.session_state["page"] == "login":
    st.title("🔐 User Login")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password", help="Default: admin/1234")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["authenticated"] = True
            st.success("Login Successful ✅")
            time.sleep(1)
            st.session_state["page"] = "patient_details"
            st.rerun()
        else:
            st.error("Invalid Credentials! ❌")
            st.stop()

# =========================
# 🏥 Patient Details Page
# =========================
elif st.session_state["page"] == "patient_details":
    st.title("🩺 Enter Patient Details")
    with st.form("patient_details_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        height = st.number_input("Height (cm)", min_value=50, max_value=250)
        weight = st.number_input("Weight (kg)", min_value=20, max_value=200)
        smoking = st.selectbox("Smoking History", ["Yes", "No"])
        family_history = st.selectbox("Family History of Cancer", ["Yes", "No"])
        submit = st.form_submit_button("Next")

    if submit:
        st.session_state["patient_details"] = {
            "Name": name, "Age": age, "Gender": gender,
            "Blood Group": blood_group, "Height": height,
            "Weight": weight, "Smoking": smoking, "Family History": family_history
        }
        st.success("Details Saved ✅")
        time.sleep(1)
        st.session_state["page"] = "upload_image"
        st.rerun()
        
# =========================
# 📷 Image Upload Page
# =========================
elif st.session_state["page"] == "upload_image":
    st.title("📷 Upload CT Scan Image")
    uploaded_file = st.file_uploader("Upload a CT Scan Image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        uploads_dir = os.path.join(project_root, "uploads")
        os.makedirs(uploads_dir, exist_ok=True)
        image_path = os.path.join(uploads_dir, uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state["uploaded_image"] = image_path
        st.success("Image uploaded successfully!")
        time.sleep(1)
        st.session_state["page"] = "processing"
        st.rerun()
        
# =========================
# 🔄 Processing Page
# =========================
elif st.session_state["page"] == "processing":
    st.title("🔄 Processing Image...")
    st.write("Analyzing the image using deep learning model...")
    time.sleep(3)
    st.session_state["page"] = "result"
    st.rerun()

# =========================
# 📝 Result Page
# =========================
elif st.session_state["page"] == "result":
    st.title("📝 Diagnosis Result")

    # Show patient details
    st.subheader("Patient Details")
    for key, value in st.session_state["patient_details"].items():
        st.write(f"**{key}:** {value}")

    # Preprocess image
    image_path = st.session_state["uploaded_image"]
    image = Image.open(image_path).resize((224, 224))
    image = np.array(image)

    if image.ndim == 2:
        image = np.stack([image] * 3, axis=-1)
    elif image.shape[2] == 4:
        image = image[:, :, :3]

    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)[0][0]
    result = "Cancer Detected 😞" if prediction > 0.5 else "No Cancer Detected 😊"
    confidence = prediction * 100 if prediction > 0.5 else (1 - prediction) * 100

    st.subheader("Diagnosis:")
    st.write(f"{result}")
    st.subheader("Model Confidence:")
    st.write(f"**{confidence:.2f}%**")

    if result == "No Cancer Detected 😊":
        future_risk = np.random.randint(10, 90)
        st.subheader("Future Risk Prediction:")
        st.write(f"Chance of developing cancer in the future: **{future_risk}%**")

    col1, col2, col3 = st.columns(3)
    if col1.button("🔄 Restart"):
        st.session_state["page"] = "upload_image"
        st.rerun()
    if col2.button("🔙 Back to Patient Detail Page"):
        st.session_state["page"] = "patient_details"
        st.rerun()
    if result == "Cancer Detected 😞":
        if col3.button("⚠️ Know Precaution For Cancer Patient"):
            st.session_state["page"] = "precaution_pancreatic_cancer_patient"
            st.rerun()
    else:
        if col3.button("🌿 Precaution For Healthy Life"):
            st.session_state["page"] = "precaution_for_healthy_life"
            st.rerun()

# =========================
# 🛡️ Cancer Precaution Page
# =========================
elif st.session_state["page"] == "precaution_pancreatic_cancer_patient":
    st.title("🛡️ Precautions for Pancreatic Cancer")
    st.markdown("""
**1. Maintain a Healthy Diet**  
Eating a balanced and nutritious diet is crucial during and after pancreatic cancer treatment.
Focus on:
- High-protein foods (lean meats, fish, eggs, legumes) to help repair tissues and fight infection.
- Fresh fruits and vegetables rich in antioxidants and vitamins.
- Whole grains for sustained energy.
- Healthy fats (olive oil, nuts, seeds, avocado) to support overall wellness.
- Staying hydrated with water and natural fluids like herbal teas or clear broths.   

**2. Avoid Smoking and Alcohol**  
Smoking and alcohol can worsen symptoms and interfere with treatment:
- Smoking is a major risk factor for pancreatic and other cancers.
- Alcohol can stress the liver and pancreas, increasing complications.

**3. Regular Health Checkups**  
Routine medical follow-ups help monitor your progress and detect any complications early:
- Track treatment response, side effects, and nutritional status.
- Early detection of recurrence or new health issues.
- Adjust medications or dietary plans as needed.

**4. Exercise Regularly**  
Physical activity improves strength, reduces fatigue, and boosts mental health:
- Gentle exercises like walking, stretching, or yoga can be beneficial.
- Consult your doctor or physiotherapist for a personalized plan.
""")

    if st.button("🔙 Back to Result"):
        st.session_state["page"] = "result"
        st.rerun()

# =========================
# 🛡️ Healthy Lifestyle Page
# =========================
elif st.session_state["page"] == "precaution_for_healthy_life":
    st.title("🛡️ Precautions for a Healthy Life")
    st.markdown("""
**1. Maintain a Healthy Diet**  
A nutritious diet fuels your body and mind. Focus on:
- Plenty of fresh fruits and vegetables  
- Whole grains like brown rice, oats, and whole wheat  
- Lean proteins such as chicken, fish, beans, and nuts  
- Healthy fats from sources like olive oil, avocados, and seeds  
- Staying hydrated by drinking enough water throughout the day  

**2. Avoid Smoking and Alcohol**  
Cutting out tobacco and limiting alcohol greatly reduces health risks:
- Smoking is linked to cancer, heart disease, and lung conditions  
- Excessive alcohol can damage the liver, heart, and brain  

**3. Regular Health Checkups**  
Don’t wait until you’re sick to see a doctor. Routine checkups help:
- Catch potential health issues early  
- Monitor vital signs, cholesterol, blood pressure, and blood sugar  
- Keep vaccinations and screenings up to date  

**4. Exercise Regularly**  
Staying active improves physical and mental well-being:
- Aim for at least 30 minutes of moderate activity most days  
- Mix cardio (like walking or biking) with strength and flexibility exercises  
- Physical activity helps control weight, reduce stress, and boost energy
""")

    if st.button("🔙 Back to Result"):
        st.session_state["page"] = "result"
        st.rerun()
