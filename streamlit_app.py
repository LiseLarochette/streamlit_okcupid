import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Wild Love')

st.write("Découvre ton match idéal")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_weather = pd.read_csv(link)

# Create a button
if st.button('Show Picture'):
    # Display an image when the button is clicked
    st.image('image.jpg', caption='A beautiful picture')

# You can replace 'image.jpg' with the path to your own image file
