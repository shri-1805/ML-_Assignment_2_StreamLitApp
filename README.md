# Heart Disease Prediction Analysis

<hr>

## <a id="problem-statement"></a>a. Problem Statement
<p align="justify">
Cardiovascular disease (CVD) has become India's leading cause of mortality, accounting for <b>31% of all deaths</b> as of 2025. Alarmingly, the ICMR-NCDIR 2024 report reveals that <b>four Indians suffer a heart attack every minute</b>, with a 13% surge in cases among adults under 45 since 2020. Unlike Western populations, heart disease strikes Indians nearly a decade earlier, often progressing silently until it reaches an advanced, irreversible stage. 
</p>

<p align="justify">
The Indian healthcare landscape faces significant challenges, including a shortage of specialized cardiologists in rural areas and a high prevalence of "silent" heart attacks. Consequently, there is an urgent need for an automated, machine-learning-based prediction system. Such a tool can leverage clinical data to provide <b>early-stage screening and risk assessment</b>, empowering primary healthcare providers to intervene before a major cardiac event occurs, thereby reducing the immense socioeconomic burden of premature mortality.
</p>

> **Goal:** To predict the presence of heart disease (Binary Classification: 0 = No Disease, 1 = Disease) using clinical and physiological data to assist in early medical intervention.

<hr>

## <a id="dataset-description"></a>b. Dataset Description
<p>
This is a <b>multivariate dataset</b> involving 14 key clinical attributes used to determine heart health. While the original database contains 76 attributes, this study focuses on the standard subset of 14 features widely used by researchers.
</p>

### Key Attributes:
<ul>
  <li><b>Demographics:</b> Age, Sex</li>
  <li><b>Pain & Symptoms:</b> Chest pain type (cp), Exercise-induced angina (exang)</li>
  <li><b>Clinical Readings:</b> Resting blood pressure (trestbps), Serum cholesterol (chol), Fasting blood sugar (fbs)</li>
  <li><b>Electrocardiographic Results:</b> restecg, Maximum heart rate achieved (thalach)</li>
  <li><b>ST Segment Analysis:</b> Oldpeak (ST depression), Slope of the peak exercise ST segment</li>
  <li><b>Advanced Imaging:</b> Number of major vessels (ca), Thalassemia (thal)</li>
</ul>

**Source:** [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

<hr>

## <a id="models-used"></a>c. Models Used: Comparison Table
<table width="100%">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th align="left">ML Model Name</th>
      <th>Accuracy</th>
      <th>AUC</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1</th>
      <th>MCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Logistic Regression</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><b>Decision Tree</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><b>kNN</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><b>Naive Bayes</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><b>Random Forest (Ensemble)</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><b>XGBoost (Ensemble)</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

<hr>

## <a id="observations"></a>d. Observations
<table>
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th align="left" width="30%">ML Model Name</th>
      <th align="left">Observation about model performance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Logistic Regression</b></td>
      <td>Often serves as a strong baseline; performs well when the relationship between features and the target is relatively linear.</td>
    </tr>
    <tr>
      <td><b>Decision Tree</b></td>
      <td>Prone to overfitting on this small dataset; provides high interpretability but may struggle with generalization without pruning.</td>
    </tr>
    <tr>
      <td><b>kNN</b></td>
      <td>Performance is highly sensitive to the choice of 'k' and requires feature scaling (like normalization) since it is distance-based.</td>
    </tr>
    <tr>
      <td><b>Naive Bayes</b></td>
      <td>Efficient and handles categorical data well, though it assumes feature independence which may not strictly hold here.</td>
    </tr>
    <tr>
      <td><b>Random Forest (Ensemble)</b></td>
      <td>Usually offers high accuracy by reducing variance through bagging; robust against outliers in clinical data.</td>
    </tr>
    <tr>
      <td><b>XGBoost (Ensemble)</b></td>
      <td>Typically the top performer; uses gradient boosting to minimize errors, though it requires careful hyperparameter tuning.</td>
    </tr>
  </tbody>
</table>
