import streamlit as st
import pandas as pd
import random

# Charger le dataframe
link = 'https://raw.githubusercontent.com/MaximeBarski/streamlit_okcupid/main/hearthack_final_df.csv'
df = pd.read_csv(link)

# Initialiser l'état de session
if 'page' not in st.session_state:
    st.session_state.page = 'Accueil'

# Extraire les valeurs uniques pour les boîtes de sélection
unique_sex = df['sex'].unique()
unique_body_type = df['body_type'].unique()
unique_status = df['status'].unique()
unique_education = df['education'].unique()
unique_job = df['job'].unique()
unique_diet = df['diet'].unique()
unique_pets = df['pets'].unique()
unique_smokes = df['smokes'].unique()

# Centrer l'image
st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="center"><img src="https://github.com/MaximeBarski/streamlit_okcupid/blob/main/Hackheart_logo.png?raw=true" alt="Hack Heart Logo"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>💖Trouve ton crush pour une nuit ou pour la vie sur le campus !💖 (just for fun)</h2>", unsafe_allow_html=True)

# Fonction pour afficher un titre centré
def centered_title(text):
    st.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{text}</h1>", unsafe_allow_html=True)

# Fonction pour changer de page
def switch_page(page):
    st.session_state.page = page
    st.experimental_rerun()

# Barre de navigation
menu = st.sidebar.selectbox("Menu", ["Accueil", "Mon Profil"], index=["Accueil", "Mon Profil"].index(st.session_state.page))

# État de session utilisateur pour stocker les données du formulaire
if "user_info" not in st.session_state:
    st.session_state.user_info = {}

# Contenu de chaque page
if menu == "Accueil" or st.session_state.page == "Accueil":
    st.session_state.page = "Accueil"
    st.markdown("""
    Bienvenue sur notre application de rencontre ! Clique sur le bouton ci-dessous pour renseigner tes informations et découvrir ton match parfait.
    """)

    # Centrer le bouton "C'est parti"
    if st.button("C'est parti !"):
        switch_page("Mon Profil")

elif menu == "Mon Profil" or st.session_state.page == "Mon Profil":
    st.session_state.page = "Mon Profil"
    centered_title("Mon Profil")

    # Formulaire d'informations utilisateur
    with st.form(key='user_info'):
        name = st.text_input("Nom")
        age = st.number_input("Âge", min_value=18, max_value=100, step=1)
        sex = st.selectbox("Sexe", unique_sex)
        height = st.number_input("Taille (cm)", min_value=100, max_value=250, step=1)
        body_type = st.selectbox("Type de corpulence", unique_body_type)
        status = st.selectbox("Situation amoureuse", unique_status)
        education = st.selectbox("Éducation", unique_education)
        job = st.selectbox("Profession", unique_job)
        diet = st.selectbox("Régime alimentaire", unique_diet)
        pets = st.selectbox("Animaux de compagnie", unique_pets)
        smokes = st.selectbox("Fume", unique_smokes)
        question_1 = st.text_area("Je pourrais probablement te battre à :")
        question_2 = st.text_area("Ma règle d’or :")
        question_3 = st.text_area("La chose la plus intime que je suis disposée à admettre :")
        
        submit_button = st.form_submit_button(label="Découvrir mon match")

    if submit_button:
        # Stocker les informations de l'utilisateur dans l'état de session
        st.session_state.user_info = {
            "name": name,
            "age": age,
            "sex": sex,
            "height": height,
            "body_type": body_type,
            "status": status,
            "education": education,
            "job": job,
            "diet": diet,
            "pets": pets,
            "smokes": smokes,
            "question_1": question_1,
            "question_2": question_2,
            "question_3": question_3,
        }

        st.write(f"**Nom:** {name}")
        st.write(f"**Âge:** {age} ans")
        st.write(f"**Sexe:** {sex}")
        st.write(f"**Taille:** {height} cm")
        st.write(f"**Type de corpulence:** {body_type}")
        st.write(f"**Situation amoureuse:** {status}")
        st.write(f"**Éducation:** {education}")
        st.write(f"**Profession:** {job}")
        st.write(f"**Régime alimentaire:** {diet}")
        st.write(f"**Animaux de compagnie:** {pets}")
        st.write(f"**Fume:** {smokes}")
        st.write(f"**Je pourrais probablement te battre à :** {question_1}")
        st.write(f"**Ma règle d’or :** {question_2}")
        st.write(f"**La chose la plus intime que je suis disposée à admettre :** {question_3}")

        # Bouton pour générer le match idéal
        if st.button("💘 Découvrir mon match idéal 💘"):
            # Filtrer les profils correspondant aux préférences de l'utilisateur
            matches = df[
                (df['sex'] == sex) &
                (df['body_type'] == body_type) &
                (df['status'] == status) &
                (df['education'] == education) &
                (df['job'] == job) &
                (df['diet'] == diet) &
                (df['pets'] == pets) &
                (df['smokes'] == smokes)
            ]

            if not matches.empty:
                match = matches.sample(1).iloc[0]
                st.success(f"Félicitations ! Vous avez un match parfait avec {match['name']}!")
                if 'image' in match and match["image"]:
                    st.image(match["image"], caption=f"{match['name']}, {match['age']} ans", width=200)
                st.write(f"**{match['name']}**, {match['age']} ans")
                st.write(f"Intérêts : {match['interests']}")
            else:
                st.error("Aucun utilisateur correspondant à vos critères n'a été trouvé.")

# Styles personnalisés
st.markdown("""
    <style>
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            display: block;
            margin: 0 auto;
        }
        .stSuccess {
            font-size: 1.2em;
        }
    </style>
""", unsafe_allow_html=True)


