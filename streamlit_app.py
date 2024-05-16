import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Wild Love')

st.write("Découvre ton match idéal")

import turtle

# Initialiser la fenêtre
window = turtle.Screen()
window.title("Dessiner un Coeur")
window.bgcolor("white")

# Créer une instance de turtle
pen = turtle.Turtle()
pen.color("red")
pen.speed(3)

# Définir une fonction pour dessiner un coeur
def draw_heart():
    pen.begin_fill()

    # Commencer à dessiner le coeur
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)

    pen.end_fill()

# Appeler la fonction pour dessiner le coeur
draw_heart()

# Cacher la turtle et terminer
pen.hideturtle()

# Garder la fenêtre ouverte
window.mainloop()





