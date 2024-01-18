# Sprint-5-proyecto

# Proyecto de Análisis de Vehículos

Este proyecto Render para crear una aplicación web interactiva que analiza y visualiza datos relacionados con anuncios de venta de vehículos. La aplicación proporciona gráficos interactivos que permiten explorar características como el odómetro, el año del modelo, el precio y más.

## Instrucciones de Ejecución

1. Clona este repositorio a tu máquina local.
2. Instala las dependencias utilizando `pip install -r requirements.txt`.
3. Ejecuta la aplicación utilizando `streamlit run app.py`.

## Contenido del Proyecto

- `app.py`: Archivo principal que contiene el código de la aplicación web.
- `vehicles_us.csv`: Conjunto de datos utilizado para el análisis.

## Desarrollo del Cuadro de Mandos

El cuadro de mandos de la aplicación incluye:

- **Histograma de Odómetro:**  Muestra la distribución del odómetro de los vehículos.
- **Gráfico de Dispersión:**  Representa el precio en función del año del modelo.
- **Gráfico de Barras (Combustible):**  Visualiza la distribución de tipos de combustible.
- **Gráfico de Pastel (Tracción a las Cuatro Ruedas):**  Muestra la proporción de vehículos con y sin tracción a las cuatro ruedas.
- 1 = Tracción en las 4 ruedas 


## Notas a Considerar

- Asegúrate de tener instalado Streamlit, Pandas y Plotly-express antes de ejecutar la aplicación (`Ejemplo para instalación pip install streamlit`).

