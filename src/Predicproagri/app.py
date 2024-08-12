import streamlit as st
import pandas as pd
import joblib
import datetime
import numpy as np

# Cargar el modelo y el scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Cargar el dataset con el historial
# Especificar el encoding para evitar errores de decodificación
data = pd.read_csv('/workspaces/proyectfinaltour/data/processed/unificado/agri.csv', encoding='latin1')

# Verificar los nombres de las columnas
st.write("Columnas disponibles en el dataset:", data.columns)

# Asegurarse de que los nombres de las columnas están en minúsculas
data.columns = data.columns.str.lower()

# Verificar si las columnas 'year' y 'month' existen, si no, crearlas
if 'year' not in data.columns:
    data['year'] = pd.DatetimeIndex(data['date']).year
if 'month' not in data.columns:
    data['month'] = pd.DatetimeIndex(data['date']).month

# Selector de mes usando un calendario
selected_date = st.date_input('Selecciona el mes y año', value=datetime.date.today())
selected_month = selected_date.month
selected_year = selected_date.year

# Desplegable para seleccionar la ciudad
ciudad = st.selectbox('Selecciona la ciudad', data['ciudad'].unique())

# Filtrar datos según la ciudad y el mes seleccionados
filtered_data = data[(data['ciudad'] == ciudad) & (data['year'] == selected_year) & (data['month'] == selected_month)]

# Mostrar los datos históricos del cultivo seleccionado
st.subheader(f'Datos históricos de {ciudad} para {selected_year}-{selected_month}')
st.write(filtered_data)

# Calcular y mostrar las medias de las variables climáticas
mean_values = filtered_data[['tempc', 'uvindex', 'precipmm', 'sunhour']].mean()
st.subheader('Medias de las variables climáticas')
st.write(mean_values)

# Entradas del usuario para predicción
temp = st.number_input('Temperatura (C°)', value=mean_values['tempc'])
uv_index = st.number_input('Índice UV', value=mean_values['uvindex'])
precip_mm = st.number_input('Precipitación (mm)', value=mean_values['precipmm'])
sun_hours = st.number_input('Horas de Sol', value=mean_values['sunhour'])

# Preparar los datos para la predicción
input_data = pd.DataFrame([[temp, uv_index, precip_mm, sun_hours]], 
                          columns=['tempc', 'uvindex', 'precipmm', 'sunhour'])

# Agregar características adicionales si fueron utilizadas en el entrenamiento del modelo
input_data['tempc_squared'] = input_data['tempc'] ** 2
input_data['precipmm_log'] = np.log1p(input_data['precipmm'])

# Escalar los datos
input_data_scaled = scaler.transform(input_data)

# Realizar la predicción
prediction = model.predict(input_data_scaled)

# Calcular la producción estimada por hectárea
superficie_ha = filtered_data['superficie_ha'].mean()  # Promedio de superficie en hectáreas
produccion_por_hectarea = prediction[0] / superficie_ha if superficie_ha > 0 else 0

# Mostrar la predicción
st.subheader('Predicción de Producción Agrícola')
st.write(f'Producción estimada: {prediction[0]:.2f} toneladas')
st.write(f'Producción estimada por hectárea: {produccion_por_hectarea:.2f} toneladas por hectárea')

