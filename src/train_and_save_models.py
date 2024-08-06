import joblib
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# Cargar los datasets
weather_file_path = '/workspaces/proyectfinaltour/data/processed/unificado/weather.csv'
agri_file_path = '//workspaces/proyectfinaltour/data/processed/unificado/agri.csv'

weather_df = pd.read_csv(weather_file_path)
agri_df = pd.read_csv(agri_file_path, encoding='latin1')

# Normalizar los nombres de las columnas en el dataset agrícola
agri_df.columns = agri_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Crear una columna de fecha en el dataset agrícola
agri_df['date'] = pd.to_datetime(agri_df['año'].astype(str) + '-01-01')

# Crear una columna de fecha en el dataset meteorológico
weather_df['date'] = pd.to_datetime(weather_df['date_time'])

# Verificar que las ciudades en ambos conjuntos de datos coincidan
agri_df['ciudad'] = agri_df['ciudad'].str.strip().str.lower()
weather_df['city'] = weather_df['city'].str.strip().str.lower()

# Crear las columnas de `year` y `month` en el dataset meteorológico
weather_df['year'] = pd.DatetimeIndex(weather_df['date_time']).year
weather_df['month'] = pd.DatetimeIndex(weather_df['date_time']).month

# Unir los datos agrícolas y meteorológicos por año y ciudad
combined_df = pd.merge(agri_df, weather_df, left_on=['año', 'ciudad'], right_on=['year', 'city'], how='inner')

# Seleccionar las columnas relevantes
data = combined_df[['ciudad', 'date_y', 'produccion_toneladas', 'tempC', 'uvIndex', 'precipMM', 'sunHour']]

# Crear columnas para el año y el mes
data['year'] = pd.DatetimeIndex(data['date_y']).year
data['month'] = pd.DatetimeIndex(data['date_y']).month

# Calcular las medias mensuales de las variables de interés
monthly_means = data.groupby(['ciudad', 'year', 'month']).agg({
    'tempC': 'mean',
    'uvIndex': 'mean',
    'precipMM': 'mean',
    'sunHour': 'mean',
    'produccion_toneladas': 'mean'
}).reset_index()

# Crear una columna de fecha para la serie temporal
monthly_means['date'] = pd.to_datetime(monthly_means[['year', 'month']].assign(day=1))

# Establecer la columna de fecha como índice
monthly_means.set_index('date', inplace=True)

# Ordenar los datos por fecha
monthly_means.sort_index(inplace=True)

# Dividir los datos en conjuntos de entrenamiento y prueba
train_size = int(len(monthly_means) * 0.8)
train, test = monthly_means.iloc[:train_size], monthly_means.iloc[train_size:]

# Definir y entrenar el modelo SARIMAX
model_sarimax = SARIMAX(train['produccion_toneladas'],
                exog=train[['tempC', 'uvIndex', 'precipMM', 'sunHour']],
                order=(1, 1, 1),
                seasonal_order=(1, 1, 1, 12))

model_fit_sarimax = model_sarimax.fit(disp=False)

# Hacer predicciones con SARIMAX
test_exog = test[['tempC', 'uvIndex', 'precipMM', 'sunHour']]
predictions_sarimax = model_fit_sarimax.predict(start=len(train), end=len(train) + len(test) - 1, exog=test_exog)

# Evaluar el modelo SARIMAX utilizando el RMSE
mse_sarimax = mean_squared_error(test['produccion_toneladas'], predictions_sarimax)
rmse_sarimax = mse_sarimax ** 0.5

# Entrenar y evaluar el modelo Random Forest
X_train = train[['tempC', 'uvIndex', 'precipMM', 'sunHour']]
y_train = train['produccion_toneladas']
X_test = test[['tempC', 'uvIndex', 'precipMM', 'sunHour']]
y_test = test['produccion_toneladas']

rf = RandomForestRegressor(random_state=42)
param_grid_rf = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search_rf = GridSearchCV(estimator=rf, param_grid=param_grid_rf, cv=3, n_jobs=-1, verbose=2)
grid_search_rf.fit(X_train, y_train)
best_rf = grid_search_rf.best_estimator_
predictions_rf = best_rf.predict(X_test)
mse_rf = mean_squared_error(y_test, predictions_rf)
rmse_rf = mse_rf ** 0.5

# Entrenar y evaluar el modelo KNN
knn = KNeighborsRegressor()
param_grid_knn = {
    'n_neighbors': [3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
}

grid_search_knn = GridSearchCV(estimator=knn, param_grid=param_grid_knn, cv=3, n_jobs=-1, verbose=2)
grid_search_knn.fit(X_train, y_train)
best_knn = grid_search_knn.best_estimator_
predictions_knn = best_knn.predict(X_test)
mse_knn = mean_squared_error(y_test, predictions_knn)
rmse_knn = mse_knn ** 0.5

# Comparar los modelos y seleccionar el mejor
if rmse_sarimax < rmse_rf and rmse_sarimax < rmse_knn:
    best_model_name = 'SARIMAX'
    best_model = model_fit_sarimax
    best_predictions = predictions_sarimax
elif rmse_rf < rmse_sarimax and rmse_rf < rmse_knn:
    best_model_name = 'Random Forest'
    best_model = best_rf
    best_predictions = predictions_rf
else:
    best_model_name = 'KNN'
    best_model = best_knn
    best_predictions = predictions_knn

# Guardar el nombre del mejor modelo
joblib.dump(best_model_name, '/workspaces/proyectfinaltour/src/best_model_name.pkl')

# Guardar el mejor modelo
if best_model_name == 'SARIMAX':
    joblib.dump(best_model, '/workspaces/proyectfinaltour/src/best_model_sarimax.pkl')
elif best_model_name == 'Random Forest':
    joblib.dump(best_model, '/workspaces/proyectfinaltour/src/best_model_rf.pkl')
else:
    joblib.dump(best_model, '/workspaces/proyectfinaltour/src/best_model_knn.pkl')
