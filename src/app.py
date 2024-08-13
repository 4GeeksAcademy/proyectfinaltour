import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Cargar el dataset para obtener las ciudades y cultivos únicos
df = pd.read_csv('/workspaces/proyectfinaltour/data/processed/datasets/combined_dataset.csv')
ciudades_disponibles = df['Ciudad'].unique().tolist()
cultivos_disponibles = df['Cultivo'].unique().tolist()

# Cargar el modelo entrenado y el scaler
model = joblib.load('/workspaces/proyectfinaltour/src/xgboost_model.pkl')
scaler = joblib.load('/workspaces/proyectfinaltour/src/scaler.pkl')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Entradas del usuario
city = st.selectbox('Selecciona la ciudad', ciudades_disponibles)
cultivo = st.selectbox('Selecciona el tipo de cultivo', cultivos_disponibles)
month = st.selectbox('Selecciona el mes', 
                     ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
temp = st.number_input('Temperatura Media (C°)')
precip_mm = st.number_input('Precipitación (mm)')
uv_index = st.number_input('Índice UV')
sun_hours = st.number_input('Horas de Sol')
hectareas = st.number_input('Superficie Cultivada (hectáreas)', value=1.0, min_value=0.1, step=0.1)

# Convertir el mes seleccionado a número (Enero = 1, Febrero = 2, etc.)
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
mes_numero = meses.index(month) + 1

# Procesar las entradas
input_data = pd.DataFrame([[temp, precip_mm, uv_index, sun_hours]], 
                          columns=['tempC', 'precipMM', 'uvIndex', 'sunHour'])
input_data_scaled = scaler.transform(input_data)

# Realizar la predicción de kilos por hectárea
kilos_por_hectarea = model.predict(input_data_scaled)[0]

# Calcular la producción total en función de las hectáreas
kilos_totales = kilos_por_hectarea * hectareas

# Mostrar las predicciones
st.write(f'Producción estimada por hectárea: {kilos_por_hectarea:.2f} Kilos por hectárea')
st.write(f'Producción total estimada: {kilos_totales:.2f} Kilos')

# Filtrar los datos históricos de la ciudad y el cultivo seleccionados
historial_df = df[(df['Ciudad'] == city) & (df['Cultivo'] == cultivo)]

# Calcular los datos medios por año
historial_medio_df = historial_df.groupby('year').agg({
    'Kilos': 'mean',
    'Hectáreas': 'mean',
    'tempC': 'mean',
    'precipMM': 'mean',
    'uvIndex': 'mean',
    'sunHour': 'mean'
}).reset_index()

# Mostrar la tabla de datos medios por año
st.write(f"### Datos Medios por Año para {cultivo} en {city}")
st.dataframe(historial_medio_df)
