import streamlit as st
from streamlit_option_menu import option_menu
import os
from auth import login, signup  # Import the login and signup functions

# Set the page configuration
st.set_page_config(page_title="Medi-Sync Pro", layout="wide", page_icon="🧑‍⚕️")
# Construct the absolute path to the logo
logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "logo.png")

with st.sidebar:
    # Display the logo if the file exists
    if os.path.exists(logo_path):
        st.image(logo_path, caption="Medi-sync", use_container_width=True)  # Show logo with caption
    else:
        st.error(f"Logo file not found at: {logo_path}. Please ensure the file exists and the path is correct.")

    # Sidebar menu
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Login','Signup','Diabetes Prediction', 'Heart Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Login Page
if selected == "Login":
    username = login()  # Call the login function from auth.py
    if username:
        # Store the username in session_state for tracking the user
        st.session_state.username = username
        st.experimental_rerun()  # Rerun the app to load the correct page after successful login

# Signup Page
if selected == "Signup":
    signup()  # Call the signup function from auth.py

# Disease Prediction Pages (show only if user is logged in)
if selected == 'Diabetes Prediction' or selected == 'Heart Disease Prediction':
    # Check if the user is logged in
    if 'username' in st.session_state:
        st.title(f'{selected} using ML')

        if selected == 'Diabetes Prediction':
            # Diabetes prediction form
            col1, col2, col3 = st.columns(3)

            with col1:
                Pregnancies = st.text_input('Number of Pregnancies')

            with col2:
                Glucose = st.text_input('Glucose Level')

            with col3:
                BloodPressure = st.text_input('Blood Pressure value')

            with col1:
                SkinThickness = st.text_input('Skin Thickness value')

            with col2:
                Insulin = st.text_input('Insulin Level')

            with col3:
                BMI = st.text_input('BMI value')

            with col1:
                DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

            with col2:
                Age = st.text_input('Age of the Person')

            # Prediction for Diabetes
            if st.button('Diabetes Test Result'):
                # Here you can connect to the diabetes prediction model
                # user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
                # Make prediction using the model (mock prediction for now)
                diab_prediction = "The person is diabetic"  # You would use the model here for prediction
                st.success(diab_prediction)

        if selected == 'Heart Disease Prediction':
            # Heart disease prediction form
            col1, col2, col3 = st.columns(3)

            with col1:
                age = st.text_input('Age')

            with col2:
                sex = st.text_input('Sex')

            with col3:
                cp = st.text_input('Chest Pain types')

            with col1:
                trestbps = st.text_input('Resting Blood Pressure')

            with col2:
                chol = st.text_input('Serum Cholestoral in mg/dl')

            with col3:
                fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

            with col1:
                restecg = st.text_input('Resting Electrocardiographic results')

            with col2:
                thalach = st.text_input('Maximum Heart Rate achieved')

            with col3:
                exang = st.text_input('Exercise Induced Angina')

            with col1:
                oldpeak = st.text_input('ST depression induced by exercise')

            with col2:
                slope = st.text_input('Slope of the peak exercise ST segment')

            with col3:
                ca = st.text_input('Major vessels colored by flourosopy')

            with col1:
                thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

            # Prediction for Heart Disease
            if st.button('Heart Disease Test Result'):
                # Here you can connect to the heart disease prediction model
                # user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
                # Make prediction using the model (mock prediction for now)
                heart_diagnosis = "The person does not have any heart disease"  # You would use the model here for prediction
                st.success(heart_diagnosis)

    else:
        st.warning("Please login to access the prediction pages.")
