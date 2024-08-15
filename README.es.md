# README - Predicción de Producción Agrícola

## Introducción

Este proyecto tiene como objetivo predecir la producción agrícola en diferentes ciudades utilizando técnicas avanzadas de Machine Learning. El proyecto aborda el problema de la predicción de la producción agrícola, un aspecto crítico para la planificación y gestión de recursos en la agricultura.

## Metodología y Procesos

### 1. Recolección y Procesamiento de Datos

- **Fuentes de Datos**: Se recopilaron datos meteorológicos y de producción agrícola de diversas fuentes.
- **Limpieza de Datos**: Los datos fueron limpiados para eliminar valores atípicos y faltantes.
- **Procesamiento de Datos**: Se unificaron y escalaron las variables relevantes para el modelado, incluyendo temperatura, precipitación, índice UV y horas de sol.

### 2. Modelos de Machine Learning

- **Modelos Utilizados**:
  - **CatBoost**: Elegido por su capacidad para manejar variables categóricas sin necesidad de preprocesamiento adicional.
  - **LightGBM**: Utilizado por su eficiencia y velocidad en el entrenamiento, especialmente con grandes volúmenes de datos.
  - **XGBoost**: Incluido debido a su robustez y capacidad de generalización en problemas complejos.
  - **Random Forest**: Modelo de ensamble que combina múltiples árboles de decisión para mejorar la precisión y reducir el sobreajuste.
  - **K-Nearest Neighbors (KNN)**: Utilizado como un enfoque basado en vecinos más cercanos, simple pero efectivo en ciertos escenarios.

- **Técnicas de Optimización**:
  - **Hiperparametrización Avanzada**: Se utilizó GridSearchCV y RandomizedSearchCV para ajustar los hiperparámetros de cada modelo, mejorando así su rendimiento.
  - **Validación Cruzada**: Se aplicó validación cruzada para asegurar la robustez de los modelos y evitar el sobreajuste.

- **Evaluación del Rendimiento**:
  - **Métrica Principal**: RMSE (Root Mean Square Error) se utilizó para evaluar el rendimiento de cada modelo.
  - **Resultados**:
    - **CatBoost RMSE**: `436341.78`
    - **LightGBM RMSE**: `443428.97`
    - **XGBoost RMSE**: `449094.98`
    - **Random Forest RMSE**: `485829.70`
    - **KNN RMSE**: `466165.99`

### 3. Análisis de Sensibilidad

- **Impacto de las Variables**: Se realizó un análisis de sensibilidad para identificar las variables meteorológicas más influyentes en la producción agrícola. Este análisis permitió ajustar y priorizar las características más relevantes en el modelado.

## Desarrollo de la Aplicación Web

- **Implementación con Streamlit**:
  - La aplicación fue desarrollada utilizando Streamlit, proporcionando una interfaz amigable para que los usuarios seleccionen la ciudad, el cultivo y otros parámetros.
  - **Funcionalidades**:
    - **Predicción en Tiempo Real**: La aplicación permite a los usuarios ingresar datos meteorológicos y obtener predicciones inmediatas sobre la producción agrícola.
    - **Visualización de Resultados**: Se integraron gráficos para mostrar la predicción de producción agrícola y la comparación con datos históricos.
    - **Descarga de Resultados**: Se incluyó la opción de descargar los resultados en formato CSV.
  
- **Mensaje Final**: Al final de la aplicación, se añadió un mensaje que indica que la aplicación está en desarrollo constante y que se espera una mejora en la fiabilidad a medida que se recolecten más datos.

## Despliegue en la Nube

- **Plataforma**: La aplicación fue desplegada en Render, asegurando su accesibilidad en la web.
- **Configuración y Despliegue**:
  - Se configuró el entorno de desarrollo y producción en Render.
  - Se incluyó la instalación de dependencias y la ejecución automática de la aplicación tras el despliegue.
  - **Archivos Clave**: `requirements.txt` para las dependencias y `app.py` para la aplicación principal.

- **Escalabilidad y Rendimiento**:
  - Se consideraron aspectos de escalabilidad y rendimiento, con planes para ajustar la infraestructura en función de la carga de usuarios.

## Conclusiones y Aprendizajes

- **Resultados Obtenidos**:
  - Se logró desarrollar un modelo de predicción agrícola efectivo, con CatBoost mostrando el mejor rendimiento en términos de RMSE.
  - La implementación en Streamlit permite una fácil interacción y visualización de resultados por parte de los usuarios.

- **Lecciones Aprendidas**:
  - La importancia de la hiperparametrización y la validación cruzada en la mejora del rendimiento de los modelos.
  - La necesidad de un procesamiento de datos robusto para asegurar la calidad de las predicciones.

- **Próximos Pasos**:
  - Recolectar más datos para mejorar la precisión de las predicciones.
  - Explorar la integración de datos en tiempo real para hacer predicciones más dinámicas.

### Datos Obtenidos de :

- KAGGLE.COM : https://www.kaggle.com/datasets/luisvivas/spain-portugal-weather
- Instituto Nacional de Estadística (INE), (INE Portugal).
- Ministerio de Agricultura, Pesca y Alimentación (MAPA).
- SIMA (Sistema de Información sobre Mercados Agrarios.
- Dirección General de Agricultura y Desarrollo Rural (DGADR).


url: https://produccion-agricola.onrender.com/