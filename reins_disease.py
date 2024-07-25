import streamlit as st
import numpy as np
import joblib

def rein_page():
    # Load model
    filename = 'reins.sav'
    reins_model = joblib.load(filename)
    
    # Apply custom CSS styling
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-color: #9FC4C0; /* Matching the background color */
        }
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }
        .stButton>button {
            background-color: #9FC4C0;
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
    st.markdown('<h1 class="title">Prédiction de la Maladie Rénale Chronique</h1>', unsafe_allow_html=True)

    # Split Columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col2:
        age = st.selectbox('Entrez votre âge', list(range(0, 100)))

    with col4:
        bp = st.number_input('Entrez la valeur de la pression artérielle')

    with col2:
        sod = st.number_input('Entrez la valeur du sodium')

    with col4:
        pot = st.number_input('Entrez la valeur du potassium')

    with col2:
        hemo = st.number_input('Entrez la valeur de l\'hémoglobine')

    with col4:
        al = st.number_input('Entrez la valeur de l\'albumine')

    with col2:
        sg = st.number_input('Entrez la valeur du SG')

    with col4:
        su = st.number_input('Entrez la valeur du SU')

    with col2:
        sc = st.number_input('Entrez la valeur du SC')

    # Prediction
    renale_diag = ''

    if st.button('Test de Prédiction de la Maladie Rénale'):
        renale_prediction = reins_model.predict([[age, bp, sod, pot, hemo, al, sg, su, sc]])

        if renale_prediction[0] == 1:
            renale_diag = 'Suspicion de maladie rénale chronique détectée'
        else:
            renale_diag = 'Aucune détection de maladie présumée rénale chronique'

    st.success(renale_diag)
