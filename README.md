a. Problem Statement
  Cardiovascular disease (CVD) has become India's leading cause of mortality, accounting for 31% of all deaths as of 2025. Alarmingly, the ICMR-NCDIR 2024 report reveals that four Indians suffer a heart attack every minute, with a 13% surge in cases among adults under 45 since 2020. Unlike Western populations, heart disease strikes Indians nearly a decade earlier, often progressing silently until it reaches an advanced, irreversible stage.
  The Indian healthcare landscape faces significant challenges, including a shortage of specialized cardiologists in rural areas and a high prevalence of "silent" heart attacks. Consequently, there is an urgent need for an automated, machine-learning-based prediction system. Such a tool can leverage clinical data to provide early-stage screening and risk assessment, empowering primary healthcare providers to intervene before a major cardiac event occurs, thereby reducing the immense socioeconomic burden of premature mortality.
  The primary goal is to predict the presence of heart disease in a patient based on clinical and physiological data. This is a binary classification problem where the target variable indicates whether a patient has heart disease (1) or does not (0). By analyzing features like age, cholesterol levels, and maximum heart rate, we aim to build a predictive model that can assist healthcare providers in early diagnosis.

b. Dataset Description
This is a multivariate type of dataset involving a variety of separate mathematical or statistical variables, multivariate numerical data analysis. It is composed of 14 attributes which are age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, oldpeak — ST depression induced by exercise relative to rest, the slope of the peak exercise ST segment, number of major vessels and Thalassemia. 
This database includes 76 attributes, but all published studies relate to the use of a subset of 14 of them. The Cleveland database is the only one used by ML researchers to date. One of the major tasks on this dataset is to predict based on the given attributes of a patient that whether that particular person has heart disease or not and other is the experimental task to diagnose and find out various insights from this dataset which could help in understanding the problem more.

https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data

c. Models Used: Comparison Table

ML Model Name,Accuracy,AUC,Precision,Recall,F1,MCC
Logistic Regression,,,,,,
Decision Tree,,,,,,
kNN,,,,,,
Naive Bayes,,,,,,
Random Forest (Ensemble),,,,,,
XGBoost (Ensemble),,,,,,

d. Observations
ML Model Name,Observation about model performance
Logistic Regression,Often serves as a strong baseline; performs well when the relationship between features and the target is relatively linear.
Decision Tree,Prone to overfitting on this small dataset; provides high interpretability but may struggle with generalization without pruning.
kNN,Performance is highly sensitive to the choice of 'k' and requires feature scaling (like normalization) since it is distance-based.
Naive Bayes,Efficient and handles categorical data well, though it assumes feature independence which may not strictly hold here.
Random Forest (Ensemble),Usually offers high accuracy by reducing variance through bagging; robust against outliers in clinical data.
XGBoost (Ensemble),Typically the top performer; uses gradient boosting to minimize errors, though it requires careful hyperparameter tuning.
