import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="PlantGuard AI", page_icon="🌿", layout="wide")

# --- CUSTOM CSS FOR FORMAL AESTHETIC ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stTitle {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #1e3d59;
        font-weight: 700;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DISEASE INFORMATION DICTIONARY ---
disease_info = {
    'Apple___Apple_scab': "Fungal infection causing dark spots. **Treatment:** Apply copper-based fungicides and clear fallen leaves.",
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': "Spread by whiteflies. **Treatment:** Use insecticidal soaps and remove infected plants immediately.",
    'Potato___Early_blight': "Fungal disease starting on older leaves. **Treatment:** Improve air circulation and apply mancozeb fungicides.",
    'Corn_(maize)___Common_rust_': "Reddish-brown pustules on leaves. **Treatment:** Use rust-resistant hybrids and rotate crops.",
    'Grape___Black_rot': "Serious fungal disease affecting fruit and leaves. **Treatment:** Prune infected vines and use Myclobutanil sprays.",
    'healthy': "No disease detected. Keep up the good irrigation and soil nutrition!"
}

# --- SIDEBAR: PROJECT OVERVIEW ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=100)
st.sidebar.title("Project Dashboard")
st.sidebar.markdown("---")
st.sidebar.header("About Project")
st.sidebar.info("""
**Model:** Convolutional Neural Network (CNN)  
**Dataset:** PlantVillage (54,000+ Images)  
**Classes:** 38 Plant-Disease Pairs  
**Goal:** Empowering farmers with instant, AI-driven crop diagnostic tools to minimize yield loss.
""")

# --- MODEL LOADING ---
@st.cache_resource
def load_my_model():
    # Ensuring pathing is robust for local/deployment
    import os

model_path = os.path.join(os.getcwd(), "trained_model", "plant_disease_prediction_model.h5")


model_path = r"C:\\Users\\gargi\\OneDrive\\Desktop\\plant detedction\\trained_models\\plant_disease_prediction_model.h5"

print("File exists:", os.path.exists(model_path))  # debug line
model = tf.keras.models.load_model(model_path)
model = load_my_model()
print("Model value:", model)
print("Model type:", type(model))

class_indices = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# --- MAIN CONTENT ---
st.title("🌿 PlantGuard AI: Intelligent Crop Diagnostic System")
st.markdown("---")

uploaded_file = st.file_uploader("Drop a leaf image here for analysis...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Using columns for side-by-side layout
    col1, col2 = st.columns([1, 1])
    
    image = Image.open(uploaded_file)
    
    with col1:
        st.subheader("Uploaded Specimen")
        st.image(image, use_container_width=True, caption="Target Image for Diagnosis")
    
    with col2:
        st.subheader("Diagnostic Results")
        with st.spinner('Neural Network is processing features...'):
            # Preprocessing
            img = image.resize((224, 224))
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Prediction
            predictions = model.predict(img_array)
            result_index = np.argmax(predictions)
            confidence = np.max(predictions)
            
            # Result Display Logic
            pred_name = class_indices[result_index]
            
            # Color logic based on 'healthy' status
            is_healthy = "healthy" in pred_name.lower()
            status_color = "#28a745" if is_healthy else "#d9534f" # Green if healthy, Red if diseased
            
            st.markdown(f"<h2 style='color: {status_color};'>{pred_name.replace('___', ': ')}</h2>", unsafe_allow_html=True)
            
            # Confidence Progress Bar
            st.write(f"**Confidence Level:** {confidence*100:.2f}%")
            st.progress(float(confidence))
            
            # Contextual Description
            st.markdown("### 💡 Recommendation")
            # Look up specific info or generic healthy/disease info
            info = disease_info.get(pred_name, "Disease identified. Consult your local agriculture department for regional treatment options.")
            if is_healthy:
                st.balloons()
                st.info(disease_info['healthy'])
            else:
                st.warning(info)

# --- FOOTER ---
st.markdown("---")
st.caption("Vellore Institute of Technology | CSE Department")