import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Wild Love') 
import streamlit as st
import numpy as np

# Create a canvas to draw the heart shape
canvas = st.empty()
canvas_width = 200
canvas_height = 200

# Draw the heart shape using a set of points
with canvas:
    ctx = canvas.drawable_canvas(
        width=canvas_width,
        height=canvas_height,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Draw the heart shape using lines
    ctx.line_width = 2
    ctx.line_join = "round"

    ctx.begin_path()
    ctx.move_to(100, 80)
    ctx.quadratic_curve_to(30, 30, 60, 10)
    ctx.quadratic_curve_to(90, 30, 100, 80)
    ctx.stroke()

    ctx.begin_path()
    ctx.move_to(100, 80)
    ctx.quadratic_curve_to(170, 30, 140, 10)
    ctx.quadratic_curve_to(110, 30, 100, 80)
    ctx.stroke()
    


st.write("Découvre ton match idéal")

# Description
st.write("""
Bienvenue sur notre application de rencontre. Cliquez sur le bouton ci-dessous pour découvrir votre match parfait !
""")

# Bouton pour générer un match
if st.button("Trouver un match"):
    match = random.choice(users)
    st.success(f"Félicitations ! Vous avez un match parfait avec {match}!")

# Afficher les images des utilisateurs (optionnel)
# Créer un dictionnaire d'images fictives (les images doivent être dans le même répertoire que le script)
images = {
    "Alice": "alice.png",
    "Bob": "bob.png",
    "Charlie": "charlie.png",
    "Diana": "diana.png",
    "Eve": "eve.png",
    "Frank": "frank.png",
    "Grace": "grace.png",
    "Hannah": "hannah.png",
    "Ivy": "ivy.png",
    "Jack": "jack.png"
}

# Afficher les images des utilisateurs (optionnel)
for user in users:
    st.image(images.get(user, "default.png"), caption=user, use_column_width=True)
title_label = tk.Label(root, text="Bienvenue sur l'application de rencontre", font=("Helvetica", 16))
title_label.pack(pady=20)

# Bouton pour générer un match
match_button = tk.Button(root, text="Trouver un match", command=generate_match, font=("Helvetica", 14))
match_button.pack(pady=20)

# Label pour afficher le match
match_label = tk.Label(root, text="", font=("Helvetica", 14), fg="green")
match_label.pack(pady=20)

# Lancer la boucle principale de l'interface
root.mainloop()



