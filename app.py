import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("Histograma con Plotly")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
fig = px.histogram(car_data, x="odometer")  # crear un histograma

# Mostrar en Streamlit
st.plotly_chart(fig)
