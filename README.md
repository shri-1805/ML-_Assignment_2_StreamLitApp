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
      <td>0.8152</td>
      <td>0.8953</td>
      <td>0.8168</td>
      <td>0.8152</td>
      <td>0.8135</td>
      <td>0.6254</td>
    </tr>
    <tr>
      <td><b>Decision Tree</b></td>
      <td>0.7609</td>
      <td>0.7580</td>
      <td>0.7609</td>
      <td>0.7609</td>
      <td>0.7609</td>
      <td>0.5160</td>
    </tr>
    <tr>
      <td><b>kNN</b></td>
      <td>0.8261</td>
      <td>0.8778</td>
      <td>0.8332</td>
      <td>0.8261</td>
      <td>0.8230</td>
      <td>0.6517</td>
    </tr>
    <tr>
      <td><b>Naive Bayes</b></td>
      <td>0.8152</td>
      <td>0.8766</td>
      <td>0.8198</td>
      <td>0.8152</td>
      <td>0.8125</td>
      <td>0.6274</td>
    </tr>
    <tr>
      <td><b>Random Forest (Ensemble)</b></td>
      <td>0.8152</td>
      <td>0.9000</td>
      <td>0.8152</td>
      <td>0.8152</td>
      <td>0.8143</td>
      <td>0.6247</td>
    </tr>
    <tr>
      <td><b>XGBoost (Ensemble)</b></td>
      <td>0.8043</td>
      <td>0.8924</td>
      <td>0.8040</td>
      <td>0.8043</td>
      <td>0.8038</td>
      <td>0.6027</td>
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
      <td>Often serves as a strong baseline; performs well when the relationship between features and the target is relatively linear. in this dataset, it has performed well with excellent accuracy and AUC scores.</td>
    </tr>
    <tr>
      <td><b>Decision Tree</b></td>
      <td>Prone to overfitting on small dataset; provides high interpretability but may struggle with generalization without pruning. Here, decision tree is the least well performing. It would require careful pruning to generalize better.</td>
    </tr>
    <tr>
      <td><b>kNN</b></td>
      <td>Performance is highly sensitive to the choice of 'k' and requires feature scaling (like normalization) since it is distance-based. Here kNN has the highest accuracy out of all models. It has been trained well.</td>
    </tr>
    <tr>
      <td><b>Naive Bayes</b></td>
      <td>Efficient and handles categorical data well, though it assumes feature independence which may not strictly hold here. It gives a decent performance for this dataset.</td>
    </tr>
    <tr>
      <td><b>Random Forest (Ensemble)</b></td>
      <td>Usually offers high accuracy by reducing variance through bagging; robust against outliers in clinical data. This model gives the top performance for this particular dataset. It has the highest AUC over the test dataset.</td>
    </tr>
    <tr>
      <td><b>XGBoost (Ensemble)</b></td>
      <td>Typically the top performer; uses gradient boosting to minimize errors, though it requires careful hyperparameter tuning. For this small dataset, xgboost is not the top performer. It needs much larger dataset and careful tuning to get better accuracy scores.</td>
    </tr>
  </tbody>
</table>
