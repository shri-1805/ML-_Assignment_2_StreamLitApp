import streamlit as st
import pandas as pd
import pickle
from metrics.metrics_computer import compute_metrics

st.title('Machine Learning Model Comparison Project')
st.header('Dataset: Grade Code Prediction')
test_data = st.file_uploader('Upload your test data file here (CSV format)', type=['csv'])
st.subheader('Choose the model you want to explore:')

models = [
        'Select',
        'Logistic Regression',
        'Decision Tree Classifier',
        'K-Nearest Neighbors',
        'Naive Bayes Classifier - Gaussian or Multinomial',
        'Ensemble model - XGBoost',
        'Ensemble Model - Random Forest',
    ]
model_selected = st.selectbox(
    'Select Model',
    options=models
)

# Import the scaler pickle file and apply
df = pd.read_csv('dataset\\test.csv')
dir = 'jobs\\'
file_path = dir+'scaler.pkl' 
with open(file_path, 'rb') as file:
    scaler = pickle.load(file)

X_test, y_test = df.drop('target', axis=1), df['target']
X_test_scaled = scaler.transform(X_test)

print(f'Model selected: {model_selected}')
switcher = {
    'Logistic Regression': 'logistic_regression_model.pkl',
    'Decision Tree Classifier': 'decision_tree_model.pkl',
    'K-Nearest Neighbors': 'knn_model.pkl',
    'Naive Bayes Classifier - Gaussian or Multinomial': 'naive_bayes_model.pkl',
    'Ensemble model - XGBoost': 'xgboost_model.pkl',
    'Ensemble Model - Random Forest': 'random_forest_model.pkl'
}

model_file = switcher.get(model_selected, 'Select')
metrics = {}
if model_file != 'Select':
    with open(dir+model_file, 'rb') as file:
        model = pickle.load(file)
    y_pred = model.predict(X_test_scaled)
    metrics = compute_metrics(y_test, y_pred)
    print(metrics)

st.subheader('Model Details and Performance Metrics')
st.table(
    {
    'Metric': list(metrics.keys()),
    'Value': [round(v, 4) for v in metrics.values()]
})
st.caption('Created with ❤️ by Shrinidhi M - 2025AA05960')
