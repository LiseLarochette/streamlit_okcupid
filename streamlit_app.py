import streamlit as st
import pandas as pd
from datetime import datetime
import random
import numpy as np


# Centrer le titre sur la page
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Wild Love</h1>", unsafe_allow_html=True)


st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>💖For one love 💖</h2>", unsafe_allow_html=True)

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
def centered_title(text):
    st.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{text}</h1>", unsafe_allow_html=True)

# Barre latérale de navigation
menu = st.sidebar.selectbox("Menu", ["Accueil", "Mon Profil"])

# Header global
st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>Bienvenue sur Wild Love</h2>", unsafe_allow_html=True)

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
