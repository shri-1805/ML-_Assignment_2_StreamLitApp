import pickle
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Import the models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, matthews_corrcoef

# 1. Load the training data
df = pd.read_csv('dataset\\train.csv')

# train and test here refers to train and validation split
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.1, random_state=42, stratify = df['target'])

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train, y_train)
X_test = scaler.transform(X_test)

scaler_path = "jobs/scaler.pkl"
with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

# 2. Define the Model Dictionary
models = {
    "Logistic_Regression": LogisticRegression(random_state=42,max_iter=500),
    "Decision_Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Naive_Bayes": GaussianNB(),
    "Random_Forest": RandomForestClassifier(random_state=42, n_estimators=100),
    "XGBoost": XGBClassifier(random_state=42, eval_metric='logloss')
}

# 3. Train and Pickle
for name, model in models.items():
    # Train the model
    print("Training model:", name)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)

    metrics = {}
    metrics['Accuracy'] = accuracy_score(y_test, y_pred)
    metrics['Precision'] = precision_score(y_test, y_pred)
    metrics['Recall'] = recall_score(y_test, y_pred)
    metrics['F1-Score'] = f1_score(y_test, y_pred)
    metrics['ROC-AUC'] = roc_auc_score(y_test, y_pred)
    metrics['MCC'] = matthews_corrcoef(y_test, y_pred)

    print("-" * 20+" METRICS "+"-" * 20)
    for metric_name, metric_value in metrics.items():
        print(f"{metric_name}: {metric_value}")
    print("=" * 40)

    # Define the filename
    filename = f"jobs/{name}_model.pkl"
    print(f"Pickling model to: {filename}")
    # Pickle the model to a file
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    
    print(f"Successfully trained and pickled: {filename}")
