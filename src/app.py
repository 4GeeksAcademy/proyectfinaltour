import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Cargar el modelo entrenado y el scaler
model = joblib.load('xgboost_model.pkl')
scaler = joblib.load('scaler.pkl')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Entradas del usuario
city = st.selectbox('Selecciona la ciudad', ['Madrid', 'Barcelona', 'Valencia'])
month = st.selectbox('Selecciona el mes', 
                     ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
temp = st.number_input('Temperatura Media (C°)')
precip_mm = st.number_input('Precipitación (mm)')
uv_index = st.number_input('Índice UV')
sun_hours = st.number_input('Horas de Sol')

# Procesar las entradas
input_data = pd.DataFrame([[temp, precip_mm, uv_index, sun_hours]], 
                          columns=['tempC', 'precipMM', 'uvIndex', 'sunHour'])
input_data_scaled = scaler.transform(input_data)

# Realizar la predicción
prediction = model.predict(input_data_scaled)

# Mostrar la predicción
st.write(f'Producción estimada: {prediction[0]:.2f} Kilos')

