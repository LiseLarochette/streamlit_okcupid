import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Wild Love')

st.write("Découvre ton match idéal")





import tkinter as tk
import random

# Liste des utilisateurs fictifs
users = [
    "Alice", "Bob", "Charlie", "Diana", "Eve", 
    "Frank", "Grace", "Hannah", "Ivy", "Jack"
]

# Fonction pour générer un match aléatoire
def generate_match():
    match = random.choice(users)
    match_label.config(text=f"Vous avez un match avec {match}!")

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Application de Rencontre")

# Configuration de la taille de la fenêtre
root.geometry("400x300")

# Titre de l'application
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



