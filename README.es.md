# Análisis Exploratorio de Datos (EDA)

Este análisis exploratorio de datos (EDA) se realiza en un dataset de condiciones climáticas con datos agrupados por diferentes ciudades. A continuación se describen los pasos seguidos en el EDA:

1. **Cargar y visualizar el dataset:**
   - Se carga el dataset desde un archivo CSV y se muestran las primeras filas del dataset.

2. **Conversión de tipos de datos:**
   - Se convierte la columna `date_time` a formato datetime.

3. **Inspección inicial:**
   - Se revisa la estructura del dataset, incluyendo tipos de datos y presencia de valores faltantes. Se genera un resumen estadístico básico del dataset.

4. **Generar estadísticas descriptivas por ciudad:**
   - Se agrupan los datos por ciudad y se calculan estadísticas descriptivas para cada grupo.

5. **Visualización de la distribución de los datos:**
   - Se generan histogramas de las temperaturas máximas y mínimas para cada ciudad.

6. **Mapas de Calor de Correlación:**
   - Se crean mapas de calor de correlación para las variables numéricas de cada ciudad.

7. **Detección de valores atípicos (anomalías):**
   - Se calculan valores intercuartílicos (IQR) para detectar y visualizar valores atípicos en las variables numéricas.

8. **Resumen general de las estadísticas descriptivas por ciudad:**
   - Se genera un resumen general de las estadísticas descriptivas para todas las ciudades y se guarda en un archivo CSV.

### Comparación con los cultivos del año


