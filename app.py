import pandas as pd
import streamlit as st
import plotly.express as px
import os

car_data = pd.read_csv("vehicles_us.csv")# leer los datos

# Encabezado de la aplicación
st.header('Aplicación de Análisis de Vehículos')

# Botón para construir un histograma
hist_button = st.button('Construir Histograma')

if hist_button:
    st.write('Construcción de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir Gráfico de Dispersión')

if scatter_button:
    st.write('Construcción de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="year", y="price")
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
