import streamlit as st


st.title('Machine Learning Model Comparison Project')
st.header('Dataset: Grade Code Prediction')
test_data = st.file_uploader('Upload your test data file here (CSV format)', type=['csv'])
st.subheader('Choose the model you want to explore:')
model_selected = st.selectbox(
    'Select Model',
    options=[
        'Logistic Regression',
        'Decision Tree Classifier',
        'K-Nearest Neighbors',
        'Naive Bayes Classifier - Gaussian or Multinomial',
        'Ensemble model - XGBoost',
        'Ensemble Model - Random Forest',
    ]
)
st.subheader('Model Details and Performance Metrics')
st.table(
    {
    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC' , 'MCC'],
    'Value': [0.85, 0.80, 0.78, 0.79, 0.88, 0.75]
})
st.caption('Created with ❤️ by Shrinidhi M - 2025AA05960')
