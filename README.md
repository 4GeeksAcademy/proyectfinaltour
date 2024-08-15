# README - Agricultural Production Prediction

## Introduction

This project aims to predict agricultural production in different cities using advanced Machine Learning techniques. The project addresses the problem of predicting agricultural production, a critical aspect for planning and resource management in agriculture.

## Methodology and Processes

### 1. Data Collection and Processing

- **Data Sources**: Meteorological and agricultural production data were collected from various sources.
- **Data Cleaning**: The data were cleaned to remove outliers and missing values.
- **Data Processing**: Relevant variables for modeling, including temperature, precipitation, UV index, and sunlight hours, were unified and scaled.

### 2. Machine Learning Models

- **Models Used**:
  - **CatBoost**: Chosen for its ability to handle categorical variables without additional preprocessing.
  - **LightGBM**: Used for its efficiency and speed in training, especially with large datasets.
  - **XGBoost**: Included due to its robustness and generalization ability in complex problems.
  - **Random Forest**: An ensemble model that combines multiple decision trees to improve accuracy and reduce overfitting.
  - **K-Nearest Neighbors (KNN)**: Utilized as a simple yet effective approach based on nearest neighbors in certain scenarios.

- **Optimization Techniques**:
  - **Advanced Hyperparameterization**: GridSearchCV and RandomizedSearchCV were used to fine-tune the hyperparameters of each model, improving their performance.
  - **Cross-Validation**: Cross-validation was applied to ensure the robustness of the models and prevent overfitting.

- **Performance Evaluation**:
  - **Main Metric**: RMSE (Root Mean Square Error) was used to evaluate the performance of each model.
  - **Results**:
    - **CatBoost RMSE**: `436341.78`
    - **LightGBM RMSE**: `443428.97`
    - **XGBoost RMSE**: `449094.98`
    - **Random Forest RMSE**: `485829.70`
    - **KNN RMSE**: `466165.99`

### 3. Sensitivity Analysis

- **Impact of Variables**: Sensitivity analysis was conducted to identify the most influential meteorological variables on agricultural production. This analysis allowed for adjusting and prioritizing the most relevant features in the modeling.

## Web Application Development

- **Implementation with Streamlit**:
  - The application was developed using Streamlit, providing a user-friendly interface for users to select the city, crop, and other parameters.
  - **Features**:
    - **Real-Time Prediction**: The application allows users to input meteorological data and obtain immediate predictions about agricultural production.
    - **Results Visualization**: Graphs were integrated to show agricultural production predictions and compare them with historical data.
    - **Download Results**: The option to download the results in CSV format was included.
  
- **Final Message**: At the end of the application, a message was added indicating that the application is in constant development and that improvements in reliability are expected as more data is collected.

## Deployment in the Cloud

- **Platform**: The application was deployed on Render, ensuring its accessibility on the web.
- **Configuration and Deployment**:
  - The development and production environments were configured on Render.
  - Dependency installation and automatic execution of the application after deployment were included.
  - **Key Files**: `requirements.txt` for dependencies and `app.py` for the main application.

- **Scalability and Performance**:
  - Scalability and performance considerations were made, with plans to adjust the infrastructure based on user load.

## Conclusions and Learnings

- **Results Achieved**:
  - An effective agricultural prediction model was developed, with CatBoost showing the best performance in terms of RMSE.
  - The implementation in Streamlit allows easy interaction and visualization of results by users.

- **Lessons Learned**:
  - The importance of hyperparameterization and cross-validation in improving model performance.
  - The need for robust data processing to ensure the quality of predictions.

- **Next Steps**:
  - Collect more data to improve the accuracy of predictions.
  - Explore the integration of real-time data to make more dynamic predictions.


url: https://produccion-agricola.onrender.com/