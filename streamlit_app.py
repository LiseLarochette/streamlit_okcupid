import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Wild Love') 
import streamlit as st
import numpy as np

st.write("Découvre ton match idéal")

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

# Titre de l'application
st.title("💖 Application de Rencontre 💖")

# Description
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

# Affichage des profils
st.header("Nos utilisateurs")

cols = st.columns(2)
for i, user in enumerate(users):
    col = cols[i % 2]
    with col:
        st.image(user["image"], width=150)
        st.write(f"**{user['name']}**, {user['age']} ans")
        st.write(f"Intérêts : {user['interests']}")

# Bouton pour générer un match
st.header("Trouver un match")

if st.button("💘 Trouver mon match parfait 💘"):
    match = random.choice(users)
    st.success(f"Félicitations ! Vous avez un match parfait avec {match['name']}!")
    st.image(match["image"], caption=f"{match['name']}, {match['age']} ans", width=200)
    st.write(f"**{match['name']}**, {match['age']} ans")
    st.write(f"Intérêts : {match['interests']}")

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
