import numpy as np

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef
)

def calculate_metrics(y_true, y_pred, y_prob=None):
    """
    Computes performance metrics for a classification model.
    
    Args:
        y_true: Actual labels
        y_pred: Predicted labels
        y_prob: Predicted probabilities (required for AUC)
        
    Returns:
        dict: A dictionary containing all calculated metrics
    """
    metrics = {}
    
    # 1. Accuracy
    metrics['Accuracy'] = accuracy_score(y_true, y_pred)
    
    # 2. AUC Score (Handles binary and multiclass cases)
    if y_prob is not None:
        try:
            # For binary classification, y_prob usually needs to be 1D array of positive class probs
            if len(np.unique(y_true)) == 2:
                 metrics['AUC'] = roc_auc_score(y_true, y_prob[:, 1])
            else:
                 metrics['AUC'] = roc_auc_score(y_true, y_prob, multi_class='ovr')
        except ValueError:
            metrics['AUC'] = "N/A"
    else:
        metrics['AUC'] = "N/A"

    # 3. Precision (weighted handles imbalance)
    metrics['Precision'] = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    
    # 4. Recall (weighted)
    metrics['Recall'] = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    
    # 5. F1 Score (weighted)
    metrics['F1 Score'] = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    # 6. Matthews Correlation Coefficient (MCC)
    metrics['MCC'] = matthews_corrcoef(y_true, y_pred)
    
    return metrics