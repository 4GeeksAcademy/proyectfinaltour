# Predicción de Producción Agrícola

## Introducción

Este proyecto tiene como objetivo predecir la producción agrícola futura utilizando variables meteorológicas. La predicción se basa en datos históricos de producción agrícola y condiciones climáticas. La aplicación web permite a los usuarios seleccionar una ciudad y un tipo de cultivo para ver las predicciones de producción por hectárea.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes herramientas y bibliotecas:

- Python 3.7+
- Pandas
- Numpy
- Scikit-learn
- Statsmodels
- Joblib
- Streamlit
- Heroku CLI (si planeas desplegar en Heroku)

## Instalación

Sigue estos pasos para configurar el entorno y las dependencias necesarias:

1. Clona el repositorio del proyecto:
   ```bash
   git clone <URL_del_repositorio>
   cd proyectfinaltour/src

## Descripción del Proyecto
Carga de Datos
Se utilizan dos conjuntos de datos: uno de producción agrícola y otro de datos meteorológicos. Los datos se combinan y procesan para obtener medias mensuales de variables climáticas como temperatura, índice UV, precipitación y horas de sol.

## Análisis Descriptivo
Se realizó un análisis descriptivo para entender mejor las relaciones entre las variables climáticas y la producción agrícola. Esto incluyó cálculos de medias, desviaciones y visualizaciones.

## Modelado
Se probaron tres modelos diferentes: SARIMAX, Random Forest y KNN. Los modelos se entrenaron utilizando los datos históricos y se evaluaron mediante la métrica RMSE.

## Optimización
Se realizó una búsqueda de hiperparámetros para encontrar la mejor configuración para cada modelo. El modelo con el mejor rendimiento se seleccionó y guardó para su uso en la aplicación web.

## Despliegue
Se creó una aplicación web utilizando Streamlit que permite a los usuarios seleccionar una ciudad y un tipo de cultivo, ingresar datos meteorológicos y obtener predicciones de producción por hectárea.

## Obtención de datos
Los datos se obtuvieron de diferentes webs:
-

## Contribución
Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
Empuja tus cambios a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
- ¡Gracias por tu contribución!