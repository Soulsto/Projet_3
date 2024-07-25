import joblib
import streamlit as st

def diabete_page():
    # Load model
    filename = 'diabete.sav'
    diabete_model = joblib.load(filename)
    
    # Apply custom CSS styling
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-color: #8FACA2; /* Matching the background color from home page */
        }
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }
        .stButton>button {
            background-color: #8FACA2;
            color: white;
            display: block;
            margin: 0 auto;
        }
        .stSuccess {
            color: #4CAF50; /* Green color for success message */
        }
        .title {
            font-family: 'Bebas Neue', sans-serif;
            color: white;
            text-align: center;
        }
        .banner img {
            display: block;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add banner image
    st.markdown(
        """
        <div class="banner">
            <img src="https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon_banner.png" width="800" height="200">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Web Title
    st.markdown('<h1 class="title">Prédiction du Diabète</h1>', unsafe_allow_html=True)

    # Split Columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col2:
        Pregnancies = st.number_input('Entrez la valeur des grossesses')

    with col4:
        Glucose = st.number_input('Entrez la valeur de la glycémie')

    with col2:
        BloodPressure = st.number_input('Entrez la valeur de la pression artérielle')

    # Removed SkinThickness field
    with col4:
        Insulin = st.number_input("Entrez la valeur de l'insuline")

    with col2:
        BMI = st.number_input("Entrez la valeur de l'IMC (Indice de Masse Corporelle)")

    with col4:
        DiabetesPedigreeFunction = st.number_input('Entrez la valeur de la fonction de pedigree du diabète')

    with col2:
        Age = st.number_input("Entrez la valeur de l'âge")

    # Prediction
    diabetes_diagnosis = ''

    if st.button('Test de Prédiction du Diabète'):
        # Prediction input without SkinThickness
        diabetes_prediction = diabete_model.predict([[Pregnancies, Glucose, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'The patient has diabetes'
        else:
            diabetes_diagnosis = 'The patient does not have diabetes'

    st.success(diabetes_diagnosis)