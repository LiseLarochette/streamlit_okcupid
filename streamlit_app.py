import streamlit as st
import random

# Liste des utilisateurs fictifs
users = [
    {"name": "Alice", "age": 25, "interests": "Voyages, Musique", "image": "alice.png"},
    {"name": "Bob", "age": 30, "interests": "Sport, Lecture", "image": "bob.png"},
    {"name": "Charlie", "age": 28, "interests": "Cuisine, Cinéma", "image": "charlie.png"},
    {"name": "Diana", "age": 22, "interests": "Art, Danse", "image": "diana.png"},
    {"name": "Eve", "age": 27, "interests": "Technologie, Randonnée", "image": "eve.png"},
    {"name": "Frank", "age": 32, "interests": "Photographie, Yoga", "image": "frank.png"},
    {"name": "Grace", "age": 29, "interests": "Mode, Lecture", "image": "grace.png"},
    {"name": "Hannah", "age": 24, "interests": "Musique, Peinture", "image": "hannah.png"},
    {"name": "Ivy", "age": 26, "interests": "Écriture, Voyage", "image": "ivy.png"},
    {"name": "Jack", "age": 31, "interests": "Fitness, Jeux vidéo", "image": "jack.png"}
]

# Fonction pour afficher le titre centré
# Header global
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Wild love</h1>", unsafe_allow_html=True)

def centered_title(text):
    st.markdown(f"<h2 style='text-align: center; color: #ff4b4b;'>For one love</h2>", unsafe_allow_html=True)

# Barre latérale de navigation
menu = st.sidebar.selectbox("Menu", ["Accueil", "Mon Profil"])


# Page d'accueil
if menu == "Accueil":
    centered_title("Wild Love")
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
        
        # Bouton pour générer un match idéal après soumission des informations
        if st.button("💘 Découvrir mon match idéal 💘"):
            match = random.choice(users)
            st.success(f"Félicitations ! Vous avez un match parfait avec {match['name']}!")
            st.image(match["image"], caption=f"{match['name']}, {match['age']} ans", width=200)
            st.write(f"**{match['name']}**, {match['age']} ans")
            st.write(f"Intérêts : {match['interests']}")

    # Affichage des profils
    st.header("Votre wild match !")

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

import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Charger le jeu de données encodé
final_df_cupid_ml = pd.read_csv('final_df_cupid_ml.csv')
# Sélectionner les caractéristiques pour le KNN
features = final_df_cupid_ml.drop(['Name'], axis=1)

# Interface utilisateur avec Streamlit
st.title('Application de Matchmaking')

# Formulaire pour les informations de l'utilisateur
name = st.text_input("Nom")
age = st.slider("Âge", 18, 100, 30)
gender = st.selectbox("Sexe", ["Homme", "Femme", "Autre"])
height = st.slider("Taille (cm)", 100, 250, 180)
interests = st.text_area("Intérêts")
submit_button = st.button("Trouver un match")

if submit_button:
    st.write(f"**Nom:** {name}")
    st.write(f"**Âge:** {age} ans")
    st.write(f"**Sexe:** {gender}")
    st.write(f"**Taille:** {height} cm")
    st.write(f"**Intérêts:** {interests}")
    
    # Prétraitement des données d'entrée utilisateur pour le KNN
    user_input = {
        'age': age,
        'status_single': 1,
        'sex_x_m': 1 if gender == "Homme" else 0,
        'orientation_straight': 1,
        'body_type_fit': 1,
        'diet_anything': 1,
        'education_bachelors': 1,
        'height': height,
        'job_computer / hardware / software': 1,
        'pets_likes pets': 1,
        'smokes_no': 1
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
    
    # Affichage des informations sur le match le plus proche
    st.write("Match le plus proche:", nearest_neighbor_info)

