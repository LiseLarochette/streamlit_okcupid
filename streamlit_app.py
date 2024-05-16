import streamlit as st
import pandas as pd
import random

# Centrer le titre sur la page
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Wild Love</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>💖For one love 💖</h2>", unsafe_allow_html=True)


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
        
        submit_button = st.form_submit_button(label="Découvrir mon match")

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
    st.header("Votre match parfait")

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
        st.write(f"** ge:** {age} ans")
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

