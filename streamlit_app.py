import streamlit as st
import pandas as pd
import random
from sklearn.neighbors import NearestNeighbors
from streamlit_option_menu import option_menu

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

# Charger le dataset encodé
final_df_cupid_ml = pd.read_csv('final_df_cupid_ml.csv')

# Sélectionner les caractéristiques pour KNN
features = final_df_cupid_ml.drop(['Name'], axis=1)  # Supprimer la colonne 'Name' car ce n'est pas une caractéristique

# Centrer le titre sur la page
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Wild Love</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>💖For one love 💖</h2>", unsafe_allow_html=True)

# Menu de navigation en haut
menu = option_menu(
    menu_title=None,  # Pas de titre pour le menu
    options=["Accueil", "Mon Profil"],  # Options du menu
    icons=["house", "person"],  # Icônes pour les options
    menu_icon="cast",  # Icône du menu
    default_index=0,  # Option par défaut
    orientation="horizontal",  # Menu horizontal
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "padding": "10px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#ff4b4b"},
    }
)

# Fonction pour afficher le pop-up de bienvenue
def show_welcome_popup():
    st.markdown("""
        <div class="popup">
            <div class="popup-content">
                <span class="close">&times;</span>
                <h2>Bienvenue sur Wild Love !</h2>
                <p>Nous espérons que vous trouverez votre match parfait.</p>
            </div>
        </div>
        <style>
            .popup {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: white;
                padding: 20px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                z-index: 1000;
                border-radius: 10px;
                text-align: center;
                width: 300px;
            }
            .popup-content {
                position: relative;
            }
            .close {
                position: absolute;
                top: 10px;
                right: 10px;
                font-size: 20px;
                cursor: pointer;
            }
            .popup h2 {
                color: #ff4b4b;
            }
        </style>
        <script>
            const closePopup = () => {
                document.querySelector('.popup').style.display = 'none';
            };
            document.querySelector('.close').onclick = closePopup;
            window.onclick = function(event) {
                if (event.target == document.querySelector('.popup')) {
                    document.querySelector('.popup').style.display = 'none';
                }
            }
        </script>
    """, unsafe_allow_html=True)

# Appel de la fonction pour afficher le pop-up de bienvenue
show_welcome_popup()

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
        status_single = st.selectbox("Statut", ["Célibataire", "En couple", "C'est compliqué"])
        orientation = st.selectbox("Orientation", ["Hétérosexuel", "Homosexuel", "Bisexuel", "Autre"])
        body_type = st.selectbox("Type de corps", ["Mince", "Moyen", "Athlétique", "Rond"])
        diet = st.selectbox("Régime alimentaire", ["Tout", "Végétarien", "Végétalien", "Autre"])
        education = st.selectbox("Niveau d'éducation", ["Lycée", "Licence", "Maîtrise", "Doctorat"])
        job = st.selectbox("Métier", ["Technologie", "Éducation", "Santé", "Arts", "Autre"])
        pets = st.selectbox("Animaux", ["Aime les animaux", "N'aime pas les animaux"])
        smokes = st.selectbox("Fumeur", ["Non", "Oui"])

        submit_button = st.form_submit_button(label="Soumettre")

    if submit_button:
        # Préparer les entrées utilisateur pour l'encodage
        user_input = {
            'age': age,
            'status_single': 1 if status_single == "Célibataire" else 0,
            'sex_x_m': 1 if gender == "Homme" else 0,
            'orientation_straight': 1 if orientation == "Hétérosexuel" else 0,
            'body_type_fit': 1 if body_type == "Athlétique" else 0,
            'diet_anything': 1 if diet == "Tout" else 0,
            'education_bachelors': 1 if education == "Licence" else 0,
            'height': height,
            'job_computer / hardware / software': 1 if job == "Technologie" else 0,
            'pets_likes pets': 1 if pets == "Aime les animaux" else 0,
            'smokes_no': 1 if smokes == "Non" else 0
        }

        # Encoder les entrées utilisateur pour correspondre au format du dataset
        user_input_encoded = pd.DataFrame(user_input, index=[0])
        user_input_aligned = user_input_encoded.reindex(columns=features.columns, fill_value=0)

        # Instancier et ajuster le modèle KNN
        knn_model = NearestNeighbors(n_neighbors=1)
        knn_model.fit(features)

        # Trouver le voisin le plus proche pour les entrées utilisateur
        distances, indices = knn_model.kneighbors(user_input_aligned)
        nearest_neighbor_index = indices[0][0]
        nearest_neighbor_info = final_df_cupid_ml.iloc[nearest_neighbor_index]

        st.write(f"**Nom:** {name}")
        st.write(f"**Âge:** {age} ans")
        st.write(f"**Sexe:** {gender}")
        st.write(f"**Taille:** {height} cm")
        st.write(f"**Statut:** {status_single}")
        st.write(f"**Orientation:** {orientation}")
        st.write(f"**Type de corps:** {body_type}")
        st.write(f"**Régime alimentaire:** {diet}")
        st.write(f"**Niveau d'éducation:** {education}")
        st.write(f"**Métier:** {job}")
        st.write(f"**Animaux:** {pets}")
        st.write(f"**Fumeur:** {smokes}")

        # Bouton pour générer un match idéal
