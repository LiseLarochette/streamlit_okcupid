import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Centrer le titre sur la page
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Wild Love</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>💖For one love 💖</h2>", unsafe_allow_html=True)

# Chargement du jeu de données encodé
final_df_cupid_ml = pd.read_csv('final_df_cupid_ml.csv')
# Sélection des caractéristiques pour le KNN
features = final_df_cupid_ml.drop(['Name'], axis=1)

# Fonction pour afficher le titre centré
def centered_title(text):
    st.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{text}</h1>", unsafe_allow_html=True)

# Barre latérale de navigation
menu = st.sidebar.selectbox("Menu", ["Accueil", "Mon Profil"])

# Page d'accueil
if menu == "Accueil":
    st.markdown("""
    Bienvenue sur notre application de rencontre ! Renseignez vos informations ci-dessous et cliquez sur le bouton pour découvrir votre match parfait.
    """)

    # Formulaire pour les informations de l'utilisateur
    with st.form(key='user_info'):
        name = st.text_input("Nom")
        age = st.number_input("Âge", min_value=18, max_value=100, step=1)
        gender = st.selectbox("Sexe", ["Homme", "Femme", "Autre"])
        height = st.number_input("Taille (cm)", min_value=100, max_value=250, step=1)
        interests = st.text_area("Intérêts")
        
        submit_button = st.form_submit_button(label="Soumettre")

    if submit_button:
        st.write(f"**Nom:** {name}")
        st.write(f"**Âge:** {age} ans")
        st.write(f"**Sexe:** {gender}")
        st.write(f"**Taille:** {height} cm")
        st.write(f"**Intérêts:** {interests}")
        
        # Prétraitement de l'entrée utilisateur pour le KNN
        user_input = {
            'age': age,
            'status_single': 1,  # Make sure to include all status options from your dataset
            'sex_x_m': 1 if gender == "Homme" else 0,  # Make sure to include all sex options from your dataset
            'orientation_straight': 1,  # Make sure to include all orientation options from your dataset
            'body_type_fit': 1,  # Make sure to include all body type options from your dataset
            'diet_anything': 1,  # Make sure to include all diet options from your dataset
            'education_bachelors': 1,  # Make sure to include all education options from your dataset
            'height': height,
            'job_computer / hardware / software': 1,  # Make sure to include all job options from your dataset
            'pets_likes pets': 1,  # Make sure to include all pets options from your dataset
            'smokes_no': 1  # Make sure to include all smokes options from your dataset
        }
        user_input_encoded = pd.DataFrame(user_input, index=[0])
        user_input_aligned = user_input_encoded.reindex(columns=features.columns, fill_value=0)
        
        # Initialisation et ajustement du modèle KNN
        knn_model = NearestNeighbors(n_neighbors=1)
        knn_model.fit(features)
        
        # Recherche du plus proche voisin
        distances, indices = knn_model.kneighbors(user_input_aligned)
        nearest_neighbor_index = indices[0][0]
        nearest_neighbor_info = final_df_cupid_ml.iloc[nearest_neighbor_index]
        st.write("Informations sur le voisin le plus proche:", nearest_neighbor_info)

    # Affichage des profils
    st.header("Nos utilisateurs")
    cols = st.columns(2)
    for i, user in enumerate(users):
        col = cols[i % 2]
        with col:
            st.image(user["image"], width=150)
            st.write(f"**{user['name']}**, {user['age']} ans")
            st.write(f"Intérêts : {user['interests']}")

# Page de profil utilisateur
elif menu == "Mon Profil":
    centered_title("Mon Profil")

    # Afficher les informations du profil si elles existent
    if 'name' in locals():
        st.write(f"**Nom:** {name}")
        st.write(f"**Âge:** {age} ans")
        st.write(f"**Sexe:** {gender}")
        st.write(f"**Taille:** {height} cm")
        st.write(f"**Intérêts:** {interests}")
    else:
        st.warning("Veuillez remplir vos informations sur la page d'accueil.")

# Styles personnalisés
st.markdown("""
    <style>
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
        }
        .stSuccess {
            font-size: 1.2em;
        }
    </style>
""", unsafe_allow_html=True)
