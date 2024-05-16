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


