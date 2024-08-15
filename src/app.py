import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# Cargar el modelo entrenado y el scaler
model = joblib.load('src/catboost_model.pkl')
scaler = joblib.load('src/scaler.pkl')

# Cargar el dataset para obtener información sobre las ciudades y cultivos
df = pd.read_csv('data/processed/datasets/combined_dataset.csv')

# Obtener la lista de ciudades únicas, eliminando duplicados
ciudades_disponibles = sorted(df['Ciudad'].unique().tolist())

# Eliminar Málaga de la lista si está presente
if 'Málaga' in ciudades_disponibles:
    ciudades_disponibles.remove('Málaga')

# Añadir las ciudades faltantes si no están ya en la lista
ciudades_faltantes = ['Vigo', 'Oporto', 'Lisboa']
for ciudad in ciudades_faltantes:
    if ciudad not in ciudades_disponibles:
        ciudades_disponibles.append(ciudad)

# Título de la aplicación
st.title('Predicción de Producción Agrícola')

# Entradas del usuario
city = st.selectbox('Selecciona la ciudad', ciudades_disponibles)

# Filtrar los cultivos disponibles según la ciudad seleccionada
cultivos_disponibles = df[df['Ciudad'] == city]['Cultivo'].unique().tolist()
if not cultivos_disponibles:
    cultivos_disponibles = ['Maíz', 'Trigo', 'Olivo', 'Vid']  # Default crops if no data available for the city

crop = st.selectbox('Selecciona el tipo de cultivo', cultivos_disponibles)

month = st.selectbox('Selecciona el mes',
                     ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])

# Nuevas entradas para los valores meteorológicos
temp = st.number_input('Temperatura Media (C°)', value=20.0)
precip_mm = st.number_input('Precipitación (mm)', value=10.0)
uv_index = st.number_input('Índice UV', value=5.0)
sun_hours = st.number_input('Horas de Sol', value=8.0)
hectares = st.number_input('Hectáreas', value=1.0)

# Botón para actualizar los datos
if st.button('Actualizar Predicción'):
    # Procesar las entradas
    input_data = pd.DataFrame([[temp, precip_mm, uv_index, sun_hours]],
                              columns=['tempC', 'precipMM', 'uvIndex', 'sunHour'])
    input_data_scaled = scaler.transform(input_data)

    # Realizar la predicción
    predicted_kilos = model.predict(input_data_scaled)
    predicted_kilos_hectare = (predicted_kilos / hectares) / 1000  # Producción en Kg/ha, dividido entre 1000

    # Mostrar la predicción
    st.write(f'Producción estimada: {predicted_kilos[0] / 1000:.2f} Kg')
    st.write(f'Producción por hectárea: {predicted_kilos_hectare[0]:.2f} Kg/ha')

    # Filtrar el dataset según la ciudad, el cultivo y el mes seleccionados
    month_index = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'].index(month) + 1
    filtered_df = df[(df['Ciudad'] == city) & (df['Cultivo'] == crop) & (df['Mes'] == month_index)]

    # Agrupar por año y calcular la media para las variables seleccionadas
    historical_avg = filtered_df.groupby('year').agg({
        'Ciudad': 'first',
        'Cultivo': 'first',
        'tempC': 'mean',
        'precipMM': 'mean',
        'uvIndex': 'mean',
        'sunHour': 'mean',
        'Kilos': 'sum',
        'Hectáreas': 'sum'
    }).reset_index()

    # Calcular la producción por hectárea
    historical_avg['Producción por Hectárea (Kg/ha)'] = (historical_avg['Kilos'] / historical_avg['Hectáreas']) / 1000

    # Mostrar la tabla histórica
    st.write(f"Historial de Producción por Año para {city} - {crop}")
    st.dataframe(historical_avg)

    # Botón para descargar los resultados
    def convertir_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convertir_csv(historical_avg)

    st.download_button(
        label="Descargar Resultados en CSV",
        data=csv,
        file_name=f'{city}_{crop}_produccion_historica.csv',
        mime='text/csv',
    )



st.markdown("""
### Aplicación en desarrollo constante:
Esta aplicación está en desarrollo constante y seguirá mejorando con el tiempo a medida que se recolecten más datos y se optimice el proceso. La fiabilidad de las predicciones aumentará con la incorporación de nuevos datos y el perfeccionamiento de los modelos.
""")



