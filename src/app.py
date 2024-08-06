import streamlit as st
import pandas as pd
import joblib

# Cargar los datos de producción agrícola
agri_file_path = '/workspaces/proyectfinaltour/data/processed/unificado/agri.csv'
agri_df = pd.read_csv(agri_file_path, encoding='latin1')

# Cargar los datos meteorológicos
weather_file_path = '/workspaces/proyectfinaltour/data/processed/unificado/weather.csv'
weather_df = pd.read_csv(weather_file_path)

# Normalizar los nombres de las columnas en el dataset agrícola y meteorológico
agri_df.columns = agri_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
weather_df.columns = weather_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Mostrar las columnas del DataFrame para verificación
#st.write("Columnas del DataFrame agrícola:", agri_df.columns)
#st.write("Columnas del DataFrame meteorológico:", weather_df.columns)

# Obtener lista de ciudades y tipos de cultivo
ciudades = agri_df['ciudad'].unique()
cultivos = agri_df['cultivo'].unique()

# Cargar el modelo guardado
best_model_name = joblib.load('/workspaces/proyectfinaltour/src/best_model_name.pkl')
if best_model_name == 'SARIMAX':
    best_model = joblib.load('/workspaces/proyectfinaltour/src/best_model_sarimax.pkl')
elif best_model_name == 'Random Forest':
    best_model = joblib.load('/workspaces/proyectfinaltour/src/best_model_rf.pkl')
else:
    best_model = joblib.load('/workspaces/proyectfinaltour/src/best_model_knn.pkl')

# Definir la interfaz de Streamlit
st.title('Predicción de Producción Agrícola por Hectárea')

# Seleccionar ciudad y tipo de cultivo
ciudad = st.selectbox('Selecciona la ciudad', ciudades)
cultivo = st.selectbox('Selecciona el tipo de cultivo', cultivos)

# Ingresar datos de entrada
tempC = st.number_input('Temperatura (°C)', min_value=-10.0, max_value=50.0, value=25.0)
uvIndex = st.number_input('Índice UV', min_value=0, max_value=11, value=5)
precipMM = st.number_input('Precipitación (mm)', min_value=0.0, max_value=500.0, value=10.0)
sunHour = st.number_input('Horas de Sol', min_value=0.0, max_value=24.0, value=10.0)

# Obtener la superficie en hectáreas para la ciudad y el tipo de cultivo seleccionados
superficie_col_name = 'superficie_ha'  # Actualiza esto con el nombre correcto de la columna después de verificar
superficie_ha = agri_df[(agri_df['ciudad'] == ciudad) & (agri_df['cultivo'] == cultivo)][superficie_col_name].values
if len(superficie_ha) > 0:
    superficie_ha = superficie_ha[0]
else:
    superficie_ha = 1  # Valor por defecto si no se encuentra la superficie

# Predicción
input_data = pd.DataFrame({
    'tempC': [tempC],
    'uvIndex': [uvIndex],
    'precipMM': [precipMM],
    'sunHour': [sunHour]
})

if st.button('Predecir Producción por Hectárea'):
    if best_model_name == 'SARIMAX':
        prediction = best_model.predict(start=0, end=0, exog=input_data)
    else:
        prediction = best_model.predict(input_data)
    
    produccion_por_hectarea = prediction[0] / superficie_ha
    st.write(f'La producción agrícola predicha por hectárea para {cultivo} en {ciudad} es: {produccion_por_hectarea:.2f} toneladas por hectárea')

# Mostrar la producción histórica de la ciudad y el tipo de cultivo seleccionado
produccion_historica = agri_df[(agri_df['ciudad'] == ciudad) & (agri_df['cultivo'] == cultivo)]
weather_historico = weather_df[weather_df['city'] == ciudad]

# Mostrar las columnas del DataFrame meteorológico para verificación
#st.write("Columnas del DataFrame histórico de clima:", weather_historico.columns)

# Calcular las medias históricas de las variables meteorológicas
media_tempC = weather_historico['tempc'].mean()
media_uvIndex = weather_historico['uvindex'].mean()
media_precipMM = weather_historico['precipmm'].mean()
media_sunHour = weather_historico['sunhour'].mean()

st.subheader(f'Producción Histórica de {cultivo} en {ciudad}')
# Eliminar columnas duplicadas al mostrar la producción histórica
produccion_historica = produccion_historica[['año', 'produccion_toneladas', superficie_col_name]].drop_duplicates()
st.write(produccion_historica)

# Mostrar las medias históricas de las variables meteorológicas
st.subheader(f'Medias Históricas de Variables Meteorológicas en {ciudad}')
st.write(f'Temperatura Media: {media_tempC:.2f} °C')
st.write(f'Índice UV Medio: {media_uvIndex:.2f}')
st.write(f'Precipitación Media: {media_precipMM:.2f} mm')
st.write(f'Horas de Sol Medias: {media_sunHour:.2f}')