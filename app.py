import streamlit as st
import pandas as pd
import pickle
from metrics.metrics_computer import compute_metrics
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = None

# Centered Title
st.markdown("<h1 style='text-align: center;'>Machine Learning Model Comparison</h1>", unsafe_allow_html=True)
# Centered Header
st.markdown("<h3 style='text-align: center;'>Dataset: Heart Disease Prediction</h3>", unsafe_allow_html=True)

st.markdown('Read about the problem statement here [README.md](https://github.com/shri-1805/ML-_Assignment_2_StreamLitApp/blob/main/README.md)')

st.subheader('1. Download the Test Dataset here')
st.markdown('[heart_disease_dataset-test.csv](https://github.com/shri-1805/ML-_Assignment_2_StreamLitApp/blob/main/dataset/test.csv)')
st.subheader('2. Upload the test dataset')
test_data = st.file_uploader(label = "Upload your test data file here (CSV format)", type=['csv'])
st.subheader('3. Choose the model you want to explore')

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

if test_data is not None:
    df = pd.read_csv(test_data)

# Import the scaler pickle file and apply
dir = 'jobs\\'
file_path = dir+'scaler.pkl' 
with open(file_path, 'rb') as file:
    scaler = pickle.load(file)

# Apply the scaler, predict the target and display the metrics
if df is not None:
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

    if model_file != 'Select':
        with open(dir+model_file, 'rb') as file:
            model = pickle.load(file)
        y_pred = model.predict(X_test_scaled)

        if hasattr(model, "predict_proba"):
            y_probs = model.predict_proba(X_test_scaled)[:, 1]
        else:
            y_probs = None

        metrics = compute_metrics(y_test, y_pred, y_probs)
        print(metrics)

        st.subheader('Model Details and Performance Metrics')
        st.table(
        {
            'Metric': list(metrics.keys()),
            'Value': [round(v, 4) for v in metrics.values()]
        })

        st.subheader(f"Confusion Matrix - {model_selected}")

        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 6))
        cm = confusion_matrix(y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

        disp.plot(ax=ax, cmap=plt.cm.Blues)
        st.pyplot(fig)
        st.write("Raw Counts")
        st.write(pd.DataFrame(cm, columns=['Predicted 0', 'Predicted 1'], index=['Actual 0', 'Actual 1']))


st.caption('Created with ❤️ by Shrinidhi M - 2025AA05960')
