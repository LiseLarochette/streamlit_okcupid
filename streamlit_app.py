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

