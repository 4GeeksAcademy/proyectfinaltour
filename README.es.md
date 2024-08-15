# Proyecto de Predicción de Producción Agrícola

## Introducción

Este proyecto se centra en predecir la producción agrícola utilizando modelos de aprendizaje automático. El objetivo es proporcionar a los agricultores y partes interesadas del sector agrícola información sobre los rendimientos esperados de los cultivos en función de varios factores meteorológicos. El proyecto aborda la necesidad de pronósticos precisos en la producción agrícola para optimizar recursos, reducir desperdicios y mejorar la toma de decisiones en el sector agrícola.

## Metodología y Procesos

### Flujo de Trabajo General

El proyecto sigue un flujo de trabajo estructurado:

1. **Recopilación y Preprocesamiento de Datos**: Recolección y limpieza de datos meteorológicos y agrícolas.
2. **Selección y Entrenamiento del Modelo**: Implementación y ajuste de modelos de aprendizaje automático.
3. **Evaluación del Modelo**: Validación del rendimiento del modelo utilizando métricas como RMSE.
4. **Desarrollo de la Aplicación Web**: Creación de una interfaz interactiva para que los usuarios ingresen datos y reciban predicciones.
5. **Despliegue**: Despliegue de la aplicación en la nube para accesibilidad.

### Explicación de los Datos

- **Fuentes**: Datos meteorológicos (e.g., temperatura, precipitación) y datos de rendimiento agrícola.
- **Limpieza y Procesamiento**: Manejo de valores faltantes, normalización de características y división de los datos en conjuntos de entrenamiento y prueba.

### Modelos de Machine Learning

- **CatBoost y LightGBM**: Seleccionados por su rendimiento con datos tabulares y capacidad para manejar variables categóricas.
- **Optimización**: Ajuste de hiperparámetros utilizando GridSearchCV y RandomizedSearchCV.

### Validación y Evaluación del Rendimiento

- **Validación Cruzada**: Para asegurar la robustez, se realizó validación cruzada y se calculó RMSE para evaluar la precisión del modelo.
- **Análisis de Sensibilidad**: Identificación de las variables más impactantes en las predicciones de rendimiento agrícola.

## Desarrollo de la Aplicación Web

### Implementación en Streamlit

La aplicación fue construida usando Streamlit, ofreciendo una interfaz fácil de usar para la entrada de datos y la visualización de predicciones. Las características clave incluyen:

- **Selección de Ciudad y Cultivo**: Los usuarios pueden seleccionar una ciudad y tipo de cultivo para las predicciones.
- **Descargar Resultados**: Opción para descargar los resultados de las predicciones en formato CSV.
- **Gráficos Históricos**: Visualización de datos históricos junto con predicciones.

## Despliegue en la Nube

### Despliegue en Render

La aplicación se desplegó en Render, siguiendo estos pasos:

1. **Configuración**: Configuración de variables de entorno y dependencias necesarias.
2. **Proceso de Despliegue**: Asegurando que la aplicación esté activa y accesible para los usuarios.

### Escalabilidad y Rendimiento

- **Escalabilidad**: Configurado para manejar un aumento de tráfico y volumen de datos.
- **Monitoreo**: Herramientas de monitoreo de rendimiento integradas para asegurar un funcionamiento fluido.

## Documentación y Presentación

### Documentación del Proyecto

El proyecto está completamente documentado:

- **Documentación del Código**: Comentarios en línea y descripciones de funciones.
- **README**: Instrucciones detalladas sobre la configuración, uso y propósito del proyecto.

## Conclusiones y Aprendizajes

### Hallazgos Clave

- **Rendimiento del Modelo**: Los modelos CatBoost y LightGBM proporcionaron predicciones precisas con un RMSE relativamente bajo.
- **Variables Impactantes**: Factores meteorológicos como la temperatura y la precipitación afectan significativamente los rendimientos de los cultivos.

### Trabajo Futuro

- **Optimización Adicional**: Explorar más modelos e hiperparámetros.
- **Integración de Datos en Tiempo Real**: Incorporar datos meteorológicos en tiempo real para predicciones dinámicas.