import joblib
import streamlit as st

def seins_page():
    # Load model
    filename = 'seins.sav'
    seins_model = joblib.load(filename)
    
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
    st.markdown('<h1 class="title">Prédiction du Cancer du Sein</h1>', unsafe_allow_html=True)

    # Split Columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col2:
        Radius = st.number_input('Entrez la valeur de Radius Mean')

    with col4:
        Texture = st.number_input('Entrez la valeur de Texture Mean')

    with col2:
        Perimeter = st.number_input('Entrez la valeur de Perimeter Mean')

    with col4:
        Area = st.number_input("Entrez la valeur de Area Mean")

    with col2:
        Smoothness = st.number_input("Entrez la valeur de Smoothness Mean")

    with col4:
        Compactness = st.number_input('Entrez la valeur de Compactness Mean')

    with col2:
        Concavity = st.number_input("Entrez la valeur de Concavity Mean")

    with col4:
        Concave_point = st.number_input("Entrez la valeur de Concave Point Mean")

    with col2:
        Symmetry = st.number_input("Entrez la valeur de Symmetry Mean")

    with col4:
        Fractal = st.number_input("Entrez la valeur de Fractal Dimension Mean")    

    # Prediction
    seins_diagnosis = ''

    if st.button('Test de Prédiction du Cancer du sein'):
        
        seins_prediction = seins_model.predict([[Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Concave_point, Symmetry, Fractal]])

        if seins_prediction[0] == 1:
            seins_diagnosis = "La patiente n'a pas de cancer du sein"
        else:
            seins_diagnosis = "La patiente a de fortes chances d'avoir le cancer du sein, des examens complémentaires sont à effectuer !"

    st.success(seins_diagnosis)







