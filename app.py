import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("Visualización de Datos de Vehículos")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
histogram = px.histogram(car_data, x="odometer")  # crear un histograma
# crear un gráfico de dispersión
dispersion = px.scatter(car_data, x="odometer", y="price")
# Mostrar en Streamlit
st.title("Histograma de Odómetro")
st.plotly_chart(histogram)
st.title("Dispersion de Precio vs Odómetro")
st.plotly_chart(dispersion)
