import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado y el scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Cargar el dataset unificado
data = pd.read_csv('data/processed/unificado/dataset_unificado.csv')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Seleccionar la ciudad
ciudad = st.selectbox('Selecciona la ciudad', data['ciudad'].unique())

# Seleccionar el mes y el año
selected_year = st.number_input('Selecciona el año', min_value=2000, max_value=2023, step=1)
selected_month = st.selectbox('Selecciona el mes', range(1, 13))

# Entradas del usuario
temp = st.number_input('Temperatura Media (C°)')
uv_index = st.number_input('Radiación UV')
precip_mm = st.number_input('Precipitación (mm)')
sun_hours = st.number_input('Horas de Sol')

# Filtrar los datos por ciudad, año y mes
filtered_data = data[(data['ciudad'] == ciudad) & 
                     (pd.to_datetime(data['date']).dt.year == selected_year) & 
                     (pd.to_datetime(data['date']).dt.month == selected_month)]

# Preparar los datos para la predicción
input_data = pd.DataFrame([[temp, uv_index, precip_mm, sun_hours]], 
                          columns=['tempC', 'uvIndex', 'precipMM', 'sunHour'])
input_data_scaled = scaler.transform(input_data)

# Realizar la predicción
prediction = model.predict(input_data_scaled)

# Calcular la producción estimada por hectárea
superficie_ha = filtered_data['superficie_ha'].mean()  # Asumiendo que la superficie es constante
produccion_por_ha = prediction[0] / superficie_ha

# Mostrar la predicción
st.write(f'Producción estimada: {prediction[0]:.2f} toneladas')
st.write(f'Producción estimada por hectárea: {produccion_por_ha:.2f} toneladas/ha')

# Mostrar los últimos 5 años de datos históricos para la ciudad seleccionada
historical_data = data[(data['ciudad'] == ciudad) & 
                       (pd.to_datetime(data['date']).dt.year >= (selected_year - 5))]

st.subheader(f'Datos históricos de los últimos 5 años en {ciudad}')
st.write(historical_data[['date', 'tempC', 'uvIndex', 'precipMM', 'sunHour', 'produccion_toneladas']].tail(60))

# Mostrar gráficos de las variables
st.line_chart(historical_data.set_index('date')[['tempC', 'uvIndex', 'precipMM', 'sunHour']])
st.line_chart(historical_data.set_index('date')[['produccion_toneladas']])


