import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Cargar el modelo entrenado y el scaler
model = joblib.load('/workspaces/proyectfinaltour/src/xgboost_model.pkl')
scaler = joblib.load('/workspaces/proyectfinaltour/src/scaler.pkl')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Entradas del usuario
ciudad = st.selectbox('Selecciona la ciudad', ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao'])
cultivo = st.selectbox('Selecciona el cultivo', ['Maíz', 'Trigo', 'Olivo', 'Girasol'])
mes = st.selectbox('Selecciona el mes', 
                   ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
temp = st.number_input('Temperatura Media (C°)')
precip_mm = st.number_input('Precipitación (mm)')
uv_index = st.number_input('Índice UV')
sun_hours = st.number_input('Horas de Sol')
hectareas = st.number_input('Número de Hectáreas', min_value=1)

# Procesar las entradas
input_data = pd.DataFrame([[temp, precip_mm, uv_index, sun_hours]], 
                          columns=['tempC', 'precipMM', 'uvIndex', 'sunHour'])
input_data_scaled = scaler.transform(input_data)

# Realizar la predicción de producción por hectárea
produccion_por_hectarea = model.predict(input_data_scaled) / 1000  # Dividir entre 1000 para convertir a kilogramos

# Calcular la producción total
produccion_total = produccion_por_hectarea[0] * hectareas

# Mostrar las predicciones
st.write(f'Producción estimada total: {produccion_total:.2f} Kilogramos')
st.write(f'Producción estimada por hectárea: {produccion_por_hectarea[0]:.2f} Kilogramos por Hectárea')

# Filtrar datos históricos para la tabla
df = pd.read_csv('/workspaces/proyectfinaltour/data/processed/datasets/combined_dataset.csv')
df_filtrado = df[(df['Ciudad'] == ciudad) & (df['Cultivo'] == cultivo)].groupby('year').mean()

# Eliminar la columna de producción por hectárea si existe
df_filtrado = df_filtrado.drop(columns=['produccion_por_hectarea'], errors='ignore')

# Mostrar la tabla histórica
st.write('Datos históricos de producción:')
st.dataframe(df_filtrado)
