import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")# leer los datos

# Encabezado de la aplicación
st.header('Aplicación de Análisis de Vehículos')

# Botón para construir un histograma
hist_button = st.button('Construir Histograma')

if hist_button:
    st.write('Histograma anuncios de venta de coches')
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir Gráfico de Dispersión')

if scatter_button:
    st.write('Gráfico de dispersión para los anuncios de venta de coches')
    # Crear un gráfico de dispersión utilizando "model_year" en lugar de "year"
    fig_scatter = px.scatter(car_data, x="model_year", y="price")
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

# Botón para construir un gráfico de barras
bar_chart_button = st.button('Gráfico de Barras (Combustible)')

if bar_chart_button:
    st.write('Grafico de barras para la distribución de tipos de combustible')
    # Crear un gráfico de barras
    fig_bar = px.bar(car_data, x="fuel", title="Distribución de Tipos de Combustible")
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_bar, use_container_width=True)

# Botón para construir un gráfico de pastel
pie_chart_button = st.button('Construir Gráfico de Pastel (Tracción a las Cuatro Ruedas)')

if pie_chart_button:
    st.write('Gráfico de pastel de vehículos con tracción a las cuatro ruedas')
    # Crear un gráfico de pastel sin mapear valores
    fig_pie = px.pie(car_data, names="is_4wd", title="Proporción de Vehículos con Tracción a las Cuatro Ruedas", color_discrete_sequence=px.colors.qualitative.Set3)
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_pie, use_container_width=True)
