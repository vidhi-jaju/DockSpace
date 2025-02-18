import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('titanic_model.pkl')

# Set Streamlit Page Config (MUST be the first command)
st.set_page_config(page_title="Titanic Survival Prediction", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .title { color: #4a90e2; font-size: 48px; font-weight: 600; text-align: center; }
    .subtitle { color: #4a5568; font-size: 20px; text-align: center; font-style: italic; margin-bottom: 30px; }
    .form-container { background-color: #ffffff; border-radius: 12px; padding: 35px; 
                      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); max-width: 800px; 
                      margin: auto; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# Title & Subtitle
st.markdown('<div class="title">Titanic Survival Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter passenger details below to predict survival chances.</div>', unsafe_allow_html=True)

# Input Fields
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
        sex = st.selectbox("Sex", ['male', 'female'])
        age = st.slider("Age", 0, 80, 25)

    with col2:
        sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
        parch = st.number_input("Parents/Children Aboard (Parch)", 0, 10, 0)
        fare = st.slider("Fare", 0, 500, 20)

# Prediction Button
if st.button("Predict Survival"):
    with st.spinner("Predicting..."):
        try:
            sex_binary = 1 if sex == 'female' else 0
            input_data = pd.DataFrame([[pclass, sex_binary, age, sibsp, parch, fare]], 
                                      columns=['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 
                                               'Parents/Children Aboard', 'Fare'])

            # Make Prediction
            prediction = model.predict(input_data)
            result = "Survived" if prediction[0] == 1 else "Did not survive"

            # Display Result
            if result == "Survived":
                st.success(f"✅ {result}")
            else:
                st.error(f"❌ {result}")

        except Exception as e:
            st.error(f"⚠️ Prediction Error: {e}")

