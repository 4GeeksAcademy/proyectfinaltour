import streamlit as st
import pandas as pd
import numpy as np
import joblib
import calendar

# Cargar el modelo entrenado y el scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Cargar el dataset unificado desde la ruta proporcionada
data = pd.read_csv('/workspaces/proyectfinaltour/data/processed/unificado/dataset_unificado.csv')

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Diccionario para traducir los nombres de los meses al español
meses_es = {
    'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo', 'April': 'Abril',
    'May': 'Mayo', 'June': 'Junio', 'July': 'Julio', 'August': 'Agosto',
    'September': 'Septiembre', 'October': 'Octubre', 'November': 'Noviembre', 'December': 'Diciembre'
}

# Seleccionar la ciudad
ciudad = st.selectbox('Selecciona la ciudad', data['ciudad'].unique())

# Seleccionar el cultivo
cultivo_opciones = ['Todos'] + list(data['cultivo'].unique())
cultivo_seleccionado = st.selectbox('Selecciona el cultivo', cultivo_opciones)

# Seleccionar el mes por nombre en español
selected_month_name_es = st.selectbox('Selecciona el mes', list(meses_es.values()))
# Obtener el nombre del mes en inglés para el procesamiento
selected_month_name = [k for k, v in meses_es.items() if v == selected_month_name_es][0]
selected_month = list(calendar.month_name).index(selected_month_name)

# Entradas del usuario para datos climáticos
temp = st.number_input('Temperatura Media (C°)')
uv_index = st.number_input('Radiación UV')
precip_mm = st.number_input('Precipitación (mm)')
sun_hours = st.number_input('Horas de Sol')

# Botón para confirmar los cambios y realizar la predicción
if st.button('Predecir Producción'):
    # Calcular las características adicionales necesarias para el modelo
    tempc_squared = temp ** 2
    precipmm_log = np.log1p(precip_mm)  # log(1 + precip_mm)

    # Preparar los datos para la predicción
    input_data = pd.DataFrame([[temp, uv_index, precip_mm, sun_hours, tempc_squared, precipmm_log]], 
                              columns=['tempC', 'uvIndex', 'precipMM', 'sunHour', 'tempc_squared', 'precipmm_log'])
    input_data_scaled = scaler.transform(input_data)

    # Realizar la predicción
    prediction = model.predict(input_data_scaled)

    # Filtrar los datos para obtener la superficie promedio en hectáreas
    filtered_data = data[(data['ciudad'] == ciudad) & 
                         (pd.to_datetime(data['date']).dt.month == selected_month)]

    if cultivo_seleccionado != 'Todos':
        filtered_data = filtered_data[filtered_data['cultivo'] == cultivo_seleccionado]

    if not filtered_data.empty:
        superficie_ha = filtered_data['superficie_ha'].mean()  # Asumiendo que la superficie es constante
        produccion_por_ha = prediction[0] / superficie_ha if superficie_ha > 0 else 0

        # Mostrar la predicción
        st.subheader('Resultados de la Predicción:')
        st.write(f'Producción estimada: **{prediction[0]:.2f} toneladas**')
        st.write(f'Producción estimada por hectárea: **{produccion_por_ha:.2f} toneladas/ha**')
    else:
        st.write("No se encontraron datos para el cultivo seleccionado en esta ciudad y mes.")
