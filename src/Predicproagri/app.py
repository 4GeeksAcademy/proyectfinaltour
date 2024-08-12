import joblib
import pandas as pd
import numpy as np
import streamlit as st

# Cargar el modelo y el escalador
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Entradas del usuario
temp = st.number_input('Temperatura (C°)')
uv_index = st.number_input('Índice UV')
precip_mm = st.number_input('Precipitación (mm)')
sun_hours = st.number_input('Horas de Sol')

# Preparar las características adicionales necesarias para el escalador
tempc_squared = temp ** 2
precipmm_log = np.log1p(precip_mm)  # Logaritmo natural de 1 + precipitación

# Crear el DataFrame de entrada con todas las características esperadas
input_data = pd.DataFrame([[temp, uv_index, precip_mm, sun_hours, tempc_squared, precipmm_log]], 
                          columns=['tempC', 'uvIndex', 'precipMM', 'sunHour', 'tempc_squared', 'precipmm_log'])

# Escalar los datos de entrada utilizando el scaler previamente ajustado
input_data_scaled = scaler.transform(input_data)

# Realizar la predicción
prediction = model.predict(input_data_scaled)

# Mostrar la predicción
st.write(f'Producción estimada: {prediction[0]} toneladas')