import streamlit as st
import numpy as np
import joblib

def heart_disease_page():
    # Load model
    filename = 'df_coeur_new.sav'
    coeur_model = joblib.load(filename)

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
    st.markdown('<h1 class="title">Détection des Maladies Cardiaques</h1>', unsafe_allow_html=True)

    # Split Columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col2:
        # Créer une liste d'âges possibles
        ages = list(range(0, 99))  # Par exemple, de 0 à 99 ans
        # Créer un menu déroulant pour sélectionner l'âge
        age = st.selectbox('Entrez votre âge', ages)

    with col4:
        Genre = st.selectbox('Entrez votre genre', ['Homme', 'Femme'])

    with col2:
        Douleur = st.number_input('Entrez la douleur ressentie')

    with col4:
        Pression = st.number_input('Entrez la valeur de la pression arterielle au repos')

    with col2:
        Cholesterol = st.number_input('Entrez la valeur du cholesterol')

    with col4:
        Sucre = st.number_input('Entrez la valeur de sucre dans le sang à jeun')

    with col2:
        Electro = st.number_input('Entrez le résultat de l\'électrocardiographie')

    with col4:
        FC = st.number_input('Entrez la valeur de la fréquence cardiaque maximale')

    with col2:
        Angine = st.number_input('Y a-t-il eu une angine induite par un exercice physique')

    with col4:
        Oldpeak = st.number_input('Dépression du segment ST induite par un exercice par rapport au repos')

    with col2:
        Slope = st.number_input('Valeur de la pente du segment ST à un effort maximal')

    with col4:
        CA = st.number_input('Nombre de vaisseaux majeurs colorés par fluoroscopie')

    with col2:
        Thal = st.number_input('Type de thalassémie')

    # Prediction
    cardiaque_diag = ''

    if st.button('Test de Prédiction Cardiaque'):
        # Prepare input data
        input_data = np.array([[age, 
                                1 if Genre == 'Homme' else 0,  # Assuming 'Homme' = 1, 'Femme' = 0
                                Douleur, Pression, Cholesterol, 
                                1 if Sucre > 0 else 0,  # Assuming 'Sucre' > 0 means True
                                Electro, FC, 
                                1 if Angine > 0 else 0,  # Assuming 'Angine' > 0 means True
                                Oldpeak, Slope, CA, Thal]])

        # Perform prediction
        renale_prediction = coeur_model.predict(input_data)

        if renale_prediction[0] == 1:
            cardiaque_diag = 'Suspicion de maladie cardiaque détectée'
        else:
            cardiaque_diag = 'Aucune détection de maladie présumée cardiaque'

    st.success(cardiaque_diag)
