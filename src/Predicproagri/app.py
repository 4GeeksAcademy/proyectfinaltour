import streamlit as st
import pandas as pd
import joblib
import datetime

# Cargar el modelo y el scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Cargar el dataset con el historial
data = pd.read_csv('ruta/a/tu/dataset.csv')

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
mean_values = filtered_data[['tempC', 'uvIndex', 'precipMM', 'sunHour']].mean()
st.subheader('Medias de las variables climáticas')
st.write(mean_values)

# Entradas del usuario para predicción
temp = st.number_input('Temperatura (C°)', value=mean_values['tempC'])
uv_index = st.number_input('Índice UV', value=mean_values['uvIndex'])
precip_mm = st.number_input('Precipitación (mm)', value=mean_values['precipMM'])
sun_hours = st.number_input('Horas de Sol', value=mean_values['sunHour'])

# Preparar los datos para la predicción
input_data = pd.DataFrame([[temp, uv_index, precip_mm, sun_hours]], 
                          columns=['tempC', 'uvIndex', 'precipMM', 'sunHour'])

# Agregar características adicionales si fueron utilizadas en el entrenamiento del modelo
input_data['tempc_squared'] = input_data['tempC'] ** 2
input_data['precipmm_log'] = np.log1p(input_data['precipMM'])

# Escalar los datos
input_data_scaled = scaler.transform(input_data)

# Realizar la predicción
prediction = model.predict(input_data_scaled)

# Mostrar la predicción
st.subheader('Predicción de Producción Agrícola')
st.write(f'Producción estimada: {prediction[0]:.2f} toneladas')
