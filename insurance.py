import streamlit as st
import pickle

# Load the pre-trained model
@st.cache_resource
def load_model():
    with open(r"C:\Users\Ranjan kumar pradhan\.vscode\insurance_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Title
st.title("Insurance Charges Prediction")

# Inputs
age = st.slider("Age", 18, 100, 25)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Southwest", "Southeast", "Northwest", "Northeast"])

# Encode inputs
sex = 1 if sex == "Female" else 0
smoker = 0 if smoker == "Yes" else 1

# Encode 'region' as a single integer
region_map = {"Southwest": 0, "Southeast": 1, "Northwest": 2, "Northeast": 3}
region_encoded = region_map[region]

# Prepare input for the model
input_features = [age, sex, bmi, children, smoker, region_encoded]

# Prediction
if st.button("Predict"):
    try:
        prediction = model.predict([input_features])  # Ensure feature count matches training
        st.success(f"Predicted Insurance Charges: ${prediction[0]:,.2f}")
    except ValueError as e:
        st.error(f"Error: {e}")


