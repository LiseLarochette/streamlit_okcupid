import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Wild Love')

st.write("Découvre ton match idéal")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_weather = pd.read_csv(link)

# Create a button
if st.button('C'est parti !'):
    st.write('C'est parti !')

#afficher le graphique de la température maximale
st.line_chart(df_weather['MAX_TEMPERATURE_C'])




import seaborn as sns
df_weather = df_weather.drop(["DATE", "OPINION"], axis=1)

viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

import streamlit as st

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")
